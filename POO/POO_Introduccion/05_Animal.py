# Ejercicio 5: Herencia y Sobrescritura
# Define una clase base Animal con un método hacer_sonido que imprima:

# "El animal hace un sonido".

# Crea dos clases hijas, Perro y Gato, que sobrescriban el método hacer_sonido con:

# "El perro ladra".
# "El gato maúlla".
# Crea una lista de objetos de ambas clases y recorre la lista llamando al método hacer_sonido.

import os
os.system('cls')


# Si se introducen los self en las funciones, en la lista hay que añadir unos parentesis al llamar a las clases en la lista
class Animal:
    
    def hacer_sonido():
        print('El animal hace un sonido.')


class Perro(Animal):
    def hacer_sonido():
        print('El perro ladra')


class Gato(Animal):
    def hacer_sonido():
        print('El gato maúlla')


animales = [Perro, Gato]

for animal in animales:
    animal.hacer_sonido()
