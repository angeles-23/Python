import os 
os.system('cls')

# Escribe un programa en Python que determine si un número entero es primo o no
# Crea una funcición llamada es primo(numero) que reciba un número entero como parámetro y devuelva True si el numero es primo, o False en caso contrario
# El programa debe pedir al usuario un número entero e indicar si es primo o no utilizando la función implementada
# Recuerda que un número primo es aquel que solo es divisible por 1 y por sí mismo

def solicitar_numero():
    while True:
        try: 
            numero = int(input('Introduce un número: '))

            if(numero > 0):
                return numero
            else:
                print('Error. El número tiene que ser positivo')
        except Exception as error:
            print('El dato introducido no es un número')


def es_primo(numero):

    if(numero < 2):
        return False
    
    for i in range(2, numero):
        if(numero % i == 0):
            return False

    return True



if __name__ == '__main__':
    
    numero = solicitar_numero()
    numero_primo = es_primo(numero)
    print(numero_primo)

    if (numero_primo):
        print(f'El número {numero} SI es primo')
    else:
        print(f'El número {numero} NO es primo')
