#! /usr/bin/python

import subprocess


def main():
    '''
    Aquí se llaman a las funciones para llevarlas al main
    '''
    clear_screen()
    pausa = input('Pulsa Enter para continuar...')
    


def clear_screen():
    '''
    Limpia la pantalla
    '''
    subprocess.run(['clear'])



if __name__ == '__main__':
    main()