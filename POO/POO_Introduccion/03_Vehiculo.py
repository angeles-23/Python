# Define una clase Vehiculo que tenga un atributo de clase tipo con el valor "Transporte". El constructor debe aceptar un parámetro marca y asignarlo como atributo de instancia.

# Crea un método que devuelva el tipo y la marca del vehículo.

import os
os.system('cls')


class Vehiculo:
    tipo = "Transporte"    # Atributo de clase, es común a todos las clases(objetos)

    def __init__(self, marca):
        self.marca = marca      # Atributo de instancia

    def obtener_marca(self):
        return self.marca

    def obtener_tipo(self):
        return self.tipo

    def __str__(self):
        return f"Vehiculo --> Marca: {self.marca} - Tipo: {self.tipo}"
    

v = Vehiculo("Toyota")
a = Vehiculo("Audi")
b = Vehiculo("BMW")
print(v)
print(a)
print(b)

print(v.marca)
print(v.tipo)
