package condicionales;

import java.util.Scanner;

public class Condicionales {

    public static void main(String[] args) {
        
        int edad;
        boolean token = true;
        Scanner keyword = new Scanner(System.in);
        
        System.out.println("Ingrese tu edad para acceder a la página:");
        edad = keyword.nextInt();

        if (edad > 18 && token == true){
            System.out.println("¡Tienes un Token y Eres mayor de 18 años!");
        } else if (edad == 18 && token == true){
            System.out.println("¡Tienes un Token y Tienes exactamente 18 años!");
        } else{
            System.out.println("¡Eres menor de 18 años! ¡No puedes acceder!");
        }
            
    }
    
}
