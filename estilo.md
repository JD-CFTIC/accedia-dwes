# Estilo del material de DWES

Este documento recoge **cómo suenan y cómo se ven** las guías, actividades y soluciones que ya funcionan. Complementa a `guia-de-trabajo.md`: allí están las reglas; aquí, el oficio. Antes de redactar nada, se contrasta con una guía modelo (`UD03_S02_01_guia_entregas_20261112.md` es la más completa; `UD03_S03_01_guia_pagos_20261113.md`, la más reciente) y con la actividad y la solución de la playlist.

## 1. Voz

- **Cercana y concreta.** Se habla a los alumnos como a compañeros: «escribimos», «comprobamos», «fíjate en…». Sin tecnicismos gratuitos y sin tono de manual.
- **Primera persona del plural** para lo que se hace en clase («construiremos», «veremos»), y **segunda persona** solo cuando se les pide algo directo o se les pone en un papel («Eres el profesor de un módulo…»).
- **Frases cortas.** Un párrafo explica una sola idea. Si hay dos, son dos párrafos.
- **El «para qué» siempre va primero.** Nunca se escribe código sin haber dicho antes por qué hace falta.
- **Las ideas se anclan con una imagen cotidiana** cuando ayuda (un almacén, una forma de pago por defecto), sin alargarse.
- **Se evitan** las frases de relleno, las listas de definiciones sueltas y los adjetivos de entusiasmo.

## 2. Cómo se abre una guía

1. Título con número de sesión y una idea: `# Sesión 2. Spring: que los objetos se conecten solos`.
2. Una introducción de dos o tres frases que enlaza con la sesión anterior y dice qué se construirá hoy.
3. **Para qué construimos esta aplicación:** el problema, en una lista corta.
4. **Qué vamos a construir:**
   - Un párrafo que pone al alumno en un papel real.
   - La **salida esperada** dentro de `<pre>`, antes de escribir ningún código.
   - Un **esquema ASCII** de cómo se conectan las clases.
   - Una **tabla de piezas** con las columnas `Clase | Qué hace | Por qué la necesitamos`.
5. **Qué haremos hoy:** tabla con `Parte | Qué hacemos`.

## 3. Cómo se escribe un paso

Todos los pasos siguen el mismo patrón, para que el alumno sepa qué esperar:

```
### Paso 3. La clase X

**Qué hacemos y para qué.** Una o dos frases.

(explicación en párrafos breves)

(cuadro de código)

**Lo que hemos visto.** Una o dos frases.
```

- **Un cuadro de código tras una explicación**, nunca antes. El refuerzo va justo después.
- El código se construye por trozos y, tras cada trozo, se enseña el estado: **«De momento, así queda la clase X»**.
- El código **intermedio no lleva comentarios**; la clase completa final lleva los mínimos.
- Cuando se usa el IDE, se dice **el atajo exacto** y **qué se selecciona**: `Alt+Insert`, `Constructor`, seleccionando `titulo` y `segundos`.
- **Avisos de rojo normal** en un recuadro de cita, con la solución:

  > **Es normal que IntelliJ marque `@Primary` en rojo.** Falta su `import`: `Alt+Enter` sobre `@Primary` y `Import class`.

- **Las salidas** se ponen siempre en `<pre>` y son las reales.
- **Los errores** se muestran con su mensaje real (sin rutas temporales) y se explica **qué dice, qué significa y cómo se arregla**.
- **Las comparaciones** (dos formas de hacer algo) van en tabla; todo lo demás, en prosa o listas.
- **Cierre de cada parte** con «Lo que hemos visto»: dos o tres ideas, no un resumen del texto.

## 4. Cómo se cierra una guía

- **Lo que hemos aprendido:** lista corta de ideas con la palabra clave en negrita.
- Si hace falta, un recuadro de **vocabulario** o un detalle que se retomará más adelante.
- **Qué viene en la próxima sesión:** el problema que se plantea, formulado como pregunta, sin soltar la solución.

## 5. Cómo es una actividad

Un enunciado que el alumno puede seguir solo, sin código resuelto:

1. **Título y una frase** que la conecta con la guía («con la aplicación de entregas como modelo»).
2. **Qué vamos a construir:** la misma estructura que en la guía (papel real, salida esperada, esquema, tabla de piezas). Se hace notar el **parecido con la guía** para que el alumno reconozca el patrón.
3. **Antes de empezar:** repasos de dos líneas de lo que se necesita de Java, cada uno con un ejemplo mínimo.
4. **Pasos:** lista numerada. Cada paso dice **qué clase crear, con qué atributos y qué métodos**, y qué se genera con el IDE.
5. **Pistas:** respuestas a los fallos más probables, **con el nombre real del error** y la causa.
6. **Reto (si terminas antes):** una mejora opcional, con la salida esperada y una pista de qué usar, sin dar el código.

## 6. Cómo es una solución

Es una **guía para el profesor**, con el mismo tono que las de los alumnos:

1. **Qué hay que comprobar:** lista de criterios para corregir.
2. **Pasos**, uno por clase, con el mismo patrón que una guía (qué hacemos y para qué → código por partes → «Lo que hemos visto»).
3. **Errores frecuentes:** cada uno con su **mensaje real** y su causa.
4. **Reto:** resuelto, con la clase completa.
5. **Para el cierre de la actividad:** lo que debe quedar claro, una pregunta para la clase y el siguiente paso.

## 7. Los zips

- Cada punto de control de la guía es un **proyecto Maven independiente** y se puede abrir solo.
- Incluyen un `LEEME.txt` que explica cuál es cuál y dice si alguno **falla a propósito**.
- Los **comentarios son abundantes**: cada clase lleva un comentario de cabecera que explica su papel y, en los puntos con fallo, dice cuál es.
- Los comentarios de cabecera **no empiezan una línea con `@`** (Javadoc lo interpretaría como etiqueta).

## 8. Lo que no se hace

- Ejemplos sin sentido o desconectados de un problema real.
- Código sin haber explicado su «para qué».
- Tablas para lo que se explica mejor con una frase.
- Frases como «pega», «sin copiar», «Para retener» o «En resumen».
- Minutos en las tablas.
- Dar por sabida una herramienta del IDE sin decir cómo se usa.
- Dejar el código, las salidas o los mensajes de error escritos a mano en el documento: salen de fuentes verificadas.

## 9. Lista final antes de entregar

- [ ] El «para qué» aparece antes de cada código.
- [ ] La salida esperada está al principio y es real.
- [ ] Cada trozo de código va seguido de «De momento, así queda…» o de «Lo que hemos visto».
- [ ] Los avisos de rojo normal están en su sitio.
- [ ] Ortografía y tildes revisadas, en español de España.
- [ ] Nombres de ficheros y carpetas según `guia-de-trabajo.md`.
- [ ] Ninguna referencia desfasada (número de clases, de partes, nombres de sesiones).
