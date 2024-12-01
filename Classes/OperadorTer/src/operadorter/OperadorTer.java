package operadorter;

import java.util.Scanner;

public class OperadorTer {

    public static void main(String[] args) {
        double promedio;
        String condicion;
        
        Scanner keyword = new Scanner(System.in);
        
        System.out.println("Ingrese el promedio del estudiante:");
        promedio = keyword.nextDouble();
        
        condicion = (promedio >= 4) ? "Aprobado" : "Reprobado";
        
        System.out.println("El estudiante tiene un promedio de " + promedio + " y esta " + condicion);
        
    }
    
}
