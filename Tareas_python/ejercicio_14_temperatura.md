# 14. TEMPERATURA
Escribe un programa en Python que convierta temperaturas entre grados Celsius y Fahrenheit.
 -  Implementa dos funciones:
    1.  celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y la convierta a grados Fahrenheit.
    2.  fahrenheit_a_celsius(fahrenheit) que reciba una temperatura en grados Fahrenheit y la convierta a grados Celsius.
 -  El programa debe permitir al usuario elegir el tipo de conversión que desea realizar e introducir la temperatura correspondiente.



``` python
import os
os.system('cls')


def mostrar_menu():
    print('-'*30)
    print('%8s TEMPERATURAS' % (' '))
    print('-'*30)
    print('1. Celsius --> Fahrenheit')
    print('2. Fahrenheit --> Celsius')


def solicitar_opcion_correcta():
    while True:
        try:
            opcion = int(input('   Elige una opción [1-2]: '))

            if(opcion == 1 or opcion == 2): 
                return opcion
            else:
                print('Error. La opción debe ser entre 1-2.\n')

        except Exception as e:
            print('Error. Tienes que introducir un número.\n')


def solicitar_grados_correctos():
    while True:
        try:
            grad = float(input('Introduce una cantidad de grados: '))
            return grad
        
        except Exception as error:
            print('Error. El dato introducido debe ser un número.')


def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8



if __name__ == '__main__':
    menu = mostrar_menu()
    opcion = solicitar_opcion_correcta()
    
    match opcion:
        case 1:
            grados_C = solicitar_grados_correctos()
            grados_C_a_F = celsius_a_fahrenheit(grados_C)
            print('%7s %.2f ºC = %.2f ºF' % (' ', grados_C, grados_C_a_F))
        case 2:
            grados_F = solicitar_grados_correctos()
            grados_F_a_C = fahrenheit_a_celsius(grados_F)
            print('%7s %.2f ºF = %.2f ºC' % (' ', grados_F, grados_F_a_C))
    
    print('Saliendo del programa...')
    
```




