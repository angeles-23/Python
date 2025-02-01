# Escribir un programa que pida al ususario dos numeros y muestre por pantalla su división. Si el divisor es 0 el programa debe mostrar un error

dividiendo = int(input('Introduce el dividiendo: '))
divisor = int(input('Introduce el divisor: '))

if(divisor == 0):
    print('ERROR: En matemáticas no se puede dividir por cero.')
else:
    cociente = dividiendo / divisor
    print(f'El resultado es ' + str(cociente))

