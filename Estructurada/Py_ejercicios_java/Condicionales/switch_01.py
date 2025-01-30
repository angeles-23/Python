import os
os.system('cls')

dia_semana = int(input('Introduce el día de la semana [1-7]: '))

if(dia_semana<1 or dia_semana>7):
    print(f'El día de la semana es incorrecto')
else:
    match dia_semana:
        case 1:
            print(f'El día {dia_semana} es el Lunes')
        case 2:
            print(f'El día {dia_semana} es el Martes')
        case 3:
            print(f'El día {dia_semana} es el Miércoles')
        case 4:
            print(f'El día {dia_semana} es el Jueves')
        case 5:
            print(f'El día {dia_semana} es el Viernes')
        case 6:
            print(f'El día {dia_semana} es el Sábado')
        case 7:
            print(f'El día {dia_semana} es el Domingo')

    # if (dia_semana == 1):
    #     print(f'El día {dia_semana} es el Lunes')
    # if (dia_semana == 2):
    #     print(f'El día {dia_semana} es el Martes')
    # if (dia_semana == 3):
    #     print(f'El día {dia_semana} es el Miércoles')
    # if (dia_semana == 4):
    #     print(f'El día {dia_semana} es el Jueves')
    # if (dia_semana == 5):
    #     print(f'El día {dia_semana} es el Viernes')
    # if (dia_semana == 6):
    #     print(f'El día {dia_semana} es el Sábado')
    # if (dia_semana == 7):
    #     print(f'El día {dia_semana} es el Domingo')
