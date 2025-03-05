# Ejercicio:
# Escribir una función que pida 2 números enteros 'n' y 'm' ambos entre 1 y 10 (hacerlo con comprobación de errores). Leer el fichero 'tabla-n.txt' (si existe) y muestre por pantalla la linea 'm' del fichero (pista: usar 'f.readlines()' para almacenar en un array las lineas del documento). Si el fichero no existe se debe mostrar un pensaje por pantalla para ello.

import os 
os.system('cls')

def solicitar_numeros():
    ''' Solicita dos numeros n y m
    Parametros: 
        None.
    Devuelve:
        n y m
    '''
    while True:
        try:
            n = int(input('Introduce el primer número: '))
            
            if(n >= 1 and n <= 10):
                m = int(input('Introduce el segundo número: '))

                if(m >= 1 and m <= 10):
                    break
                else:
                    print('El segundo número debe estar entre 1 y 10')
            else:
                print('El primer número debe estar entre 1 y 10')

        except Exception as error:
            print('Error. El dato introducido no es un número')

    return n, m


def obtener_lineas_del_archivo():
    '''Imprime una linea concreta de un fichero especifico
    Parametros:
        None.
    Devuelve:
        None, solo imprime.
    '''
    
    fichero = f'tabla-{n}.txt'

    try:
        f = open(fichero, 'r')  # Abre el fichero y lo lee
        lista = (f.readlines())    # Crea una lista con el todas las lineas del fichero
        print(lista) 
        # n = 2  ->  ['2 * 1 = 2\n', '2 * 2 = 4\n', '2 * 3 = 6\n', '2 * 4 = 8\n', '2 * 5 = 10\n', '2 * 6 = 12\n', '2 * 7 = 14\n', '2 * 8 = 16\n', '2 * 9 = 18\n', '2 * 10 = 20\n']
        
        print(lista[m-1])    # Da la linea del archivo según m, y se le resta 1 porque la lista empieza en la posicion 0
        # m = 4-1  ->   2 * 3 = 6
    except FileNotFoundError:
        print(f'Error. No existe el fichero con la tabla del {n}')
    else:
        print(f.read())
        f.close()



if __name__ == '__main__':
    n, m = solicitar_numeros()
    linea = obtener_lineas_del_archivo()