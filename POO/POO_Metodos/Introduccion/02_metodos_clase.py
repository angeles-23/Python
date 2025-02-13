import os
os.system('cls')


import math
print(math.e)

class math2:
    pi = 3.141592653589793
    e = 2.718281828459045

    # Método de clase:
    #   - Siempre reciben 'cls' como primer parámetro
    #   - Se definen con @classmethod
    #   - Pueden acceder y modificar los atributos de clase, pero no los de instancia
    #   - Pueden se llamados desde la clase o desde una instancia

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def mostrar_pi(cls):
        print(cls.pi)
    
    def saludar(self):
        print(f'Hola, soy {self.nombre} y mi numero favorito es {self.mostrar_pi()}')


math2.mostrar_pi()   # Llamado desde la clase
# 2.718281828459045                                                                                        
# 3.141592653589793  

m = math2('Javier')
m.mostrar_pi()
m.saludar()

# Cuando modifica la clase, por ejemplo en un contador de vehiculos o cuando al reiniciar el contador