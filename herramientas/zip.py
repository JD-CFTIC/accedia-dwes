"""Construye el zip de proyectos Maven de una guía o solución, con comentarios de cabecera en cada clase.

Uso:
    python3 -I zip.py CONFIG.json RAIZ [--classpath CLASSPATH.txt --main es.accedia.paquete.Aplicacion]

- CONFIG.json: ver ejemplo/zip-config.json.
- RAIZ:        carpeta de trabajo; usa RAIZ/limpio/<etapa>/ (lo genera render.py) y escribe en RAIZ/zipproj/.
- Con --classpath y --main, compila y ejecuta cada proyecto antes de empaquetar y enseña la salida.

Los ficheros que no son .java de RAIZ/limpio/<etapa>/ (por ejemplo un .properties) son recursos: van a src/main/resources y
se ponen en el classpath al ejecutar. Los .html van a static/, los .css a static/css y los .js a static/js.

Cada proyecto es un proyecto Maven independiente, con su pom.xml. Si un proyecto necesita otra librería, se
declara en config["extras"] ({"proyecto": [{"coordenadas": "grupo:artefacto:version", "comentario": "..."}]}). El comentario de cabecera de cada clase
sale de config["docs"]: para cada clase, un texto por etapa (o «*» para todas). Si una clase no tiene texto
en una etapa, se usa el de la última etapa anterior que lo tenga. Los textos no empiezan una línea con «@»
(Javadoc lo interpretaría como etiqueta).
"""
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

args = sys.argv[1:]
if len(args) not in (2, 6) or (len(args) == 6 and (args[2] != "--classpath" or args[4] != "--main")):
    raise SystemExit(__doc__)
cfg = json.loads(Path(args[0]).read_text(encoding="utf-8"))
raiz = Path(args[1])
cp = Path(args[3]).read_text(encoding="utf-8").strip() if len(args) == 6 else None
principal = args[5] if len(args) == 6 else None

nombre = cfg["nombre_zip"]
paquete_ruta = cfg["paquete"].replace(".", "/")
destino = raiz / "zipproj" / nombre
if destino.exists():
    shutil.rmtree(destino)

POM = """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>es.accedia</groupId>
    <artifactId>@@ARTIFACT@@</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- spring-context: la parte de Spring que contiene el contenedor.
             Maven la descarga de Internet junto con las librerías que necesita
             (spring-core, spring-beans...), sin que tengamos que declararlas. -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>@@SPRING@@</version>
        </dependency>
    </dependencies>
</project>
"""


def doc_de(clase, etapa):
    d = cfg["docs"][clase]
    if "*" in d:
        return d["*"]
    ultimo = None
    for e in cfg["etapas"]:
        if e in d:
            ultimo = d[e]
        if e == etapa:
            break
    return ultimo


for proyecto, etapa in cfg["proyectos"].items():
    base = destino / proyecto
    java = base / "src/main/java" / paquete_ruta
    java.mkdir(parents=True)
    pom = POM.replace("@@ARTIFACT@@", cfg["artifactId"]).replace("@@SPRING@@", cfg.get("spring", "7.0.9"))
    extra = ""
    for e in cfg.get("extras", {}).get(proyecto, []):
        grupo, artefacto, version = e["coordenadas"].split(":")
        extra += f"\n        <!-- {e['comentario']} -->\n        <dependency>\n            <groupId>{grupo}</groupId>\n"
        extra += f"            <artifactId>{artefacto}</artifactId>\n            <version>{version}</version>\n        </dependency>\n"
    pom = pom.replace("    </dependencies>", extra.rstrip("\n") + "\n    </dependencies>" if extra else "    </dependencies>")
    (base / "pom.xml").write_text(pom, encoding="utf-8")
    for f in sorted((raiz / "limpio" / etapa).glob("*.java")):
        lineas = f.read_text(encoding="utf-8").split("\n")
        i = next(k for k, l in enumerate(lineas) if l.startswith("@Component") or l.startswith("public "))
        texto = doc_de(f.stem, etapa)
        if texto is None:
            raise SystemExit(f"Falta el comentario de {f.stem} en la etapa {etapa}")
        for l in texto.split("\n"):
            if l.strip().startswith("* @") or l.strip().startswith("@"):
                raise SystemExit(f"Una línea de {f.stem} empieza por @: {l!r}")
        bloque = ["/**", " * " + texto, " */"]
        (java / f.name).write_text("\n".join(lineas[:i] + bloque + lineas[i:]), encoding="utf-8")
    recursos = [f for f in (raiz / "limpio" / etapa).iterdir() if f.is_file() and f.suffix != ".java"]
    if recursos:
        (base / "src/main/resources").mkdir(parents=True)
        for f in recursos:
            # Los .html, .css y .js de una web van a static/ (los .css a static/css, los .js a static/js)
            sub = {".html": "static", ".css": "static/css", ".js": "static/js"}.get(f.suffix, "")
            (base / "src/main/resources" / sub).mkdir(parents=True, exist_ok=True)
            shutil.copy(f, base / "src/main/resources" / sub / f.name)
    if cp:
        with tempfile.TemporaryDirectory() as tmp:
            fuentes = [str(p) for p in java.glob("*.java")]
            subprocess.run(["javac", "-encoding", "UTF-8", "-parameters", "-cp", cp, "-d", tmp, *fuentes],
                           check=True, capture_output=True)
            shutil.copytree(base / "src/main/resources", tmp, dirs_exist_ok=True)
            r = subprocess.run(["java", "-Dstdout.encoding=UTF-8", "-Dstderr.encoding=UTF-8",
                                "-cp", f"{tmp}:{cp}", principal], capture_output=True, text=True)
        lineas = [l for l in (r.stdout + r.stderr).splitlines()
                  if l and not l.startswith(("Picked up", "\tat ", "\t..."))]
        print(f"== {proyecto}")
        for l in lineas[:6]:
            print("   ", l[:160])

(destino / "LEEME.txt").write_text(cfg["leeme"].strip("\n") + "\n", encoding="utf-8")
archivo = raiz / "zipproj" / (nombre + ".zip")
with zipfile.ZipFile(archivo, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(destino.rglob("*")):
        if p.is_file():
            z.write(p, p.relative_to(destino.parent))
print("OK", archivo, len(zipfile.ZipFile(archivo).namelist()), "ficheros")
