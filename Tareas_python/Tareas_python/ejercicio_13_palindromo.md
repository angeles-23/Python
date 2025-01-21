# 13. PALINDROMO
Escribe un programa en Python que determine si una palabra o frase es un palíndromo.
 -  Crea una función llamada es_palindromo(cadena) que reciba una cadena de texto como parámetro y devuelva True si es un palíndromo, o False en caso contrario.
 -  Ignora los espacios y convierte todas las letras a minúsculas para comparar correctamente.
 -  El programa debe pedir al usuario una palabra o frase e indicar si es un palíndromo utilizando la función implementada.
 -  Para transformar una cadena a minusculas: cadena.lower()
 -  Para solo agregar caracteres alfanuméricos: cadena.isalnum()


``` python
import os
os.system('cls')

def es_palindromo(cadena):
    
    palindromo_correcto = False
    cadena_texto_1 = []
    cadena_texto_2 = []

    
    for i in cadena:
        cadena_texto_1.append(i)
        cadena_texto_2.append(i)
    
    cadena_texto_2.reverse()

    for i in range(len(cadena_texto_1)):
        if(cadena_texto_1[i] == cadena_texto_2[i]):
            palindromo_correcto = True

    print(cadena_texto_1, cadena_texto_2)

    return palindromo_correcto



if __name__ == '__main__':
    texto = input('Introduce una palabra o frase: ').lower()
    palindromo = es_palindromo(texto)
    
    if(palindromo == True):
        print(f'"{texto}" no es palindromo')
    else:
        print(f'"{texto}" si es palindromo')
```



