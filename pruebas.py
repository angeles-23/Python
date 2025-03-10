import os 
os.system('cls')


class Herramienta:
    categoria = 'Software'

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_categoria(self):
        return f'Categoría: {Herramienta.categoria}' # Devuelve el valor del atributo de la clase
    
    @classmethod
    def cambiar_categoria(cls, nueva_categoria): # Modifica la categoría de TODAS las instancias
        cls.categoria = nueva_categoria

    @staticmethod   # Método independiente de la clase y de la instancia
    def utilidad():
        return 'Optimiza procesos específicos'

herramienta = Herramienta('Editor de texto')
Herramienta.cambiar_categoria('Utilidad')
print(herramienta.mostrar_categoria())
