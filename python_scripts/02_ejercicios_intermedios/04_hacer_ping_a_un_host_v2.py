#! usr/bin/python

import subprocess, sys

ERROR_NUMERO_ARGUMENTOS = 1
ERROR_LONGITUD_INCORRECTA = 2
ERROR_DIRECCION_NO_VALIDA = 3

def main():
    argumentos = sys.argv[1:]
    limpiar_pantalla()

    ip = recoger_argumentos(argumentos)
    ip_valida = validar_ip(ip)
    test_communications(ip_valida)


def limpiar_pantalla():
    subprocess.run(['clear'])


def recoger_argumentos(argumentos):

    if len(argumentos) != 0 and len(argumentos) != 1:
        print('Error: Cantidad de argumentos incorrecto')
        sys.exit(ERROR_NUMERO_ARGUMENTOS)

    if(len(argumentos) == 0):
        ip = input('IP: ')
    else:
        ip = argumentos[0]

    return ip
    

def validar_ip(ip) -> str:
    formato_ip = ip.split('.')

    if(len(formato_ip) != 4):
        print('Error: longitud incorrecta')
        sys.exit(ERROR_LONGITUD_INCORRECTA)
    else:
        for num in formato_ip:
            numero = int(num)
            if(numero >=0 and numero <=255):
                ip_valida = ip
                es_valido = True
            else:
                es_valido = False
                break
        
        if(es_valido == True):
            print(f'La IP:{ip} es válida')
            return ip_valida
        else:
            print('Error. El rango de los números es incorrecto')
            sys.exit(ERROR_DIRECCION_NO_VALIDA)

    
def test_communications(ip:str) -> None:
    test = subprocess.run(['ping', '-c', '1', ip], capture_output=True, text=True)
    
    if(test.returncode == 0):
        print('Hay comuncación con el destino')
    else:
        print('No hay comunicación con el destino')



if __name__ == '__main__':
    main()