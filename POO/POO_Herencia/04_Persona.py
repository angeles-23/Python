# Ejercicio 4: Uso de super() en Herencia Jerárquica
# Crea una clase Persona con los atributos nombre y edad y un método presentacion().

# Luego, crea una clase Profesor que herede de Persona y tenga un atributo adicional materia. Usa super() en el constructor y sobrescribe presentacion() para incluir la materia que enseña.

# Objetivo:
# Crea una instancia de Profesor y llama a presentacion() para comprobar la herencia y reutilización de código.


import os
os.system('cls')

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentacion(self):
        return f'Hola, me llamo {self.nombre} y tengo {self.edad} años.'
    
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def presentacion(self):
        return f'Hola, soy profesor. Me llamo {self.nombre}, tengo {self.edad} y enseño {self.materia}'
    

profesor = Profesor('Angeles', 20, 'Programación')
print(profesor.presentacion())
