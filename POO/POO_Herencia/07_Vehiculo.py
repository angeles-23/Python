# Ejercicio 7: Clases con métodos adicionales

# Crea una clase Vehiculo con los atributos:
# marca (str)
# modelo (str)
# velocidad_maxima (int)

# Y los métodos:
# detalles(): Imprime la información del vehículo.
# acelerar(): Imprime "El vehículo está acelerando".

# Luego, crea dos clases derivadas:
# Coche: Agrega un atributo adicional tipo_combustible y sobrescribe acelerar() para imprimir "El coche está acelerando rápidamente".
# Bicicleta: Agrega un atributo tipo (por ejemplo, "montaña" o "ciudad") y sobrescribe acelerar() para imprimir "La bicicleta está tomando velocidad".

# Objetivo:
# Instancia objetos y prueba los métodos.

import os
os.system('cls')

class Vehiculo:
    def __init__(self, marca=str, modelo=str, velocidad_maxima=int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def detalles(self):
        print( f'Marca: {self.marca} | Modelo: {self.modelo} | Velocidad máxima: {self.velocidad_maxima}')

    def acelerar(self):
        print('El vehículo está acelerando')


class Coche(Vehiculo):

    def __init__(self, marca=str, modelo=str, velocidad_maxima=int, tipo_combustible=str):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_combustible = tipo_combustible


    def acelerar(self):
        print('El coche está acelerando rápidamente.')


class Bicicleta(Vehiculo):
    def __init__(self, marca=str, modelo=str, velocidad_maxima=int, tipo=str):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo
    
    def acelerar(self):
        print(f'La bicicleta está tomando velocidad')



vehiculo = Vehiculo('Toyota', 'Corolla', 180)
coche = Coche('Ford','Focus', 200, 'Diesel')
bicicleta = Bicicleta('Trek', 'Domane SLR 9', 45, 'montaña')

vehiculo.detalles()
vehiculo.acelerar()
print(vehiculo.marca)
print(vehiculo.modelo)

print()

coche.detalles()
coche.acelerar()
print(f'Tipo combustible: {coche.tipo_combustible}')

print()

bicicleta.detalles()
bicicleta.acelerar()
print(f'Tipo: {bicicleta.tipo}')