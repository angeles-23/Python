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
        if(cantidad > 0):
            self.__vida -= cantidad
            if(self.__vida < 0):
                self.__vida = 0
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

    def atacar(self):
        print(f'El pícaro ataca con una fuerza de {self.__fuerza}!')
    
    def mejorar_fuerza(self):
        self.__fuerza += 5
    
    def __str__(self):
        return f'Picaro --> Vida: {self.get_vida()} | Nivel: {self.get_nivel()}'

    def mostrar_fuerza(self):
        return self.__fuerza


class Monstruo:
    def __init__(self):
        self.__nivel = 1
        self.__vida = 50
        
    def recibir_danio(self, cantidad):
        if(cantidad > 0):
            self.__vida -= cantidad
            if(self.__vida < 0):
                self.__vida = 0
    
    def get_vida(self):
        return self.__vida
    
    def __str__(self):
        return f'Mostruo --> Vida: {self.__vida} | Nivel: {self.__nivel}'
    

def mostrar_menu():
    print('- '*15 + ' M E N U ' + '- '*15)
    print('1. Aparecer un mostruo')
    print('2. Atacar al mostruo')
    print('3. Picaro recibe daño del mostruo')
    print('4. Mejorar fuerza del pícaro')
    print('(El juego acabará, si pícaro o monstruo llegan a 0 en vida)\n')


if __name__ == '__main__':

    picaro = Picaro()
    monstruo = Monstruo()

    while monstruo.get_vida() > 0 and picaro.get_vida() > 0:
        try:
            menu = mostrar_menu()
            opcion = int(input('Elige una opción: '))
            
            match opcion:
                case 1:
                    print('Se ha creado un mostruo con las siguientes características:')
                case 2:
                    danio = int(input('Cantidad de daño para el monstruo: '))
                    monstruo.recibir_danio(danio)
                case 3:
                    danio = int(input('Cantidad de daño para el picaro: '))
                    picaro.recibir_danio(danio)
                case 4:
                    picaro.mejorar_fuerza()
                    print(f'Fuerza: {picaro.mostrar_fuerza()}')
                case _:
                    print('Opción incorrecta. Debe ser entre 1-5')
            
            print(f'{monstruo}    -    {picaro}')

            if monstruo.get_vida() <= 0:
                print('Has matado a monstruo.')
                break

            if picaro.get_vida() <= 0:
                print('Has matado a picaro')
                break

            print('\n')

        except Exception as error:
            print(f'Se ha producido un error. Vuelve a intentarlo')