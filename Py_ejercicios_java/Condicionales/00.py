numero = int(input('Introduce un numero: '))

esPar = False

if(numero%2 == 0):
    esPar = True

if(esPar == True):
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')