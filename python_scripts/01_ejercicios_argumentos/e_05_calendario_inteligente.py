#! usr/bin/python3

import subprocess, sys


def main():
    argumentos = sys.argv[1:]
    print(obtener_anio_actual())


def obtener_anio_actual():
    resultado = subprocess.run(['date'], capture_output=True, text=True)
    
    if resultado.returncode != 0:
        print('Se ha producido un error al obtener la fecha actual')

    return resultado

if __name__ == '__main__':
    main()