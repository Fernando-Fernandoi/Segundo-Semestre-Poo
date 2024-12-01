import java.util.Scanner;

public class PrecioDeEntrada {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese su edad: ");
        int edad = scanner.nextInt();
        
        int precio;
        if (edad < 5) {
            precio = 0;
        } else if (edad <= 12) {
            precio = 1500;
        } else if (edad <= 17) {
            precio = 3000;
        } else if (edad <= 64) {
            precio = 5000;
        } else {
            precio = 2000;
        }
        
        System.out.println("Su precio de entrada es: $" + precio);
        scanner.close();
    }
}