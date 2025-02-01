import os 
os.system('cls')


PESO_PREGUNTA = (0.75, 0.75, 1 ,1 ,1.25 ,1.50 ,2 ,1.75)
# ------------------------------------------------------

def pedir_datos(total_preguntas):
    calificaciones = []

    for i in range(0, total_preguntas): # for i in range(1, total_preguntas+1)
        while True:
            try:
                calificacion = int(input(f'Dime la calificación de la pregunta {i+1} (0..100): '))  # {i}
                if (0 <= calificacion <= 100):
                    calificaciones.append(calificacion)
                    break
                else:
                    print(f'ERROR. La calificacion debe se ser un número entre 0 y 100.')
            except:
                print('ERROR.Debes introducir un número entero válido')
    return calificaciones


def calcular_nota_ponderada(calificaciones, ponderaciones):
    nota_final = 0
    
    for i in range(0, len(calificaciones)):
        nota_final += calificaciones[i]*ponderaciones[i]

    return nota_final/100


def mostrar_nota_examen(nota):
    print(f'La calificación de tu examen es: {nota}')





if __name__ == '__main__':
    tupla_calificaciones = pedir_datos(len(PESO_PREGUNTA))
    nota_final = calcular_nota_ponderada(tupla_calificaciones, PESO_PREGUNTA)
    mostrar_nota_examen(nota_final)