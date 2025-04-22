#! usr/bin/python3

import subprocess, os, sys


def main():
    argumentos = sys.argv[1:]
    limpiar_pantalla()
    ruta = obtener_ruta(argumentos)
    elementos = os.listdir(ruta)
    mostrar_directorios_y_ficheros(elementos, ruta)
    


def limpiar_pantalla():
    subprocess.run(['clear'])



def obtener_ruta(argumentos):

    if len(argumentos) == 1:
        ruta = argumentos[0]
        
        if os.path.isdir(ruta) == False:
            print(f'Error. No existe la ruta: {ruta}')

    else:
        ruta = os.getcwd()  

    return ruta



def obtener_directorios(elementos, ruta):
    directorios = []
    contador_directorios = 0

    for elemento in elementos:
        if os.path.isdir((ruta + '/' + elemento)) == True:
            contador_directorios += 1
            directorios.append(elemento)
    
    return directorios, contador_directorios



def obtener_ficheros(elementos, ruta):
    ficheros = []
    contador_ficheros = 0

    for elemento in elementos:
        if os.path.isfile(ruta + '/' + elemento) == True:
            contador_ficheros += 1
            ficheros.append(elemento)

    return ficheros, contador_ficheros



def mostrar_directorios_y_ficheros(elementos, ruta):
    directorios, contador_directorios = obtener_directorios(elementos, ruta)
    ficheros, contador_ficheros = obtener_ficheros(elementos, ruta)

    print(f'📌   Contenido de {ruta}')
    print(f'📂   Directorios ({contador_directorios})')
    for i, nombre in enumerate(directorios, start=1):
        print(f'- {nombre}')


    print(f'\n📄   Ficheros ({contador_ficheros})')
    for i, nombre in enumerate(ficheros, start=1):
        print(f'- {nombre}')



if __name__ == '__main__':
    main()
