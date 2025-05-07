import subprocess, sys

ERROR_CANTIDAD_ARGUMENTOS_INCORRECTOS = '❌   ERROR: Has introducido argumentos'
ERROR_COPIA_DE_SEGURIDAD = '❌   ERROR: No se ha podido hacer una copia de seguridad'
ERROR_ARCHIVO_NO_ENCONTRADO = '❌   ERROR: El archivo {archivo} no existe'

def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    copia_del_archivo()
    comprobar_argumentos(argumentos)
    leer_archivo()


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
    ruta = '/etc/passwd9'
    argumentos = sys.argv[1:]

    try:
        if (comprobar_argumentos(argumentos) == True):
            try:
                with open(ruta, mode='r') as f:
                    print('LEIDO')
            except FileNotFoundError:
                raise Exception(ERROR_ARCHIVO_NO_ENCONTRADO.format(archivo = ruta))
            
    except Exception as e:
        print(f'{e}')
        sys.exit(1)


# Mostrar usuarios ej.6


#  Abrir archivo modo='r'
    # Generar array modificado
# Guardar archivo w



if __name__ == '__main__':
    main()
