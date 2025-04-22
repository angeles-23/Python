#! usr/bin/python3

'''
Calendario del mes 
Muestra el calendario del mes actual utilizando el comando 'cal' y el modulo datetime para obtener el mes y el año actual
'''

import subprocess
from datetime import datetime

# Paso 1: obtener la fecha de hoy en python
today = datetime.now()
mes = today.month
anio = today.year

# Paso 2: mostrar por pantalla el mes y el año:
print(f"\n  Calendario del mes {mes} del año {anio}\n")

# Paso 3: Ejecutar el comando 'cal' con 'subprocess':
subprocess.run(['cal', str(mes), str(anio)])