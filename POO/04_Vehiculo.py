# Ejercicio 4: Encapsulamiento y Herencia
# Objetivo: Aplicar encapsulamiento en una clase base y heredarla.

# Instrucciones:
# Crea una clase Vehiculo con:
# __velocidad (privado, inicializado en 0)
# acelerar(cantidad): Aumenta la velocidad si la cantidad es positiva.
# frenar(cantidad): Reduce la velocidad sin que sea menor a 0.
# get_velocidad(): Retorna la velocidad actual.

# Crea una subclase Coche que tenga:
# marca (público)
# __modo_sport (privado, inicializado en False)
# activar_sport(): Activa __modo_sport e imprime "Modo Sport activado!".

# Prueba la clase creando un Coche, acelerando, frenando y activando el modo sport.


import os
os.system('cls')

class Vehiculo:
    def __init__(self):
        self.__velocidad = 0

    def acelerar(self, cantidad):
        if(cantidad > 0):
            self.__velocidad += cantidad

    def frenar(self, cantidad):
        if(cantidad > 0 and self.__velocidad > 0):
            self.__velocidad -= cantidad

    def get_velocidad(self):
        return self.__velocidad


class Coche(Vehiculo):
    def __init__(self, marca):
        super().__init__()
        self.marca = marca
        self.__modo_sport = False

    def activar_sport(self):
        self.__sport = True
        print('Modo Sport activado!')

    def __str__(self):
        return f'Coche -> Marca: {self.marca}  |  Velocidad: {self.get_velocidad()}'  # Otra forma: {self._Vehiculo__velocidad}



# Llamar a un atributo privado
# p = Persona(_Persona__vida)

# Llamar a un metodo privado fuera de la clase:
# Crear un objeto y llamar a -> objeto._Clase__metodoPrivado()       Es mejor usar getter y setter
# Para llamar al metodo get -> self.get_velocidad()

coche = Coche('Audi')
print(coche)
coche.acelerar(100)
print(coche)
coche.activar_sport()
print(coche)