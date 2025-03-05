# 📌 Ejercicio 5: Clases y Métodos Abstractos
# ✔️ Objetivo: Trabajar con clases abstractas y la implementación de métodos en clases derivadas.

# 🔹 Ejercicio:
# Crea una clase abstracta Empleado con:

# Un método __init__ que reciba el nombre del empleado.
# Un método abstracto calcular_salario que deberá ser implementado por las clases hijas.
# Crea dos clases EmpleadoPorHora y EmpleadoFijo que hereden de Empleado:

# EmpleadoPorHora recibirá el número de horas trabajadas y la tarifa por hora, y calculará el salario multiplicando estos valores.
# EmpleadoFijo recibirá un sueldo fijo y lo devolverá como salario.
# Crea instancias de ambas clases y calcula el salario de diferentes empleados.

import os
os.system('cls')

from abc import ABC, abstractmethod


class Empleado(ABC):
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def calcular_salario(self):
        pass


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, horas, tarifas):
        super().__init__(nombre)
        self.horas = horas
        self.tarifas = tarifas
    
    def calcular_salario(self):
        return self.horas * self.tarifas


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, salario_fijo):
        super().__init__(nombre)
        self.salario_fijo = salario_fijo
    
    def calcular_salario(self):
        return self.salario_fijo

e1 = EmpleadoPorHora('María', 40, 15)
e2 = EmpleadoFijo('Roberto', 3000)

print(f'Salario de {e1.nombre}: {e1.calcular_salario()}')
print(f'Salario de {e2.nombre}: {e2.calcular_salario()}')