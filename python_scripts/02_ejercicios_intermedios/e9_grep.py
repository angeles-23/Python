#!/usr/bin/env python3
import subprocess, sys, os

def pedir_termino():
    while True:
        termino = input("Introduce el término a buscar: ").strip()
        if termino:
            return termino
        print("⚠️ El término no puede estar vacío. Inténtalo de nuevo.")

def pedir_directorio():
    while True:
        directorio = input("Introduce el directorio donde buscar: ").strip()
        if os.path.isdir(directorio) and os.access(directorio, os.R_OK):
            return directorio
        print(f"⚠️ El directorio '{directorio}' no existe o no es accesible. Inténtalo de nuevo.")

def ejecutar_grep(termino, directorio):
    try:
        resultado = subprocess.run(['grep', '-r', termino, directorio],capture_output=True,text=True)
        return resultado.returncode, resultado.stdout, resultado.stderr
    except Exception as e:
        return 2, '', f"Error al ejecutar grep: {e}"

def procesar_resultados(termino, directorio, returncode, stdout, stderr):
    if returncode == 0:
        # Coincidencias encontradas
        lineas = stdout.strip().split('\n')
        archivos = set()
        for linea in lineas:
            if ':' in linea:
                archivo = linea.split(':', 1)[0]
                archivos.add(archivo)
        print(f"\nEl término '{termino}' se encontró en {len(archivos)} archivo(s):")
        for archivo in sorted(archivos):
            print(f" - {archivo}")
        print(f"Número total de ocurrencias encontradas: {len(lineas)}\n")
        return True
    elif returncode == 1:
        # No hay coincidencias
        print(f"\nNo se encontraron coincidencias para '{termino}' en {directorio}.\n")
        return True
    elif returncode == 2:
        # Error de ejecución
        print(f"\nError al ejecutar grep:\n{stderr.strip()}")
        # Pedir acción al usuario: reintentar, cambiar directorio o salir
        while True:
            print("\n¿Qué deseas hacer?")
            print("1) Reintentar con el mismo término y directorio")
            print("2) Cambiar directorio")
            print("3) Salir")
            opcion = input("Selecciona una opción: ").strip()
            if opcion == '1':
                return 'retry'
            elif opcion == '2':
                return 'change_dir'
            elif opcion == '3':
                print("Saliendo del programa...")
                sys.exit(0)
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    else:
        # Otros códigos no previstos
        print(f"\nCódigo de salida inesperado de grep: {returncode}\n{stderr.strip()}")
        return True

def menu_post_busqueda():
    while True:
        print("¿Qué deseas hacer?")
        print("1) Nueva búsqueda con mismo directorio")
        print("2) Cambiar directorio")
        print("3) Salir")
        opcion = input("Selecciona una opción: ").strip()
        if opcion in ('1', '2', '3'):
            return opcion
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

def modo_interactivo(directorio=None):
    if directorio is None:
        directorio = pedir_directorio()

    while True:
        termino = pedir_termino()
        returncode, stdout, stderr = ejecutar_grep(termino, directorio)
        accion = procesar_resultados(termino, directorio, returncode, stdout, stderr)

        if accion == 'retry':
            # Repetir con mismo término y directorio
            continue
        elif accion == 'change_dir':
            directorio = pedir_directorio()
            continue
        elif accion is True:
            opcion = menu_post_busqueda()
            if opcion == '1':
                # Nueva búsqueda mismo directorio
                continue
            elif opcion == '2':
                # Cambiar directorio
                directorio = pedir_directorio()
            elif opcion == '3':
                print("Saliendo del programa...")
                sys.exit(0)

def main():
    args = sys.argv[1:]

    if len(args) == 2:
        termino, directorio = args
        if not termino.strip():
            print("⚠️ El término de búsqueda no puede estar vacío.")
            sys.exit(1)
        if not os.path.isdir(directorio) or not os.access(directorio, os.R_OK):
            print(f"⚠️ El directorio '{directorio}' no existe o no es accesible.")
            sys.exit(1)

        returncode, stdout, stderr = ejecutar_grep(termino, directorio)
        procesar_resultados(termino, directorio, returncode, stdout, stderr)
    else:
        modo_interactivo()

if __name__ == '__main__':
    main()
