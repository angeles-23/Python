#Calcular la media de altura en metros
estaturas = (1.68, 1.88, 1.52, 1.73, 1.57, 1.79, 1.65, 1.84)

tamanio_tupla = len(estaturas)


# SIN FUNCION Y CON i
cantidadEstaturas = 0
total = 0
for estatura in estaturas:
    total += estatura
    cantidadEstaturas += 1

media = total / cantidadEstaturas

print(f'Media: {media} (sin decimales)')
print(f'Media: %.2f (con dos decimales)' % media)

print('-'*50)



# CON FUNCIÓN Y CON len
def calcularMedia(estaturas):
    total = 0
    for estatura in estaturas:
        total += estatura

    media = total / tamanio_tupla

    return media

print(f'Media: {calcularMedia(estaturas)} (sin decimales)')
print(f'Media: %.2f (con dos decimales)' % calcularMedia(estaturas))





# Calcular la altura maxima de la clase

# SIN FUNCION
maximo = 0

for estatura in estaturas:
    if(maximo < estatura):
        maximo = estatura

print(f'Estatura maxima: {maximo}')

print('-'*50)


# CON FUNCION
def calcularAlturaMaxima(estaturas):
    maximo = 0

    for estatura in estaturas:
        if(maximo < estatura):
            maximo = estatura
    return maximo

print(f'Estatura maxima: {calcularAlturaMaxima(estaturas)}')