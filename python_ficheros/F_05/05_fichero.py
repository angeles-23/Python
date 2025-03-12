# Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

def get_phone(file, client):
    '''
    Función que devuelve el teléfono de un cliente de un fichero dado.
    Parámetros:
        file: Es un fichero con los nombres y teléfonos de clientes.
        client: Es una cadena con el nombre del cliente.
    Devuelve:
        El teléfono del cliente guardado en el fichero o un mensaje de error si el teléfono o el fichero no existe.
    '''
    
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return 'No existe un cliente con ese numero'
    else:
        lineas = f.readlines()

        for linea in lineas:
            if(linea.startswith(client)):
                telefono = linea.split(',')[1]
                return telefono

        f.close()
        return 'No existe ningún cliente con ese telefono'
            

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
    try:
        f = open(file, 'a')
    except FileNotFoundError:
        return 'No existe ningun fichero'
    else:
        f.write(f'{client},{telf}\n')
        f.close()
        return 'El telefono se ha añadido'

def remove_phone(file, client):
    '''
    Función que elimina el teléfono de un cliente de un fichero dado.
    Parámetros:
        file: Es un fichero con los nombres y teléfonos de clientes.
        client: Es una cadena con el nombre del cliente.
    Devuelve:
        Un mesaje informando sobre si el teléfono se ha borrado o ha habido algún problema.
    '''
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return 'No se ha encontrado el fichero'  
    else:
        nueva_lista_clientes = []
        clientes = f.readlines()

        for cliente in clientes:
            nombre = cliente.split(',')[0]
            
            if nombre != client:
                nueva_lista_clientes.append(f'{cliente}\n')
        
        f.close()

        try:
            f = open(file, 'w')
        except FileNotFoundError:
            return f'No se ha encontrado el fichero {file}'
        else:
            for linea in nueva_lista_clientes:
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
    return f'Se ha creado el fichero {file}'
 
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
        return f'El fichero {file} no existe'
    else:
        contenido = f.read()
        f.close()
        return contenido

def menu():
    '''
    Función que presenta un menú con las operaciones disponibles sobre un listín telefónico y devuelve la opción seleccionada por el usuario.
    Devuelve:
        La opción seleccionada por el usuario.
    '''
    print('Gesión del listín telefónico')
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
    import os 
    os.system('cls')
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
            print(remove_phone(file, name))
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