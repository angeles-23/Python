import os
os.system('cls')

examen1 = float(input('Nota examen 1: '))
examen2 = float(input('Nota examen 2: '))
examen3 = float(input('Nota examen 3: '))
entrega_trabajo = input('Has entregado el trabajo [S/N]: ')

porcentaje_examen1 = 30
porcentaje_examen2 = 30
porcentaje_examen3 = 40

if((examen1<0 or examen1>10) or (examen2<0 or examen2>10) or (examen3<0 or examen3>10)):
    if(examen1<0 or examen1>10):
        print('La nota del examen 1 es incorrecta')
    
    if(examen2<0 or examen2>10):
        print('La nota del examen 2 es incorrecta')
    
    if(examen3<0 or examen3>10):
        print('La nota del examen 3 es incorrecta')
else:
    nota_final = int(examen1*porcentaje_examen1)/100 + (examen2*porcentaje_examen2)/100 + (examen3*porcentaje_examen3)/100

    if (entrega_trabajo == 'N'):
        nota_final = 4
        print(f'La nota final es {nota_final:.2f}')
    elif (entrega_trabajo == 'S'):
        if (nota_final < 5):
            print(f'Suspenso con un {nota_final:.2f}')
        elif (nota_final < 6):
            print(f'Suficiente con un {nota_final:.2f}')
        elif (nota_final < 7):
            print(f'Bien con un {nota_final:.2f}')
        elif (nota_final < 8):
            print(f'Notable bajo con un {nota_final:.2f}')
        elif (nota_final < 9):
            print(f'Notable alto con un {nota_final:.2f}')
        elif (nota_final < 10):
            print(f'Sobresaliente con un {nota_final:.2f}')
        elif(nota_final == 10):
            print(f'Matricula de honor con un {nota_final:.2f}')
