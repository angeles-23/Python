#! usr/bin/python

import subprocess


def main():
    while True:
        mostrar_menu()
        opcion = elegir_opcion()

        match opcion:
            case 1:
                print(mostrar_fecha())
            case 2:
                mostar_usuario()
            case 3:
                mostrar_usuarios_conectados()
            case 4:
                mostrar_calendario_actual()
            case 5:
                cambiar_contrasenia()
            case 6:
                print('Saliendo...')
                break


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
    fecha_docker = subprocess.getoutput(['date'])
    fecha = fecha_docker.split(' ')

    dia_docker = fecha[0]
    mes_docker = fecha[1]
    anio_docker = fecha[5]

    match mes_docker:
        case 'Jan':
            mes = 1
        case 'Feb':
            mes = 2
        case 'Mar':
            mes = 3
        case 'Apr':
            mes = 4
        case 'May':
            mes = 5
        case 'Jun':
            mes = 6
        case 'Jul':
            mes = 7
        case 'Aug':
            mes = 8
        case 'Sep':
            mes = 9
        case 'Oct':
            mes = 10
        case 'Nov':
            mes = 11
        case 'Dec':
            mes = 12

    fecha_formateada = f'{dia_docker}/{mes}/{anio_docker}'
    return fecha_formateada


def mostar_usuario():
    ...

def mostrar_usuarios_conectados():
    ...

def mostrar_calendario_actual():
    ...

def cambiar_contrasenia():
    ...



if __name__ == '__main__':
    main()