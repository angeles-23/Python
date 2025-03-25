#! usr/bin/python

import subprocess



def main():
    usuario = mostrar_usuario()
    fecha = mostrar_fecha()
    print(f'Soy {usuario}')
    print(formatear_fecha(fecha))
    # print(formatear_fecha_facil())



def mostrar_usuario():
    return subprocess.getoutput(['whoami'])


def mostrar_fecha():
    return subprocess.getoutput(['date'])


def formatear_fecha(fecha:str):
    array_lista_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    array_lista_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    array_lista_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    array_lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] 

    fecha = fecha.split(' ')

    dia_docker = fecha[0]
    mes_docker = fecha[1]
    numero_dia_docker = fecha[2]
    anio_docker = fecha[5]

    posicion_dia = array_lista_days.index(dia_docker)
    dia_espanol = array_lista_dias[posicion_dia]

    posicion_mes = array_lista_months.index(mes_docker)
    mes_espaniol = array_lista_meses[posicion_mes]

    fecha_formateada = f'Hoy es {dia_espanol}, {numero_dia_docker} de {mes_espaniol} de {anio_docker}'

    return fecha_formateada


def formatear_fecha_facil():
    fecha_docker = mostrar_fecha().split(' ')

    dia_docker = fecha_docker[0]
    mes_docker = fecha_docker[1]
    numero_dia_docker = fecha_docker[2]
    anio_docker = fecha_docker[5]

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

    return f'Hoy es {dia}, {numero_dia_docker} de {mes} de {anio_docker}'




if __name__ == '__main__':
    main()