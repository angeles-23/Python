#! usr/bin/python3

import subprocess, sys
from terminal_colors import TerminalColors

ERROR_CANTIDAD_DE_ARGUMENTOS = 1
ERROR_CANTIDAD_DE_DATOS_SUBRED = 2
ERROR_DIGITOS_FUERA_DE_RANGO_SUBRED = 3



def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    subred = comprobar_subred(argumentos)
    subred_correcta = validar_subred(subred)
    test_communications_host(subred_correcta)



def comprobar_subred(argumentos) -> str:
    puertas_enlace = {'DAW1':'192.168.0', 'MURCIAEDUCA-DOC':'10.88.75', 'Datos':'192.168.239'}
                         #  192.168.0.1                 10.88.75.254        192.168.239.189

    if len(argumentos) == 1:
        subred = argumentos[0]
    elif len(argumentos) == 0:
        subred = puertas_enlace
    else:
        print(f'❌    Error: La cantidad de argumentos es incorrecto')
        sys.exit(ERROR_CANTIDAD_DE_ARGUMENTOS)

    return subred



def validar_subred(subred:str) -> str:

    if type(subred) == dict:
        return subred

    elif type(subred) == str:
        formato_subred = subred.split('.')

        if(len(formato_subred) != 3):
            print(f'❌    Error: Cantidad de datos de la subred incorrecta')
            sys.exit(ERROR_CANTIDAD_DE_DATOS_SUBRED)

        else:   
            for n in formato_subred:
                numero = int(n)

                if(numero >= 0 and numero <= 255):
                    subred_valida = subred
                    es_valido = True
                else:
                    es_valido = False
                    break
                    
            if es_valido == True:
                return subred_valida
            else:
                print(f'❌    Error: El rango de los digitos es incorrecto')
                sys.exit(ERROR_DIGITOS_FUERA_DE_RANGO_SUBRED)



def test_communications_host(subred:str) -> None:

    direcciones_con_comunicacion = []

    if type(subred) == dict:
        for ultimo_digito,(clave, valor) in enumerate(subred.items()):
            print(f'WIFI: {clave}')

            for ultimo_digito in range(1, 255):
                try:
                    ip = f'{valor}.{ultimo_digito}'
                    resultado = subprocess.run(['ping', '-c', '1', ip], 
                                                capture_output=True, 
                                                text=True, 
                                                timeout=0.25)

                    if resultado.returncode == 0:
                        print(f'📡    {TerminalColors.GREEN}{clave} - Hay comunicación con el destino <{ip}>{TerminalColors.RESET}')
                        direcciones_con_comunicacion.append(ip)
                except subprocess.TimeoutExpired:
                    print(f'🕐    {clave} - No hay comunicación con el destino <{ip}>')
            
            print()

    elif type(subred) == str:

        for ultimo_digito in range(1, 255): #255
            try:
                ip = f'{subred}.{ultimo_digito}'
                resultado = subprocess.run(['ping', '-c', '1', ip], 
                                        capture_output=True, 
                                        text=True, 
                                        timeout=0.25)
                
                if resultado.returncode == 0:
                    print(f'📡    {TerminalColors.GREEN}Hay comunicación con el destino <{ip}>{TerminalColors.RESET}')
                    direcciones_con_comunicacion.append(ip)
            except subprocess.TimeoutExpired:
                print(f'🕐    No hay comunicación con el destino <{ip}>')

    print('\nDIRECCIONES DISPONIBLES')
    for direccion in direcciones_con_comunicacion:
        print(direccion)




def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == '__main__':
    main()