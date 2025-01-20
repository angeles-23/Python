import os
os.system('cls')

import statistics

notas = [
 7, 6, 3, 9, 8, 4, 8, 2, 10, 5, 7, 5, 9, 8, 4, 1, 8, 4, 6
]

# En esta clase se han matriculado 4 alumnos nuevos. Sus notas han sido 8, 5, 4 y 9. Calcular la media de la clase teniendo en cuenta los nuevos alumnos.
# ¿Cuál ha sido la nota mas alta? ¿Y la más baja?

notas.append(8)
notas.append(5)
notas.append(4)
notas.append(9)


# Obtener la suma de las notas
suma = 0
for nota in notas:
    suma += nota


# Obtener el numero total de notas
cantidad_notas = 0
for nota in notas:
    cantidad_notas += 1

# cantidad_notas = len(notas)


media_notas = suma / cantidad_notas
print(f'La media de la clase es %.2f' %media_notas)


# Calcular la nota mayor
nota_maxima = 0
for nota in notas:
    if(nota > nota_maxima):
        nota_maxima = nota
    

# Calcular la nota menor
nota_menor = 10
for nota in notas:
    if(nota < nota_menor):
        nota_menor = nota

    
# Calcular el numero de aprobados y suspensos
aprobado = 5
numero_aprobados = 0
numero_suspensos = 0

for nota in notas:
    if(nota >= aprobado):
        numero_aprobados += 1
    else:
        numero_suspensos += 1


print(f'El número de alumnos aprobados son {numero_aprobados}')
print(f'El número de alumnos suspensos son {numero_suspensos}')



# tupla_notas = tuple(notas)

# nota_media = statistics.mean(tupla_notas)
# nota_mas_baja = min(tupla_notas)
# nota_mas_alta = max(tupla_notas)

# print('La nota media es: %2.2f' % nota_media)
# print('La nota mas baja es: %2.2f' % nota_mas_baja)
# print('La nota mas alta es: %2.2f' % nota_mas_alta)