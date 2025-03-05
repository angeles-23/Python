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
    def es_primo(n):
        # Primera forma
        # if n < 2:
        #     return False
        
        # if n in(2,3):
        #     return True
        
        # if n % 2 == 0 or n % 3 == 0:
        #     return False
        
        # i = 5
        # while i * i <= n:
        #     if n % i == 0 or n % (1 + 2) == 0:
        #         return False
        #     i += 6
        # return True


        # Segunda forma
        if n <= 1:
            return False
        
        if n == 2:
            return True 

        if n % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

        return True
    

    @staticmethod
    def lista_primos(n):

        lista_numeros_primos = []

        for i in range(0, n+1):
            if(Numeros.es_primo(i)):
                lista_numeros_primos.append(i)

        return lista_numeros_primos


numero = 97
print(f'El número {numero} es {Numeros.es_primo(numero)}')
print(f'Lista numeros primos hasta el {numero}: {Numeros.lista_primos(numero)}')