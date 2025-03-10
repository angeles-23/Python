
## Contar palabras
``` python
import os
import string
import random

os.system("cls")

def create_text_file(file="archivo_palabras.txt", word_count=500):
    """
    Crea un archivo con un conjunto de palabras aleatorias.
    
    Parámetros:
        file (str): Nombre del archivo a crear.
        word_count (int): Cantidad de palabras a escribir en el archivo.
    
    Devuelve:
        str: Mensaje indicando que el archivo se ha creado con éxito.
    """
    palabras = [
        "casa", "perro", "gato", "árbol", "cielo", "playa", "montaña", "libro", "mesa", "silla",
        "ventana", "sol", "luna", "estrella", "camino", "puerta", "jardín", "flor", "nube", "río",
        "ciudad", "pueblo", "auto", "tren", "avión", "barco", "bicicleta", "caminar", "correr", "saltar",
        "dormir", "soñar", "reír", "llorar", "comer", "beber", "jugar", "cantar", "bailar", "escribir",
        "leer", "pintar", "dibujar", "escuchar", "hablar", "pensar", "aprender", "enseñar", "trabajar", "viajar"
    ]
    try:
        f =  open(file, 'w')
        for i in range(word_count):
            f.write(random.choice(palabras) + ' ')
        f.close()
    except FileNotFoundError:
        return f'Error al crear el archivo'
    
    return f'Archivo {file} creado con {word_count} palabras'


def count_words(file="archivo_palabras.txt"):
    """
    Cuenta la frecuencia de las palabras en un archivo de texto.
    
    Parámetros:
        file (str): Nombre del archivo de texto.
    
    Devuelve:
        dict: Un diccionario con las palabras y su frecuencia.
    """
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return '¡El fichero no existe!\n'
    
    # Eliminamos signos de puntuación y pasamos a minúsculas
    text = text.replace('!', '').replace('¡', '')
    text = text.lower()
    
    # Contamos manualmente las palabras
    palabras = text.split(' ')

    contar_palabras = {}

    for palabra in palabras:
        if(palabra in contar_palabras):
            contar_palabras[palabra] += 1
        else:
            contar_palabras = 1
    # Crear el return
    return contar_palabras


def show_most_common(file, n=10):
    """
    Muestra las 'n' palabras más comunes del archivo.

    Parámetros:
        file (str): Nombre del archivo de texto.
        n (int): Cantidad de palabras más comunes a mostrar (por defecto 10).
    
    Devuelve:
        str: Lista de las palabras más comunes con sus frecuencias.
    """
    contar_palabras = count_words(file)

    lista_palabras = list(contar_palabras.items())

    for i in range(len(lista_palabras)):
        for j in range(i+1, len(lista_palabras)):
            if lista_palabras[i][1] < lista_palabras[j][1]:
                lista_palabras[i], lista_palabras[j] = lista_palabras[j], lista_palabras[i]

    return lista_palabras[:n]


def save_word_count(file, output_file="frecuencia_palabras.txt"):
    """
    Guarda la frecuencia de palabras en un archivo de salida.

    Parámetros:
        file (str): Nombre del archivo de texto.
        output_file (str): Nombre del archivo donde se guardará la información.

    Devuelve:
        str: Mensaje indicando si la operación fue exitosa o no.
    """
    contar_palabras = count_words(file)

    try:
        f = open(output_file, 'w')

        for palabra in contar_palabras:
            f.write(palabra + ': ' + str(contar_palabras[palabra]) + '\n') 
        
        f.close()

        return f"Se ha guardado la frecuencia de palabras en '{output_file}' + '.'"
    except:
        return 'Error al guardar el archivo'

def menu():
    """
    Muestra un menú de opciones para gestionar el contador de palabras.
    """
    # file = input("Introduce el nombre del archivo de texto a analizar: ")
    file = ""
    while True:
        print("\nMenú del Contador de Palabras")
        print("=============================")
        print("1 - Contar palabras en el archivo")
        print("2 - Mostrar las 10 palabras más comunes")
        print("3 - Guardar resultado en un archivo")
        print("4 - Crear archivo palabras random")
        print("0 - Salir")

        option = input("Elige una opción: ")
        
        if option == '1':
            print(count_words(file))
        elif option == '2':
            print(show_most_common(file))
        elif option == '3':
            print(save_word_count(file))
        elif option == '4':
            print("¿Quieres un nombre personalizado?")
            personalizar = input("[1] -> Crear el archivo con nombre por default.\n[Cualquier otra tecla] -> Crear archivo con nombre personalizado.\n")
            if personalizar == "1":
                print(create_text_file())
            else:
                print(create_text_file(input("Dime el nombre de tu archivo: ")))
        elif option == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()


```