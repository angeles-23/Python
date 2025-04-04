#! usr/bin/python3

import subprocess, sys


def main():
    fichero = sys.argv[0]
    argumentos = sys.argv[1:]
    print(validar_diferentes_entradas(argumentos))



def validar_diferentes_entradas(argumentos):

    if len(argumentos) < 1 or len(argumentos) > 3:
        return 'La cantidad de argumentos en incorrecta'
    

    if len(argumentos) == 1:

        if not argumentos[0].isnumeric():
            if argumentos[0].isalpha():
                mes_nombre = argumentos[0].lower()

                match mes_nombre:
                    case 'enero':
                        mes = 1
                    case 'febrero':
                        mes = 2
                    case 'marzo':
                        mes = 3
                    case 'abril':
                        mes = 4
                    case 'mayo':
                        mes = 5
                    case 'junio':
                        mes = 6
                    case 'julio':
                        mes = 7
                    case 'agosto':
                        mes = 8
                    case 'septiembre':
                        mes = 9
                    case 'octubre':
                        mes = 10
                    case 'noviembre':
                        mes = 11
                    case 'diciembre':
                        mes = 12
                    case _:
                        return f'El mes {argumentos[0]} no es válido'
                
                resultado = subprocess.run(['cal', str(mes), '2025'], capture_output=True, text=True)

                if resultado.returncode == 0:
                    print(f'Mostrando calendario del mes: {argumentos[0]}')
                    return resultado.stdout
                else:
                    print(f'Se ha producido un error al mostrar el calendario del mes: {argumentos[0]}')
                    return resultado.stderr
        else:
            if len(argumentos[0]) == 4:
                resultado = subprocess.run(['cal','-y', argumentos[0]], capture_output=True, text=True)
            
                if resultado.returncode == 0:
                    print(f'Monstrando calendario del año: {argumentos[0]}')
                    return resultado.stdout
                else:
                    print(f'Se ha producido un error al mostrar el calendario del año: {argumentos[0]}')
                    return resultado.stderr

            mes = int(argumentos[0])
            if mes < 1 or mes > 12:
                print('El mes elegido no existe')
            else:
                resultado = subprocess.run(['cal', argumentos[0], '2025'], capture_output=True, text=True)

                if resultado.returncode == 0:
                    print(f'Mostrando calendario del mes: {mes}')
                    return resultado.stdout
                else:
                    print(f'Se ha producido un error al mostrar el calendario del mes: {mes}')
                    return resultado.stderr


    if len(argumentos) == 2:
        mes = argumentos[0]
        anio = argumentos[1]

        if mes.isnumeric() and anio.isnumeric():
            
            if len(mes) == 4:
                mes = argumentos[1]
                anio = argumentos[0]

            mes_numero = int(mes)
            if mes_numero < 1 or mes_numero > 12:
                return 'El mes introducido es incorrecto'
            
            resultado = subprocess.run(['cal', mes, anio], capture_output=True, text=True)

            if resultado.returncode == 0:
                print(f'Mostrando calendario del mes {mes} del {anio}:')
                return resultado.stdout
            else:
                print(f'Se ha producido un erro al mostrar el calendario del mes {mes} del {anio}')
                return resultado.stderr

        else:
            return 'No has introducido un valor numérico'
            

    if len(argumentos) == 3:

        festivos = {
            1: [(1, "Año Nuevo"), (6, "Día de Reyes")],
            3: [(29, "Viernes Santo")],  # Variable: puedes calcularlo si quieres más precisión
            5: [(1, "Día del Trabajo")],
            8: [(15, "Asunción de la Virgen")],
            10: [(12, "Fiesta Nacional de España")],
            11: [(1, "Día de Todos los Santos")],
            12: [
                (6, "Día de la Constitución Española"),
                (8, "Inmaculada Concepción"),
                (25, "Navidad")
            ]
        }

        texto_festivo = argumentos[0]
        mes = argumentos[1]
        anio = argumentos[2]

        if texto_festivo == '--festivos':

            if mes.isnumeric():
                mes_numero = int(mes)

                match mes_numero:
                    case 1:
                        mes_texto = 'Enero'
                    case 2:
                        mes_texto = 'Febrero'
                    case 3:
                        mes_texto = 'Marzo'
                    case 4:
                        mes_texto = 'Abril'
                    case 5:
                        mes_texto = 'Mayo'
                    case 6:
                        mes_texto = 'Junio'
                    case 7:
                        mes_texto = 'Julio'
                    case 8:
                        mes_texto = 'Agosto'
                    case 9:
                        mes_texto = 'Septiembre'
                    case 10:
                        mes_texto = 'Octubre'
                    case 11:
                        mes_texto = 'Noviembre'
                    case 12:
                        mes_texto = 'Diciembre'
                    case _:
                        return 'Has introducido un mes incorrecto'
                
                
                if anio.isnumeric() and int(anio) > 0:

                    for numero_mes_festivo in festivos:
                        if numero_mes_festivo == mes_numero:
                            print(f'{mes_texto} contiene los siguiente festivos en España')

                            for numero_mes in festivos:
                                fiestas_mes = festivos[numero_mes]

                                if numero_mes == mes_numero:
                                    for i in range(len(fiestas_mes)):
                                        descripcion_dia = fiestas_mes[i]
                                        numero_dia = descripcion_dia[0]
                                        nombre_fiesta = descripcion_dia[1]

                                        print(f'- {numero_dia}: {nombre_fiesta}')
                
                    return f'Se han mostrado los dias festivos del {mes_numero}/{anio} en España'
                
    return 'Se ha producido un error inesperado'


if __name__ == '__main__':
    main()