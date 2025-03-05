import os 
os.system('cls')

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Método de instancia:
#   - Siempre reciben 'self' como primer parámetro
#   - Pueden acceder y modificar los atributos de instancia
#   - Pueden llamar a otros métodos de instancia

    def saludar(self):  # Método de instancia, siempre self y est la primera
        print(f'Hola me llamo {self.nombre} y tengo {self.edad} años.') # Llamo a los tributos de la instancia
        print(f'Hola me llamo {self.nombre} y tengo {self.devolver_la_edad()}') # Llamo a un método de instancia
    
    def devolver_la_edad(self):     # Método de instanca
        return f'Tengo {self.edad} años.'


p = Persona('Javier', 28)
p.saludar()