import os 
os.system('cls')


def solicitar_matricula():
    ''' 
    Solicita al usuario una matricula de un coche.
    Argumentos:
        None
    Devuelve:
        Una cadena de texto
    '''
    matricula = input('Introduce la matricula: ')
    return matricula


def validar_matricula(matricula:str):
    '''
    Validar si una cadena de texto cumple con el formato requerido para una matricula de un coche
    4 números enteros seguido de 3 letra mayúsculas.
    Argumentos:
        1: Una cadena de texto
    Devuelve:
        True, si se cumplen las condiciones
        False, si no se cumplen las condiciones
    '''

    lista_caracteres = []
    
    if len(matricula) != 7:
        return False


    for caracter in matricula:
        lista_caracteres.append(caracter)


    for caracter in range(0,4):
        caracter = str(caracter)

        if not caracter.isnumeric():
            return False


    for caracter in range(4, len(matricula)):
        if not lista_caracteres[caracter].isupper():
            return False
        

    return True



if __name__ == '__main__':
    s = solicitar_matricula()
    if validar_matricula(s):
        print(f'{s} es una matricula de coche válida')
    else:
        print(f'{s} no es una matricula de coche válida')

        
