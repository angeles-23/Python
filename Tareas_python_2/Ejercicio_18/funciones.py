import os
os.system('cls')

# Crea un programa que reciba una lista de estudiantes con sus nombres y sus notas, calcule la media de cada estudiante, determine quién aprobó (promedio >= 5.0) y quién no, y devuelva el estudiante con la nota promedio más alta. Hay errores intencionales para depuración.

estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6]},
    {"nombre": "Luis", "notas": [4, 5, 3]},
    {"nombre": "Marta", "notas": [10, 9]},
    {"nombre": "Carlos", "notas": [2, 3, 1]},
    {"nombre": "Juan", "notas": [6, 4, 8]},
    {"nombre": "Florin", "notas": [10, 3, 8]},
    {"nombre": "Pablo", "notas": [9, 9, 8]}
]


def calcular_media(lista_estudiantes):
    
    medias = []

    for estudiante in lista_estudiantes:
        notas = estudiante['notas']
        nota_total = 0
        cantidad_notas = 0

        for nota in notas:
            nota_total += nota
            cantidad_notas += 1

        media = nota_total / cantidad_notas
        media = round(media, 2)
        estudiante['media'] = media
        medias.append(media)

    return medias


def encontrar_aprobados_y_suspensos(lista_estudiantes):
    lista_aprobados = []
    lista_suspensos = []
    promedio = 5
    
    for estudiante in lista_estudiantes:
        media = estudiante['media']

        if media >= promedio:
            lista_aprobados.append(estudiante['nombre'])
            estudiante['estado'] = 'Aprobado'
        else:
            lista_suspensos.append(estudiante['nombre'])
            estudiante['estado'] = 'Reprobado'

    return lista_aprobados, lista_suspensos



def encontrar_mejor_estudiante(lista_estudiantes):

    media_mayor = lista_estudiantes[0]['media']
    mejor_estudiante = lista_estudiantes[0]['nombre']

    for estudiante in lista_estudiantes:
        if estudiante['media'] > media_mayor:
            media_mayor = estudiante['media']
            mejor_estudiante = estudiante['nombre']
    
    return media_mayor, mejor_estudiante
    


# if __name__ == '__main__':
#     print(calcular_media(estudiantes))
#     print(encontrar_aprobados_y_suspensos(estudiantes))
#     print(encontrar_mejor_estudiante(estudiantes))
