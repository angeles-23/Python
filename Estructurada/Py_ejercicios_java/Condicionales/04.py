import os 
os.system('cls')

hora = int(input('Introduce la hora [24h]: '))

if(hora < 0 or hora > 24):
    print('La hora es incorrecta')
else:
    if (hora >= 6 and hora < 12):
        print(f'Son las {hora}. BUENOS DÍAS')
    elif (hora >= 12 and hora < 21):
        print(f'Son las {hora}. BUENAS TARDES')
    elif ((hora >=21 and hora <= 23) or (hora > 0 and hora <6)):
        print(f'Son las {hora}. BUENAS NOCHES')-5
    