import os 
os.system('cls')

# Escribe una función que elimine los elementos duplicados de una lista.

def eliminar_duplicados(arr):

    array_sin_duplicados = []

    for i in arr:
        if (i not in array_sin_duplicados):
            array_sin_duplicados.append(i)

    return array_sin_duplicados
    
    
if __name__ == '__main__':
    lista = [1, 2, 2, 3, 4, 4, 5]
    print(eliminar_duplicados(lista))


# print(eliminar_duplicados([1, 2, 2, 3, 4, 4, 5]))  # Salida: [1, 2, 3, 4, 5]
