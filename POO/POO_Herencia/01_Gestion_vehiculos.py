# Ejercicio 1: Herencia Simple - Gestión de Vehículos
# Crea una clase base llamada Vehiculo con los siguientes atributos y métodos:

# Atributos:
# marca (str)
# modelo (str)

# Métodos:
# descripcion(): Devuelve una cadena con la marca y el modelo.
# Luego, crea una clase Moto que herede de Vehiculo y sobrescriba descripcion() para agregar un mensaje indicando que es una moto.

# Objetivo:
# Crea una instancia de Moto y llama al método descripcion() para comprobar el resultado.
import os
os.system('cls')

class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo}'
    

class Moto(Vehiculo):
    def descripcion(self):
        return f'{super().descripcion()} es una moto'
        # return f'Marca: {self.marca} | Modelo: {self.modelo} es una moto'


moto = Moto('Yamaha', 'MT-07')
print(moto.descripcion())