
package pkgswitch;

import java.util.Scanner;

public class Switch {

    public static void main(String[] args) {
        
        // Declaración de Variables
        
        int dia;
        String nombreDia;
        Scanner keyword = new Scanner(System.in);
        
        System.out.println("Ingrese un número del 1 al 7 para seleccionar el día");
        dia = keyword.nextInt();
        
        switch(dia){
            case 1: nombreDia = "Lunes";
                        break;
            case 2: nombreDia = "Martes";
                        break;   
            case 3: nombreDia = "Miércoles";
                        break;
            case 4: nombreDia = "Jueves";
                        break;         
            case 5: nombreDia = "Viernes";
                        break;
            case 6: nombreDia = "Sábado";
                        break;    
            case 7: nombreDia = "Domingo";
                        break;           
            default: nombreDia = "Dia Incorrecto";
        } 
        
        System.out.println("El día de la semana es: " + nombreDia);

    }
    
}
