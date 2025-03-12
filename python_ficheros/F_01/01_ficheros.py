## Ejercicio:

# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre `tabla-n.txt` la tabla de multiplcar de ese número, donde `n` es el número introducido.
import os 
os.system('cls')

while True:
    try:
        n = int(input('Número entre 1 y 10: '))

        if n <= 0 or n > 10:
            print('Número incorrecto. Vuelve a intentarlo')
        else:
            break
    except Exception:
        print('El valor introducido no es correcto')


f = open(f'./F_01/tabla-{n}.txt', 'w')

for i in range(1,11):
    if(i == 10): 
        f.write(f'{n} * {i} = {n*i}')
    else:
        f.write(f'{n} * {i} = {n*i}\n')
        
f.close()