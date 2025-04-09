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
La herencia permite que una clase hija o subclase adquiera atributos y métodos de otra clase padre o superclase. Esto fomenta la reutilización de código, evita la redundancia y facilita la mantenibilidad del software.

#### Tipos de Herencia
Existen varios tipos de herencia en POO:
- **Herencia Simple**: Una clase hija hereda de una sola clase padre.
- **Herencia Múltiple**: Una clase hija hereda de múltiples clases padres.
- **Herencia Multinivel**: Una clase hija hereda de otra clase hija, formando una cadena de herencia.
- **Herencia Jerárquica**: Varias clases hijas heredan de una misma clase padre.
- **Herencia Híbrida**: Combinación de dos o más tipos de herencia anteriores.
  

**Herencia Simple**
```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def descripcion(self):
        return f'Vehículo de marca {self.marca}'


class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)    # Llamamos al constructor de la clase padre
        self.modelo = modelo

    def descripcion(self):
        return f'Coche ->  Modelo: {self.modelo}, Marca: {self.marca}'
    

coche = Coche('Toyota', 'Corolla')
print(coche.descripcion())    # Coche ->  Modelo: Corolla, Marca: Toyota
``` 



**Herencia Múltiple**
```python
class Motor:
    def tipo_motor(self):
        return 'Motor de combustión interna'
    
class Chasis:
    def tipo_chasis(self):
        return 'Chasis monocasco'
    
class Automovil(Motor, Chasis):
    def descripcion(self):
        return f'Automóvil con {self.tipo_motor()} y tiene un {self.tipo_chasis()}'

    def __str__(self):
        return f'Motor: {self.tipo_motor()}, {self.tipo_chasis()}'
    
    
automovil = Automovil()
print(automovil)   # Motor: Motor de combustión interna, Chasis monocasco
``` 



**Herencia Multinivel**
```python
class Animal:
    def sonido(self):
        return 'Sonido genérico'

    
class Mamifero(Animal):
    def caracteristica(self):
        return 'Es un mamífero'
    

class Perro(Mamifero):
    def sonido(self):
        return 'Ladrido'


perro = Perro()
print(perro.sonido())            # Ladrido
print(perro.caracteristica())    # Es un mamífero
``` 


**Super()**
Se usa para llamar a métodos de la clase padre dentro de la clase hija.

**Sin `super()`**
``` python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentacion(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre  # Se repite la asignación de atributos de la clase padre
        self.edad = edad
        self.carrera = carrera

    def presentacion(self):
        return f"Me llamo {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."

estudiante = Estudiante("Pedro", 22, "Ingeniería Informática")
print(estudiante.presentacion())  # Me llamo Pedro, tengo 22 años y estudio Ingeniería Informática.
```


**Con `super()`**
``` python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentacion(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase padre
        self.carrera = carrera

    def presentacion(self):
        return f"{super().presentacion()} Estudio {self.carrera}."

estudiante = Estudiante("Pedro", 22, "Ingeniería Informática")
print(estudiante.presentacion())  # Me llamo Pedro y tengo 22 años. Estudio Ingeniería Informática.
```

### 6.4. Tipos de métodos 
#### 6.4.1 Métodos de instancia
Operan sobre una instancia específica de la clase. Pueden acceder y modificar los atributos de la instancia
✔️ Características:
- Siempre reciben self como primer parámetro.
- Pueden acceder y modificar atributos de instancia.
- Pueden llamar a otros métodos de la misma instancia.

``` python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    
    def saludar(self):
        return f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.'
    

persona1 = Persona('Ana', 25)
print(persona1.saludar())  
# Hola, mi nombre es Ana y tengo 25 años.
```



#### 6.4.2 Métodos de Clase(`@classmethod`)
Operan sobre la clase en sí misma, en lugar de una instancia.

✔️ Características:
- Se definen con @classmethod.
- Reciben **cls** como primer parámetro en lugar de self.
- Pueden modificar atributos de clase, pero no de instancia.
- Se pueden llamar desde la clase o desde una instancia.

``` python
class Coche:
    cantidad_coches = 0

    def __init__(self, marca):
        self.marca = marca
        Coche.cantidad_coches += 1                                                                   

    @classmethod
    def total_coches(cls):
        return f'Total coches: {cls.cantidad_coches}'
    
coche1 = Coche('Peugeot')
print(Coche.total_coches())     # Total coches: 1

coche2 = Coche('BMW')
print(Coche.total_coches())     # Total coches: 2
```



