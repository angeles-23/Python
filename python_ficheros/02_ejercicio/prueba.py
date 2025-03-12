import os 
os.system('cls')
try:
    f = open('./02_ejercicio/nombres.txt', 'w')
    f.write('Sara Fernandez\nAlejandro Garcia\nTom Gutierrez\nSergio Gamarra\nCarlos Fernandez\nMarta Pascual\nAlba Martinez')
    f.close()
except FileNotFoundError:
    print('El archivo no existe')


try:
    f = open('./02_ejercicio/nombres.txt', 'r')
    contenido = f.readlines()
    print(contenido)
    f.close()
except FileNotFoundError:
    print('No se ha encontrado el archivo')


nombres = []
apellidos = []

fichero = open('./02_ejercicio/nombres_menor_6.txt', 'w')

for elemento in contenido:
    nombre = elemento.split(' ')[0]
    apellido = elemento.split(' ')[1]

    nombres.append(nombre)
    apellidos.append(apellido)

    inicial = nombre[0]

    if inicial == 'A':
        fichero.write(f'{nombre} {apellido}')

    # if len(nombre) < 6:
    #     fichero.write(f'{nombre} {apellido}\n')

fichero.close()

print(nombres)
print(apellidos)