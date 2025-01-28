import os
os.system('cls')

from funciones import estudiantes, calcular_media, encontrar_aprobados_y_suspensos, encontrar_mejor_estudiante


if __name__ == '__main__':

    for i in estudiantes:
        media = calcular_media(estudiantes)
        aprobados_y_suspensos = encontrar_aprobados_y_suspensos(estudiantes)
        mejor_media, mejor_estudiante = encontrar_mejor_estudiante(estudiantes)

    for estudiante in estudiantes:
        print(f'{estudiante['nombre']} - Promedio: {estudiante['media']:.2f} - Estado: {estudiante['estado']}')
    
    print(f"El mejor estudiante es {mejor_estudiante} con un promedio de {mejor_media:.2f}")

