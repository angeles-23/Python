# 📌 Ejercicio 2: Métodos de Clase (@classmethod)
# ✔️ Objetivo: Trabajar con métodos de clase y atributos compartidos entre instancias.

# 🔹 Ejercicio:
# Crea una clase Tienda que tenga:

# Un atributo de clase total_tiendas que cuente cuántas tiendas se han creado.
# Un constructor __init__ que reciba el nombre de la tienda y aumente el contador de total_tiendas.
# Un método de clase cantidad_tiendas que devuelva el número total de tiendas creadas.
# Crea varias instancias de Tienda y usa el método de clase para verificar cuántas tiendas hay.



import os 
os.system('cls')

class Tienda:
    total_tiendas = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Tienda.total_tiendas += 1

    @classmethod
    def cantidad_tiendas(cls):
        return f'Tiendas creadas: {cls.total_tiendas}'
    

sprinter = Tienda('Sprinter')
lefties = Tienda('lefties')
nike = Tienda('nike')
adidas = Tienda('adidas')

print(Tienda.cantidad_tiendas())
# Tiendas creadas: 4