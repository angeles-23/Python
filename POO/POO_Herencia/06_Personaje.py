# Ejercicio 6: Sistema de personajes en un juego
# Crea una clase base llamada Personaje con los siguientes atributos y métodos:

# Atributos:
# nombre (str)
# vida (int)

# Métodos:
# atacar(): Imprime "El personaje ataca".
# recibir_danio(puntos): Resta puntos a vida e imprime "Vida restante: [vida]".
# Luego, crea dos clases derivadas:

# Guerrero:
# Sobrescribe atacar() para imprimir "El Guerrero golpea con su espada!".

# Mago:
# Sobrescribe atacar() para imprimir "El Mago lanza un hechizo!".

# Objetivo:
# Crea instancias de Guerrero y Mago, haz que ataquen y que reciban daño.

import os
os.system('cls')


class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
    
    def atacar(self):
        return f'El personaje ataca'
    
    def recibir_danio(self, puntos):
        return f'Vida restante: {self.vida-puntos}'
    


class Guerrero(Personaje):
    def atacar(self):
        return f'El Guerrero golpea con su espada!'


class Mago(Personaje):
    def atacar(self):
        return f'El Mago lanza un hechizo!'
    

guerrero = Guerrero('Manuel', 100)
mago = Mago('German', 100)

print(mago.atacar())
print(mago.recibir_danio(15))
print(guerrero.atacar())
print(guerrero.recibir_danio(20))