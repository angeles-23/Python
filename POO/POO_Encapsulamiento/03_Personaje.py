# ## Ejercicio 3: Encapsulamiento y Herencia en un Videojuego de Rol

# ### **Objetivo:**
# Aplicar encapsulamiento en una clase base y heredarla en un contexto de videojuegos de rol con interacciones dinámicas.

# ### **Instrucciones:**
# 1. Crea una clase `Personaje` con:
#    - `__nivel` (privado, inicializado en 1)
#    - `__vida` (privado, inicializado en 100)
#    - `subir_nivel()`: Aumenta el nivel en 1 y mejora la vida en 10 puntos.
#    - `recibir_daño(cantidad)`: Reduce la vida si la cantidad es positiva y no deja que sea menor a 0.
#    - `get_nivel()`: Retorna el nivel actual.
#    - `get_vida()`: Retorna la vida actual.

# 2. Crea una subclase `Picaro` que tenga:
#    - `__fuerza` (privado, inicializado en 10).
#    - `atacar()`: Imprime "El pícaro ataca con una fuerza de X!", donde X es el valor de `__fuerza`.
#    - `mejorar_fuerza()`: Aumenta la fuerza en 5 cada vez que se llama.

# 3. Crea una clase `Monstruo` con:
#    - `__vida` (privado, inicializado en 50)
#    - `recibir_daño(cantidad)`: Reduce la vida si la cantidad es positiva y no deja que sea menor a 0.
#    - `get_vida()`: Retorna la vida actual.

# 4. Implementa un menú donde:
#    - Aparezca un monstruo.
#    - El jugador pueda elegir atacar al monstruo.
#    - El pícaro pueda recibir daño del monstruo.
#    - Se muestre la vida actual de ambos personajes tras cada acción.
#    - Se pueda mejorar la fuerza del pícaro.
#    - El juego termine si el pícaro o el monstruo llegan a 0 de vida.

# Prueba la clase creando un `Pícaro`, subiendo de nivel, atacando, mejorando su fuerza y enfrentándose a un `Monstruo` en el menú interactivo.

import os
os.system('cls')

class Personaje():
    def __init__(self):        # No le pasamos parámtros
        self.__nivel = 1        # Atributos privados
        self.__vida = 100

    def subir_nivel(self):
        self.__nivel += 1
        self.__vida += 10

    def recibir_danio(self, cantidad):
        if(cantidad > 0 and self.__vida > cantidad and self.__vida >= 0):
            self.__vida -= cantidad
        else:
            print('El daño no puede ser negativo')
    
    def get_nivel(self):
        return self.__nivel
    
    def get_vida(self):
        return self.__vida
    

class Picaro(Personaje):
    def __init__(self):
        super().__init__()
        self.__fuerza = 10

    def __str__(self):
        return f'Mostruo --> Vida: {self.get_vida()} | Nivel: {self.get_nivel()}'
    
    def atacar(self):
        print(f'El pícaro ataca con una fuerza de {self.__fuerza}!')
    
    def mejorar_fuerza(self):
        self.__fuerza += 5


class Monstruo:
    def __init__(self):
        self.__nivel = 1
        self.__vida = 50
        

    def recibir_danio(self, cantidad):
        if(cantidad > 0 and self.__vida > cantidad and self.__vida >= 0):
            self.__vida -= cantidad
    
    def get_vida(self):
        return self.__vida
    
    def __str__(self):
        return f'Mostruo --> Vida: {self.__vida} | Nivel: {self.__nivel}'
    

def mostrar_menu():
    print('- '*15 + ' M E N U ' + '- '*15)
    print('1. Aparecer un mostruo')
    print('2. Atacar al mostruo')
    print('3. Picaro recibe daño del mostruo')
    print('4. Mostrar vida actual de mostruo y pícaro tras cada acción')
    print('5. Mejorar fuerza del pícaro')
    print('(El juego acabará, si pícaro o monstruo llegan a 0 en vida)\n')



if __name__ == '__main__':
    menu = mostrar_menu()
    opcion = int(input('Elige una opción: '))
    
    picaro = Picaro()

    match opcion:
        case 1:
            mostruo = Monstruo()
            print('Se ha creado un mostruo con las siguientes características')
            print(mostruo)
        case 2:
            print(picaro)
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case _:
            print('Opción incorrecta. Debe ser entre 1-5')
