argumento1 = 'fruta'
argumento2 = 'hielo'
argumento3 = 'azucar'

def licuadora(argumento1, argumento2, argumento3):
    if(argumento1 == 'fruta' and argumento2 == 'hielo' and argumento3 == 'azucar'):
        return 'Licuado de fruta'
    elif (argumento1 == 'banana' and argumento3 == 'azucar'):
        return 'Licuado de banana'
    elif (argumento1 == 'naranja' and argumento2 == 'hielo' and argumento3 == 'vodka'):
        return 'Licuado de naranja'
    else:
        return 'Licuado error'

print(licuadora('fruta', 'hielo', 'azucar'))
print(licuadora('banana', '', 'azucar'))
print(licuadora('naranja', 'hielo', 'vodka'))
print(licuadora('limon', 'agua', 'azucar'))
