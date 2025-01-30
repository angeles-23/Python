numero = int(input('Introduce un numero: '))

if(numero == 0):
    print(f'El número {numero} es cero')
elif(numero%2 == 0):
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')