#### 6.4.3 Métodos Estáticos(`@staticmethod`)
Son independientes de la clase y de las instancias. No pueden modificar ni acceder a atributos de instancia o de clase

✔️ Características:
- Se definen con @staticmethod.
- No reciben self ni cls.
- Funcionan como funciones normales, pero se organizan dentro de la clase.

``` python
class Utilidades:

    @staticmethod
    def es_par(numero):
        if numero%2 == 0:
            return True
        else:
            return False
        
print(Utilidades.es_par(5))     # True
print(Utilidades.es_par(6))     # False
```



#### 6.4.4 Métodos y Clases Abstractos
Es una clase que no puede ser instanciada directamente y sirve como plantilla para otras clases. Un método abstracto es un método definido en una clase base abstracta que debe ser implementado por las clase hijas.

Pyhton proporciona el módulo `abc` para definir clases abstractas y métodos abstractos

``` python
from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def encender(self):
        ...

class Telefono(Dispositivo):
    def encender(self):
        return f'El telefono {self.marca} - {self.modelo} se está encendiendo'

class Portatil(Dispositivo):
    def encender(self):
        return f'El portátil {self.marca} - {self.modelo} está arracando el sistema'
    

dispositivos = [
    Telefono('Samsung', 'Galaxy 210'),
    Portatil('Dell', 'XPS 15')
]

for dispositivo in dispositivos:
    print(dispositivo.encender())

# El telefono Samsung - Galaxy 210 se está encendiendo
# El portátil Dell - XPS 15 está arracando el sistema

```




## 7. Polimorfismo 
Permite utilizar un mismo método en diferentes clases, asegurando que cada clase implemente su propia versión del método. Esto favorece la flexibilidad y la escalabilidad del código, permitiendo que se interactúe con objetos de distintos tipos de manera uniforme

Tipos de Polimorfismo:
- **Polimorfismo de Sobreescritura** (Overriding): Cuando una subclase redefine un método de la superclase para adaptarlo a su propio comportamiento.
- **Polimorfismo de Sobrecarga** (Overloading): Cuando múltiples métodos comparten el mismo nombre pero tienen diferentes parámetros (en Python, esto se simula con argumentos opcionales o *args).
- **Polimorfismo basado en interfaces**: Cuando diferentes clases implementan los mismos métodos sin necesidad de heredar de una clase base.

#### Polimorfismo de Sobreescrcitura
``` python
class Animal:
    def sonido(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase")

class Perro(Animal):
    def sonido(self):
        return "Ladra"

class Gato(Animal):
    def sonido(self):
        return "Maúlla"

# Lista de objetos de diferentes tipos
animales = [Perro(), Gato()]

# Uso de polimorfismo: mismo método llamado en diferentes clases
for animal in animales:
    print(animal.sonido())
# Ladra
# Maúlla
```


#### Polimorfismo de Sobrecarga 
``` python
class Calculadora:
    def suma(self, a, b, c=0):
        return a + b + c  # El tercer parámetro es opcional

calc = Calculadora()
print(calc.suma(2, 3))      # Salida: 5
print(calc.suma(2, 3, 4))   # Salida: 9
```


#### Polimorfismo basado en interfaces 
```python
class Pato:
    def sonido(self):
        return "Cua cua"

class Persona:
    def sonido(self):
        return "Hola!"

# Lista de objetos sin relación de herencia
objetos = [Pato(), Persona()]

for objeto in objetos:
    print(objeto.sonido())  # Se ejecuta el método correspondiente a cada clase
```

## 8. Encapsulamiento
Controla cómo se accede y modifica la información de un objeto. Esto ayuda a mantener la integridad y seguridad de los datos dentro de una clase.

### Niveles de Accesibilidad en Python
- **Público**: Se puede acceder desde cualquier parte del código. No tiene prefijo especial.
- **Protegido**: Se indica con un guión bajo `_` y sugiere que solo debe usarse dentro de la clase o sus subclases.
- **Privado**: Se indica con un doble guión bajo `__` y oculta el atributo o método, evitando su acceso directo fuera de la clase.



