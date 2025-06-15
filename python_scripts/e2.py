#!/usr/bin/python3
import subprocess, os, sys
import e1

ERROR_IP_ADDR = 'Error: no se ha podido ejecutar el comnado "ip addr"'
ERROR_IP_ROUTE = 'Error: no se ha podido ejecutar el comando "ip route"'
ERROR_SERVIDOR_DNS = 'Error: no se ha podido ejecutar el comando "/etc/resolv.conf"'
ERROR_VERIFICACION = 'Error: en la verificación de datos'
ERROR_LONGITUD = 'Error: longitud de {e_valor} incorrecto'
ERROR_RANGO= 'Error: fuera del rango establecido (0-256) -> {e_valor}'
ERROR_GATEWAY_INCORRECTO = 'Error: el {e_gateway} no pertenece a la misma red que la ip {e_ip}'

def main():
    try:
        limpiar_pantalla()
        ip, mascara = obtener_ip_y_mascara()
        gateway = obtener_gateway()
        dns = obtener_dns()
        validar_datos(ip, mascara, gateway, '192.168.1.365')
        escribir_informe(ip, mascara, gateway, dns)

    except Exception as error:
        print(error)

def limpiar_pantalla():
    subprocess.run(['clear'])

def obtener_ip_y_mascara() -> tuple[str, str]:
    """
    Extrae la IP y la máscara de red del sistema usando `ip addr`.
    Devuelve:
        tuple: (ip, mascara) en formato decimal
    """
    try:
        resultado_ip_addr = subprocess.run(['ip', 'addr'], capture_output=True, text=True)

        if resultado_ip_addr.returncode != 0:
            raise Exception(ERROR_IP_ADDR)
        
        contenido = resultado_ip_addr.stdout.splitlines()

        ip_y_mascara = contenido[2].strip().split(' ')[1]
        ip = ip_y_mascara.strip().split('/')[0]
        mascara = int(ip_y_mascara.strip().split('/')[1])


        # Máscara a binario
        mascara_binaria = ''
        contador_puntos = 0

        for i in range(0,32):
            contador_puntos += 1

            if i < mascara:
                mascara_binaria += '1'
            else:
                mascara_binaria += '0'

            if contador_puntos == 8 and i != 31:
                contador_puntos = 0
                mascara_binaria += '.'

        
        # Binario a decimal
        mascara_decimal = ''

        for i in range(0, 4):
            octeto = mascara_binaria.strip().split('.')[i]
            mascara_decimal += str(int(octeto, 2))
            
            if i != 3:
                mascara_decimal += '.'

    except Exception as error:
        sys.exit(error)

    return (ip, mascara_decimal)

def obtener_gateway() -> str:
    """
    Extrae la puerta de enlace del sistema usando `ip route`.
    Devuelve:
        str: gateway (ej: '192.168.1.1')
    """
    try:
        resultado_ip_route = subprocess.run(['ip','route'], capture_output=True, text=True)

        if resultado_ip_route.returncode != 0:
            raise Exception(ERROR_IP_ROUTE)
        
        contenido = resultado_ip_route.stdout.splitlines()
        ip_route = contenido[1].strip().split(' ')[0]
        ip = ip_route.strip().split('/')[0]

    except Exception as error:
        print(error)
    
    return ip

def obtener_dns() -> str:
    """
    Lee el primer servidor DNS de `/etc/resolv.conf`.
    Devuelve:
        str: DNS (ej: '8.8.8.8')
    """
    try:
        resultado_DNS = subprocess.run(['cat', '/etc/resolv.conf'], capture_output=True, text=True)

        if resultado_DNS.returncode != 0:
            raise Exception(ERROR_SERVIDOR_DNS)
        
        contenido_dns = resultado_DNS.stdout.splitlines()
        dns = contenido_dns[1].strip().split(' ')[1]
        
    except Exception as error:
        sys.exit(error)
    
    return dns

def validar_datos(ip: str, mascara: str, gateway: str, dns: str) -> bool:
    """
    Verifica que todos los datos tengan formato correcto.
    Devuelve:
        bool: True si todo está bien, False o Exception si algo falla
    """
    try:
        datos = [ip, mascara, gateway, dns]

        for dato in datos:

            if dato == dns:
                ip_octetos = ip.strip().split('.')
                gateway_octetos = gateway.strip().split('.')

                if ip_octetos[:3] != gateway_octetos[:3]:
                    raise Exception(ERROR_GATEWAY_INCORRECTO.format(e_gateway = gateway, e_ip = ip))

            octetos = dato.strip().split('.')
            print(octetos)
            
            if len(octetos) != 4:
                raise Exception(ERROR_LONGITUD.format(e_valor = len(octetos)))
            
            for octeto in octetos:
                if int(octeto) < 0 or int(octeto) > 255:
                    raise Exception(ERROR_RANGO.format(e_valor = octeto))

    except Exception as error:
        sys.exit(error)

    return True


def escribir_informe(ip: str, mascara: str, gateway: str, dns: str) -> None:
    """
    Escribe los datos en un archivo 'informe_red.txt' en formato legible.
    Devuelve:
        None
    """
    pass


if __name__ == '__main__':
    main()