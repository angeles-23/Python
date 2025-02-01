arg1 = 10
arg2 = 30

def suma (parametro1, parametro2):
    resultado = parametro1 + parametro2
    print(resultado)

suma(arg1, arg2)



def resta (arg1, arg2):
    resultado = arg1 - arg2
    return resultado

operacionResta = resta(arg1, arg2)
print(operacionResta)


# Codigo optimizado
def resta(parametro1, parametro2):
    return parametro1 - parametro2

print(resta(arg1, arg2))