# Ejercicio 3: Herencia Multinivel - Clasificación de Animales
# Crea una clase base Animal con un método sonido() que devuelva "Sonido genérico".

# Luego, crea una clase Mamifero que herede de Animal y tenga un método caracteristica() que devuelva "Es un mamífero".

# Por último, crea una clase Gato que herede de Mamifero y sobrescriba sonido() para devolver "Miau".

# Objetivo:
# Crea una instancia de Gato y prueba los métodos sonido() y caracteristica().


import os
os.system('cls')

class Animal:
    def sonido(self):
        return 'Sonido genérico'
    

class Mamifero(Animal):
    def caracteristica(self):
        return 'Es un mamífero'
    
class Gato(Mamifero):
    def sonido(self):
        return 'Miau'

gato = Gato()
print(gato.sonido())
print(gato.caracteristica())