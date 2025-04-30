#! usr/bin/python

import subprocess, sys


def main():
    argumentos = sys.argv[1:]
    limpiar_pantalla()  
    ip = get_ip(argumentos)
    test_communications(ip)  
    


def get_ip(argumentos) -> str:
    if len(argumentos) != 1:
        print(f'Error: hay que suministrar una IP')
        sys.exit(1)     # Cierra el programa

    ip = argumentos[0]
    return ip


def test_communications(ip:str) -> None:
    test = subprocess.run(['ping', '-c', '1', ip], capture_output=True, text=True)
    
    if(test.returncode == 0):
        print('Hay comuncación con el destino')
    else:
        print('No hay comunicación con el destino')



def limpiar_pantalla():
    subprocess.run(['clear'])

if __name__ == '__main__':
    main()