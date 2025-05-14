#! usr/bin/python3
import subprocess, sys

ERROR_CANTIDAD_ARGUMENTOS_INCORRECTOS = '❌   ERROR: Has introducido argumentos'
ERROR_COPIA_DE_SEGURIDAD = '❌   ERROR: No se ha podido hacer una copia de seguridad'
ERROR_ARCHIVO_NO_ENCONTRADO = '❌   ERROR: El archivo {archivo} no existe'

def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    copia_del_archivo()
    comprobar_argumentos(argumentos)
    print(leer_archivo())
    lista_usuarios = leer_archivo()
    agrupar_y_mostrar_usuarios(lista_usuarios)


def limpiar_pantalla():
    subprocess.run('clear')


# Realizar una copia de seguridad
def copia_del_archivo():
    # cp /etc/passwd /etc/passwd.bak
    try:

        resultado = subprocess.run(['cp', '/etc/passwd', '/etc/passwd.back'], capture_output=True, text=True)

        if resultado.returncode == 0:
            print('📋   Copia de seguridad realizada con éxito')
        else:
            raise Exception(ERROR_COPIA_DE_SEGURIDAD)
        
    except Exception as error:
        print(f'{error}')
        sys.exit(1)

# Comprobar que no se introduzcan argumentos
def comprobar_argumentos(argumentos):
    son_argumentos_correctos = True
    try:
        if len(argumentos) != 0:
            raise Exception(ERROR_CANTIDAD_ARGUMENTOS_INCORRECTOS.format())
        else:
            return son_argumentos_correctos
        
    except Exception as e:
        son_argumentos_correctos = False 
        print(f'{e}')
        sys.exit(1)
        return son_argumentos_correctos

# Leer archivo etc
def leer_archivo():
    ruta = '/etc/passwd'
    argumentos = sys.argv[1:]

    try:
        if (comprobar_argumentos(argumentos) == True):
            try:
                with open(ruta, mode='r') as f:
                    lista_usuarios_UID_mayor_1000 = []
                    
                    for linea in f:
                        # print(linea, end='')
                        usuario = linea.strip().split(':')[0]
                        UID = int(linea.strip().split(':')[2])
                        GID = linea.strip().split(':')[3]
                        UID_nobody = 65534
                        
                        if(UID >= 1000 and UID != UID_nobody):
                            lista_usuarios_UID_mayor_1000.append(f'{usuario}:{UID}:{GID}')

                    return lista_usuarios_UID_mayor_1000

            except FileNotFoundError:
                raise Exception(ERROR_ARCHIVO_NO_ENCONTRADO.format(archivo = ruta))
            except Exception as e:
                raise Exception(f'Se produjo un error al leer el archivo: {e}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
        sys.exit(1)

def agrupar_y_mostrar_usuarios(lista_usuarios):
    ruta = '/etc/passwd'
    UID_actual = 1000
    UID_maximo = 2000
    diccionario_usuarios_grupo = {}
    inicial_a_GID = {}

    print(f'Usuarios simulados ({len(lista_usuarios)}):')
    for linea in lista_usuarios:
        nombre = linea.strip().split(':')[0].lower()
        UID = linea.strip().split(':')[1]
        GID = linea.strip().split(':')[2]
        inicial = nombre[0] 

        if(UID >= 1001 and UID < 2000):
            print(f'- {nombre} (UID {UID})')
            if inicial not in diccionario_usuarios_grupo:
                diccionario_usuarios_grupo[inicial] = []
                inicial_a_GID[inicial] = UID_actual
                UID_actual += 1
            
            diccionario_usuarios_grupo[inicial].append((nombre, UID))
        
    
    for inicial in sorted(diccionario_usuarios_grupo.keys()):
        gid = inicial_a_GID[inicial]
        print(f'\nUsuarios en el grupo {gid}')
        for usuario in diccionario_usuarios_grupo[inicial]:
            print(f'- {usuario[0]} (UID {usuario[1]})')

    print(diccionario_usuarios_grupo)


    with open(ruta, 'w') as f:
        f.writelines(diccionario_usuarios_grupo)
    print("✔️    Los usuarios han sido agrupados correctamente por GID.")

if __name__ == '__main__':
    main()
