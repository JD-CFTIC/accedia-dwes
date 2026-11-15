# Guía de trabajo: Desarrollo Web en Entorno Servidor (0613)

Este documento recoge cómo trabajamos para preparar el material de la asignatura. Se lee al empezar cada chat de sesión.

## 1. Contexto

- **Módulo:** Desarrollo Web en Entorno Servidor (0613). CFGS Desarrollo de Aplicaciones Web, 2.º curso.
- **Centro:** ACCEDIA (PROEDUCA), Madrid. Presencial. Curso 2026/27. 12 alumnos.
- **Horario:** lunes, miércoles, jueves y viernes, 2 h cada día (8 h a la semana).
- **Evaluaciones:** 2.
- **Tecnología:** Java 21, Maven, IntelliJ (Windows 11). GroupId `es.accedia`, paquetes `es.accedia.*`.
- **Alumnado:** saben algo de Java del curso anterior, pero hay que reexplicar y afianzar. Nada se da por sabido sin un repaso breve.
- **Punto de partida:** un primer material, generado sin supervisar, resultó denso, difícil de seguir y con ejemplos sin sentido. Todo lo que sigue existe para evitarlo.

## 2. Qué se prepara en cada sesión

Hay tres tipos de material:

| Tipo | Para quién | Contenido |
|---|---|---|
| **Guía** (`.md`) y su **zip** | Alumnos | Construye la mini aplicación paso a paso. El zip trae los proyectos de cada punto de control |
| **Actividad** (`.md`) | Alumnos | Enunciado sin código resuelto: objetivo, resultado esperado, pasos, pistas y un reto opcional |
| **Solución** (`.md`) y su **zip** | Solo el profesor | Se explica paso a paso como una guía, con qué comprobar al corregir, errores frecuentes (con el mensaje real) y la solución del reto |

**El número de guías, actividades y soluciones es variable en cada sesión.** Una sesión puede llevar una guía y ninguna actividad, dos guías, varias actividades, etc. Cada actividad tiene su propia solución. Antes de producir nada, el planteamiento de la sesión fija qué material lleva. Si la guía ocupa la clase, la actividad pasa a la sesión siguiente.

## 3. Principios didácticos

1. **Primero el problema, después el concepto.** Cada sesión parte de algo que el alumno quiere conseguir; el concepto aparece cuando hace falta.
2. **Pocos conceptos nuevos por sesión.** Mejor uno bien asentado que cinco apuntados.
3. **Cada sesión termina en algo que funciona:** una mini aplicación completa, hecha dentro de las horas de clase.
4. **Cada cosa lleva un «para qué»**, dicho antes de hacerla. Si un ejemplo no tiene sentido por sí solo, se cambia el ejemplo.
5. **Muy progresivo:** se construye por partes pequeñas, y tras cada parte se muestra cómo queda el conjunto.
6. **Visualmente limpio:** poco texto por bloque, tablas solo cuando comparan, sin adornos.
7. **Antes de usar un recurso conocido** (listas, bucles, interfaces…), un repaso de dos líneas.
8. **El fallo también se enseña:** se provoca un error a propósito y se lee el mensaje real.

## 4. Estructura de una guía

1. Título y una introducción breve (qué aprenderemos hoy).
2. **Para qué** hacemos esto (el problema que motiva la sesión).
3. **Qué vamos a construir:** salida esperada al principio, un esquema y una tabla de piezas con la columna «Por qué la necesitamos».
4. **Qué haremos hoy:** hoja de ruta por partes.
5. Los pasos. Cada paso tiene: *Qué hacemos y para qué* → explicación → cuadro de código → refuerzo.
6. **Cierre:** lo aprendido y un adelanto de la próxima sesión.

### Reglas de redacción

- Las guías se comparten con los alumnos, así que se redactan **para ellos**: primera persona del plural y futuro («construiremos», «escribimos»). No se usa lenguaje dirigido al profesor.
- Se dice **«escribimos»**, nunca «pega». No se usan frases como «sin copiar».
- El código se **construye por partes:** primero la explicación, luego el cuadro de código, luego **«De momento, así queda la clase X»**.
- El código intermedio va **sin comentarios**. Los comentarios (mínimos) solo aparecen cuando se entrega la clase completa.
- Lo que genera el IDE (constructores, getters y setters, `main`) se genera con el IDE, explicando **para qué sirve** antes de generarlo.
- Cuando el IDE marque algo en rojo que es normal en ese momento, se avisa **en la propia guía** y se explica cómo arreglarlo.
- Etiqueta de resumen tras cada bloque: **«Lo que hemos visto»** (nunca «Para retener» ni «En resumen»).
- **Sin minutos en las tablas.**
- Español de España, con ortografía y tildes correctas. Es un requisito muy importante.

## 5. Nombres de carpetas y ficheros

Estructura en Drive:

```
Entorno servidor 2DAW/
├── Teoría (temas)/
└── UD03_Spring_Core/
    ├── S01_Cafeteria_20261111/
    ├── S02_Entregas_20261112/
    └── S03_Pagos_20261113/
```

