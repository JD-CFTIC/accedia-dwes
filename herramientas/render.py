"""Genera un documento (guía, actividad o solución) a partir de una plantilla, con código y salidas reales.

Uso:
    python3 -I render.py PLANTILLA RAIZ CLASSPATH SALIDA --main es.accedia.paquete.Aplicacion

- PLANTILLA: fichero .md con marcadores @@...@@ (ver más abajo).
- RAIZ:      carpeta de trabajo; debe contener src/<etapa>/<Clase>.java.
- CLASSPATH: fichero de texto con el classpath de Spring (ver LEEME.md).
- SALIDA:    fichero .md que se genera.
- --main:    clase con el main que se ejecuta para obtener las salidas.

Las fuentes de src/ llevan marcadores //<nombre> ... //</nombre> que delimitan secciones.
Lo que va antes de la primera sección es el preámbulo (package, imports, cabecera de la clase).
Una sección llamada «cierre» contiene las llaves finales; si no existe, se usa «}».

Marcadores de la plantilla:
- @@frag:etapa/Clase.java:a,b@@     solo esas secciones, lo que se escribe dentro de la clase
- @@parcial:etapa/Clase.java:a,b@@  la clase con solo esas secciones (el «de momento, así queda…»)
- @@code:etapa/Clase.java@@         la clase completa
- @@out:etapa@@                     salida real de ejecutar la etapa
- @@err:etapa@@                     solo la línea Exception y la línea Caused by, sin rutas temporales
- @@res:etapa/fichero@@             un fichero que no es .java (por ejemplo un .properties), tal cual, en un bloque de código

Los ficheros que no son .java de src/<etapa>/ son recursos: se copian a limpio/<etapa>/ y se ponen en el classpath al ejecutar.

También escribe las clases limpias (sin marcadores) en RAIZ/limpio/<etapa>/, que usa zip.py.
Los fragmentos (frag y parcial) salen sin comentarios de línea; la clase completa (code) los conserva.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if len(sys.argv) != 7 or sys.argv[5] != "--main":
    raise SystemExit(__doc__)
plantilla, raiz, cpfile, salida = (Path(a) for a in sys.argv[1:5])
principal = sys.argv[6]
cp = cpfile.read_text(encoding="utf-8").strip()
src = raiz / "src"


def analizar(ruta):
    preambulo, secciones, actual = [], {}, None
    for linea in (src / ruta).read_text(encoding="utf-8").splitlines():
        m_ini = re.fullmatch(r"//<(\w+)>", linea)
        m_fin = re.fullmatch(r"//</(\w+)>", linea)
        if m_ini:
            actual = m_ini.group(1)
            secciones[actual] = []
        elif m_fin:
            actual = None
        elif actual is not None:
            secciones[actual].append(linea)
        elif not secciones:
            preambulo.append(linea)
    while preambulo and not preambulo[-1].strip():
        preambulo.pop()
    return preambulo, {k: "\n".join(v) for k, v in secciones.items()}


def componer(ruta, nombres):
    pre, sec = analizar(ruta)
    cuerpo = "\n\n".join(sec[n] for n in nombres)
    sep = "\n" if "static void main" in pre[-1] else "\n\n"
    cierre = sec.get("cierre", "}")
    return "\n".join(pre) + (sep + cuerpo if nombres else "") + "\n" + cierre + "\n"


def todos(ruta):
    return [n for n in analizar(ruta)[1] if n != "cierre"]


def sin_comentarios(texto):
    return "\n".join(l for l in texto.split("\n") if not l.strip().startswith("//"))


def bloque(texto):
    return "```java\n" + texto.rstrip("\n") + "\n```"


def pre(lineas):
    return "<pre>\n" + "\n".join(lineas) + "\n</pre>"


def recursos(directorio):
    return [p for p in Path(directorio).iterdir() if p.is_file() and p.suffix != ".java"]


def ejecutar(directorio):
    with tempfile.TemporaryDirectory() as tmp:
        fuentes = [str(p) for p in Path(directorio).glob("*.java")]
        subprocess.run(["javac", "-encoding", "UTF-8", "-parameters", "-cp", cp, "-d", tmp, *fuentes],
                       check=True, capture_output=True)
        for f in recursos(directorio):
            shutil.copy(f, tmp)
        r = subprocess.run(["java", "-Dfile.encoding=UTF-8", "-Dstdout.encoding=UTF-8",
                            "-Dstderr.encoding=UTF-8", "-cp", f"{tmp}:{cp}", principal],
                           capture_output=True, text=True)
    return [l for l in (r.stdout + r.stderr).splitlines()
            if not l.startswith("Picked up JAVA_TOOL_OPTIONS")]


def limpiar_ruta(linea):
    return re.sub(r"\[/[^\]]*/(\w+\.class)\]", r"[\1]", linea)


limpio = raiz / "limpio"
for etapa in sorted(p.name for p in src.iterdir() if p.is_dir()):
    destino = limpio / etapa
    destino.mkdir(parents=True, exist_ok=True)
    for f in sorted((src / etapa).glob("*.java")):
        (destino / f.name).write_text(componer(f"{etapa}/{f.name}", todos(f"{etapa}/{f.name}")),
                                      encoding="utf-8")
    for f in recursos(src / etapa):
        shutil.copy(f, destino)


def salida_err(etapa):
    lineas = ejecutar(limpio / etapa)
    ex = [l for l in lineas if l.startswith("Exception in thread")][:1]
    ca = [l for l in lineas if l.startswith("Caused by")][:1]
    if not ex:
        raise SystemExit(f"@@err:{etapa}@@ pero la etapa no falla")
    return pre([limpiar_ruta(l) for l in ex + ca])


texto = plantilla.read_text(encoding="utf-8")
texto = re.sub(r"@@frag:([^:@]+):([^@]+)@@",
               lambda m: bloque(sin_comentarios("\n\n".join(analizar(m.group(1))[1][n] for n in m.group(2).split(",")))), texto)
texto = re.sub(r"@@parcial:([^:@]+):([^@]*)@@",
               lambda m: bloque(sin_comentarios(componer(m.group(1), [n for n in m.group(2).split(",") if n]))), texto)
texto = re.sub(r"@@code:([^:@]+)@@",
               lambda m: bloque(componer(m.group(1), todos(m.group(1)))), texto)
texto = re.sub(r"@@res:([^:@]+)@@",
               lambda m: "```" + Path(m.group(1)).suffix[1:] + "\n" + (src / m.group(1)).read_text(encoding="utf-8").rstrip("\n") + "\n```", texto)
texto = re.sub(r"@@out:([^@]+)@@", lambda m: pre(ejecutar(limpio / m.group(1))), texto)
texto = re.sub(r"@@err:([^@]+)@@", lambda m: salida_err(m.group(1)), texto)
assert "@@" not in texto, "Quedan marcadores sin sustituir"
salida.write_text(texto, encoding="utf-8")
print("OK", salida, len(texto), "caracteres")
