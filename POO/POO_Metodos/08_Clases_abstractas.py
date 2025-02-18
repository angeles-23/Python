# ### 📌 **Ejercicio 8: Implementación de una Jerarquía de Transporte con Clases Abstractas**
# ✔️ **Objetivo:** Utilizar clases y métodos abstractos para modelar diferentes tipos de transporte.

# 🔹 **Ejercicio:**
# Crea una clase abstracta `Transporte` con:
# - Un constructor que reciba la velocidad máxima del transporte.
# - Un método abstracto `tipo_transporte`, que deberá ser implementado por las clases derivadas.

# Crea dos clases `Automovil` y `Bicicleta` que hereden de `Transporte`:
# - `Automovil` deberá definir `tipo_transporte` y devolver `"Automóvil - Transporte motorizado"`.
# - `Bicicleta` deberá definir `tipo_transporte` y devolver `"Bicicleta - Transporte ecológico"`.

# Crea instancias de ambas clases y muestra su tipo de transporte.


import os
os.system('cls')

from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, velocidad_maxima):
        self.velocidad_maxima= velocidad_maxima
    
    @abstractmethod
    def tipo_transporte(self):
        pass


class Automovil(Transporte):   # No hace falta hacer el init, lo hereda. Es algo especial de la clase abstracta

    def __init__(self, vm, marca):
        super().__init__(vm)
        self.marca = marca

    def tipo_transporte(self):
        return f'{self.marca} Automóvil - Transporte motorizado tiene una velocidad máxima de {self.velocidad_maxima}'


class Bicicleta(Transporte):

    def __init__(self, velocidad_max, color):
        super().__init__(velocidad_max)
        self.color = color

    def tipo_transporte(self):
        return f'Bici - Transporte ecológico tiene una velocidad máxima de {self.velocidad_maxima} y es de color {self.color}'
    

automovil = Automovil(100, 'Peugeot')
print(automovil.tipo_transporte())
bici = Bicicleta(50, 'negro')
print(bici.tipo_transporte())