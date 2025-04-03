#! usr/bin/python3

import sys

def main():
    # print(sys.argv)        # Devuelve una lista con los argumentos que son cadenas de texto
    argumentos = sys.argv[1:]
    describir_argumentos(argumentos)



def describir_argumentos(argumentos):

    contador_enteros = 0
    contador_decimales = 0
    contador_cadenas = 0
    contador_mixto = 0
    caracter_punto = '.'

    for i in range(len(argumentos)):

        if argumentos[i].isalpha():
            contador_cadenas += 1
            descripcion = calcular_longitud(argumentos[i])

        elif argumentos[i].isnumeric():
            contador_enteros += 1
            descripcion = es_par(argumentos[i])

        elif caracter_punto in argumentos[i]:
            contador_decimales += 1
            descripcion = es_positivo(argumentos[i])

        else: 
            contador_mixto += 1
            descripcion = 'Mixto'
        
        print(f'Argumento {i+1}: {argumentos[i]} →  {descripcion}')

    print('\nResumen:')
    print(f'Enteros: {contador_enteros}')
    print(f'Decimales: {contador_decimales}')
    print(f'Textos: {contador_cadenas}')
    print(f'Mixtos: {contador_mixto}')
            


def calcular_longitud(argumento_texto):
    return f'Texto longitud ({len(argumento_texto)})'



def es_par(argumento_entero):
    
    argumento_entero = int(argumento_entero)

    if argumento_entero % 2 == 0:
        return 'Entero (par)'
    else:
        return 'Entero (impar)'



def es_positivo(argumento_decimal):

    argumento_decimal = float(argumento_decimal)

    if argumento_decimal > 0:
        return 'Decimal positivo'
    else:
        return 'Decimal negativo'




if __name__ == '__main__':
    main()