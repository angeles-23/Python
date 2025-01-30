# Ejercicio 4: Métodos de Clase y Métodos Estáticos
# Crea una clase Banco con un atributo de clase tasa_interes inicializado a 0.05.

# Define un método de clase que permita actualizar la tasa de interés.
# Añade un método estático llamado convertir_moneda que reciba un valor en dólares y lo convierta a euros (asume una tasa fija de 0.85).
# Prueba la clase actualizando la tasa de interés y utilizando el método estático.


import os
os.system('cls')

class Banco:
    def __init__(self, tasa_intereses = 0.05):
        self.tasa_intereses = tasa_intereses

    def modificar_intereses(self):
        return self.tasa_intereses
    
    @staticmethod
    def convertir_moneda(dolares):
        euros = (dolares*1) / 0.85
        return euros
    


banco = Banco(10)
banco.modificar_intereses(1)

print(banco.convertir_moneda(10))