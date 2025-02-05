# Ejercicio 1: Crear una Clase Simple
# Crea una clase llamada Persona con los atributos nombre y edad. Añade un método llamado saludar que devuelva un mensaje en el formato:

# "Hola, mi nombre es [nombre] y tengo [edad] años".

# Prueba la clase creando una instancia y llamando al método.

import os 
os.system('cls')


class Persona:
    """Clase de una persona"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    

# Creamos y usamos la instancia del objeto
p = Persona("Javier", 28)
print(p.saludar())