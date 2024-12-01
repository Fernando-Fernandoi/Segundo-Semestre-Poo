package ciclos;
import java.util.Scanner;

public class Ciclos {

    public static void main(String[] args) {
        int contador = 0;
        int i = 0;
        int j;
        
        System.out.println("############### CICLO DO-WHILE ###############");
        //Do-While
        do{
            System.out.println("Estoy en la vuelta N° " + contador);
            contador += 1;
        } while (contador<=10);
        
         System.out.println("############### CICLO WHILE ###############");

       //While
       while(i <= 10){
           System.out.println("Vuelta N° " + i);
           i++;
       }
       
       //For
       System.out.println("############### FOR ###############" );

       for(j = 0; j <= 10; j++){
           System.out.println("La Vuelta N° " + j);
       }
       
       
       System.out.println("############### BUCLE INFINITO ###############" );
       
       boolean flag = true;
       Scanner keyword = new Scanner(System.in);
       String respuesta;
       
       while(flag == true){
           System.out.println("¿Quieres terminar el programa? (Si/No)");
           respuesta = keyword.next();
           
           if(respuesta.equalsIgnoreCase("si")){
               flag = false;
           }
       }
    }
    
}
