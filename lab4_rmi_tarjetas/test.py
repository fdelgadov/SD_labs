import unittest
from unittest import mock
from io import StringIO
from atm_simple import Cajero

class CajeroTest(unittest.TestCase):
    def setUp(self):
        self.cajero = Cajero()
        
    def tearDown(self):
        del self.cajero

    def testLeerCuentas(self):
        
        self.cajero.leer_cuentas()
        
        # Verificar que exista una cuenta con usuario "Juan" y saldo 6000
        self.assertIn("Juan", self.cajero.cuentas)
        
        # Verificar que exista una cuenta con usuario "María"
        self.assertNotIn("Maria", self.cajero.cuentas)
        
        # Verificar el saldo de la cuenta Juan
        self.assertEqual(self.cajero.cuentas["Juan"]["saldo"], 6000)
        
        # Verificar saldo erroneo de la cuenta Juan
        self.assertNotEqual(self.cajero.cuentas["Juan"]["saldo"], 5000)
    
    def testDepositar(self):
    # Establecer datos de prueba
        self.cajero.leer_cuentas()
        self.cajero.usuario_actual = "Juan"

        # Redirigir la entrada del usuario
        deposito_input = "5\n"
        expected_output = "\nUsted ha depositado 5\nSu nuevo saldo es 6005\n"

        with mock.patch('builtins.input', side_effect=deposito_input), \
             mock.patch('sys.stdout', new=StringIO()) as output:
            self.cajero.depositar()
            self.assertEqual(output.getvalue().rstrip(), expected_output.rstrip())
            self.assertEqual(self.cajero.monto, 5005)
            self.assertEqual(self.cajero.cuentas["Juan"]["saldo"], 6005)
            
        #Deposito de 0
        deposito_input = "0\n"
        expected_output = "\nValor Erroneo\n"

        with mock.patch('builtins.input', side_effect=deposito_input), \
             mock.patch('sys.stdout', new=StringIO()) as output: 
            self.cajero.depositar()
            self.assertEqual(output.getvalue().rstrip(), expected_output.rstrip())
        
        #Deposito negativo
        deposito_input = "-5\n"
        expected_output = "\nValor Erroneo\n"

        with mock.patch('builtins.input', side_effect=deposito_input), \
             mock.patch('sys.stdout', new=StringIO()) as output: 
            self.cajero.depositar()
            self.assertEqual(output.getvalue().rstrip(), expected_output.rstrip())

    def testRetirar(self):
    # Establecer datos de prueba
        self.cajero.leer_cuentas()
        self.cajero.usuario_actual = "Juan"

        # Redirigiendo la entrada del usuario
        deposito_input = "500\n"
        expected_output = "\nUsted ha retirado 500\nSu saldo es 5500\n"

        with mock.patch('builtins.input', side_effect=deposito_input), \
             mock.patch('sys.stdout', new=StringIO()) as output:
            self.cajero.depositar()
            self.assertEqual(output.getvalue().rstrip(), expected_output.rstrip())
            self.assertEqual(self.cajero.monto, 4500)
            self.assertEqual(self.cajero.cuentas["Juan"]["saldo"], 5500)
            
        # Valor Negativo
        deposito_input = "-500\n"
        expected_output = "\nValor Erroneo\n"

        with mock.patch('builtins.input', side_effect=deposito_input), \
             mock.patch('sys.stdout', new=StringIO()) as output:
            self.cajero.depositar()
            self.assertEqual(output.getvalue().rstrip(), expected_output.rstrip())
        
        # Valor Cero
        deposito_input = "0\n"
        expected_output = "\nValor Erroneo\n"

        with mock.patch('builtins.input', side_effect=deposito_input), \
             mock.patch('sys.stdout', new=StringIO()) as output:
            self.cajero.depositar()
            self.assertEqual(output.getvalue().rstrip(), expected_output.rstrip())
            
        # Valor Excede monto de Cajero
        deposito_input = "5500\n"
        expected_output = "\nImposible realizar el retiro, saldo insuficiente en el cajero\n"

        with mock.patch('builtins.input', side_effect=deposito_input), \
             mock.patch('sys.stdout', new=StringIO()) as output:
            self.cajero.depositar()
            self.assertEqual(output.getvalue().rstrip(), expected_output.rstrip())
        
        # Valor Excede monto de Cuenta
        deposito_input = "5500\n"
        expected_output = "\nImposible realizar el retiro, saldo insuficiente en la cuenta\n"

        with mock.patch('builtins.input', side_effect=deposito_input), \
             mock.patch('sys.stdout', new=StringIO()) as output:
            self.cajero.depositar()
            self.assertEqual(output.getvalue().rstrip(), expected_output.rstrip())
            
        
if __name__ == '__main__':
    unittest.main()