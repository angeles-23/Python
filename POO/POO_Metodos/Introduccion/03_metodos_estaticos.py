# Los métodos estáticos son independientes de la clase y de las instancias.
# No pueden modificar ni acceder a atributos de instancia o de clase

import os 
os.system('cls')


import math

class Daw:
    numero_alumnos = 0

    def __init__(self, curso):
        self.curso = curso
        Daw.numero_alumnos += 1

    # Se define un método estático con '@staticmethod':
    @staticmethod
    def sumar(a, b):    # No recibe ni 'self' ni 'cls'. Funciona como funciones normales.
        return a + b
        # No se puede acceder a los self

    def cambiar_curso(self, nuevo_curso):
        self.curso = nuevo_curso
    
print(Daw.sumar(8,15))
print(math.pow(5,2))