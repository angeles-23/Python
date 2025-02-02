# Ejercicio 2: Constructor con Valores Predeterminados
# Crea una clase Producto con un constructor que acepte dos parámetros: nombre y precio, donde precio tenga un valor predeterminado de 0. Añade un método que permita modificar el precio del producto.

# Prueba creando un objeto sin especificar el precio y otro especificándolo, mostrando los resultados.

import os
os.system('cls')



class Producto:

    def __init__(self, nombre = "null", precio = 0): #Aquí se le da valor a los parametros, se le puedar valores por defecto
        self.nombre = nombre
        self.precio = precio

    # Método para modificar el precio
    def modificar_precio(self, precio):
        self.precio = precio

    # Método para modificar el nombre
    def modificar_nombre(self, nombre):
        self.nombre = nombre
    

    def __str__(self):
        return f"Producto --> Nombre:{self.nombre} - Precio: {self.precio}"


prod_1 = Producto() # Si no le paso nada, usa los valores por defecto del __init__
prod_2 = Producto('Teclado', 50)

print(prod_1)     # Imprime el __self__
print(prod_2.nombre)
print(prod_2.precio)

prod_2.modificar_nombre('Monitor')
prod_2.nombre = "Portatil"             # Otra forma de cambiar el nombre de la variable
prod_2.modificar_precio(300)

print(prod_2)