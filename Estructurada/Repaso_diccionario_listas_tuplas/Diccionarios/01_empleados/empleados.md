# EMPLEADOS

**1. Buscar empleados por rango de edad**
- Ejercicio: Dado un rango de edades, crea una función que retorne una lista de empleados que se encuentren dentro de ese rango (por ejemplo, de 30 a 40 años).
Ejemplo: Si el rango es 30-40, el resultado debería incluir a "Ana Martínez", "Carlos Gómez", "Raquel Fernández", etc.
``` python
def buscar_empleados_entre_30_40(diccionario_empleados):
    edades_encontradas = []

    for numero_empleado in diccionario_empleados:
        empleado = diccionario_empleados[numero_empleado]

        if(empleado['edad'] >= 30 and empleado['edad'] <= 40):
            edades_encontradas.append(empleado['nombre'])

    return edades_encontradas


if __name__ == '__main__':
buscar_empleados = buscar_empleados_entre_30_40(empleados)
print(buscar_empleados)     
# ['Ana Martínez', 'Marta López', 'Carlos Gómez', 'Sara Ruiz']
```


**2. Calcular la antigüedad de cada empleado**
- Ejercicio: Implementa una función que calcule y muestre la antigüedad de cada empleado en la empresa (en años).
Pistas: Puedes utilizar la fecha actual y restar el año de ingreso de cada empleado. Si necesitas exactitud, puedes hacer el cálculo considerando meses y días.
``` python

def calcular_antiguedad_dias(diccionario_empleados):
    fecha_actual = datetime.today().date()
    antiguedad_empleados = []

    for numero_empleado in diccionario_empleados:
        empleado = diccionario_empleados[numero_empleado]
        fecha_ingreso_empresa = datetime.strptime(empleado['fecha_ingreso'], '%Y-%m-%d').date()
        
        antiguedad = fecha_actual - fecha_ingreso_empresa
        antiguedad_empleados.append(antiguedad.days)

    return antiguedad_empleados


def calcular_anios_antiguedad(diccionario_empleados):
    dias_antiguedad = calcular_antiguedad_dias(diccionario_empleados)

    antiguedad = {}

    i = 0
    
    for numero_empleado in diccionario_empleados:
        
        if (i <= len(dias_antiguedad)):
            
            anios_antiguedad = dias_antiguedad[i]/365
            i += 1
            antiguedad[numero_empleado] = {'anios': int(f'{anios_antiguedad:.0f}')}

    return antiguedad
    
    
        
if __name__ == '__main__':
    antiguedad_empleados = calcular_antiguedad_dias(empleados)
    print(antiguedad_empleados)
    print(calcular_anios_antiguedad(empleados))
```


**3. Modificar salario de un empleado**
- Ejercicio: Crea una función que permita actualizar el salario de un empleado dado su ID. La función debe aceptar el ID del empleado y el nuevo salario como parámetros y luego actualizar el diccionario de empleados.
``` python
def actualizar_salario(diccionario_empleados, ID, nuevo_salario):

    for numero_empleado in diccionario_empleados:
        if ID == numero_empleado:
            diccionario_empleados[numero_empleado]['salario'] = int(nuevo_salario)
            diccionario_empleado = diccionario_empleados[numero_empleado]

    return diccionario_empleado

if __name__ == '__main__':
    salario_actualizado = actualizar_salario(empleados, 1001, 150)
    print(salario_actualizado)
```


**4. Encontrar al empleado con el salario más alto y más bajo**
- Ejercicio: Implementa una función que retorne el nombre y salario del empleado que tiene el salario más alto, y otra que retorne el del salario más bajo.
``` python
def encontrar_empleado_salario_mayor(empleados):

    numero_empleado_salario_mayor = 1001

    for empleado in empleados:
        if(empleados[empleado]['salario'] > empleados[numero_empleado_salario_mayor]['salario']):
            numero_empleado_salario_mayor = empleado
            
    return empleados[numero_empleado_salario_mayor]['nombre'], empleados[numero_empleado_salario_mayor]['salario']


def encontrar_empleado_salario_menor(empleados):

    numero_empleado_menor_salario = 1001

    for empleado in empleados:
        if(empleados[empleado]['salario'] < empleados[numero_empleado_menor_salario]['salario']):
            numero_empleado_menor_salario = empleado

    return empleados[numero_empleado_menor_salario]['nombre'], empleados[numero_empleado_menor_salario]['salario']


if __name__ == '__main__':
    nombre_empleado_mayor_salario, salario_mayor = encontrar_empleado_salario_mayor(empleados)
    print(nombre_empleado_mayor_salario, salario_mayor)
    
    nombre_empleado_menor_salario, salario_menor = encontrar_empleado_salario_menor(empleados)
    print(nombre_empleado_menor_salario, salario_menor)
```


**5. Generar un reporte por cargo**
- Ejercicio: Dado un cargo (por ejemplo, "Desarrollador"), crea una función que retorne una lista de todos los empleados que ocupan ese cargo, mostrando su nombre y salario.
``` python
def buscar_desarrolladores(empleados):

    lista_desarrolladores = []

    for empleado in empleados:
        if(empleados[empleado]['cargo'] == 'Desarrollador'):
            lista_desarrolladores.append(f"{empleados[empleado]['nombre']}: {empleados[empleado]['salario']}")
            
    lista_desarrolladores = sorted(lista_desarrolladores)
    return lista_desarrolladores


def buscar_gerentes(empleados):
    lista_gerentes = []

    for empleado in empleados:
        if(empleados[empleado]['cargo'] == 'Gerente'):
            lista_gerentes.append(f'{empleados[empleado]['nombre']}: {empleados[empleado]['salario']}')
    
    lista_gerentes = sorted(lista_gerentes)
    return lista_gerentes


if __name__ == '__main__':
    while True:
        try:
            print('--- Cargo ---')
            print('1. Gerente')
            print('2. Desarrollador')
            print('3. Salir')
            cargo = int(input('Nombre del cargo: '))

            match cargo:
                case 1:
                    desarrolladores = buscar_desarrolladores(empleados)
                    print(desarrolladores)
                   
                case 2:
                    gerentes = buscar_gerentes(empleados)
                    print(gerentes)
                    
                case 3:
                    print('Saliendo...')
                    break
                case _:
                    print('Opción inválida. Vuelve a intentarlo')

            print('')
        except Exception:
            print('Error. Has introducido algo incorrecto\n')

```


