# Planificación: Desarrollo Web en Entorno Servidor (0613)

Este documento recoge el plan de las sesiones y los criterios con los que se reparte el tiempo. El estado de cada sesión (qué material hay, si se ha impartido) está en `seguimiento.csv`, y cada cambio de plan, con su motivo, en `cambios.md`.

## Horario

| Día | Horas |
|---|---|
| Lunes | 2 |
| Miércoles | 2 |
| Jueves | 2 |
| Viernes | 2 |

8 horas a la semana. Hasta el viernes 13 de noviembre el horario era otro (miércoles 1 h, jueves 3 h, viernes 2 h), y las sesiones 1 a 3 se dieron con él.

## UD03. Spring Core

**Horas:** 18. **Idea que lo une todo:** quién crea los objetos y quién los conecta. Spring Framework (sin Spring Boot) antes de Spring Boot.

| Sesión | Fecha | Horas | Problema | Concepto nuevo | Mini aplicación | Actividad | Estado del plan |
|---|---|---|---|---|---|---|---|
| S01 | mié 11 nov | 1 | Una clase necesita a otra | Dependencia e inyección por constructor | Cafetería | Gimnasio (sin Spring) | Impartida |
| S02 | jue 12 nov | 3 | Montar a mano falla al compartir una pieza | Contenedor, bean, `@Component` | Entregas | Playlist | Impartida |
| S03 | vie 13 nov | 2 | Hay dos piezas posibles para lo mismo | `@Primary`, `@Qualifier` | Pagos | Pasa a S04 | Impartida |
| S04 | lun 16 nov | 2 | Repaso de `@Primary` y `@Qualifier` con la guía de S03, y práctica con una actividad relacionada | Ninguno: repaso | Duelo (Guerrero y Mago) | Duelo; de reserva, Bots (Recepcionista y Streamer) | Propuesta |
| S05 | mié 18 nov | 2 | ¿Cuántos objetos crea Spring y cuánto viven? | `@Scope`: singleton y prototype; `@PostConstruct`, `@PreDestroy` | Contador de turnos con carga inicial | Por decidir | Propuesta |
| S06 | jue 19 nov | 2 | Usar una clase que no es nuestra como bean | `@Configuration`, `@Bean` | Generador de códigos de pedido | Por decidir | Propuesta |
| S07 | vie 20 nov | 2 | Cambiar un dato sin recompilar | `@Value` y propiedades | Tienda con IVA configurable | Por decidir | Propuesta |
| S08 | lun 23 nov | 2 | Juntar todo en una aplicación | Capas: `@Service`, `@Repository` | Tienda completa | Por decidir | Propuesta |
| S09 | mié 25 nov | 2 | Verla funcionando y asentar | Ninguno: cliente en el navegador y repaso | La misma tienda | Por decidir | Propuesta |

Las horas suman 18 (6 de S01 a S03 y 12 de S04 a S09). Las sesiones S04 a S09 son una **propuesta pendiente de confirmar**.

## Criterios del plan

1. **Cada sesión termina en una mini aplicación que funciona**, hecha dentro de las horas de clase.
2. **Pocos conceptos nuevos por sesión.** Si una clase queda densa, se mueve la actividad a la sesión siguiente antes que acelerar. Por eso S04 es ligera: repasa S03 y hace su actividad, sin concepto nuevo.
3. **Spring Framework antes que Spring Boot:** el alumno entiende qué hace el contenedor antes de que Boot lo configure por él.
4. **S09 es un colchón:** no lleva concepto nuevo y absorbe retrasos. Si no hace falta, se usa para repaso y práctica. S05 es la sesión más cargada (alcance y ciclo de vida de los beans); si se queda larga, el ciclo de vida pasa a S09.
5. **El número de guías, actividades y soluciones varía por sesión.** Lo fija el planteamiento de cada una.
6. **El ejemplo cambia cada sesión,** pero la estructura se mantiene, para que el alumno reconozca el patrón.

## Ideas para más adelante

- **Cliente en el navegador (S09):** una página con JavaScript que pide datos a la aplicación Spring, con un servidor HTTP que arranca como bean (el que trae Java, sin Spring Boot). Ya está probado con la tienda de pagos.
- **Spring Boot:** vista en el navegador con Thymeleaf, y que los alumnos escriban un cliente para la aplicación de un compañero.
- **Un juego en consola** con las piezas de Spring Core (por ejemplo, una arena donde cada personaje elige su ataque con `@Qualifier`).

## Pendiente de decidir

- Confirmar el plan de las sesiones S04 a S09.
- Qué actividad lleva cada una de S05 a S09.
- Calendario de festivos y de evaluaciones.
- Reparto del resto de unidades del módulo.
