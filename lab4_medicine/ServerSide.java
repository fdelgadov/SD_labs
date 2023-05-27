package lab4_medicine;

import java.rmi.registry.*;

public class ServerSide {
    public static final int PORT = 1234;
    public static void main(String[] args) throws Exception {
        Stock pharmacy = new Stock();
        pharmacy.addMedicine("Paracetamol", 3.2f, 10);
        pharmacy.addMedicine("Mejoral", 2.0f, 20);
        pharmacy.addMedicine("Amoxilina", 1.0f, 30);
        pharmacy.addMedicine("Aspirina", 5.0f, 40);
        Registry r = LocateRegistry.createRegistry(PORT);
        r.bind("PHARMACY", pharmacy);
        System.out.println("Server ready");
    }
}