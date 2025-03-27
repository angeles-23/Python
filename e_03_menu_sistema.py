#! usr/bin/python

# IMPORTAR FICHEROS
import e_01_limpiar_pantalla  # Opción 1: Importa el fichero entero
from e_01_limpiar_pantalla import clear_screen  # Opción 2: Desde el fichero importa una funcion específica

# LLAMAR FUNCIONES
e_01_limpiar_pantalla.clear_screen    # Opción 1: LLamar al fichero y seguido a la función separada por un punto
clear_screen() # Opción 2: Escribir la función específica

import e_02_informacion_sistema
import subprocess, sys


def main():
    e_01_limpiar_pantalla.clear_screen

    while True:
        mostrar_menu()
        opcion = elegir_opcion()

        match opcion:
            case 1:
                print(e_02_informacion_sistema.formatear_fecha_array())
            case 2:
                print(f'Usuario: {e_02_informacion_sistema.mostrar_usuario()}')
            case 3:
                nombre_nuevo_usuario = input('Nombre del nuevo usuario: ')
                aniadir_usuario(nombre_nuevo_usuario)
            case 4:
                mostrar_calendario_actual()
            case 5:
                cambiar_contrasenia()
            case 6:
                print('Saliendo...')
                sys.exit(0)
        print()


def mostrar_menu():
    print('*** MENÚ ***')
    print('1) Mostrar la fecha')
    print('2) Mostrar usuario actual')
    print('3) Añadir un usuario (sin contraseña)')
    print('4) Mostrar calendario actual')
    print('5) Cambiar contraseña')
    print('6) Salir')


def elegir_opcion():
    while True:
        try:
            opcion = int(input('Elige una opción: '))

            if opcion > 0 and opcion < 7:
                return opcion
            else:
                print('Error. Has introducido una opción incorrecta. Vuelve a intentarlo')

        except Exception:
            print('Error. Has introducido un valor incorrecto')


def mostrar_usuario_actual():
    print(subprocess.getoutput(['whoami']))


def aniadir_usuario(nombre):
    try:
        subprocess.run(['sudo, adduser', nombre])
    except Exception:
        print('Error al añadir al usuario')

def mostrar_calendario_actual():
    print(subprocess.getoutput(['cal']))

def cambiar_contrasenia():
    ...



if __name__ == '__main__':
    main()