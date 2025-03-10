import os 
os.system('cls')

from datetime import datetime, timedelta

empleados = {
    1001: {
        "nombre": "Ana Martínez",
        "edad": 35,
        "cargo": "Gerente",
        "salario": 100_000,
        "fecha_ingreso": "2015-03-01"
    },
    1002: {
        "nombre": "Luis Pérez",
        "edad": 28,
        "cargo": "Desarrollador",
        "salario": 10_000,
        "fecha_ingreso": "2018-07-22"
    },
    1003: {
        "nombre": "Marta López",
        "edad": 40,
        "cargo": "Desarrollador",
        "salario": 20_000,
        "fecha_ingreso": "2013-06-15"
    },
    1004: {
        "nombre": "Carlos Gómez",
        "edad": 33,
        "cargo": "Gerente",
        "salario": 59_000,
        "fecha_ingreso": "2017-09-05"
    },
    1005: {
        "nombre": "Sara Ruiz",
        "edad": 30,
        "cargo": "Diseñador",
        "salario": 35_000,
        "fecha_ingreso": "2019-01-11"
    }
}

def encontrar_cuantos_empleados_hay(empleados):
    contador_gerente = 0
    contador_diseñador = 0
    contador_desarrollador = 0
    lista_cantidad_empleados = []

    for empleado in empleados:
        cargo = empleados[empleado]['cargo']

        if (cargo == 'Gerente'):
            contador_gerente += 1
        elif (cargo == 'Diseñador'):
            contador_diseñador += 1
        elif(cargo == 'Desarrollador'):
            contador_desarrollador += 1
    
    lista_cantidad_empleados.append(f'Gerente = {contador_gerente}')
    lista_cantidad_empleados.append(f'Diseñador = {contador_diseñador}')
    lista_cantidad_empleados.append(f'Desarrollador = {contador_desarrollador}')

    return lista_cantidad_empleados



if __name__ == '__main__':
    cantidad_empleados = encontrar_cuantos_empleados_hay(empleados)
    print(cantidad_empleados)
