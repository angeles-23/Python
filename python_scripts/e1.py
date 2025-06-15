#!/usr/bin/python3
import subprocess, os, sys

ERROR_IP_BINARIA_INCORRECTA = 'Error: la IP binaria es incorrecta'
ERROR_RANGO_OCTETO = 'Error: el rango de los octetos es incorrecto'
ERROR_PERTENECE_A_RED = 'Error: la ip {e_ip} no pertenece a la red {e_red}'
ERROR_BINARIO_INCORRECTO = 'Error: el numero binario es incorrecto en cuanto a longitud'
ERROR_NUMERO_BINARIO = 'Error: el numero binario es incorrecto en cuanto a digitos 0 y 1'


class Ejercicio:
    def main():
        try:
            
            Ejercicio.limpiar_pantalla()
            
            args = sys.argv[1:]
            if len(args) == 0:
                sys.exit('Error. Tienes que introducir una opcion como argumento')

            opcion = args[0]

            match opcion:
                case 'decimal-a-binario':
                    arg_decimal = args[1]
                    if Ejercicio.validar_ip(arg_decimal) == None:
                        print(Ejercicio.decimal_a_binario(arg_decimal))
                    
                case 'binario-a-decimal':
                    arg_binario = args[1]
                    
                    if len(arg_binario) != 35:
                        raise Exception(ERROR_BINARIO_INCORRECTO)

                    binarios = arg_binario.strip().split('.')
                    
                    for binario in binarios:
                        for numero in binario:
                            if numero != '0' and numero != '1':
                                raise Exception(ERROR_NUMERO_BINARIO)
                            
                    print(Ejercicio.binario_a_decimal(arg_binario))

                case 'validar-ip':
                    arg_ip = args[1]
                    
                    if Ejercicio.validar_ip(arg_ip) == False:
                        print(ERROR_RANGO_OCTETO)

                    print('La Ip es correcta, felicidades !!!')

                case 'pertenece':
                    arg_ip = args[1]
                    arg_red = args[2]
                    arg_decimal = args[3]

                    if Ejercicio.pertenece_a_red(arg_ip, arg_red, arg_decimal) == True:
                        print('Si pertenece a la red.')


                case _:
                    sys.exit(f'Opción incorrecta: {opcion}')

        except Exception as error:
            print(error)


    def limpiar_pantalla():
        subprocess.run(['clear'])

    def binario_a_decimal(ip_binaria: str) -> str:
        """
        Convierte una IP binaria (ej: '11000000.10101000.00000001.00000001') a decimal (ej: '192.168.1.1')
        Devuelve:
            str: IP en formato decimal
        """
        try:
            cadena_decimal = ''

            for i in range(4):
                octeto = ip_binaria.strip().split('.')[i]
                cadena_decimal += str(int(octeto, 2))
                
                if i != 3:
                    cadena_decimal += '.'
                
        except Exception as error:
            sys.exit(error)
        
        return cadena_decimal

    def decimal_a_binario(ip_decimal: str) -> str:
        """
        Convierte una IP decimal (ej: '192.168.1.1') a binaria (ej: '11000000.10101000.00000001.00000001')
        Devuelve:
            str: IP en formato binario
        """
        binarios = []

        for i in range(4):
            numero = int(ip_decimal.strip().split('.')[i])
            cadena_binaria = ''

            while numero > 0:
                resto = numero % 2
                cadena_binaria = str(resto) + cadena_binaria
                numero = numero // 2
            
            binarios.append(cadena_binaria.zfill(8))

        union = str('.'.join(binarios))
        return union

    def pertenece_a_red(ip: str, red: str, mascara: str) -> bool:
        """
        Indica si la IP pertenece a la red con esa máscara.
        Devuelve:
            bool: True si pertenece, False si no
        """

        try:
            red_ultimo_octeto = int(red.strip().split('.')[3])
            red_maximo_octeto = 255
            red_minimo_octeto = 0

            ip_ultimo_octeto = int(ip.strip().split('.')[3])

            if not ip.startswith(red[0:7]):
                return False

            if ip_ultimo_octeto < red_minimo_octeto or ip_ultimo_octeto > red_maximo_octeto:
                return False
            
        except Exception as error:
            sys.exit(error)

        return True

    def validar_ip(ip: str) -> None:
        """
        Valida que la IP tenga formato correcto (decimal con 4 octetos entre 0 y 255).
        Lanza:
            Exception si no es válida
        Devuelve:
            None
        """
        try:
            if len(ip) > 15:
                raise Exception(ERROR_IP_BINARIA_INCORRECTA)
            
            octetos = ip.strip().split('.')
            
            for octeto in octetos:
                octeto_int = int(octeto)

                if octeto_int < 0 or octeto_int > 255:
                    raise Exception(ERROR_RANGO_OCTETO)

        except Exception as error:
            sys.exit(error)



if __name__ == '__main__':
    Ejercicio.main()