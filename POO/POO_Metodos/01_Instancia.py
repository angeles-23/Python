#  Ejercicio 1: Métodos de Instancia
# ✔️ Objetivo: Practicar métodos de instancia accediendo y modificando atributos de una instancia de la clase.

# 🔹 Ejercicio:
# Crea una clase CuentaBancaria que tenga:

# Un constructor __init__ que reciba el nombre del titular y el saldo inicial.
# Un método depositar que permita aumentar el saldo de la cuenta.
# Un método retirar que disminuya el saldo, solo si hay suficiente dinero.
# Un método mostrar_saldo que devuelva el saldo actual.


import os
os.system('cls')

class CuentaBancaria():

    def __init__(self, nombre_titular, saldo_inicial):
        self.nombre_titular = nombre_titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        if(self.saldo > 0 and self.saldo > cantidad):
            self.saldo -= cantidad
    
    def mostrar_saldo(self):
        return f'Saldo actual: {self.saldo}'
    
    def __str__(self):
       return f'{self.nombre_titular}, {self.saldo}'


cuenta = CuentaBancaria('Ángeles', 1500)
cuenta.depositar(300)
cuenta.retirar(100)
print(cuenta.mostrar_saldo())           # Saldo actual: 1700
