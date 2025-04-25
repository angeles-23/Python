#!usr/bin/python3

import subprocess, sys, os
import terminal_colors


def main():   
    argumentos = sys.argv[1:]

    limpiar_pantalla()
    es_directorio_correcto, directorio = comprobar_directorio(argumentos)

    if(es_directorio_correcto == False):
        print(f'❌    {terminal_colors.TerminalColors.BLACK_RED}Error: El directorio "{directorio}" no existe\033[0m')
    else:
        print(f'✅    {terminal_colors.TerminalColors.BLACK_YELLOW}El directorio "{directorio}" existe\033[0m')
        # listar_elementos_directorio(directorio)
        mostrar_directorios_y_ficheros(directorio)



def limpiar_pantalla():
    subprocess.run(['clear'])


def comprobar_directorio(argumentos):
    es_directorio_correcto = True
    
    if(len(argumentos) > 1):
        es_directorio_correcto = False
    
    if(len(argumentos) == 1):
        directorio = argumentos[0]

        if(os.path.isdir(directorio) == False):
            es_directorio_correcto = False
    else:
        directorio = os.getcwd()
    
    return es_directorio_correcto, directorio
    

def listar_elementos_directorio(directorio):
    lista_elementos = os.listdir(directorio)
    print(f'\nLista de elementos del directorio "{directorio}":')

    for elemento in lista_elementos:
        print(f'- {elemento}')
    

def obtener_directorios(directorio):
    lista_elementos = os.listdir(directorio)
    lista_directorios = []
    contador_directorios = 0

    for dir in lista_elementos:
        ruta_completa = os.path.join(directorio, dir)
        if(os.path.isdir(ruta_completa) == True):
            contador_directorios += 1
            lista_directorios.append(dir)

    return lista_directorios, contador_directorios


def obtener_ficheros(directorio):
    lista_elementos = os.listdir(directorio)
    lista_ficheros = []
    contador_ficheros = 0

    for fichero in lista_elementos:
        ruta_completa = os.path.join(directorio, fichero)
        if(os.path.isfile(ruta_completa) == True):
            contador_ficheros += 1
            lista_ficheros.append(fichero)
    
    return lista_ficheros, contador_ficheros


def mostrar_directorios_y_ficheros(directorio):
    lista_directorios, contador_directorios = obtener_directorios(directorio)
    lista_ficheros, contador_ficheros  = obtener_ficheros(directorio)

    print(f'{terminal_colors.TerminalColors.BLACK_BLUE}📁    Directorios ({contador_directorios}):\033[0m')
    for direct in lista_directorios:
        print(f'- {direct}')

    print(f'{terminal_colors.TerminalColors.BLACK_GREEN}📄    Ficheros({contador_ficheros}):\033[0m')
    for fichero in lista_ficheros:
        print(f'- {fichero}')


if __name__ == '__main__':
    main()