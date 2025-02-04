# Ejercicio 2: Herencia Múltiple - Componentes de un Automóvil
# Crea dos clases base:

# Motor con un método tipo_motor() que devuelva un tipo de motor.
# Chasis con un método tipo_chasis() que devuelva un tipo de chasis.
# Luego, crea una clase Automovil que herede de ambas y tenga un método descripcion() que combine la información de las clases base.

# Objetivo:
# Crea una instancia de Automovil y llama al método descripcion().



import os
os.system('cls')

# Tambien se puede hacer sin parentesis y sin self
class Motor():
    def tipo_motor(self):
        return f'V6'
    

class Chasis:
    def tipo_chasis(self):
        return f'Monasco'
    

class Automovil(Motor, Chasis):
    def descripcion(self):
        return f'El automovil tiene un motor {self.tipo_motor()} y un tipo de chasis {self.tipo_chasis()}.'
    
automovil = Automovil()
print(automovil.descripcion())