### Ejemplo de encapsulamiento
``` python
class Datos:
    def __init__(self):
        self.publico = 'Accesible'          # Atributo público
        self._protegido = 'Uso interno'     # Atributo protegido
        self.__privado = 'Oculto'           # Atributo privado

    def obtener_privado(self):
        return self.__privado   # Método para acceder a un atributo privado
    

dato_1 = Datos()
print(dato_1.publico)
print(dato_1._protegido)

# print(dato_1.__privado)     ERROR. Es un metodo privado
print(dato_1.obtener_privado())
```

### Encapsulación en Métodos
Los métodos también pueden ser públicos, protegidos o privados
``` python
class Ejemplo:
    def metodo_publico(self):
        return 'Método público'
    
    def _metodo_protegido(self):
        return 'Metodo protegido'
    
    def __metodo_privado(self):
        return 'Método privado'
    
    def llamar_metodo_privado(self):
        return self.__metodo_privado()     # Acceder al método privado desde dentro de la clase
    

objeto_1 = Ejemplo()
print(objeto_1.metodo_publico())
print(objeto_1._metodo_protegido())

# print(objeto_1.__metodo_privado())  ERROR. Es un metodo privado
print(objeto_1.llamar_metodo_privado())
```


### Modificación de Atributos Privados
Aunque los atributos privados no pueden ser accedidos directamente, se pueden modificar usnado getter y setter.

``` python
class Persona:
    
    def __init__(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre
    
    def cambiar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

persona_1 = Persona('Carlos')
print(persona_1.obtener_nombre())   # Carlos
persona_1.cambiar_nombre('Oscar')
print(persona_1.obtener_nombre())   # Oscar
```




## 9. Ficheros 📁

### 9.1. Apertura de un Archivo
Usa la funcion `open()`: recibe nombre del archivo y modo de apertura

``` python
f = open("datos.txt", "modo")  # Abrir el archivo
```

### 9.2. Modos de apertura
- `r`: Lector (error si el archivo no existe)
- `w`: Escriture (crea el archivo si no existe, sobreescribe si existe)
- `a`: Añadir (agrega al final, sin borrar contenido)
- `t`: Texto(modo por defecto)

### 📌Lectura de Archivos
#### Leer todo el contenido `read()`
```python
f = open('datos.txt', 'r')    
contenido = f.read()      # Lee todo el archivo
print(contenido)
f.close()
```

#### Leer la primera linea `readline()`
```python
f = open('datos.txt', 'r')
linea = f.readline()      # Lee la primera linea
print(linea)
f.close()
```

#### Leer todas las linea `readlines()`
```python
f = open('datos.txt', 'r')
lineas = f.readlines()    # Devuelve una lista con todas las líneas
print(lineas)
f.close()
```


### 📌Escritura de Archivos
#### Sobreescribir (`w`)
```python
f = open('datos.txt', 'w')
f.write('Hola, esto sobreescribirá todo el contenido.\n')
f.close()
```


### 📌Lectura de Archivos
#### Añadir texto (`a`)
```python
f = open('datos.txt', 'a')
f.write('Nueva línea añadida al final.\n')
f.close()
```

### 9.3. Empleo de lambda, filter, map, reduce

#### 1️⃣ lambda
Define funciones pequeñas y simples de una manera compacta.
#### `lambda argumentos: expresión`

- **argumentos**: Los parámetros que recibe la función.
- **expresión**: El valor que se devuelve, basado en los argumentos.

Ejemplo: 
Crear una función lambda que sume dos números
```python
suma = lambda x, y: x + y
resultado = suma(3, 5)

print(resultado)  # Resultado: 8
```

Explicación:
- `lambda x, y: x + y` define una función que toma dos argumentos (`x` y `y`) y devuelve su suma.
- Luego, la función se invoca pasando los valores `3` y `5`, y el resultado es `8`.

Ejemplo con tuplas:
Ordenar las tuplas por el primer valor (el primer elemento de cada tupla)
```python
tuplas = [(1, 'a'), (3, 'c'), (2, 'b')]
ordenadas = sorted(tuplas, key=lambda x: x[0])

print(ordenadas)  # Resultado: [(1, 'a'), (2, 'b'), (3, 'c')]
```

