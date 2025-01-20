nombre1 = input('Datos de entrada 1:')
nombre2 = input('Datos de entrada 2:')

print('-'*50)
datos1 = nombre1.split(',')
datos2 = nombre2.split(',')

print(f'Nombre: {datos1[0]:15} Edad: {datos1[1]:3} Altura: {float(datos1[2]):.3f}')
print(f'Nombre: {datos2[0]:15} Edad: {datos2[1]:3} Altura: {float(datos2[2]):.3f}')

