#! usr/bin/python

import subprocess


def main():
    while True:
        mostrar_menu()
        opcion = elegir_opcion()

        match opcion:
            case 1:
                ...
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 5:
                ...
            case 6:
                ...


def mostrar_menu():
    print('1) Mostrar la fecha')
    print('2) Mostrar usuario actual')
    print('3) Mostrar usuarios conectados')
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
                print('Has introducido una opción incorrecta. Vuelve a intentarlo')

        except Exception:
            print('Error. Has introducido un valor incorrecto')


def mostrar_fecha():
    ...

def mostar_usuario():
    ...

def mostrar_usuarios_conrectados():
    ...




if __name__ == '__main__':
    main()