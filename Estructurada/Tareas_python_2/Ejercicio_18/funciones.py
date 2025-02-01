<<<<<<< HEAD:Tareas_python/ejercicio_18_medias_clase.py
import os
os.system('cls')

# Crea un programa que reciba una lista de estudiantes con sus nombres y sus notas, calcule la media de cada estudiante, determine quién aprobó (promedio >= 5.0) y quién no, y devuelva el estudiante con la nota promedio más alta. Hay errores intencionales para depuración.

estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6]},
    {"nombre": "Luis", "notas": [4, 5, 3]},
    {"nombre": "Marta", "notas": [10, 9]},
    {"nombre": "Carlos", "notas": [2, 3, 1]},
]

def calcular_media(listas):
    medias = []
    
    for lista in listas:
        notas = lista['notas']
        nota_total = 0
        media = 0
        cantidad_notas = 0

        for nota in notas:
            nota_total += nota
            cantidad_notas += 1

        media = nota_total / cantidad_notas
        medias.append(media)

    return medias


def calcular_aprobados(lista_medias):

    lista_aprobados = []

    for media in lista_medias:
        if (media >= 5):
            lista_aprobados.append(media)
    
    return lista_aprobados



def averiguar_nombres_aprobados(lista_estudiantes, lista_medias):
    
    ...







if __name__ == '__main__':
    medias = calcular_media(estudiantes)
    print(f'Medias: {medias}')
    aprobados = calcular_aprobados(medias)
    print(f'Aprobados: {aprobados}')
    nombres_aprobados = averiguar_nombres_aprobados(estudiantes, aprobados)
    print(nombres_aprobados)
=======
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


def calcular_media(listas):
    medias = []

    for lista in listas:
        notas = lista['notas']
        nota_total = 0
        media = 0
        cantidad_notas = 0

        for nota in notas:
            nota_total += nota
            cantidad_notas += 1

        media = nota_total / cantidad_notas
        media = round(media, 1)
        medias.append(media)
        
    return medias


def calcular_aprobados(lista_medias):

    lista_aprobados = []

    for media in lista_medias:
        if (media >= 5):
            lista_aprobados.append(media)
    
    return lista_aprobados


def calcular_suspensos(lista_medias):
    lista_suspensos = []

    for media in lista_medias:
        if (media < 5):
            lista_suspensos.append(media)
    
    return lista_suspensos


def encontrar_estudiante_media_mayor(lista_medias, lista_estudiantes):
    nota_mayor = lista_medias[0]
    indice_mayor = 0

    for i in range(len(lista_medias)):
        if(lista_medias[i] > nota_mayor):
            nota_mayor = lista_medias[i]
            indice_mayor = i
    
    return lista_estudiantes[indice_mayor]['nombre'], nota_mayor
>>>>>>> 737dd1e95804f9def1f807bcd3410848c8fd3c5e:Estructurada/Tareas_python_2/Ejercicio_18/funciones.py
