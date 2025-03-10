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
- `%s`: cadenas de texto
- `%d`: numeros enteros
- `%f`: numeros flotantes (double)
- `%.2f`: muestra hasta dos decimales de un float (cantidad de decimales) ```{'anios': float(f'➡️{anios_antiguedad:.2f}⬅️')}, texto con 2 decimales y luego lo paso a float {'anios': 7.51}```
- `%c`: char


### 5.1. Con `printf`
``` python
texto = 'Python'
numero = '10'

print(f'Mensaje: {texto} se merece un {numero}')    # Mensaje: Python se merece un 10

alumno1 = 'David'
alumno2 = 'Rubén'
alumno3 = 'Pedro'

estatura1 = '178'
estatura2 = 180
estatura3 = 168

# NOTA 🗒️: Las cadenas empiezan por el principio(izquierda) y los numeros apor el final(derecha)
print(f'{'Alumno':20} {'Escritura':10}')        # Alumno               Escritura
print(f'{'-'*20} {'-'*10}')                     # -------------------- ----------
print(f'{alumno1:20} {estatura1:10}')           # David                178
print(f'{alumno2:20} {estatura2:10}')           # Rubén                       180
print(f'{alumno3:20} {estatura3:10}')           # Pedro                       168
```


### 5.2. Con `%` 
``` python
texto = 'python'
numero = 10

print('Mensaje: %s se merece un %d' %(texto, numero))       # Mensaje: Python se merece un 10
pi = 3.141592
print('Pi con dos decimales es: %.2f' %(pi))                # Pi con dos decimales es: 3.14
```





## 6. Clases
En Python, las clases son estructuras que permiten organizar código en objetos con atributos y métodos. Existen varios tipos de **clases y métodos**, cada uno con características específicas.  

### 6.1. Sintaxis
``` python
class MiClase:
    '''
    Ejemplo básico de una clase.
    '''

    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def metodo(self):
        return f'Valores: {self.atributo1}, {self.atributo2}'

# Crear y usar una instancia
objeto = MiClase('Python', 'Clases')
print(objeto.metodo())  # Valores: Python, Clases
``` 

### 6.2. Conceptos fundamentales
#### CONSTRUCTOR`(__init__)`
El constructor se encarga de crear un objeto al crear una instancia. A través de él podemos configurar el estado inicial de la instancia creada
``` python
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
usuario = Usuario('Ana', 24)
print(usuario.nombre)       # Ana
```

También puede recibir valores predeterminados que se usan en caso de no proporcionar parámetris al crear una instancia
``` python
class Usuario:
    def __init__(self, nombre='Desconocido', edad=0):
        self.nombre = nombre
        self.edad = edad
    
usuario = Usuario()
print(usuario.nombre)       # Desconocido
```

#### Atributos: Instancia y Clase
- **Instancia**: Único para cada objeto, normalmente definidos en `__init__` y se acceden a ellos a través de `self`.
- **Clase**: Compartidos entre todas las instancias, útiles para constantes o configuraciones comunes.
``` python
class Configuracion:
    version = '1.0.0'   # Atributo de CLASE

    def __init__(self, usuario, permisos=[]):
        self.usuario = usuario      # Atributo de instancia
        self.permisos = permisos

    def agregar_permiso(self, permiso):
        self.permisos.append(permiso)


config = Configuracion('Admin')
config.agregar_permiso('lectura')
print(config.permisos)    # ['lectura']
```



#### Métodos
Son funciones que definen los comportamientos de los objetos. Tenemos 3 tipos de métodos:
- **Métodos de Instancia**: Operan sobre datos únicos de una instancia y utilizan `self`.
- **Métodos de Clase**: Con el decorador `@classmethod`,permiten interactuar con atributos de clase. Usan `cls` en lugar de `self`.
- **Métodos Estáticos**: No dependen de ninguna instancia o clase y funcionan como funciones regulares dentro del contexto de la clase. No usa `cls` ni `self`.

``` python
class Herramienta:
    categoria = 'Software'

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_categoria(self):
        return f'Categoría: {Herramienta.categoria}' # Devuelve el valor del atributo de la clase
    
    @classmethod
    def cambiar_categoria(cls, nueva_categoria): # Modifica la categoría de TODAS las instancias
        cls.categoria = nueva_categoria

    @staticmethod   # Método independiente de la clase y de la instancia
    def utilidad():
        return 'Optimiza procesos específicos'


herramienta = Herramienta('Editor de texto')
Herramienta.cambiar_categoria('Utilidad')
print(herramienta.mostrar_categoria())
```


Los métodos estáticos son especialmente útiles cuando no necesitamos acceso directo ni a la instancia ni a la clase, como en funciones o validaciones.

``` python
class Matematica:

    @staticmethod
    def sumar(a, b):
        return a + b

resultado = Matematica.sumar(5, 3)
print(resultado)  # 8
``` 

### 6.3. Herencia 




``` python

```

### 6.4. Encapsulamiento 

``` python

```

### 6.5. Clase 

``` python

```

### 6.6. Clase 


``` python

```



  
``` python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Método de instancia:
#   - Siempre reciben 'self' como primer parámetro
#   - Pueden acceder y modificar los atributos de instancia
#   - Pueden llamar a otros métodos de instancia

    def saludar(self):  # Método de instancia, siempre self y est la primera
        print(f'Hola me llamo {self.nombre} y tengo {self.edad} años.') # Llamo a los atributos de la instancia
        print(f'Hola me llamo {self.nombre} y {self.devolver_la_edad()}') # Llamo a un método de instancia
    
    def devolver_la_edad(self):     # Método de instanca
        return f'Tengo {self.edad} años.'


p = Persona('Javier', 28)
p.saludar()
# Hola me llamo Javier y tengo 28 años.
# Hola me llamo Javier y Tengo 28 años.
```




## 7. Ficheros
### 7.1. Creación de 
### 7.2. Creación de 
