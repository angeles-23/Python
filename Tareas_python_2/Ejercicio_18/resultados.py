import os
os.system('cls')


from funciones import calcular_media, calcular_aprobados, calcular_suspensos, estudiantes

if __name__ == '__main__':

    for estudiante in estudiantes:
        nombre = estudiante['nombre']
        print(nombre)
        promedio = calcular_media(estudiante)
        print(promedio)

    medias = calcular_media(estudiantes)
    print(f'Medias: {medias}')
    aprobados = calcular_aprobados(medias)
    print(f'Aprobados: {aprobados}')
    aprobados = calcular_suspensos(medias)
    print(f'Suspensos: {aprobados}')
