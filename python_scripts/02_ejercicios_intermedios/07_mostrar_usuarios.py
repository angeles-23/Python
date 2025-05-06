import subprocess, sys

ERROR_CANTIDAD_ARGUMENTOS_INCORRECTOS = '❌   ERROR: Has introducido argumentos'
ERROR_ARCHIVO_NO_ENCONTRADO = '❌   ERROR: El archivo {archivo} no existe'

def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    comprobar_argumentos(argumentos)
    leer_archivo()


def limpiar_pantalla():
    subprocess.run('clear')


def copia_del_archivo():
    # cp /etc/passwd /etc/passwd.bak
    subprocess.run(['cp', '/etc/passwd', '/etc/passwd.back'])
    ...


# Comprobar que no se introduzcan argumentos
def comprobar_argumentos(argumentos):
    try:
        if len(argumentos) != 0:
            raise Exception(ERROR_CANTIDAD_ARGUMENTOS_INCORRECTOS.format())
    except Exception as e:
        print(f'{e}')
        sys.exit(1)



# Leer archivo etc
def leer_archivo():
    try:
        ruta_fichero = '/etc/password/12'
        with open(ruta_fichero) as f:
            ...
            raise Exception(ERROR_ARCHIVO_NO_ENCONTRADO.format(ruta_fichero = archivo))
    except Exception as e:
        print(f'{e}')
        sys.exit(1)


# Mostrar usuarios ej.6


#  Abrir archivo modo='r'
    # Generar array modificado
# Guardar archivo w



if __name__ == '__main__':
    main()
