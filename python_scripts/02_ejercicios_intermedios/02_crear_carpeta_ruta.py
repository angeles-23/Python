#!usr/bin/python3

import subprocess, sys, os
import terminal_colors


def main():
    limpiar_pantalla()    
    argumentos = sys.argv[1:]
    nombre_carpeta = sys.argv[1]
    son_argumentos_validos, ruta = son_argumentos_correctos(argumentos)

    if(son_argumentos_validos == False):
        print(f'❌    Error: La ruta "{ruta}" no existe')
    else:
        print(f'✅    La ruta "{ruta}" existe')
        existe_carpeta_en_la_ruta(ruta, nombre_carpeta)


def limpiar_pantalla():
    subprocess.run(['clear'])
    

def son_argumentos_correctos(argumentos):
    
    if(len(argumentos) == 0):
        ruta = ""
        print('❌    Error: Debes indicar al menos el nombre de la carpeta.')
        return False, ruta

    if(len(argumentos) > 2):
        ruta = argumentos[1]
        print('❌    Error: Has introducido muchos argumentos.')
        return False, ruta
    
    nombre_carpeta = argumentos[0]

    if(len(argumentos) == 1):
        ruta = os.getcwd()

    elif(len(argumentos) == 2):
        ruta = argumentos[1]

        if(os.path.isdir(ruta) == False):
            return False, ruta

    return True, ruta


def existe_carpeta_en_la_ruta(ruta, nombre_carpeta):
    ruta_completa = os.path.join(ruta, nombre_carpeta)

    if(os.path.isdir(ruta_completa) == True):
        print(f'⚠️    Ya existe una carpeta llamada "{nombre_carpeta}" en esa ruta.')
        return False
    else:
        subprocess.run(['mkdir', ruta_completa])
        print(f'✅    Carpeta "{nombre_carpeta}" creada en {ruta_completa}')
        return True



if __name__ == '__main__':
    main()