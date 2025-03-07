def save_word_count(word_count, file="frecuencia_palabras.txt"):
    """
    Guarda la frecuencia de palabras en un archivo.

    Parámetros:
        word_count (dict): Diccionario con palabras y su frecuencia.
        file (str): Nombre del archivo donde se guardará la información.

    Devuelve:
        str: Mensaje indicando si la operación fue exitosa o no.
    """


# Prueba con un conteo de palabras
word_count = {"hola": 2, "mundo": 3, "python": 1}
print(save_word_count(word_count))