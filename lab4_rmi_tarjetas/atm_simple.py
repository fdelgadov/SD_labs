import csv

class Cajero:
    def __init__(self):
        self.continuar = True
        self.monto = 5000
        self.cuentas = {}

    def leer_cuentas(self):
        with open('names.csv', newline='') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            for row in reader:
                usuario = row[0]
                contraseña = row[1]
                saldo = int(row[2])
                self.cuentas[usuario] = {'contraseña': contraseña, 'saldo': saldo}

    def contraseña(self):
        self.leer_cuentas()
        contador = 1
        while contador <= 3:
            user = input("Ingrese su usuario: ")
            password = input("Ingrese su contraseña: ")
            if user in self.cuentas and password == self.cuentas[user]['contraseña']:
                print("Contraseña correcta")
                self.usuario_actual = user
                break
            else:
                print(f"Contraseña incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("No puede realizar operaciones.")
                    self.continuar = False
                contador += 1

    def menu(self):
        self.contraseña()
        opcion = 0
        while opcion != "5":
            print("""Bienvenido al cajero automático
                    ******Menú******
                    1- Depositar
                    2- Retirar
                    3- Ver saldo
                    4- Ver monto disponible del cajero
                    5- Salir""")
            opcion = input("Su opción es: ")
            if self.continuar:
                if opcion == "1":
                    self.depositar()
                elif opcion == "2":
                    self.retiro()
                elif opcion == "3":
                    self.ver()
                elif opcion == "4":
                    self.ver_monto_cajero()
                elif opcion == "5":
                    print("Programa finalizado")
                else:
                    print("No existe esa opción")
            else:
                if opcion in "123":
                    print("Imposible realizar esa operación")
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("No existe esa opción")

    def depositar(self):
        dep = int(input("Ingrese su monto a depositar: "))
        if (dep <= 0):
            print ("Valor erroneo")
        else:
            print("Usted ha depositado", dep)
            self.monto += dep
            self.cuentas[self.usuario_actual]['saldo'] += dep
            print(f"Su nuevo saldo es {self.cuentas[self.usuario_actual]['saldo']}")

    def retiro(self):
        retirar = int(input("¿Cuánto desea retirar? : "))
        if(retirar<=0):
            print ("Valor Erroneo")
        else:
            saldo_cuenta = self.cuentas[self.usuario_actual]['saldo']
            if saldo_cuenta >= retirar and self.monto >= retirar:
                print(f"Usted ha retirado: {retirar}")
                self.monto -= retirar  # Reduce el saldo total del cajero
                self.cuentas[self.usuario_actual]['saldo'] -= retirar  # Reduce el saldo de la cuenta individual
                print(f"Su nuevo saldo es {self.cuentas[self.usuario_actual]['saldo']}")
            elif saldo_cuenta < retirar:
                print("Imposible realizar el retiro, saldo insuficiente en la cuenta")
            else:
                print("Imposible realizar el retiro, saldo insuficiente en el cajero")

    def ver(self):
        print("Su saldo es:", self.cuentas[self.usuario_actual]['saldo'])
    
    def ver_monto_cajero(self):
        print("El monto disponible del cajero es:", self.monto)
        
cajero = Cajero()
cajero.menu()
