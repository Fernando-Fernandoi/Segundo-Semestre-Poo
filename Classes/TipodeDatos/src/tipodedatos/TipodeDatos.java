package tipodedatos;

public class TipodeDatos {
    public static void main(String[] args) {
        String nombre = "Victor";
        int edad = 30; // (Ocupa 4 bytes)
        long sueldoMensual = 1900000; // Rango: –9,223,372,036,854,775,808 a 9,223,372,036,854,775,807 (Ocupa 8 bytes)
        short sueldoHora = 18000; // Rango: –32,768 to 32,767 (Ocupa 2 bytes)
        double estatura = 1.75; // Flotante de Doble Presición (Ocupa 8 bytes)
        float pi = 3.14f;  // Decimal simple (Ocupa 4 bytes)
        boolean estado = true;
        char categoria = 'A';
        
        System.out.println("Mi nombre es " + nombre + " tengo " + edad + " y mi estatura es de " + estatura);
        System.out.println("Número PI: " + pi);
        System.out.println("El sueldo mensual es de: " + sueldoMensual);
        System.out.println("El sueldo por hora es de: " + sueldoHora);
        System.out.println("Esto es un booleano:" + estado);
        System.out.println("Categoria:" + categoria);
        
        // Usando printf con marcadores de formato
        System.out.printf("Nombre: %s, Edad: %d, Estatura: %.2f metros%n", nombre, edad, estatura);
    }
    
}
