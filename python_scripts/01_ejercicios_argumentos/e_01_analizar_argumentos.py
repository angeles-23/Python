#! usr/bin/python

import sys

def main():
    # print(sys.argv) Los argumentos son cadenas de texto
    argumentos = sys.argv[1:]
    describir_argumentos(argumentos)



def describir_argumentos(argumentos):

    # Recorrer la lista argumentos uno a uno, luego intentar cambiar el tipo de cada argumento y si sí se puede hacer ese tipo que lo pinte

    for argumento in argumentos:
        es_entero = True
        
        try:
            cadena_a_int = int(argumento)
            es_entero = True
        except Exception:
        # if es_entero == True:
        #     print(f'Argumento {argumentos[argumento]}: {argumento} - {calcular_longitud(cadena_a_int)}')
        


        # CODIGOS DE INTENTO
        # try:
        #     cadena_a_cadena = str(argumento)
        # except Exception:
        #     ...

        # try:
        #     cadena_a_float = float(argumento)
        # except Exception:
        #     ...
        
        # mixto_letra = False
        # mixto_numero = False

        # for letra in argumento:
        #     if letra.isdigit() == True:
        #         mixto_letra = True
        #         break

        #     if letra.isalpha():
        #         mixto_numero = True
        #         break



        # if int(argumento) == True:
        #     print(f'Argumento {argumentos[argumento]}: {argumento} - {calcular_longitud(argumento)}')

        # if float(argumento) == True:
        #     print(f'Argumento {argumentos[argumento]}: {argumento} - {es_positivo(argumento)}')
        
        # if str(argumento) == True and int(argumento) == True:
        #     print(f'Argumento {argumentos[argumento]}: {argumento} - Mixto')

        

        # if isinstance(argumento, int) == True:
        #     print(f'Argumento {argumentos[argumento]}: {argumento} - {es_par(argumento)}')
        
        # if isinstance(argumento, str) == True:
        #     print(f'Argumento {argumentos[argumento]}: {argumento} - {calcular_longitud(argumento)}')
        
        # if isinstance(argumento, float) == True:
        #     print(f'Argumento {argumentos[argumento]}: {argumento} - {es_positivo(argumento)}')

        # if isinstance(argumento, int) == True and isinstance(argumento, str) == True:
        #     print(f'Argumento {argumentos[argumento]}: {argumento} - Mixto')



def calcular_longitud(argumento_texto):
    return f'Texto longitud ({len(argumento_texto)})'


def es_par(argumento_entero):
    
    if argumento_entero % 2 == 0:
        return 'Entero (par)'
    else:
        return 'Entero (impar)'


def es_positivo(argumento_decimal):
    if argumento_decimal > 0:
        return 'Decimal positivo'
    else:
        return 'Decimal negativo'


if __name__ == '__main__':
    main()