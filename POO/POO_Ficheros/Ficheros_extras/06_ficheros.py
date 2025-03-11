import os 
os.system('cls')

def cargar_datos(file):
    '''
    Cargar los datos desde el archivo de texto
    '''

    try:
        # Intentamos abrir el documento y devolver la información del array
        f = open(file, 'r')
        array = f.readlines()
        f.close()

        lineas_devolver = []
        contador = 0

        for linea in array:
            if contador >= 1:
                lineas_devolver.append(linea)
            contador += 1

        return lineas_devolver
    
    except FileNotFoundError:
        return f'Error: No se encuentra el fichero indicado'
   
def mostrar_datos(file):
    ''' Formatea el documento '''
    array = cargar_datos(file)
    print(array)

    print('Lista usuarios:')
    # Trabajamos linea a linea para imprimir los datos de forma estética
    for linea in array:
        # Obtenemos cada uno de los elementos:
        array_linea = linea.split(',')
        id = array_linea[0]
        nombre = array_linea[1]
        edad = array_linea[2]
        salario = array_linea[3]
        # Imprimimos
        print(f'ID: {id} - Nombre: {nombre} - Edad: {edad} - Salario: {salario}'.strip())

def buscar_usuario(file, name):
    '''
    Devuelve la linea con la información de la persona que buscamos 
    '''
    # Creo una variable que inicializo en Falso. Cambio a True si se cumple la condicion usuario encontrado
    array = cargar_datos(file)

    existe = False

    for linea in array:
        array_linea = linea.split(',')
        id = array_linea[0]
        nombre = array_linea[1]
        edad = array_linea[2]
        salario = array_linea[3]

        if name == nombre:
            existe = True
            print('Persona encontrada: ')
            print(f'ID:{id} - Nombre:{nombre} - Edad:{edad} - Salario por hora:{salario}')
    
    if not existe:
        print('No existe una persona con ese nombre')

def aniadir_datos(file, usuario):
    '''
    Añdir un usuario nuevo, dado las caracteristicas
    '''
    f = open(file, 'a')
    f.write(usuario)
    f.close()
    print('Usuario añadido')



def eliminar_usuario(file, id):
    ''' 
    Si existe el usuario, eliminados sus datos
    '''
    # Acceder a la información del fichero completo
    f = open(file, 'r')
    array_todas_las_lineas = f.readlines()

    # Crear un array que quqremos guardar en el fichero con todas las lineas excepto la que contenga el parametro id
    array_lineas_a_imprimir = []

    for linea in array_todas_las_lineas: 
        if not linea.startswith(id):
            array_lineas_a_imprimir.append(linea)
    
    f = open(file, 'w')
    for linea in array_lineas_a_imprimir:
        f.write(linea)

    f.close()




if __name__ == '__main__':
    # datos_cargados = cargar_datos('datos.txt')
    # datos = mostrar_datos('datos.txt')
    # buscar_un_usuario = buscar_usuario('datos.txt', '3, Julio, 58,35')
    eliminar_un_usuario = eliminar_usuario('datos.txt', '1')