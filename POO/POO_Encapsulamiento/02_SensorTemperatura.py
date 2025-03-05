# Ejercicio 2: Métodos Privados
# Objetivo: Aplicar encapsulamiento en métodos de una clase.

# Instrucciones:
# Crea una clase SensorTemperatura con los atributos:
# __temperatura (privado, valor inicial 25°C)

# Implementa los métodos:
# __calibrar(): Método privado que imprime "Calibrando sensor...".
# medir_temperatura(): Llama a __calibrar() y devuelve la temperatura.
# set_temperatura(nueva_temp): Modifica la temperatura solo si está en el rango -50 a 150°C.
# Prueba la clase instanciando un objeto y llamando a los métodos.

import os
os.system('cls')

class SensorTemperatura:
    def __init__(self, temperatura = 25):
        self.__temperatura = temperatura

    def __calibrar(self):
        print('Calibrando sensor...')
    
    def medir_temperatura(self):
        self.__calibrar()
        return self.__temperatura
    
    def set_temperatura(self, nueva_temp):
        if nueva_temp > -50 and nueva_temp < 150:
            self.__temperatura = nueva_temp

    def get_saldo(self):
        return self.__temperatura


temperatura = SensorTemperatura()
temperatura._SensorTemperatura__calibrar()
print(temperatura.medir_temperatura())
temperatura.set_temperatura(10)
print(temperatura.get_saldo())