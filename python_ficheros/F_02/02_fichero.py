## Ejercicio
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero `tabla-n.txt` con la tabla de multiplicar de ese número, donde `n` es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import os
os.system('cls')

while True:
    try:
        n = int(input('Introduce un número [1-10]: '))

        if n > 0 and n <= 10:
            break
        else:
            print('Error. Numero incorrecto.')
    except Exception:
        print('Error. Valor incorrecto')



try:
    nombre_fichero = f'./F_02/tabla-{n}.txt'
    f = open(nombre_fichero, 'r')

    contendido = f.readlines()
    print(contendido)
    f.close()
except FileNotFoundError:
    print(f'Error. No existe el archivo')