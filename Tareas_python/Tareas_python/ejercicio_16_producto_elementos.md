# 16. PRODUCTO ELEMENTOS

Escribe una función que devuelva el producto de todos los números de una lista


``` python
import os
os.system('cls')

def producto_array(arr):
    producto = 1

    for i in arr:
        producto *= i

    return producto


if __name__ == '__main__':
    array = [1, 2, 3, 4]
    producto = producto_array(array)
    print(producto)

    # print(producto_array([1, 2, 3, 4]))  # Salida: 24
```

