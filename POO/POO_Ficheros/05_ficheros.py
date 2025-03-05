# Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa debe incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
import os
os.system('cls')

def get_phone(file, client):
    '''
    Función que devuelve el teléfono de un cliente de un fichero dado.
    Parámetros:
        file: Es un fichero con los nombres y teléfonos de clientes.
        client: Es una cadena con el nombre del cliente.
    Devuelve:
        El teléfono del cliente guardado en el fichero o un mensaje de error si el teléfono o el fichero no existe.
    '''
    # Buscar el fichero, si se encuentra, recorrer las lineas y buscar el nombre del cliente con el dato del cliente
    try:
        f = open(file, 'r')
        arrayAgenda = f.readlines()
        print(arrayAgenda)
        
        for linea in arrayAgenda:
            if linea.startswith(client):
                arrayLinea = linea.strip().split(',')
                telefono = arrayLinea[1]
                return f'{telefono}\n'

        f.close()
        return f'Error, no se ha encontrado en la agenda un contacto de nombre {client}'

    except FileNotFoundError:
        return f'El fichero {file} no existe.'

   
def add_phone(file, client, telf):
    '''
    Función que añade el teléfono de un cliente de un fichero dado.
    Parámetros:
        file: Es un fichero con los nombres y teléfonos de clientes.
        client: Es una cadena con el nombre del cliente.
        telf: Es una cadena con el teléfono del cliente.
    Devuelve:
        Un mesaje informando sobre si el teléfono se ha añadido o ha habido algún problema.
    '''
    # 'a' de append -> añadir
    try:
        f = open(file, 'a')
        f.write(f'{client},{telf}\n')
        f.close()
        return('Contacto añadido.')
    except FileNotFoundError:
        print(f'El fichero {file} no existe.')


def remove_contact(file, client):
    '''
    Función que elimina el contacto de un cliente de un fichero dado.
    Parámetros:
        file: Es un fichero con los nombres y teléfonos de clientes.
        client: Es una cadena con el nombre del cliente.
    Devuelve:
        Un mensaje informando sobre si el teléfono se ha borrado o ha habido algún problema.
    '''

    arraySinContacto = []

    try:
        f = open(file, 'r')
        arrayLineasAgenda = f.readlines()

        # Comprobación de si existe un usuario con el nombre que se quiere borrar
        existeCliente = False

        for linea in arrayLineasAgenda:
            if(linea.startswith(client)):
                existeCliente = True
                
        if existeCliente == False:
            return f'Error: no existe un cliente con ese nombre'

        # Creación de un nuevo array con los contactos exceptuando el que se quiere borrar
        for linea in arrayLineasAgenda:
            if not linea.startswith(client):
                arraySinContacto.append(linea)
        f.close()

    except FileNotFoundError:
        return f'Error. No se ha podido encontrar el fichero {file}'
    else:
        # Sobreescribe el archivo con los contactos actualizados
        f = open(file, 'w')
        f.write(arraySinContacto)
        for linea in arraySinContacto:
            f.write(linea)
        f.close()
        return 'Contacto eliminado'


def create_directory(file):
    '''
    Función que crea un fichero vacío para guardar un listín telefónico.
    Parámetros:
        file: Es un fichero.
    Devuelve:
        Un mesaje informando sobre si el fichero se ha creado correctamente o no.
    '''
    f = open(file, 'w')
    f.close()
    return 'Fichero creado'


def show_agenda(file):
    '''
    Función que muestra el contenido completo de un fichero dado.
    Paramétros:
        file: Es un fichero
    Devuelve:
        Un mensaje con todo el contenido del fichero si se realmente existe
    '''
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return f'El fichero {file} no existe.'
    else:
        agenda = f.read()
        f.close()
        return agenda


def menu():
    '''
    Función que presenta un menú con las operaciones disponibles sobre un listín telefónico y devuelve la opción seleccionada por el usuario.
    Devuelve:
        La opción seleccionada por el usuario.
    '''
    print('Gestión del listín telefónico')
    print('============================')
    print('1 - Consultar un teléfono')
    print('2 - Añadir un teléfono')
    print('3 - Eliminar un teléfono')
    print('4 - Crear el listín')
    print('5 - Mostrar Agenda completa')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def directory():
    '''
    Función que lanza la aplicación para la gestión del listín telefónico.
    '''
    file = 'listin.txt' 
    while True:
        option = menu()
        if option == '1':
            name = input('Introduce el nombre del cliente: ')
            print(get_phone(file, name))
        elif option == '2':
            name = input('Introduce el nombre del cliente: ')
            telf = input('Introduce el teléfono del cliente: ')
            print(add_phone(file, name, telf))
        elif option == '3':
            name = input('Introduce el nombre del cliente: ')
            print(remove_contact(file, name))
        elif option == '4':
            print(create_directory(file))
        elif option == '5':
            print(show_agenda(file))
        else:
            break
        print()
    return


if __name__ == "__main__":
    directory()