# Ejercicio 4: Métodos de Clase y Métodos Estáticos
# Crea una clase Banco con un atributo de clase tasa_interes inicializado a 0.05.

# Define un método de clase que permita actualizar la tasa de interés.
# Añade un método estático llamado convertir_moneda que reciba un valor en dólares y lo convierta a euros (asume una tasa fija de 0.85).
# Prueba la clase actualizando la tasa de interés y utilizando el método estático.

import os
os.system('cls')


class Banco:

    tasa_interes = 0.05 # Atributo de clase

    def __init__(self, persona1, capacidad_monetaria): 
        self.persona1 = persona1                        # Atributo de instancia
        self.capacidad_monetaria = capacidad_monetaria  # Atributo de instancia

    def modificar_tasa(self, nueva_tasa):
        self.tasa_interes = nueva_tasa


    # Permite MODIFICAR los atributos (tanto de clase como de instancia) de la clase SIN NECESIDAD DE HACER INSTANCIAS
    @classmethod 
    def actualizar_tasa(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa

    # Permite llamar a la funcion SIN NECESIDAD DE HACER INSTANCIAS
    @staticmethod
    def convertir_moneda(dolares):
        euros = dolares * 0.85
        print(f'{dolares}$ son {euros}€')



banco = Banco(150,6000000)      # Esto crea una instancia

print('Tasa de interes antes de cambiar:')
print(Banco.tasa_interes)

banco_sabadell = Banco(250,4000000)
print(f'\nBanco Sabadell: {banco_sabadell.tasa_interes}')

banco_BBVA = Banco(500,8000000)
print(f'Banco BBVA: {banco_BBVA.tasa_interes}')

print('\nModifico la tasa del banco BBVA: ')
Banco.actualizar_tasa(0.14)
print(f'Banco Sabadell: {banco_sabadell.tasa_interes}')
print(f'Banco BBVA: {banco_BBVA.tasa_interes}')


print('\nCambio el atributo de clase de la tasa de interés: ')
Banco.actualizar_tasa(0.10)
print(f'Banco Sabadell: {banco_sabadell.tasa_interes}')
print(f'Banco BBVA: {banco_BBVA.tasa_interes}')
print('\nTasa de interes después de cambiar:')
print(Banco.tasa_interes)
