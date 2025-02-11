## 📌 Ejercicios sobre Tipos de Métodos en Python

---

### 📌 **Ejercicio 1: Métodos de Instancia**
✔️ **Objetivo:** Practicar métodos de instancia accediendo y modificando atributos de una instancia de la clase.

🔹 **Ejercicio:**  
Crea una clase `CuentaBancaria` que tenga:
- Un constructor `__init__` que reciba el nombre del titular y el saldo inicial.
- Un método `depositar` que permita aumentar el saldo de la cuenta.
- Un método `retirar` que disminuya el saldo, solo si hay suficiente dinero.
- Un método `mostrar_saldo` que devuelva el saldo actual.

### SOLUCIÓN
``` python
import os
os.system('cls')

class CuentaBancaria():

    def __init__(self, nombre_titular, saldo_inicial):
        self.nombre_titular = nombre_titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        if(self.saldo > 0 and self.saldo > cantidad):
            self.saldo -= cantidad
    
    def mostrar_saldo(self):
        return f'Saldo actual: {self.saldo}'
    
    def __str__(self):
       return f'{self.nombre_titular}, {self.saldo}'


cuenta = CuentaBancaria('Ángeles', 1500)
cuenta.depositar(300)
cuenta.retirar(100)
print(cuenta.mostrar_saldo())           # Saldo actual: 1700

```
---

### 📌 **Ejercicio 2: Métodos de Clase (`@classmethod`)**
✔️ **Objetivo:** Trabajar con métodos de clase y atributos compartidos entre instancias.

🔹 **Ejercicio:**  
Crea una clase `Tienda` que tenga:
- Un atributo de clase `total_tiendas` que cuente cuántas tiendas se han creado.
- Un constructor `__init__` que reciba el nombre de la tienda y aumente el contador de `total_tiendas`.
- Un método de clase `cantidad_tiendas` que devuelva el número total de tiendas creadas.

Crea varias instancias de `Tienda` y usa el método de clase para verificar cuántas tiendas hay.

### SOLUCIÓN
``` python
import os 
os.system('cls')

class Tienda:
    total_tiendas = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Tienda.total_tiendas += 1

    @classmethod
    def cantidad_tiendas(cls):
        return f'Tiendas creadas: {cls.total_tiendas}'
    

sprinter = Tienda('Sprinter')
lefties = Tienda('lefties')
nike = Tienda('nike')
adidas = Tienda('adidas')

print(Tienda.cantidad_tiendas())        # Tiendas creadas: 4
```
---
### 📌 **Ejercicio 3: Verificación de Números Primos con Método Estático**
✔️ **Objetivo:** Practicar métodos estáticos verificando si un número es primo.

🔹 **Ejercicio:**  
Crea una clase `Numeros` que incluya:
- Un método estático `es_primo` que reciba un número entero y devuelva `True` si es primo, `False` en caso contrario.
- Un método estático `lista_primos` que reciba un número entero `n` y devuelva una lista con todos los números primos hasta `n`.

Prueba los métodos sin crear una instancia de la clase.

### SOLUCIÓN
``` python

```
---

### 📌 **Ejercicio 4: Uso combinado de Métodos de Instancia, Clase y Estáticos**
✔️ **Objetivo:** Aplicar diferentes tipos de métodos en una misma clase de forma más estructurada.

🔹 **Ejercicio:**  
Crea una clase `Vehiculo` que tenga:
- Un atributo de clase `total_vehiculos` que almacene cuántos vehículos han sido creados.
- Un constructor que reciba el modelo y el año de fabricación del vehículo, almacenándolo como un atributo de instancia, e incremente `total_vehiculos`.
- Un método de instancia `detalles` que devuelva la información del vehículo.
- Un método de clase `contar_vehiculos` que devuelva cuántos vehículos existen.
- Un método estático `es_vehiculo_moderno` que reciba una instancia de `Vehiculo` y devuelva `True` si su atributo `año_fabricacion` es del 2015 en adelante, `False` en caso contrario.

Crea varias instancias de `Vehiculo` y verifica el uso correcto de los métodos.