Explicación:
- `lambda x: x[0]` es una función anónima que toma una tupla `x` y devuelve su primer valor (`x[0]`).
- La función `sorted()` usa esta función `lambda` para ordenar las tuplas según su primer valor.





#### 2️⃣ filter
Filtra los elementos de un iterable según una condición, y devuelve los elementos para lo que la función devuelve True.
#### **`filter(función, iterable)`**

- **función**: Una función que devuelve True o False para cada elemento.
- **iterable**: El iterable cuyos elementos serán filtrados.

Ejemplo:
Imagina que tienes una lista de números y quieres obtener solo los números pares.

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list (filter (lambda x: x % 2 == 0, numeros ) )

print(pares)  # Resultado: [2, 4, 6]
```
Explicación:
- `filter` aplica la función `lambda x: x % 2 == 0`, que devuelve True solo para los números pares, y filtra el resto.
- El resultado es un iterable con solo los números pares de la lista original.





#### 3️⃣ map
Aplica una función a cada elemento de un iterable (lista, tupla, etc.) y devuelve un nuevo iterable con los resultados.
#### `map(función, iterable)`

- **función**: La función que se aplica a cada elemento del iterable.
- **iterable**: El iterable cuyos elementos serán transformados.

Ejemplo:
Imagina que tienes una lista de números y quieres obtener una lista de sus cuadrados.

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))

print(cuadrados)  # Resultado: [1, 4, 9, 16, 25]
```

Explicación:
- `map` aplica la función `lambda x: x ** 2` (que eleva cada número al cuadrado) a cada elemento de la lista `numeros`.
- El resultado es un iterable con los cuadrados de los números, que se convierte en lista usando `list()`.





##### 4️⃣ reduce
Se encuentra en le módulo **`functools`**, aplica una función de manera acumulativa a los elementos de un iterable, de modo que el resultado final es un solo valor.

#### `from functools import reduce`
#### `reduce(función, iterable, valor_inicial)`

- **función**: La función que realiza la operación acumulativa.
- **iterable**: El iterable cuyos elementos se combinan.
- `valor_inicial (opcional)`: Un valor inicial que se usa como base para el primer paso de la reducción.

Ejemplo:
Imagina que tienes una lista de números y quieres calcular la suma total de todos ellos.

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, numeros)

print(suma_total)  # Resultado: 15
```

Explicación:
- `reduce` aplica la función `lambda x, y: x + y` de forma acumulativa:
  - Primero suma 1 + 2 = 3.
  - Luego suma 3 + 3 = 6.
  - Luego suma 6 + 4 = 10.
  - Finalmente suma 10 + 5 = 15.
- El resultado es un solo valor: la suma total de los elementos.



---





#### Resumen y comparación
|Función|Descripción|Ejemplo|
|-------|-----------|-------|
|`lambda`|	Crea una función anónima, es decir, una función sin nombre, para operaciones simples en una sola línea. Se usa comúnmente con funciones como map, filter y reduce.|Sumar 2 números|
|`filter`|	Filtra los elementos de un iterable según una condición, y devuelve los elementos para los que la función devuelve True.|Obtener solo los números pares de una lista.|
|`map`|Aplica una función a cada elemento de un iterable y devuelve un nuevo iterable con los resultados|Convertir una lista de números a sus cuadrados.|
|`reduce`|Aplica una operación acumulativa a los elementos de un iterable, reduciendo el iterable a un solo valor.|Sumar todos los elementos de una lista.|

#### Ejemplo de uso combinado:
Imagina que tienes una lista de números y quieres filtrar los números pares, luego elevarlos al cuadrado y finalmente obtener la suma de los cuadrados.

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

# Filtrar los números pares
pares = filter(lambda x: x % 2 == 0, numeros)

# Elevar al cuadrado los números filtrados
cuadrados = map(lambda x: x ** 2, pares)

# Obtener la suma de los cuadrados
suma = reduce(lambda x, y: x + y, cuadrados)

print(suma)  # Resultado: 56 (4 + 16 + 36)
```
Explicación:
- `filter` filtra los números pares: `[2, 4, 6]`.
- `map` eleva al cuadrado esos números: `[4, 16, 36]`.
- `reduce` suma los cuadrados: `4 + 16 + 36 = 56`.
