package lab4_rmi;

import java.rmi.registry.*;

public class CalculatorServer {
    final int PUERTO = 1100;
    public CalculatorServer() throws Exception {
        Registry registry = LocateRegistry.createRegistry(PUERTO);
        System.out.println("Servidor escuchando en el puerto " + String.valueOf(PUERTO));
        registry.bind("Calculator", new CalculatorImpl()); // Registrar calculadora
    }

    public static void main(String args[]) throws Exception {
        new CalculatorServer();
    }
}