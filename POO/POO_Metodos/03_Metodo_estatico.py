# 📌 Ejercicio 3: Verificación de Números Primos con Método Estático
# ✔️ Objetivo: Practicar métodos estáticos verificando si un número es primo.

# 🔹 Ejercicio:
# Crea una clase Numeros que incluya:

# Un método estático es_primo que reciba un número entero y devuelva True si es primo, False en caso contrario.
# Un método estático lista_primos que reciba un número entero n y devuelva una lista con todos los números primos hasta n.
# Prueba los métodos sin crear una instancia de la clase.

class Numeros():
    @staticmethod

    def es_primo(numero):
        numero_primo = False

        if numero <= 2:
            for i in range(2, numero):
                ...

        return numero_primo