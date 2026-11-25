# Cambios de plan: Desarrollo Web en Entorno Servidor (0613)

Aquí se anota cada reordenación o decisión que cambia el plan, con su motivo. El plan vigente está en `planificacion.md` y el estado de cada sesión, en `seguimiento.csv`. Las entradas van de la más reciente a la más antigua.

## 2026-11-25

### S09 no se terminó en clase; S10 pasa a ser terminar S09 y el cliente en el navegador
- **Qué cambia:** S09 se imparte, pero los alumnos no terminan la actividad de las bicicletas (unos casi acaban y otros van cerca). S10 se reparte así: 40 minutos para terminarla, 10 de puesta en común y 50 en los que el profesor construye el cliente web (HTML, CSS y JavaScript) sobre el proyecto de las bicicletas. S11 sigue siendo el simulacro de examen.
- **Motivo:** la actividad integradora lleva más de lo previsto y es mejor que la terminen antes de seguir.
- **Material:** `UD03_S10_01` (guía de 6 pasos y zip con 5 puntos de control) y `UD03_S10_02` (guion del profesor, solo para él), en Drive. El guion reparte los 50 minutos e incluye qué recortar y una tabla de fallos con los mensajes reales. El servidor es el `HttpServer` que trae Java, como bean de Spring; no hay persistencia.
- **Herramientas:** `zip.py` coloca los `.html`, `.css` y `.js` de una web en `static/` dentro del proyecto.
- **Dónde va el material:** los materiales de cada sesión se guardan en Drive, no en el repositorio.

## 2026-11-24

### S08 impartida resultó larga; S09 se pule con puntos de control
- **Qué cambia:** la guía de S08 se regenera siguiendo las reglas de redacción (cada elemento de Java o Spring se explica al aparecer, «De momento, así queda…», clase completa y «En este paso cambian:» en cada paso). El enunciado de S09 fija cómo se elige la bicicleta, aclara quién recibe el `Alquiler` y marca tres puntos de control con su salida. La solución de S09 se reordena en esos tres puntos de control, que se ejecutan.
- **Motivo:** la clase de S08 fue demasiado larga y el profesor se perdió; faltaban explicaciones de Java (`Collections.shuffle`, bucles, interfaz) y la salida de S09 dependía de cómo se eligiera la bicicleta.
- **Herramientas:** `render.py` comprueba la estructura de los pasos de una guía (opción `--sin-comprobar` para saltarla).

## 2026-11-22

### Contextos de S08 y S09: el torneo y las bicicletas
- **Qué cambia:** la guía de S08 usa **el torneo** y la actividad integradora de S09 usa **las bicicletas**, en lugar de la tienda y de las matrículas propuestas antes. La semilla del generador vale 42 para pruebas y se deja en blanco para uso real. S09 no lleva actividad de reserva.
- **Motivo:** la tienda repetía el contexto de sesiones anteriores. En S09 el alumno tarda unos 75 a 100 minutos en las bicicletas, y los proyectos con error del zip sirven para «encuentra el fallo» en pantalla si sobra tiempo.
- **Material:** `UD03_S08_01` (guía y zip) y `UD03_S09_01` y `UD03_S09_02` (enunciado, solución y zip), en Drive.

### S08 y S09 pasan a ser repaso integrador; `@Autowired`, `@Service` y `@Repository` se ven en UD04
- **Qué cambia:** S08 es una guía que explica el profesor, sin concepto nuevo, y repasa de forma explícita S01 a S07 con una tienda completa. S09 es la actividad integradora, con «encuentra el fallo» de reserva. `@Autowired`, `@Service` y `@Repository` se dejan para la primera sesión de UD04. UD03 se alarga dos sesiones: S10 (jue 26 nov) es el cliente en el navegador y S11 (vie 27 nov) un simulacro de examen. UD04 empieza el lunes 30 nov, con cuatro sesiones antes del 4 dic.
- **Motivo:** en la práctica esas anotaciones se usan dentro de una aplicación Spring Boot, y allí se entienden con controlador, servicio y repositorio delante. UD03 queda como contenedor y beans, y el examen solo evalúa lo practicado.
- **Pendiente:** la programación didáctica lista esas tres anotaciones en los contenidos de UD03; hay que corregirla.

## 2026-11-15

### La actividad de S04 pasa a ser el duelo, con los bots de reserva
- **Qué cambia:** la actividad prevista para después de S03 (la playlist con dos formatos de duración) se sustituye por **el duelo** (guerrero y mago). Se prepara también **los bots** (recepcionista y streamer), por si la clase termina antes.
- **Motivo:** la playlist se veía poco motivadora. El duelo practica lo mismo (`@Primary` y `@Qualifier`) con un ejemplo que engancha más, y los bots añaden métodos que reciben un dato y devuelven un texto.
- **Material:** `UD03_S04_01` a `UD03_S04_04`, en Drive. Los cierres de la guía de S03 y de la solución de la playlist se actualizaron para que no anuncien la playlist.

### S04 es una sesión ligera, de repaso
- **Qué cambia:** S04 no lleva concepto nuevo. Repasa `@Primary` y `@Qualifier` con la guía de S03 y dedica el resto a la actividad.
- **Motivo:** la guía de S03 ocupa la clase de dos horas y no quedó tiempo para practicar. Se prefiere asentar antes que acelerar (criterio 2 de `planificacion.md`).

### La actividad de S03 pasa a S04
- **Qué cambia:** S03 se queda solo con su guía; su actividad se hace en S04.
- **Motivo:** la guía de pagos deja la clase densa para dos horas.

### Nuevo horario: lunes, miércoles, jueves y viernes, 2 horas cada día
- **Qué cambia:** hasta el viernes 13 de noviembre el horario era miércoles 1 h, jueves 3 h y viernes 2 h. A partir del lunes 16 de noviembre son 8 horas a la semana repartidas en cuatro días de 2 h.
- **Motivo:** cambio en el reparto de las horas semanales. S01 a S03 se dieron con el horario anterior.
- **Consecuencia:** la UD03 (18 h) queda en nueve sesiones: S01 a S03 (6 h) y S04 a S09 (12 h), con S09 como colchón.

### Organización del material
- **Qué cambia:** el material se guarda en Drive por unidad y por sesión (`UD03_Spring_Core/S04_Repaso_y_duelo_20261116/`), y los ficheros se numeran según el orden de uso en clase. Los documentos de trabajo (esta guía, `planificacion.md`, `estilo.md`, `seguimiento.csv` y este fichero) pasan al repositorio.
- **Motivo:** seguir el mismo criterio que el material de otros módulos y que cada sesión se prepare en su propio chat de un proyecto de Claude.
