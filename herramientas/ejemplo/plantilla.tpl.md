# Ejemplo: saludos

Esta plantilla de ejemplo muestra cómo se usan los marcadores. No es material de clase.

Al final, la aplicación hará esto:

@@out:c@@

## Paso 1. Una sola opción

**Qué hacemos y para qué.** Una interfaz con una opción.

Escribimos dentro de las llaves:

@@frag:a/Saludo.java:metodo@@

De momento, así queda la interfaz `Saludo`:

@@parcial:a/Saludo.java:metodo@@

Esta es la clase completa:

@@code:a/SaludoFormal.java@@

Resultado:

@@out:a@@

## Paso 2. Dos opciones

Ejecutamos otra vez y falla:

@@err:b@@

## Paso 3. La clase final

@@code:c/SaludoFormal.java@@
