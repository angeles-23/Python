import os
os.system('cls')

# 1. Abrir el archivo y leer linea a linea -> readline
f = open('./01_ficheros/prueba.txt', 'r')
primeraLinea = f.readline()
print(primeraLinea)
print(f.readline())
print(f.readline())
f.close()





# 2. Abrir el archivo y leer todas las lineas -> readlines
f = open('./01_ficheros/prueba.txt', 'r')
lista_lineas = f.readlines()
print(lista_lineas)
f.close()





# 3.Escribir en un fichero existente -> w
# Si un fichero ya tiene contendido, tenemos 2 opciones: Sobeescribir el contenido o añadir el contenido al final del que ya existe
f = open('./01_ficheros/prueba.txt', 'w')
f.write('Me he cargado todo lo que habia.\n')

lista_contenido = [ 
    'Dimas es el mejor Youruber.\n',
    'Me turboflipa su curso de Python.\n',
    'Adios muy buenas.'
]

f.writelines(lista_contenido) # Escribe varias lineas de una lista
f.close()
# Solo se sobreescribe lo que ya había escrito al hacer el open()




# 4. Escribir en un fichero existente -> a
f = open('./01_ficheros/prueba.txt', 'a')
f.write('\n\n\nEsto es una nueva linea.')
f.close()





# 5. Crear un nuevo fichero -> open
try:
    f = open('./01_ficheros/pruebas_2.txt', 'w')
    f.write('Soy un fichero nuevoooo')
    print(f.readable())
    print(f.writable())
    f.close()
except:
    print('No se puede crear porque ya existe')





# 6. Método seek. Podemos controlar la posicion desde la cual empezamos a leer
f = open('./01_ficheros/prueba.txt', 'r')
f.seek(8)
print('\nEstamos leyendo desde el 8º caracter:')
print('*  '*15)
print(f.read())
f.close()





# 7. Lectura y escritura simultaneas
f = open('./01_ficheros/prueba.txt', 'r+')
lineas = f.readlines()
print(lineas)

f.write('\nEsta linea es nueva.\n')

f.close()