| Elemento | Patrón | Ejemplo |
|---|---|---|
| Carpeta de unidad | `UDnn_Titulo_de_la_unidad` | `UD03_Spring_Core` |
| Carpeta de sesión | `Snn_Tema_AAAAMMDD` | `S03_Pagos_20261113` |
| Fichero | `UDnn_Snn_orden_tipo_tema_AAAAMMDD.ext` | `UD03_S03_01_guia_pagos_20261113.md` |
| Zip | Mismo nombre que su guía o solución | `UD03_S03_01_guia_pagos_20261113.zip` |

- El número de sesión se cuenta **dentro de la unidad** (S01, S02…).
- La fecha es la de **impartición**.
- El orden (`01`, `02`, `03`…) numera **todos los ficheros de la sesión** en el orden en que se usan en clase, sea cual sea su tipo. Como el número de materiales varía, la numeración llega hasta donde haga falta (`01` guía, `02` actividad, `03` solución, `04` otra actividad…). El zip comparte el número de su guía o solución.
- Tipos: `guia`, `actividad`, `solucion`. El tema distingue entre varios del mismo tipo (`02_actividad_gimnasio`, `04_actividad_playlist`).
- En el nombre del fichero, el tema va en minúsculas, sin tildes ni espacios.
- Dentro del zip, la carpeta raíz lleva el mismo nombre que el zip.
- Cada punto de control de una guía es un proyecto Maven independiente dentro del zip (`1-…`, `2-…`) más un `LEEME.txt` que explica cuál es cuál.

## 6. Verificación (obligatoria)

- **Todo el código se compila y se ejecuta** antes de escribirlo en un documento. Las salidas que aparecen en las guías son las **reales**.
- Los mensajes de error que se muestran son los reales: se provoca el error y se copia (sin rutas temporales).
- Los fragmentos de código, las clases completas y las salidas salen de **fuentes verificadas**, no se teclean a mano en el documento. Para ello se usan las plantillas de `herramientas/`.
- Los zips se abren y se ejecutan antes de entregarlos.
- Se revisa la ortografía y que no quede ninguna referencia desfasada (nombres de paquetes, de ficheros o de sesiones, número de clases, etc.).
- La última tarea de cada sesión es comprobar el trabajo: hechos contra sus fuentes, y documentos abiertos y releídos.

## 7. Cómo es cada chat de sesión

1. **Entrada.** Se lee esta guía, `planificacion.md`, `seguimiento.csv` y `cambios.md`.
2. **Resumen corto:** qué se vio, qué queda pendiente y qué toca hoy. Se espera la confirmación del profesor antes de preparar nada.
3. **Planteamiento** de la sesión: objetivo didáctico, reparto de las horas y ejemplo propuesto. Si hay varias opciones (nombres, ejemplos, estructura), se proponen pocas y bien distintas, y se recomienda una.
4. **Entrega por partes**, esperando el visto bueno en cada una, en el orden de uso en clase y con el material que haya fijado el planteamiento: por ejemplo, guía, su zip, actividad, solución y su zip.
5. **Cierre.** Se actualiza `seguimiento.csv`, se anota en `cambios.md` cualquier reordenación con su motivo y se confirma qué falta.

## 8. Forma de trabajar con el profesor

- **Un paso confirmado a la vez.** Se avisa antes de empezar algo grande.
- **No se regenera ni se rehace un entregable sin orden explícita.** Si se detecta un fallo en algo ya entregado, se avisa y se espera.
- Las respuestas son **concisas y directas**.
- **Sustituir un fichero en Drive** significa subir el nuevo y enviar el antiguo a la papelera, porque Drive no permite cambiar el contenido de un fichero ya subido.
- Los ficheros nuevos se suben a Drive y a Moodle solo cuando el profesor lo pide.

## 9. Qué va en cada sitio

| Dónde | Qué |
|---|---|
| **Drive** (`Entorno servidor 2DAW`) | Guías, actividades, soluciones y zips de cada sesión |
| **Repositorio** (`accedia-dwes`) | Esta guía, `planificacion.md`, `cambios.md`, `seguimiento.csv` y `herramientas/` |
| **Proyecto de Claude** | Instrucciones y la programación didáctica en PDF |

**Regla del repositorio:** no se suben soluciones ni datos de alumnos.

## 10. Archivos del repositorio

| Archivo | Para qué sirve | Cuándo cambia |
|---|---|---|
| `guia-de-trabajo.md` | Método y reglas (este documento) | Pocas veces |
| `planificacion.md` | Plan de la unidad: horas, sesiones, criterios | Si cambia el plan |
| `seguimiento.csv` | Una fila por sesión: tema, estado del material, impartida o no | Cada semana |
| `cambios.md` | Reordenaciones y decisiones, con su motivo | Cuando algo se mueve |
| `herramientas/` | Plantillas y scripts para generar guías y zips con código verificado | Cuando se mejoran |
