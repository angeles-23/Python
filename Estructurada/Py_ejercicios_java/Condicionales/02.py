nombre = input('Nombre: ')
contrasenia = input('Contraseña: ')

nombre_correcto = 'root'
contrasenia_correcta = 'toor'

# CON if...else
# if(nombre == nombre_correcto and contrasenia == contrasenia_correcta):
#     print('Has entrado al sistema')
# else:
#     print('No has entrado al sistema')


# CON if...else anidado
# if(nombre == nombre_correcto):
#     if(contrasenia == contrasenia_correcta):
#         print('Has entrado al sistema')
#     else:
#         print('La contraseña no es correcta')
# else:
#     print('El nombre no es correcto')


# CON booleanos
es_nombre_correcto = False
es_contrasenia_correcta = False

if(nombre == nombre_correcto):
    es_nombre_correcto = True

if(contrasenia == contrasenia_correcta):
    es_contrasenia_correcta = True

if(es_nombre_correcto == True and es_contrasenia_correcta == True):
    print('Has entrado al sistema')
else:
    print('No has entrado al sistema')