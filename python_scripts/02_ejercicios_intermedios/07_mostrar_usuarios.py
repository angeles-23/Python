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
    lista_usuarios = leer_archivo()
    mostrar_usuarios(lista_usuarios)


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

def mostrar_usuarios(lista_usuarios):
    UID_maximo = 1000
    diccionario_usuarios_grupo = {}

    for linea in lista_usuarios:
        nombre = linea.strip().split(':')[0].lower()
        UID = linea.strip().split(':')[1]
        GID = linea.strip().split(':')[2]
        inicial_nombre = nombre[0] 
        
        #  En caso de que ya exista la inicial añadir el nombre al diccionario de dicha inicial, junto con el UID 
        
        for letra in nombre[0]:
            print(letra)
            # if letra[0] == inicial_nombre:
            #     diccionario_usuarios_grupo[letra] = [nombre]
            # else:
            #     ...
            
        
    print(diccionario_usuarios_grupo)
          
# Mostrar usuarios ej.6

#  Abrir archivo modo='r'
    # Generar array modificado
# Guardar archivo w

if __name__ == '__main__':
    main()
