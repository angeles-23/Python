## Ejercicios sobre Encapsulamiento en Python

### **Ejercicio 1: Atributos Privados y Métodos Getter/Setter**
**Objetivo:** Comprender el uso de atributos privados y métodos getter y setter.

#### **Instrucciones:**  
1. Crea una clase `CuentaBancaria` con los siguientes atributos:
   - `titular` (público)
   - `__saldo` (privado)
2. Implementa los métodos:
   - `depositar(cantidad)`: Aumenta el saldo si la cantidad es positiva.
   - `retirar(cantidad)`: Reduce el saldo si la cantidad es menor o igual al saldo disponible.
   - `get_saldo()`: Retorna el saldo actual.
   - `set_saldo(nuevo_saldo)`: Permite modificar el saldo solo si el valor es mayor o igual a 0.
3. Prueba la clase creando una cuenta y manipulando el saldo con estos métodos.

## SOLUCION 
``` python
import os
os.system('cls')

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular                      # Atributo publico
        self.__saldo = saldo_inicial                # Atributo privado

    def depositar(self, cantidad):
        """Aumenta el saldo si la cantidad es positiva"""
        if cantidad > 0:
            self.__saldo += cantidad
            print('Depósito exitoso')
        else:
            print('La cantidad a depositar tiene que ser positiva')

    def retirar(self, cantidad):
        """Retira el saldo si la cantidad es menor o igual al saldo disponible"""
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print('Retiro exitoso.')
        else:
            print('Retiro insuficiente o cantidad inválida')
    

    # Cuando son privados:
    # Getter
    def get_saldo(self):
        return self.__saldo
    
    # Setter
    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo
    
    # Métodos privado
    def __cuenta_privada(self):
        print('Esta cuenta es privada')



cuenta_corriente = CuentaBancaria('Javier', 18500)
print(cuenta_corriente.titular)

# Acceder objeto privado (otra forma) --> objeto._nombreClase__nombreAtributo
print(cuenta_corriente.get_saldo())
print(cuenta_corriente._CuentaBancaria__saldo)

# Acceder métodos_privados
print(cuenta_corriente._CuentaBancaria__saldo)
cuenta_corriente._CuentaBancaria__cuenta_privada()
```
---

### **Ejercicio 2: Métodos Privados**
**Objetivo:** Aplicar encapsulamiento en métodos de una clase.

#### **Instrucciones:**  
1. Crea una clase `SensorTemperatura` con los atributos:
   - `__temperatura` (privado, valor inicial 25°C)
2. Implementa los métodos:
   - `__calibrar()`: Método privado que imprime `"Calibrando sensor..."`.
   - `medir_temperatura()`: Llama a `__calibrar()` y devuelve la temperatura.
   - `set_temperatura(nueva_temp)`: Modifica la temperatura solo si está en el rango -50 a 150°C.
3. Prueba la clase instanciando un objeto y llamando a los métodos.

## SOLUCION 
``` python
import os
os.system('cls')

class SensorTemperatura:
    def __init__(self, temperatura = 25):
        self.__temperatura = temperatura

    def __calibrar(self):
        print('Calibrando sensor...')
    
    def medir_temperatura(self):
        self.__calibrar()
        return self.__temperatura
    
    def set_temperatura(self, nueva_temp):
        if nueva_temp > -50 and nueva_temp < 150:
            self.__temperatura = nueva_temp

    def get_saldo(self):
        return self.__temperatura


temperatura = SensorTemperatura()
temperatura._SensorTemperatura__calibrar()
print(temperatura.medir_temperatura())
temperatura.set_temperatura(10)
print(temperatura.get_saldo())
```
---

## Ejercicio 3: Encapsulamiento y Herencia en un Videojuego de Rol

### **Objetivo:**
Aplicar encapsulamiento en una clase base y heredarla en un contexto de videojuegos de rol con interacciones dinámicas.

### **Instrucciones:**

1. Crea una clase `Personaje` con:
   - `__nivel` (privado, inicializado en 1)
   - `__vida` (privado, inicializado en 100)
   - `subir_nivel()`: Aumenta el nivel en 1 y mejora la vida en 10 puntos.
   - `recibir_daño(cantidad)`: Reduce la vida si la cantidad es positiva y no deja que sea menor a 0.
   - `get_nivel()`: Retorna el nivel actual.
   - `get_vida()`: Retorna la vida actual.

2. Crea una subclase `Picaro` que tenga:
   - `__fuerza` (privado, inicializado en 10).
   - `atacar()`: Imprime "El pícaro ataca con una fuerza de X!", donde X es el valor de `__fuerza`.
   - `mejorar_fuerza()`: Aumenta la fuerza en 5 cada vez que se llama.

3. Crea una clase `Monstruo` con:
   - `__vida` (privado, inicializado en 50)
   - `recibir_daño(cantidad)`: Reduce la vida si la cantidad es positiva y no deja que sea menor a 0.
   - `get_vida()`: Retorna la vida actual.

4. Implementa un menú donde:
   - Aparezca un monstruo.
   - El jugador pueda elegir atacar al monstruo.
   - El pícaro pueda recibir daño del monstruo.
   - Se muestre la vida actual de ambos personajes tras cada acción.
   - Se pueda mejorar la fuerza del pícaro.
   - El juego termine si el pícaro o el monstruo llegan a 0 de vida.

Prueba la clase creando un `Pícaro`, subiendo de nivel, atacando, mejorando su fuerza y enfrentándose a un `Monstruo` en el menú interactivo.

## SOLUCION 
``` python

```
---

### **Ejercicio 4: Encapsulamiento y Herencia**
**Objetivo:** Aplicar encapsulamiento en una clase base y heredarla.

#### **Instrucciones:**  
1. Crea una clase `Vehiculo` con:
   - `__velocidad` (privado, inicializado en 0)
   - `acelerar(cantidad)`: Aumenta la velocidad si la cantidad es positiva.
   - `frenar(cantidad)`: Reduce la velocidad sin que sea menor a 0.
   - `get_velocidad()`: Retorna la velocidad actual.
2. Crea una subclase `Coche` que tenga:
   - `marca` (público)
   - `__modo_sport` (privado, inicializado en `False`)
   - `activar_sport()`: Activa `__modo_sport` e imprime `"Modo Sport activado!"`.
3. Prueba la clase creando un `Coche`, acelerando, frenando y activando el modo sport.

## SOLUCION 
``` python

```