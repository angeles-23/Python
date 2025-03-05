## 1. Listas
Las listas en Python son colecciones desordenadas y mutables de elementos. Se definen con corchetes `[]`.


### 1.1. Creación de una lista 
Sintaxis: `nombreLista [] = [elemento_1, elemento_2, elemento_3]`
``` python
frutas = ['manzana', 'cereza', 'pera']
print(frutas)   # ['manzana', 'cereza', 'pera']
```


### 1.2. Accceder a elementos
Para acceder a un elemento en concreto, se debe llamar a la lista y entre corchetes la posición del elemento: `nombreLista[posicion_elemento]`. Se puede obtener al último elemento colocando -1 entre los corchetes
```python
print(frutas[0])            # manzana
print(frutas[-1])           # pera
```


### 1.3. Modificar elementos 
Cuando se quiere modificar un elemento nombramos la lista, la posición a ocupar y le asignamos el valor que queremos: `nombreLista[posicion] = valorNuevo`
```python
frutas[1] = 'melón'         # ['manzana', 'melón', 'pera']
```


### 1.4. Agregar y eliminar elementos 
- Agregar:
  - `.append(elemento)`: Agrega un elemento al final de la lista.
  - `.insert(posicion, elemento)`: Agrega en la posicion indicada el elemento dado
  - `.extend([elemento_nuevo_1, elemento_nuevo_2])`: Agrega varios elementos al final de la lista
  - `.insert(posicion, elemento)`: Agrega en la posicion indicada el elemento dado
- Eliminar:
  - `.pop()`, `.pop(posicion)` : Elimina el último elemento, y si en los paréntesis le damos la posición del elemento lo elimina
  - `.remove(elemento)`: Elimina dicho elemento
  - `.clear()`: Elimina todos los elementos de la lista 

```python
frutas.append('melocotón')              # ['manzana', 'cereza', 'pera', 'melocotón']
frutas.insert(3, 'plátano')             # ['manzana', 'cereza', 'pera', 'plátano', 'melocotón']
frutas.extend(['coco', 'fresa'])        #['manzana', 'cereza', 'pera', 'plátano', 'melocotón', 'coco', 'fresa']

frutas.pop()                            # ['manzana', 'cereza', 'pera', 'plátano', 'melocotón', 'coco']
frutas.pop(3)                           # ['manzana', 'cereza', 'pera', 'melocotón', 'coco']
frutas.remove('pera')                   # ['manzana', 'cereza', 'melocotón', 'coco']
frutas.clear()                          # []
```


### 1.5. Saber si existe o no un elemento y obtener su posición
```python
existe = 'coche' in frutas                  # False                       
indice_cereza = frutas.index('cereza')      # 1
```


### 1.6. Ordenar lista, saber la longitud y darle la vuelta
```python
frutas.sort()       # ['cereza', 'coco', 'manzana', 'melocotón']
len(frutas)         # 4
frutas.reverse()    # ['melocotón', 'manzana', 'coco', 'cereza']
```





# 2. Diccionarios
Los diccionarios almacenan datos en pares clave-valor y se defienen con llaves `{}`

### 2.1. Creación de un diccionario
Sintaxis: `nombre_diccionario = {'clave': 'valor'}` 
``` python
colores = {'azul':'blue', 'rojo':'red', 'verde':'green'}
print(colores)                      # {'azul':'blue', 'rojo':'red', 'verde':'green'}
print(colores.keys())               # dict_keys(['azul', 'rojo', 'verde'])
print(colores.values())             # dict_values(['blue', 'red', 'green'])
colores.update({'negro': 'black'})  # {'azul': 'blue', 'rojo': 'red', 'verde': 'green', 'negro': 'black'}
```


### 2.2. Acceder a los valores
Se accede mediante la clave. De esta forma:  `nombre_diccionario['clave']` 
``` python
colores['azul']        # blue
```


### 2.3. Modificar valores
Llamamos al diccionario y entre corchetes ponemos la clave y finalmente le asignamos un valor nuevo. `nombre_diccionario['clave] = nuevoValor`  
``` python
colores['azul'] = 'BLUE'      # {'azul': 'BLUE', 'rojo': 'red', 'verde': 'green'}
```


### 2.4. Añadir y eliminar un elemento
- Añadir: se hace de la misma forma que se modifica un elemento solo que si no existe lo crea.
- Eliminar: usando la función *del* y llamando al diccionario con su clave
``` python
colores['amarillo'] = 'yellow'    # {'azul': 'BLUE', 'rojo': 'red', 'verde': 'green', 'amarillo': 'yellow'}
del(colores['rojo'])              # {'azul': 'BLUE', 'verde': 'green', 'amarillo': 'yellow'}
```


