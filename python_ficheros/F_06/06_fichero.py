import os
os.system('cls')

def crear_datos(file):
    f = open(file, 'w')
    f.close()
    return 'Archivo creado'

def cargar_datos(file):
    try:
        f = open(file, 'r')

        array_nuevo = []
        datos = f.readlines()

        for i in range(1, len(datos)):
            array_nuevo.append(datos[i])

        f.close()
        return array_nuevo
    
    except FileNotFoundError:
        return f'No existe el fichero {file}'
    
def mostrar_datos(file):

    datos = cargar_datos(file)

    print('Lista usuarios:')
    for dato in datos:
        id = dato.split(',')[0]
        nombre = dato.split(',')[1]
        edad = dato.split(',')[2]
        salario = dato.split(',')[3]
        print(f'ID:{id} - Nombre: {nombre} - Edad: {edad} - Salario por hora: {salario}', end='')
    
def buscar_usuario(file, usuario):
    try:
        f = open(file, 'r')

        datos = cargar_datos(file)
        usuario_buscado = []
        usuarioEncontrado = False

        for dato in datos:
            nombre = dato.split(',')[1]

            if nombre.startswith(usuario):
                usuarioEncontrado = True
                usuario_buscado = dato
                break
        
        if(usuarioEncontrado == True):
            f.close()
            return usuario_buscado
        else:
            return 'No existe dicho usuario'

    except FileNotFoundError:
        return 'No se ha encontrado el fichero'
        
def anadir_usuario(file, id, nombre, edad, salario_por_hora):
    try:
        f = open(file, 'a')
        f.write(f'{id},{nombre},{edad},{salario_por_hora}\n')
        f.close()
        return 'Usuario añadido'
    except Exception:
        return 'No se ha encontrado el fichero'

def borrar_usuario(file, name):
    try:
        f = open(file, 'r')
        lineas = cargar_datos(file)
    except Exception:
        return 'No se ha encontrado el archivo'
    
    
    nueva_lista_usuarios = []
    usuarios = f.readlines()

    for linea in lineas:
        nombre = linea.split(',')[0]

        if nombre != name:
            nueva_lista_usuarios.append(f'{linea}\n')

    f.close()

    f = open(file, 'w')
    for linea in nueva_lista_usuarios:
        f.write(linea)
    f.close()
    return 'Usuario eliminado'

  


if __name__ == '__main__':
    # datos_creados = crear_datos('datos.txt')
    # print(datos_creados)

    datos_cargados = cargar_datos('datos.txt')
    print(datos_cargados)

    mostrar_datos_formateados = mostrar_datos('datos.txt')

    print(buscar_usuario('datos.txt', 'Carlos'))
    print(anadir_usuario('datos.txt', 3, 'Angeles', 20, 25))

    print(borrar_usuario('datos.txt', 'Angeles'))