# Una clase abstracta es una clase que no puede instancias directamente, pero sirve como plantilla para otras clases.
# Un método abstracto es un método definido en una clase abstracta que debe ser implementado por otras clases HIJAS.

import os
os.system('cls')


# tenemos que importar de la libreria 'abc':'ABC' y 'abstractmethod'
from abc import ABC, abstractmethod


class Dispositivo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod
    def encender(self):
        pass


class Telefono(Dispositivo):
    def encender(self):
        return f'El teléfono {self.modelo} {self.marca} se está encendiendo.'

class Portatil(Dispositivo):
    def encender(self):
        return f'El portátil {self.marca} {self.modelo} se enciende correctamente'

class Monitor(Dispositivo):
    def encender(self):
        return f'El monitor {self.marca} {self.modelo} se enciende correctamente'


t = Telefono('A71', 'Samsung')
print(t.encender())