import os

elementos = os.listdir()


print(f'\n📂  Contenido del directorio actual:\n')
for i, nombre in enumerate(elementos, start=1):
    print(f"{i}) {nombre}")
