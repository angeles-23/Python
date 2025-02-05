# Crea una clase Vehiculo que permita gestionar un conjunto de vehículos de una flota. La clase debe permitir manejar información de los vehículos y realizar conversiones de unidades de velocidad.

# Requisitos:
# Atributo de clase: cantidad_vehiculos: Un contador que registre cuántos vehículos han sido creados.
# Constructor: Debe recibir la marca del vehículo y su velocidad_kmh (velocidad en kilómetros por hora).
# Método de instancia: mostrar_info(): Muestra la marca y la velocidad del vehículo en km/h.
# Método de clase: vehiculos_totales(): Devuelve la cantidad total de vehículos creados.
# Método estático: convertir_millas(velocidad_kmh): Convierte la velocidad de km/h a millas por hora (1 km/h = 0.621371 mph).

# Casos de Prueba:
#   Crea al menos tres instancias de Vehiculo con diferentes marcas y velocidades.
#   Muestra la información de cada vehículo utilizando mostrar_info().
#   Usa vehiculos_totales() para obtener cuántos vehículos han sido creados.
#   Convierte la velocidad de un vehículo a millas por hora usando convertir_millas() y muestra el resultado.

# Salida esperada
# Marca: Toyota | Velocidad: 120 km/h
# Marca: Ford | Velocidad: 90 km/h
# Marca: BMW | Velocidad: 150 km/h
# Total de vehículos en la flota: 3
# Velocidad de BMW en millas por hora: 93.21 mph


import os
os.system('cls')

class Vehiculo:

    cantidad_vehiculos = 0      # Se le llama con el nombre de la clase

    def __init__(self, marca, velocidad_kmh):
        self.marca = marca
        self.velocidad = velocidad_kmh
        Vehiculo.cantidad_vehiculos += 1
        

    def mostrar_info(self):
        return f"Marca: {self.marca} | Velocidad: {self.velocidad} km/h"
    
    
    @classmethod
    def vehiculos_totales(cls):     # cls: es un metodo de la clase, devuelve return o un print
        return cls.cantidad_vehiculos

    @staticmethod
    def convertir_millas(velocidad_kmh):
        km_millas = 0.621371
        millas = velocidad_kmh * km_millas
        return millas

    

toyota = Vehiculo('Toyota', 120)
ford = Vehiculo('Ford', 90)
bmw = Vehiculo('BMW', 150)

print(toyota.mostrar_info())
print(ford.mostrar_info())
print(bmw.mostrar_info())
print(f'Total de vehiculos en la flota: {Vehiculo.cantidad_vehiculos}')
print('Velocidad de %s en millas por hora: %d mph' %(bmw.marca, Vehiculo.convertir_millas(bmw.velocidad)))