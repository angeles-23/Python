import os
os.system('cls')

'''
Busca los códigos postales de las siguientes ciudades: Cáceres, Lorca, Madrid, Padrón, La Unión, Teruel, Lugo, Totana, Rueda y Santander.

Algunas ciudades tienen varios códigos postales, usa solo uno de ellos.
Almacena los datos en un diccionario.
Muestra por la consola: Los códigos postales almacenados en nuestra base de datos son:
Muestra por consola: Las ciudades que pertenecena a la comunidad murciana son: (los códigos postales de Murcia están comprendidos entre 30000 y 30999)
'''

CODIGOS_POSTALES = {

}

CODIGOS_POSTALES[10001] = 'Caceres'
CODIGOS_POSTALES[30800] = 'Lorca'
CODIGOS_POSTALES[28001] = 'Madrid'
CODIGOS_POSTALES[15900] = 'Padrón'
CODIGOS_POSTALES[30360] = 'La Unión'
CODIGOS_POSTALES[44001] = 'Teruel'
CODIGOS_POSTALES[27001] = 'Lugo'
CODIGOS_POSTALES[30850] = 'Totana'
CODIGOS_POSTALES[47490] = 'Rueda'
CODIGOS_POSTALES[39001] = 'Santander'


def mostrar_codigos_postales(diccionario_codigos_postales):
    print(f'Códigos postales: {diccionario_codigos_postales.keys()}')


def mostrar_ciudades_murcianas(diccionario_codigos_postales):
    print('Las ciudades murcianas son: ')

    for CLAVE_codigo_postal in diccionario_codigos_postales:
        if (30000 <= CLAVE_codigo_postal <= 30999):
            print(f'{diccionario_codigos_postales[CLAVE_codigo_postal]}')


if __name__ == '__main__':
    mostrar_codigos_postales(CODIGOS_POSTALES)
    mostrar_ciudades_murcianas(CODIGOS_POSTALES)