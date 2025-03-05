# 📌 Ejercicio 4: Uso combinado de Métodos de Instancia, Clase y Estáticos
# ✔️ Objetivo: Aplicar diferentes tipos de métodos en una misma clase de forma más estructurada.

# 🔹 Ejercicio:
# Crea una clase Vehiculo que tenga:

# Un atributo de clase total_vehiculos que almacene cuántos vehículos han sido creados.
# Un constructor que reciba el modelo y el año de fabricación del vehículo, almacenándolo como un atributo de instancia, e incremente total_vehiculos.
# Un método de instancia detalles que devuelva la información del vehículo.
# Un método de clase contar_vehiculos que devuelva cuántos vehículos existen.
# Un método estático es_vehiculo_moderno que reciba una instancia de Vehiculo y devuelva True si su atributo año_fabricacion es del 2015 en adelante, False en caso contrario.
# Crea varias instancias de Vehiculo y verifica el uso correcto de los métodos.

# 🔹 Ejemplos de instancias:

# # Crear instancias de Vehiculo
# vehiculo1 = Vehiculo("Toyota Corolla", 2010)
# vehiculo2 = Vehiculo("Honda Civic", 2018)
# vehiculo3 = Vehiculo("Ford Focus", 2022)

# # Verificar los detalles de cada vehículo
# print(vehiculo1.detalles())  # Debería mostrar información del Toyota Corolla
# print(vehiculo2.detalles())  # Debería mostrar información del Honda Civic
# print(vehiculo3.detalles())  # Debería mostrar información del Ford Focus

# # Verificar si los vehículos son modernos
# print(Vehiculo.es_vehiculo_moderno(vehiculo1))  # False
# print(Vehiculo.es_vehiculo_moderno(vehiculo2))  # True
# print(Vehiculo.es_vehiculo_moderno(vehiculo3))  # True

# # Contar el total de vehículos creados
# print(Vehiculo.contar_vehiculos())  # Debería mostrar 3
# Crea más instancias y verifica su funcionamiento.

import os 
os.system('cls')

class Vehiculo:
    total_vehiculos = 0     # Atributo de clase

    def __init__(self, modelo, anio):
        self.modelo = modelo    # Atributos de instancia
        self.anio = anio
        Vehiculo.total_vehiculos += 1

    def detalles(self):     # Método de instancia
        return f'El vehiculo {self.modelo} es del año {self.modelo}'

    @classmethod
    def contar_vehiculos(cls):
        return cls.total_vehiculos


    def es_vehiculo_moderno(vehiculo):
        if vehiculo.anio>= 2015:
            return True
        else:
            return False


v1 = Vehiculo('Toyota Corolla', 2019)
v2 = Vehiculo('Terreneitor', 2018)
v3 = Vehiculo('Kawasaki Cargo', 2008)

print(v1.detalles())
print(v2.detalles())
print(v3.detalles())

print(Vehiculo.contar_vehiculos())

print(f'El vehiculo {v1.modelo}, ¿es moderno?: {Vehiculo.es_vehiculo_moderno(v1)}')
print(f'El vehiculo {v2.modelo}, ¿es moderno?: {Vehiculo.es_vehiculo_moderno(v2)}')
print(f'El vehiculo {v3.modelo}, ¿es moderno?: {Vehiculo.es_vehiculo_moderno(v3)}')
