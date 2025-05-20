#!usr/bin/python3

import subprocess, sys

ERROR_DE_FORMATO_DE_OPCION = '❌    Error tipo formato'

def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]

    if(comprobar_argumentos(argumentos) == False):
        termino = input('Introduce el término a buscar: ')
        directorio = input('Introduce el directorio donde buscar: ')

        while True:
            mostrarMenu()
            try:
                opcionMenu = int(input('Selecciona una opción: '))

                if(opcionMenu > 0 and opcionMenu < 4):
                    match(opcionMenu):
                        case 1:
                            ...

                        case 2:
                            ...

                        case 3:
                            print('Saliendo del programa...')
                            sys.exit(1)
                    
                else:
                    print('Error: Fuera del rango [1-3]')
            except ValueError:
                print(ERROR_DE_FORMATO_DE_OPCION)
    else:
        comprobar_argumentos(argumentos)


def limpiar_pantalla():
    subprocess.run(['clear'])

def mostrarMenu():
    print('\n¿Qué deseas hacer?')
    print('1. Nueva búsqueda con mismo directorio')
    print('2. Cambiar directorio')
    print('3. Salir del programa')

def comprobar_argumentos(argumentos):

    if(len(argumentos)) != 2:
        return False
    
    if(argumentos[0] == ''):
        return False
    
    if(argumentos[1] == ''):
        return False

    return True

def verificar_ejecucion(termino, directorio):
    ...



if __name__ == '__main__':
    main()