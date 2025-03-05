# Ejercicio
# Escribir una función que pida un número `n` entero entre 1 y 10 y guarde en un fochero el nombre `tabla-n.txt` la tabla de multiplicar de ese número, donde `n` es el numero introducido.

# Bucle par que solicite un múmero correcto al usuario
while True:

    #Capturamos posibles errores del tipo de argumento
    try:
        # Solicitamos un número al usuario
        n = int(input('Introduce un número(1-10): '))
        if 1 <= n <= 10:
            break
        else:
            print('Error: no has instroducido un número entre 1 y 10')
    except ValueError:
        print(f'Error lo que has introducido es incorrecto')


# Construir el nombre del archivo donde se guardará la tabla de multiplicar:
nombre_archivo = 'tabla-' + str(n) + '.txt'     
# Otra forma: nombre_archivo = f'tabla-{n}.txt'

# Abrir el archivo en modo escritura('w'), ⚠ lo que sobre escribirá el contenido si el archivo ya existe
f = open(nombre_archivo, 'w')

# Bucle que genera la tabla de multiplicar del número registrado
for i in range(1, 10+1): # El fin del rango es un nº +

    # Creamos una linea con la multiplicacion en formado 'n x i = resultado'
    f.write(f'{str(n)} * {str(i)} = {str(n*i)}\n')

    print(f'{str(n)} * {str(i)} = {str(n*i)}') # Mostrar el contenido por la consola
    # Otra forma: print(f'{n} * {i} = {i*n}')

# Cierra el archivo para asegurar que los cambios se guardan correctamente
f.close()
print('Archivo creado correctamente')
