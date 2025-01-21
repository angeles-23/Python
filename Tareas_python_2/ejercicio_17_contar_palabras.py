import os 
os.system('cls')

# Crea una función que reciba un texto (string) y devuelva las palabras únicas ordenadas alfabéticamente, ignorando mayúsculas/minúsculas, y cuántas veces aparece cada una.

# Entrada (Ejemplo):
# texto = "Hola mundo. El mundo es increíble. Hola de nuevo."

# Salida esperada:
# {'de': 1, 'el': 1, 'es': 1, 'hola': 2, 'increíble': 1, 'mundo': 2, 'nuevo': 1}

# Crea un menú: 
#   - opción 1: la cadena de texto es un input
#   - opcion 2: la cadena de texto es una aleatoria de un Diccionario que tendreis que crear con al menos 6 frases. 





def mostrar_menu():
    print('- '*57)
    print('%-1s %60s %50s' %('|', 'CONTAR PALABRAS', '|'))
    print('- '*57)
    print('%1s %-105s %5s' %('|', '1. La cadena de texto es un input.', '|'))
    print('%1s %-105s %5s' %('|', '2. la cadena de texto es una aleatoria de un Diccionario.', '|'))
    print('- '*57)

def comprobar_opcion():
    while True:
        try:
            opcion = int(input('Elige una opción: '))

            if(opcion < 1 or opcion >2):
                print('Error. La opción tiene que ser entre 1-2\n')
            else:
                return opcion

        except Exception as error:
            print('Error. La opción tiene que ser un número\n')








# Hay que pasarle una cadena de texto a la función
# Pasarlo todo a minuscula para que no haya palabras que se repiten
# introducirlo en un diccionario

def contar_palabras(cadena):
    cadena = cadena.lower().split('.')
    palabras_sin_repetir = {}

    for i in cadena:
        if (i not in palabras_sin_repetir):
            palabras_sin_repetir[i] += 1
        else:
            palabras_sin_repetir[i] = 1

    return 





# dividir el diccionario en palabras y contar cada una de ellas
# en caso de que se repita aumentar en uno el contador
# darlas de forma ordenada alfabeticamente

def contar_palabras(cadena):
    return ...





if __name__ == '__main__':
    texto = {
        1: "Hola mundo. ",
        2: "El mundo es increíble." ,
        3: "Hola de nuevo.", 
        4: "Hoy es un dia increíble para programar. ",
        5: "Este es mi primer hola mundo. ",
        6: "Hoy voy a programar en Python.",
        7: "Mi lenguaje de programación favorito es Python."
    }

    menu = mostrar_menu()
    opcion = comprobar_opcion()

    match opcion:
        case 1:
            texto = input('Introduce un texto: ')
            
        case 2:
            ...
    
    