package operadores;

import java.util.Scanner;

public class Operadores {
    public static void main(String[] args) {
        // Ingresar dos números y realizar una operación de suma
        
        // Declaración de Variables
        Scanner keyword = new Scanner(System.in);
        
        double n1, n2, suma;
        
        System.out.println("Ingrese el primer número para la operación: ");
        n1 = keyword.nextDouble();
        
        System.out.println("Ingrese el primer número para la operación: ");
        n2 = keyword.nextDouble();
        
        suma = n1 + n2;
        
        System.out.println("La suma de los dos números es de: " + suma);
        
               
    }
    
}
