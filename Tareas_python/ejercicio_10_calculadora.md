# 10. CALCULADORA
Calculadora con manejo de excepciones y menú interactivo
Crea un programa en Python que simule una calculadora interactiva. El programa debe cumplir con los siguientes requisitos:

Menú interactivo:

    El programa debe mostrar un menú con las siguientes opciones:
        1. Sumar dos números.
        2. Restar dos números.
        3. Multiplicar dos números.
        4. Dividir dos números.
        5. Salir del programa.

    Entrada del usuario:
        Los usuarios seleccionan una opción introduciendo el número correspondiente.
        El programa debe solicitar dos números para realizar la operación seleccionada.

Manejo de excepciones con try-except:

    Captura los siguientes errores:
        El usuario introduce un valor no numérico al seleccionar una opción o introducir números.
        Intento de división por cero.
        Selección de una opción fuera del rango permitido (1-5).

Comportamiento del programa:
    El programa debe continuar ejecutándose hasta que el usuario elija la opción 5 (Salir).
    Si ocurre un error, el programa debe mostrar un mensaje adecuado y permitir al usuario intentarlo de nuevo.


``` python
import os
os.system('cls')


def mostrar_menu():
    print('-'*33)
    print('%1s %20s %10s' %('|','Calculadora','|'))
    print('-'*33)
    print('%1s %-28s %2s' % ('|', '1. Sumar dos números', '|'))
    print('%1s %-28s %2s' % ('|', '2. Restar dos números', '|'))
    print('%1s %-28s %2s' % ('|', '3. Multiplicar dos números', '|'))
    print('%1s %-28s %2s' % ('|', '4. Dividir dos números', '|'))
    print('%1s %-28s %2s' % ('|', '5. Salir del programa','|'))
    print('-'*33)


def solicitar_opcion():
    while True:
        try:
            opcion = int(input('Introduce una opción [1-5]: '))

            if opcion>0 and opcion<6:
                return opcion
            else:
                print('Error. La opciones son entre 1-5.\n')

        except Exception as e:
            print('Error. Introduce una número.')


def solicitar_primer_numero():
    while True:
        try:
            numero1 = input('Introduce el primer número: ')
           
            if numero1.isnumeric():
                return int(numero1)
            else:
                print('Por favor introduzca un número válido')

        except Exception as e:
            print('El dato introducido no es un número')


def solicitar_segundo_numero():
    while True:
        try:
            numero2 = input('Introduce el segundo número: ')
            if numero2.isnumeric():
                return int(numero2)
            else:
                print('Por favor introduzca un número válido')
        except Exception as e:
            print('El dato introducido no es un número')


def calcular_suma(num1, num2):
    return num1 + num2


def calcular_resta(num1, num2):
    return num1 - num2


def calcular_multiplicacion(num1, num2):
    return num1 * num2


def calcular_division(num1, num2):
    while True:
        try:
            if num2 != 0:
                return num1 / num2
            else:
                print('No se puede dividir entre 0')
                num2 = int(input('Introduce un nuevo valor para el segundo número: '))
                return num1 / num2
        except Exception as e:
            print('Error. No se puede dividir por 0')



if __name__ == '__main__':

    while True:
        menu = mostrar_menu()
        opcion = solicitar_opcion()
       
        if opcion == 5:
            print('Saliendo del programa...')
            break
        else:
            numero1 = solicitar_primer_numero()
            numero2 = solicitar_segundo_numero()

            match opcion:
                case 1:
                    suma = calcular_suma(numero1, numero2)
                    print('%d + %d = %d' % (numero1, numero2, suma))
                case 2:
                    resta = calcular_resta(numero1, numero2)
                    print('%d - %d = %d' % (numero1, numero2, resta))
                case 3:    
                    multiplicacion = calcular_multiplicacion(numero1, numero2)
                    print('%d * %d = %d' % (numero1, numero2, multiplicacion))
                case 4:
                    division = calcular_division(numero1, numero2)
                    print('%d / %d = %.2f' % (numero1, numero2, division))
                case 5:
                    print('Saliendo del programa...')
            print('')
```

