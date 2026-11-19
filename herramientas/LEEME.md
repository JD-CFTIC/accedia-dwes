# Herramientas

Scripts y plantillas para preparar guías, actividades, soluciones y zips con **código y salidas verificados**: el código se compila y se ejecuta, y lo que aparece en el documento sale de esas ejecuciones, nunca de teclearlo a mano.

Requisitos: Python 3, Java 21 (`javac` y `java`) y Maven.

## Qué hay

| Fichero | Para qué sirve |
|---|---|
| `render.py` | Genera el `.md` a partir de una plantilla: sustituye los marcadores por código y salidas reales |
| `zip.py` | Construye el zip de proyectos Maven (uno por punto de control) con comentarios de cabecera, lo compila y lo ejecuta |
| `plantillas/guia.tpl.md` | Esqueleto de una guía |
| `plantillas/actividad.tpl.md` | Esqueleto de una actividad |
| `plantillas/solucion.tpl.md` | Esqueleto de una solución |
| `ejemplo/zip-config.json` | Configuración de ejemplo para `zip.py` |
| `ejemplo/` | Un ejemplo pequeño y neutro (saludos) para probar las herramientas |

## Cómo se usa

**1. El classpath de Spring.** Un fichero de texto con las librerías, para compilar y ejecutar. Se saca de un proyecto con `spring-context` en su `pom.xml`:

```
mvn -q dependency:build-classpath -Dmdep.outputFile=classpath.txt
```

**2. Las fuentes por etapas.** En `RAIZ/src/<etapa>/` se escribe cada clase del proyecto en cada punto de control (`a`, `b`, `c`…). Las clases llevan marcadores de sección:

```java
package es.accedia.ejemplo;

public class Cuenta {

//<atributo>
    private int saldo;
//</atributo>
//<constructor>
    public Cuenta(int saldo) {
        this.saldo = saldo;
    }
//</constructor>
//<cierre>
}
//</cierre>
```

Lo que va antes de la primera sección es el preámbulo. La sección `cierre` lleva las llaves finales. Para una clase con `main`, el preámbulo termina en la línea del `main` y `cierre` es `    }` y `}`.

**3. La plantilla.** Un `.md` con marcadores (ver `plantillas/`):

| Marcador | Qué pone |
|---|---|
| `@@frag:etapa/Clase.java:a,b@@` | Solo esas secciones, sin comentarios: lo que se escribe dentro de la clase |
| `@@parcial:etapa/Clase.java:a,b@@` | La clase con solo esas secciones, sin comentarios: el «De momento, así queda…» |
| `@@code:etapa/Clase.java@@` | La clase completa, con sus comentarios |
| `@@out:etapa@@` | La salida real de ejecutar la etapa |
| `@@err:etapa@@` | Solo la línea `Exception` y la `Caused by`, sin rutas temporales. Falla si la etapa no da error |
| `@@res:etapa/fichero@@` | El contenido de un fichero de recursos (por ejemplo un `.properties`) |

**Ficheros de recursos.** Los ficheros que no son `.java` de `RAIZ/src/<etapa>/` (por ejemplo `tienda.properties`) se copian a `RAIZ/limpio/<etapa>/` y se ponen en el classpath al ejecutar la etapa. `zip.py` los copia a `src/main/resources` de cada proyecto. Una etapa sin fichero (para enseñar el error de fichero que falta) simplemente no lo lleva.

**4. Generar el documento:**

```
python3 -I render.py plantilla.tpl.md RAIZ classpath.txt salida.md --main es.accedia.paquete.Aplicacion
```

También escribe las clases limpias, sin marcadores, en `RAIZ/limpio/<etapa>/`.

**5. Generar el zip.** Se escribe una configuración, copiando `ejemplo/zip-config.json`: nombre del zip, paquete, proyectos con su etapa y el comentario de cabecera de cada clase en cada etapa. Después:

```
python3 -I zip.py config.json RAIZ --classpath classpath.txt --main es.accedia.paquete.Aplicacion
```

Compila y ejecuta cada proyecto antes de empaquetar y enseña la primera salida de cada uno. El zip queda en `RAIZ/zipproj/`.

## Probarlas

Con el ejemplo, desde esta carpeta:

```
mkdir -p /tmp/prueba && cp -r ejemplo/src /tmp/prueba/
python3 -I render.py ejemplo/plantilla.tpl.md /tmp/prueba classpath.txt /tmp/prueba/salida.md --main es.accedia.saludos.Aplicacion
python3 -I zip.py ejemplo/zip-config.json /tmp/prueba --classpath classpath.txt --main es.accedia.saludos.Aplicacion
```

Debe salir `OK` en los dos, la salida `Buenos días, Ana.` en los proyectos 1 y 3, y el error `NoUniqueBeanDefinitionException` en el 2.

## Reglas

- Las salidas y los errores de un documento salen siempre de `@@out@@` y `@@err@@`, no se escriben a mano.
- Los comentarios de cabecera del zip no empiezan ninguna línea con `@` (Javadoc lo interpretaría como etiqueta); `zip.py` lo comprueba.
- Las soluciones no se suben a este repositorio. El ejemplo de `ejemplo/` es neutro y no es material de clase.
