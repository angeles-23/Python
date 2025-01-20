import os
os.system('cls')

# Escribe un factorial recursivo en Python que calcule el factorial de un número entero no negativo utilizando recursividad
# - Crea una función llamada factorial(n) que reciba un número entero como parámetro y devuelva su factorial 
# - El programa debe pedir al usuario un número entero positivo y mostrar su factorial calculado mediante la función implementada
# - Asegúrate de maneja correctamente el caso base para la recursión


def factorial(n):
    factorial = 1

    for i in range(1, n+factorial):
        factorial *= i

    return factorial


if __name__ == '__main__':
    try:
        numero = int(input('Introduce un número: '))
        factorial_calculado = factorial(numero)

        if(numero >= 0):
            print(f'El factorial de {numero} es {factorial_calculado}')
        else:
            print('El número %d no tiene factorial porque no puede ser negativo' %(numero))
            
    except Exception as error:
        print(f'Error. El dato introducido no es un número')