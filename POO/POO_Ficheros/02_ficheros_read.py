# Ejercicio
# Escribir una función que pida un número entero entre 1 y 10, lea el ficghero `tabla-n.txt` con la tabla de multiplicar de ese número, donde `n` es el número introducido y lo muestre por consola. Si el fichero no existe debe mostrar un mensaje por consola informando de ello.

# Solicitar al usuario un número entre 1 y 10  al usuario
while True:

    #Capturamos posibles errores del tipo de argumento
    try:
        # Solicitamos un número al usuario
        n = int(input('Introduce un número(1-10): '))
        # Si el numero esta entre 1 y 10 salimos del bucle while
        if 1 <= n <= 10:
            break
        else:
            print('Error: no has instroducido un número entre 1 y 10')
    except ValueError:
        print(f'Error lo que has introducido es incorrecto')

# Construir la cadena de texto del fichero que tenemos que leer:
nombre_fichero = f'tabla-{n}.txt'

# Intentar abrir el archivo en modo lectura('r')
try:
    f = open(nombre_fichero, 'r')
except FileNotFoundError:
    print(f'No existe el fichero con la tabla del {n}')
else:
    print(f.read()) # Si el archivo existe, lee su contenido y lo muestre por pantalla
    f.close() # Cierra el archivo despues de leer el contenido