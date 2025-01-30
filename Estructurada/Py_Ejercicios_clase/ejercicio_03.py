import os
os.system('cls')

# Añadir animales a la granja

animales = [
    'oveja',
    'caballo',
    'cerdo'
]

# Añadir a la lista 6 gallinas, 3 burros, 2 caballos y 3 cerdos
# Mostrar por pantalla cuantos animales de cada tipo tenemos en total.

# Añadimos 6 gallinas
contador = 6
for i in range(contador):
    animales.append('gallina')


# Añadimos 3 burros
contador = 3
for i in range(contador):
    animales.append('burro')

# Añadimos 2 caballos
contador = 2
for i in range(contador):
    animales.append('caballo')

# Añadir 3 cerdos
contador = 3
for i in range(contador):
    animales.append('cerdo')


contador_ovejas = 0
contador_caballos = 0
contador_cerdos = 0
contador_gallinas = 0
contador_burros = 0

for animal in animales:
    if animal == 'oveja':
        contador_ovejas += 1
    if animal == 'caballo':
        contador_caballos += 1
    if animal == 'cerdo':
        contador_cerdos += 1
    if animal == 'gallina':
        contador_gallinas += 1
    if animal == 'burro':
        contador_burros += 1

# contador_ovejas = animales.count('oveja')
# contador_gallinas = animales.count('gallina')
# contador_caballos = animales.count('caballo')
# contador_cerdos = animales.count('cerdo')
# contador_burros = animales.count('burro')


print(f'En esta granja hay {contador_ovejas} ovejas.')
print(f'En esta granja hay {contador_caballos} caballos.')
print(f'En esta granja hay {contador_cerdos} cerdos.')
print(f'En esta granja hay {contador_gallinas} gallinas.')
print(f'En esta granja hay {contador_burros} burros.')

print()
print(animales)