# Indicar la cantidad total de dinero que tiene que pagar la empresa en salarios
salarios = (1500,1250,2300,900,900,2800,1600,1500,1800)


# Forma normal
total = 0

for salario in salarios:
    print(salario)
    total += salario

print(f'La cantidad total de salarios es {total}')


# Con una función y un printf
def calcularTotal(salarios):
    total = 0
    for salario in salarios:
        total += salario
    return total

print(f'Total salarios: {calcularTotal(salarios)}')