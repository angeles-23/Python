#!usr/bin/python3

import os, subprocess, shutil

ERROR_AL_LEER_EL_ARCHIVO_PASSWD = 'Se ha producido un error al leer el archivo passwd'
ERROR_AL_LEER_EL_ARCHIVO_GROUP = 'Se ha producido un error al leer el archivo group'
ERROR_AL_CREAR_LA_COPIA_DE_SEGURIDAD = 'Se ha producido un crear la copia de seguridad'
def main():
    limpiar_pantalla()
    archivo_passwd = '/etc/passwd'
    archivo_group = '/etc/group'
    backup_group = '/etc/group.bak'

    if not os.path.exists(archivo_group):
        print(f'El archivo {archivo_group} no existe')
        return 

    crear_backup()

    usuarios_por_gid = leer_usuarios()
    gids_existentes = obtener_gids()

    grupos_faltantes = {}
    for gid, usuarios in usuarios_por_gid.items():
        if gid not in gids_existentes:
            grupos_faltantes[gid] = usuarios

    if(grupos_faltantes):
        agregar_grupos_nuevos(grupos_faltantes)
    else:
        print('No hay grupos faltantes por añadir')

def limpiar_pantalla():
    subprocess.run(['clear'])


def leer_usuarios(archivo_passwd):
    usuarios_por_gid = {}

    try:
        with open(archivo_passwd, mode='r') as f:
            for linea in f:
                partes = linea.strip().split(':')

                if(len(partes) < 4):
                    continue

                usuario = partes[0]
                uid = int(partes[2])    
                gid = int(partes[3])

                if(1001 <= uid <= 1999 and usuario not in ['root', 'nobody']):
                    if gid not in usuarios_por_gid:
                        usuarios_por_gid[gid] = []
                    usuarios_por_gid[gid].append(usuario)

    except Exception as error:
        print(ERROR_AL_LEER_EL_ARCHIVO_PASSWD)
    
    return usuarios_por_gid


def obtener_gids(archivo_group):
    gids = set()
    try:
        with open(archivo_group, mode='r') as f:
            for linea in f:
                partes = linea.strip().split(':')

                if(len(partes) >= 3):
                    try:
                        gid = int(partes[2])
                        gids.add(gid)
                    except ValueError:
                        continue
    except Exception as error:
        print(ERROR_AL_LEER_EL_ARCHIVO_GROUP)
    return gids


def crear_backup(archivo_group, backup_group):
    try:
        shutil.copy(archivo_group, backup_group)
        print(f'Copia de seguridad creada en: {backup_group}')
    except Exception as error:
        print(ERROR_AL_CREAR_LA_COPIA_DE_SEGURIDAD)


def agregar_grupos_nuevos(archivo_group, grupos_nuevos):
    try:
        with open(archivo_group, mode='a') as f:
            for gid, usuarios in grupos_nuevos.items():
                linea = f'grupo{gid}:x:{gid}:{','.join(usuarios)}\n'
                f.write(linea)
        print('Grupos añadidos correctamente')
    except Exception as error:
        print('Error al añadir grupos:', error)



if __name__ == '__main__':
    main()