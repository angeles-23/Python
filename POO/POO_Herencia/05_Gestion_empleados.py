# Ejercicio 5: Gestión de empleados
# Crea una clase base llamada Empleado con los siguientes atributos y métodos:

# Atributos:
# nombre (str)
# salario (float)

# Métodos:
# mostrar_info(): Debe imprimir "Empleado: [nombre], Salario: [salario]".
# calcular_bono(): Devuelve el 10% del salario.
# Luego, crea dos clases derivadas:

# Gerente:
# Sobrescribe calcular_bono() para devolver el 20% del salario.

# Desarrollador:
# Sobrescribe calcular_bono() para devolver el 15% del salario.

# Objetivo:
# Crea instancias de Gerente y Desarrollador y muestra su información junto con el bono calculado.


class Empleado:
    def __init__(self, nombre=str, salario=float):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f'Empleado: {self.nombre}, Salario: {self.salario}'
    
    def calcular_bono(self):
        return (self.salario * 0.1) 


class Gerente(Empleado):
    def calcular_bono(self):
        return (self.salario * 0.2)
    

class Desarrollador(Empleado):
    def calcular_bono(self):
        return (self.salario * 0.15)

gerente = Gerente('Isabel', 2000)
empleado = Empleado('Oscar', 1200)

print(f'El bono es de {gerente.calcular_bono()}')
print(f'El bono es de {empleado.calcular_bono()}')