🔹 **Ejemplos de instancias:**
```python
# Crear instancias de Vehiculo
vehiculo1 = Vehiculo("Toyota Corolla", 2010)
vehiculo2 = Vehiculo("Honda Civic", 2018)
vehiculo3 = Vehiculo("Ford Focus", 2022)

# Verificar los detalles de cada vehículo
print(vehiculo1.detalles())  # Debería mostrar información del Toyota Corolla
print(vehiculo2.detalles())  # Debería mostrar información del Honda Civic
print(vehiculo3.detalles())  # Debería mostrar información del Ford Focus

# Verificar si los vehículos son modernos
print(Vehiculo.es_vehiculo_moderno(vehiculo1))  # False
print(Vehiculo.es_vehiculo_moderno(vehiculo2))  # True
print(Vehiculo.es_vehiculo_moderno(vehiculo3))  # True

# Contar el total de vehículos creados
print(Vehiculo.contar_vehiculos())  # Debería mostrar 3
```

Crea más instancias y verifica su funcionamiento.

### SOLUCIÓN
``` python

```
---

### 📌 **Ejercicio 5: Clases y Métodos Abstractos**
✔️ **Objetivo:** Trabajar con clases abstractas y la implementación de métodos en clases derivadas.

🔹 **Ejercicio:**  
Crea una clase abstracta `Empleado` con:
- Un método `__init__` que reciba el nombre del empleado.
- Un método abstracto `calcular_salario` que deberá ser implementado por las clases hijas.

Crea dos clases `EmpleadoPorHora` y `EmpleadoFijo` que hereden de `Empleado`:
- `EmpleadoPorHora` recibirá el número de horas trabajadas y la tarifa por hora, y calculará el salario multiplicando estos valores.
- `EmpleadoFijo` recibirá un sueldo fijo y lo devolverá como salario.

Crea instancias de ambas clases y calcula el salario de diferentes empleados.

### SOLUCIÓN
``` python

```
---

### 📌 **Ejercicio 6: Registro de Usuarios con Métodos de Clase y Estáticos**
✔️ **Objetivo:** Implementar un sistema de registro de usuarios con métodos de clase y estáticos.

🔹 **Ejercicio:**  
Crea una clase `Usuario` que tenga:
- Un atributo de clase `usuarios_registrados`, que almacene un contador de usuarios creados.
- Un constructor que reciba el nombre del usuario e incremente `usuarios_registrados`.
- Un método de instancia `mostrar_usuario` que devuelva el nombre del usuario.
- Un método de clase `cantidad_usuarios` que devuelva el número total de usuarios registrados.
- Un método estático `validar_nombre_usuario` que reciba un nombre y devuelva `True` si tiene más de 3 caracteres, `False` en caso contrario.

Crea varias instancias de `Usuario` y prueba los métodos.

### SOLUCIÓN
``` python

```
---

### 📌 **Ejercicio 7: Sistema de Facturación con Métodos de Instancia, Clase y Estáticos**
✔️ **Objetivo:** Aplicar los tres tipos de métodos en una simulación de facturación.

🔹 **Ejercicio:**  
Crea una clase `Factura` que tenga:
- Un atributo de clase `tasa_iva`, que almacene el porcentaje de IVA aplicado a las facturas.
- Un constructor que reciba el número de factura y el monto base.
- Un método de instancia `calcular_total` que devuelva el monto con IVA incluido.
- Un método de clase `cambiar_tasa_iva` que permita modificar el valor del IVA.
- Un método estático `formatear_monto` que reciba un monto y lo devuelva formateado con dos decimales y el símbolo de moneda.

Crea facturas, cambia la tasa de IVA y prueba los métodos.

### SOLUCIÓN
``` python

```
---

### 📌 **Ejercicio 8: Implementación de una Jerarquía de Transporte con Clases Abstractas**
✔️ **Objetivo:** Utilizar clases y métodos abstractos para modelar diferentes tipos de transporte.

🔹 **Ejercicio:**  
Crea una clase abstracta `Transporte` con:
- Un constructor que reciba la velocidad máxima del transporte.
- Un método abstracto `tipo_transporte`, que deberá ser implementado por las clases derivadas.

Crea dos clases `Automovil` y `Bicicleta` que hereden de `Transporte`:
- `Automovil` deberá definir `tipo_transporte` y devolver `"Automóvil - Transporte motorizado"`.
- `Bicicleta` deberá definir `tipo_transporte` y devolver `"Bicicleta - Transporte ecológico"`.

Crea instancias de ambas clases y muestra su tipo de transporte.

### SOLUCIÓN
``` python

```