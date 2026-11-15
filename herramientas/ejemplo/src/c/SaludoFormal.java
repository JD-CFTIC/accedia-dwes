package es.accedia.saludos;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Component
@Primary
public class SaludoFormal implements Saludo {

//<saludar>
    // SaludoFormal
    @Override
    public String saludar(String nombre) {
        return "Buenos días, " + nombre + ".";
    }
//</saludar>
}
