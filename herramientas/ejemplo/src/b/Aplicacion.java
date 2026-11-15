package es.accedia.saludos;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Aplicacion {

    public static void main(String[] args) {
//<contexto>
        // Arrancamos el contenedor
        AnnotationConfigApplicationContext contexto =
                new AnnotationConfigApplicationContext("es.accedia.saludos");
//</contexto>
//<usar>
        // Pedimos el saludo y lo escribimos
        Saludo saludo = contexto.getBean(Saludo.class);
        System.out.println(saludo.saludar("Ana"));
//</usar>
//<cerrar>
        // Cerramos el contenedor
        contexto.close();
//</cerrar>
//<cierre>
    }
}
//</cierre>
