import random

def create_random_text_file(file="archivo_palabras.txt", word_count=100):
    """
    Crea un archivo con palabras aleatorias.

    Parámetros:
        file (str): Nombre del archivo a crear.
        word_count (int): Número de palabras a generar.

    Devuelve:
        str: Mensaje indicando que el archivo se ha creado correctamente.
    """

# Prueba creando un archivo con 100 palabras
print(create_random_text_file())