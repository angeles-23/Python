# Ejercicio 1: Atributos Privados y Métodos Getter/Setter
# Objetivo: Comprender el uso de atributos privados y métodos getter y setter.

# Instrucciones:
# Crea una clase CuentaBancaria con los siguientes atributos:
# titular (público)
# __saldo (privado)

# Implementa los métodos:
# depositar(cantidad): Aumenta el saldo si la cantidad es positiva.
# retirar(cantidad): Reduce el saldo si la cantidad es menor o igual al saldo disponible.
# get_saldo(): Retorna el saldo actual.
# set_saldo(nuevo_saldo): Permite modificar el saldo solo si el valor es mayor o igual a 0.

# Prueba la clase creando una cuenta y manipulando el saldo con estos métodos.


import os
os.system('cls')

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular                      # Atributo publico
        self.__saldo = saldo_inicial                # Atributo privado

    def depositar(self, cantidad):
        """Aumenta el saldo si la cantidad es positiva"""
        if cantidad > 0:
            self.__saldo += cantidad
            print('Depósito exitoso')
        else:
            print('La cantidad a depositar tiene que ser positiva')

    def retirar(self, cantidad):
        """Retira el saldo si la cantidad es menor o igual al saldo disponible"""
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print('Retiro exitoso.')
        else:
            print('Retiro insuficiente o cantidad inválida')
    

    # Cuando son privados:
    # Getter
    def get_saldo(self):
        return self.__saldo
    
    # Setter
    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo
    
    # Métodos privado
    def __cuenta_privada(self):
        print('Esta cuenta es privada')



cuenta_corriente = CuentaBancaria('Javier', 18500)
print(cuenta_corriente.titular)

# Acceder objeto privado (otra forma) --> objeto._nombreClase__nombreAtributo
print(cuenta_corriente.get_saldo())
print(cuenta_corriente._CuentaBancaria__saldo)

# Acceder métodos_privados
print(cuenta_corriente._CuentaBancaria__saldo)
cuenta_corriente._CuentaBancaria__cuenta_privada()