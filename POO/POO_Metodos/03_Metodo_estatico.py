# 📌 Ejercicio 3: Verificación de Números Primos con Método Estático
# ✔️ Objetivo: Practicar métodos estáticos verificando si un número es primo.

# 🔹 Ejercicio:
# Crea una clase Numeros que incluya:

# Un método estático es_primo que reciba un número entero y devuelva True si es primo, False en caso contrario.
# Un método estático lista_primos que reciba un número entero n y devuelva una lista con todos los números primos hasta n.
# Prueba los métodos sin crear una instancia de la clase.

import os, math
os.system('cls')

class Numeros():

    @staticmethod
    def es_primo(numero):
        
        if numero <= 1:
            return False
        
        if numero == 2:
            return True 

        if numero % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(numero))):
            if numero % i == 0:
                return False

        return True

    @staticmethod
    def lista_primos(n):
        numeros_primos = []

        if Numeros.es_primo(n):
            numeros_primos.append(n)



numero = 23
print(f'El número {numero} es {Numeros.es_primo(numero)}')

Numeros.lista_primos(numero)