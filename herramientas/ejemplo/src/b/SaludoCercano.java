package es.accedia.saludos;

import org.springframework.stereotype.Component;

@Component
public class SaludoCercano implements Saludo {

//<saludar>
    // SaludoCercano
    @Override
    public String saludar(String nombre) {
        return "Hola, " + nombre + ".";
    }
//</saludar>
}
