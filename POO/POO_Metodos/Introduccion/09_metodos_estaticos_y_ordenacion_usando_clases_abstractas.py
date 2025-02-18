# Crear un ejercicio de personajes de Hogwarts con métodos estáticos y ordenación utilizando clases abstractas.

# Definir una clase abstracta 'Hechicero' con:
# - Atributos: 'nombre', 'casa', 'poder_magico'
# - Método abstracto: 'mostrar_info()' (para que cada clase lo implemente)

# Crear 2 subclases: 'Mago' y 'Bruja' que hereden de 'Hechicero' e implementen 'mostrar_info()'.
# - Mago tiene un atributo de instancia: 'lechuza'
# - Bruja tiene un atributo de instancia: 'escoba'
# Implementar método '__str()__'
# Implementar métodos 'cambiar_nombre()' y 'cambiar_casa()'
# Implementar método 'estudiar_para_examenes()' sube el 'poder_magico()' 100 puntos

# Añadir una clase 'UtilidadesHogwarts' con un metodo estático:
# - 'ordenar_por_poder(lista_hechiceros)': Ordena una lista de hechiceros por su nivel de poder magico.
# - 'fusionar_hechiceros': Hay que pasar 2 instancias de mago o bruja. Si ambos son de la misma casa sumamos el poder mágico de ambos hehchiceros. Si son de 2 clases distintas se suma el 75% de cada hechicero

# Probar el código con una lista de 4 magos y 5 brujas. Ordenarlos por poder mágico.

import os 
os.system('cls')

from abc import ABC, abstractmethod


class Hechicero(ABC):
    def __init__(self, nombre, casa, poder_magico):
        self.nombre = nombre
        self.casa = casa
        self.poder_magico = poder_magico
    
    @abstractmethod
    def mostrar_info(self):
        pass

    def __str__(self):
        return f'{self.nombre}'
        
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def cambiar_casa(self, nueva_casa):
        self.casa = nueva_casa
    
    def estudiar_para_examenes(self):
        self.poder_magico += 100


class Mago(Hechicero):
    def __init__(self, nombre, casa, poder_magico, escoba):
        super().__init__(nombre, casa, poder_magico)
        self.escoba = escoba

    def mostrar_info(self):
        return f'Nombre: {self.nombre}, Casa:{self.casa}, Poder mágico: {self.poder_magico}, Escoba:{self.escoba}'
    
    def __str__(self):
        return f'{super().__str__()}, {self.casa}'


class Bruja(Hechicero):
    def __init__(self, nombre, casa, poder_magico, lechuza):
        super().__init__(nombre, casa, poder_magico)
        self.lechuza = lechuza
    
    def mostrar_info(self):
        return f'Nombre: {self.nombre}, Casa:{self.casa}, Poder mágico: {self.poder_magico}, Lechuza:{self.lechuza}'

    def __str__(self):
        return f'{super().__str__()}, {self.lechuza}'



class UtilidadesHogwarts:

    @staticmethod
    def ordenar_por_poder(lista_hechiceros: list):
        lista_ordenada = sorted(lista_hechiceros, key=lambda hechicero: hechicero.poder_magico)
        for hechicero in lista_ordenada:
            print(hechicero)

    @staticmethod
    def fusionar_hechiceros(hechicero1, hechicero2):
        if hechicero1.casa == hechicero2.casa:
            resultado = hechicero1.poder_magico + hechicero2.poder_magico
        else:
            porcentaje_hechicero1 = 0.75 * hechicero1.poder_magico
            porcentaje_hechicero2 = 0.75 * hechicero2.poder_magico
            resultado = porcentaje_hechicero1 + porcentaje_hechicero2
        
        print(resultado)
        return resultado



lista = []
mago1 = Mago('Dynamo', 'Hogwarts', 5, 'Rumba')
lista.append(mago1)

mago2 = Mago('Pconi', 'Hogwarts', 50, 'Flac')
lista.append(mago2)

mago3 = Mago('Ronaldo', 'Slytherin', 5, 'Member')
lista.append(mago3)
UtilidadesHogwarts.ordenar_por_poder(lista)

bruja1 = Bruja('Bruja piruja', 'Hufflpuff', 700, 'Bola') 

UtilidadesHogwarts.fusionar_hechiceros(mago1, mago2)

UtilidadesHogwarts.fusionar_hechiceros(mago2, bruja1)