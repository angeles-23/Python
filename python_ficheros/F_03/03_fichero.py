## Ejercicio 3
# Escribir una función que pida dos números `n` y `m` entre 1 y 10 (comprobación de errores), lea el fichero `tabla-n.txt` (si existe, en caso contrario mostrar error) con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero (pista: usa `f.readlines()` para almacenar en un array las lineas del documento). Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import os 
os.system('cls')


def pedir_numeros():

    while True:

        try:
            n = int(input('Número n [1-10]: '))

            if(n > 0 and n <= 10):
                
                while True:
                    try:
                        m = int(input('Número m [1-10]: '))

                        if not (m > 0 and m <= 10):
                            print('Error: m incorrecto. Vuelve a intentarlo.')
                        else:
                            break

                    except Exception:
                        print('Error. Valor incorrecto de m')
                break

            else:
                print('Error: n incorrecto. Vuelve a intentarlo')

        except ValueError:
            print('Error. Valor incorrecto de n')

    return n, m

def buscar_fichero(n,m):
    try:
        f = open(f'./F_03/tabla-{n}.txt', 'r')
        contenido = f.readlines()
        print(contenido)
        f.close()

        f = open(f'./F_03/tabla-{n}.txt', 'w')

        for i in range(1,11):
            f.write(f'{n} * {i} = {n*i}\n')

        linea_buscada = contenido[m-1]
        print(linea_buscada)

        f.close()
    except FileNotFoundError:
        print('Error. No existe el fichero')

        


if __name__ == '__main__':
    n,m = pedir_numeros()
    fichero = buscar_fichero(n,m)