### 2.5. Saber la información de un solo diccionario
``` python
personas = {
  "Alejandro": {"edad": 22, "altura": 1.73}, 
  "José": {"edad": 21, "altura": 1.75}, 
  "María": {"edad":22, "altura":1.67}
} 

personas['Alejandro']          # {'edad': 22, 'altura': 1.73}
```


## 2.6. Recorrer un diccionario
```python
for clave, valor in personas.items():
    print(f"{clave}: {valor}")

# Alejandro: {'edad': 22, 'altura': 1.73}
# José: {'edad': 21, 'altura': 1.75}
# María: {'edad': 22, 'altura': 1.67}
```



# 3. Tuplas
Las tuplas son colecciones desordenadas e inmutables de elementos. Se definen con paréntesis `()`.

### 3.1. Creación de una tupla 
Sintaxis: `nombre_tupla = (elemento1, elemento2, elemento3)`
``` python
datos = (2, "Hola", 6.78, [1,2,3], 4, 3, 7, -1, 6)
print(datos)        # (2, 'Hola', 6.78, [1, 2, 3], 4, 3, 7, -1, 6)
```


### 3.2. Acceder a los elementos 
Se acceden según la posición: `nombre_tupla[posicion]`
``` python
datos[1]            # Hola
```


### 3.3. Mostrar varios elementos y saber si existe un elemento 
``` python
datos[2:5]          # (6.78, [1, 2, 3], 4)
4 in datos          # True
```


### 3.4. Buscar elemento y ver cuantos elementos tiene
``` python
datos.index(6.78)     # 2
len(datos)            # 9
```


### 3.5. Pasar de tupla a lista y de lista a tupla 
``` python
lista = [2, 7, 23, "Ángeles", "Santiago", "Patricio", 19]

datos = list(datos)         # [2, 'Hola', 6.78, [1, 2, 3], 4, 3, 7, -1, 6]
lista = tuple(datos)        # (2, 'Hola', 6.78, [1, 2, 3], 4, 3, 7, -1, 6)
```





## 4. While
Se usa cuando no se sabe el número de veces que se va arepetir. Se repetirá mientras se cumpla su condición, cuando la condición sea False parará.

``` python
while condición:
    # Bloque de código que se ejecuta mientras la condición sea True
```
**break**: sale del bucle
**continue**: salta el código actual y pasa al aiguiente
**else**: cuando acabe de ejecutarse el bucle sin break, se ejecutará el else
**try exception**: controla los errores ➡️ try: el código a intentar y exception: como manejarlo

``` python
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        if edad > 0:
            print(f"Tu edad es {edad}.")
            break
    except ValueError:
        print("Por favor, introduce un número válido.")
``` 





## 5. Formateo de variables
```python
# Con formato printf
texto = 'Python'
numero = '10'

print(f'Mi mensaje es: {texto} se merece un {numero}')

alumno1 = 'David'
alumno2 = 'Rubén'
alumno3 = 'Pedro'
alumno4 = 'Silvia'

# Diseño de multiplicacion de cadenas
estatura1 = '178'
estatura2 = 180
estatura3 = 168
estatura4 = 158

print(f'{'Alumno':20} {'Escritura':10}')
print(f'{'-'*20} {'-'*10}')
# numeros al final y cadenas al principio
print(f'{alumno1:20} {estatura1:10}')
print(f'{alumno2:20} {estatura2:10}')
print(f'{alumno3:20} {estatura3:10}')
print(f'{alumno4:20} {estatura4:10}')


# Con %
texto = 'python'
numero = 10

# %s es para cadenas de texto
# %d es para enteros
# %f es para numeros flotantes (double)
# %.2f es para mostrar hasta dos decimales de un flotante (cambiar numero de decimales)
# %c es para char
# %x es para hexadecimales
# %o es para octales

print('Mi mensaje es: %s se merece un %d' %(texto, numero))
pi = 3.141592
print('Pi con dos decimales es: %.2f' %pi)
```

### 5.1. Creación de una lista 
### 5.2. Creación de una lista 
### 5.3. Creación de una lista 
### 5.4. Creación de una lista  


## 6. Clases
### 6.1. Clase 
### 6.2. Clase 
### 6.3. Clase 
### 6.4. Clase 
### 6.5. Clase 
### 6.6. Clase 

## 7. Ficheros
### 7.1. Creación de 
### 7.2. Creación de 
### 7.3. Creación de 
### 7.4. Creación de 
### 7.5. Creación de 