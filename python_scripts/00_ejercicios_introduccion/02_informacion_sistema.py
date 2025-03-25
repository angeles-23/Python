#! /usr/bin/python

import subprocess


def main():
    mostrar_fecha()
    # formatear_fecha_facil()
    formatear_fecha_array()


def mostrar_fecha():
    return subprocess.getoutput(['date'])


def mostrar_usuario():
    return subprocess.getoutput(['whoami'])


def formatear_fecha_array():
    
    array_lista_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    array_lista_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    array_lista_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    array_lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] 

    fecha_docker = mostrar_fecha().split(' ')
    dia_docker = fecha_docker[0]
    mes_docker = fecha_docker[1]
    numero_docker = fecha_docker[2]
    anio = fecha_docker[5]
    usuario = mostrar_usuario()

    posicion_dia = array_lista_days.index(dia_docker)
    dia_espaniol = array_lista_dias[posicion_dia]

    poscion_mes = array_lista_months.index(mes_docker)
    mes_espaniol = array_lista_meses[poscion_mes]

    print(f'Soy {usuario}')
    print(f'Hoy es {dia_espaniol}, {numero_docker} de {mes_espaniol} de {anio}')



def formatear_fecha_facil():
    fecha = mostrar_fecha().split(' ')
    usuario = mostrar_usuario()

    dia_docker = fecha[0]
    mes_docker = fecha[1]
    numero_dia_docker = fecha[2]
    anio_docker = fecha[5]
    
    match dia_docker:
        case 'Mon':
            dia = 'Lunes'
        case 'Tue':
            dia =  'Martes'
        case 'Wed':
            dia =  'Miércoles'
        case 'Thu':
            dia =  'Jueves'
        case 'Fri':
            dia =  'Viernes'
        case 'Sat':
            dia =  'Sábado'
        case 'Sun':
            dia =  'Domingo'
    
    match mes_docker:
        case 'Jan':
            mes = 'Enero'
        case 'Feb':
            mes = 'Febrero'
        case 'Mar':
            mes = 'Marzo'
        case 'Apr':
            mes = 'Abril'
        case 'May':
            mes = 'Mayo'
        case 'Jun':
            mes = 'Junio'
        case 'Jul':
            mes = 'Julio'
        case 'Aug':
            mes = 'Agosto'
        case 'Sep':
            mes = 'Septiembre'
        case 'Oct':
            mes = 'Osctubre'
        case 'Nov':
            mes = 'Noviembre'
        case 'Dec':
            mes = 'Diciembre'

    print(f'Soy {usuario}')
    print(f'Hoy es {dia}, {numero_dia_docker} de {mes} de {anio_docker}')



if __name__ == '__main__':
    main()