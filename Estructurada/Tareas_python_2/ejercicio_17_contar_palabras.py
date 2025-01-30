import os, random
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
    print('- '*35)
    print('%-1s %40s %26s' %('|', 'CONTAR PALABRAS', '|'))
    print('- '*35)
    print('%1s %-61s %5s' %('|', '1. La cadena de texto es un input.', '|'))
    print('%1s %-61s %5s' %('|', '2. La cadena de texto es una aleatoria de un Diccionario.', '|'))
    print('- '*35)

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


def contar_palabras(cadena):

    frecuencia_palabras = {}
    palabras = cadena.split(' ')

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    return frecuencia_palabras


if __name__ == '__main__':
    texto = {
        1: "Hola mundo y de nuevo hola mundo",
        2: "El mundo es increíble" ,
        3: "Hola de nuevo y adios de nuevo", 
        4: "Hoy es un dia increíble para programar, el el dia del programador",
        5: "Este es mi primer hola mundo",
        6: "Hoy voy a programar en Python",
        7: "Mi lenguaje de programación favorito es Python "
    }

    menu = mostrar_menu()
    opcion = comprobar_opcion()

    match opcion:
        case 1:
            texto = input('Introduce un texto: ').lower()
            cantidad_palabras = contar_palabras(texto)
            print(cantidad_palabras)
        case 2:
            textos_aleatorios = texto
            numero_aleatorio = random.randint(1,6)

            frases = str(textos_aleatorios[numero_aleatorio]).lower()
            cantidad_palabras = contar_palabras(frases)
            print(cantidad_palabras)

            # Para todas las frases
            # for textos in textos_aleatorios:
            #     frases = str(textos_aleatorios[textos])
            #     print(contar_palabras(frases))

    print('\nLista ordenada')
    print(sorted(cantidad_palabras))