**6. Verificar si un empleado ha sido contratado recientemente**
- Ejercicio: Crea una función que determine si un empleado fue contratado en los últimos 6 meses, dadas las fechas de ingreso. Deberás comparar la fecha de ingreso con la fecha actual y devolver un mensaje indicando si es un empleado reciente o no.
``` python
def empleados_contratados_hace_6_meses(empleados):

    fecha_actual = datetime.today().date()
    hace_6_meses = fecha_actual - timedelta(days=6*30)

    for empleado in empleados:
        fecha_ingreso = datetime.strptime(empleados[empleado]['fecha_ingreso'], '%Y-%m-%d').date()

        if(fecha_ingreso <= hace_6_meses):
            empleados[empleado]['contratado_recientemente'] = 'si'
        else:
            empleados[empleado]['contratado_recientemente'] = 'no'

    return empleados


if __name__ == '__main__':
    print(empleados_contratados_hace_6_meses(empleados))
```


**7. Sumar salarios por cargo**
- Ejercicio: Implementa una función que reciba un cargo (por ejemplo, "Desarrollador") y retorne la suma total de los salarios de todos los empleados que ocupan ese cargo.
``` python
def cantidad_total_cargo(empleados, nombre_cargo):
    cantidad_total = 0

    for empleado in empleados:
        if(empleados[empleado]['cargo'] == nombre_cargo):
            cantidad_total += empleados[empleado]['salario']

    return cantidad_total


if __name__ == '__main__':
    nombre_cargo = input('Nombre del cargo: ')
    print(cantidad_total_cargo(empleados, nombre_cargo))
```



**8. Listar los empleados más jóvenes**
- Ejercicio: Crea una función que liste a los 3 empleados más jóvenes en la empresa, mostrando su nombre y edad.
``` python
def empleados_mas_jovenes(empleados):
    
    lista_empleados_mas_jovenes = {}
    empleados_mas_jovenes = []

    for empleado in empleados:
        lista_empleados_mas_jovenes[empleado] = (empleados[empleado]['edad'], empleados[empleado]['nombre'])
        empleados_mas_jovenes.append(empleados[empleado]['edad'])
    
    empleados_mas_jovenes_ordenados = sorted(empleados_mas_jovenes)

    empleados_mas_jovenes_resultado = []
    
    for i in range(0,3):
        empleados_mas_jovenes_resultado.append(empleados_mas_jovenes_ordenados[i])

    return empleados_mas_jovenes_resultado



if __name__ == '__main__':
    print(empleados_mas_jovenes(empleados))
```


**9. Generar un informe de empleados con salarios por encima del promedio**
- Ejercicio: Calcula el salario promedio de la empresa. Luego, crea una función que liste a todos los empleados que ganan más que el salario promedio, mostrando su nombre y salario.
``` python
def calcular_promedio(empleados):
    contador = 0
    acumulador = 0

    for empleado in empleados:
        salario = empleados[empleado]['salario']
        contador += 1
        acumulador += salario
    
    media = acumulador / contador

    return media


def encontrar_salarios_por_encima_promedio(empleados, media):

    empleados_salario_mayor_promedio = {}

    media = calcular_promedio(empleados)

    for empleado in empleados:
        salario = empleados[empleado]['salario']
        nombre = empleados[empleado]['nombre']

        if(salario > media):
            empleados_salario_mayor_promedio[empleado] = f"['nombre' = {nombre}, 'salario' = {salario}]"
        
    return empleados_salario_mayor_promedio


if __name__ == '__main__':
    media = calcular_promedio(empleados)
    print(media)
    empleados_mayor_salaario_que_media = encontrar_salarios_por_encima_promedio(empleados, media)
    print(empleados_mayor_salaario_que_media)
```



**10. Contar empleados por cargo**
- Ejercicio: Crea una función que cuente cuántos empleados hay en cada cargo (por ejemplo, cuántos "Desarrolladores", cuántos "Gerentes", etc.) y muestre el resultado en un formato legible.
``` python

```



**11. Aumentar el salario de empleados por antigüedad**
- Ejercicio: Crea una función que aumente el salario de los empleados que tienen más de 5 años en la empresa. El aumento será un porcentaje que se pase como parámetro a la función.
``` python

```



**12. Eliminar un empleado por ID**
- Ejercicio: Crea una función que elimine un empleado de la base de datos dado su ID.
``` python

```


**13. Modificar múltiples datos de un empleado**
- Ejercicio: Crea una función que permita modificar varios campos de un empleado a la vez (por ejemplo, cambiar el salario, cargo y la fecha de ingreso).
``` python

```


**14. Mostrar empleados según criterio**
- Ejercicio: Implementa una función que permita filtrar empleados por un criterio específico, como por ejemplo, todos los empleados que ganan más de 50,000, o los empleados que han ingresado en el último año.
``` python

```


**15. Generar un informe de empleados con salarios superiores a un umbral**
- Ejercicio: Crea una función que reciba un umbral de salario (por ejemplo, 59,000) y retorne una lista con los empleados cuyo salario es superior a ese umbral.