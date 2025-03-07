import os 
os.system('cls')

from datetime import datetime, timedelta

empleados = {
    1001: {
        "nombre": "Ana Martínez",
        "edad": 35,
        "cargo": "Gerente",
        "salario": 75_000,
        "fecha_ingreso": "2015-03-01"
    },
    1002: {
        "nombre": "Luis Pérez",
        "edad": 28,
        "cargo": "Desarrollador",
        "salario": 55_000,
        "fecha_ingreso": "2018-07-22"
    },
    1003: {
        "nombre": "Marta López",
        "edad": 40,
        "cargo": "Desarrollador",
        "salario": 60_000,
        "fecha_ingreso": "2013-06-15"
    },
    1004: {
        "nombre": "Carlos Gómez",
        "edad": 33,
        "cargo": "Gerente",
        "salario": 100_000,
        "fecha_ingreso": "2017-09-05"
    },
    1005: {
        "nombre": "Sara Ruiz",
        "edad": 30,
        "cargo": "Desarrollador",
        "salario": 50_000,
        "fecha_ingreso": "2019-01-11"
    }
}

def empleados_mas_jovenes(empleados):
    
    lista_empleados_mas_jovenes = {}
    empleados_mas_jovenes = []

    for empleado in empleados:
        lista_empleados_mas_jovenes[empleado] = (empleados[empleado]['edad'], empleados[empleado]['nombre'])
        empleados_mas_jovenes.append(empleados[empleado]['edad'])
    
    empleados_mas_jovenes_ordenados = sorted(empleados_mas_jovenes)

    empleados_mas_jovenes_resultado = []
    
    for i in range(3):
        ...

    return empleados_mas_jovenes_ordenados



if __name__ == '__main__':
    print(empleados_mas_jovenes(empleados))