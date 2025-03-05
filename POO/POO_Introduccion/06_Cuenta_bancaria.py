# Ejercicio 6: Encapsulación
# Crea una clase CuentaBancaria con un atributo privado __saldo y métodos para:

# Depositar una cantidad, sumándola al saldo.
# Retirar una cantidad si hay suficiente saldo; de lo contrario, imprime un mensaje indicando que no hay fondos suficientes.
# Consultar el saldo mediante un método público.
# Prueba las operaciones de depósito, retiro y consulta.

import os
os.system('cls')

class CuentaBancaria:
    
    def __init__(self, __saldo):
        self.__saldo = __saldo

    def depositar_cantidad(self, cantidad):
        saldo_actual = self.__saldo + cantidad
        return saldo_actual


    def retirar_cantidad(self, cantidad):

        if(self.__saldo > cantidad):
            saldo_actual = self.__saldo - cantidad
            return saldo_actual
        else:
            print('No hay suficientes fondos')

        
