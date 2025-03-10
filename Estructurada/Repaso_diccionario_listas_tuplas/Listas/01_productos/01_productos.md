1. Listar todos los productos de la categoría "Electrónica".
``` python
def listar_productos_electronica(productos):
    
    lista_productos = []

    for producto in productos:
        if producto['categoria'] == 'Electrónica':
            lista_productos.append(producto['nombre'])

    return lista_productos


if __name__ == '__main__':
    productos_electronica = listar_productos_electronica(productos)
    print(productos_electronica)
```


2. Encontrar el producto más caro en la lista y mostrar su nombre y precio.
``` python
def buscar_producto_mas_caro(productos):
    
    precio_producto_mas_caro = productos[0]['precio']

    for producto in productos:
        if producto['precio'] > precio_producto_mas_caro:
            precio_producto_mas_caro = producto['precio']
    
    for producto in productos:
        if(precio_producto_mas_caro == producto['precio']):
            return producto['nombre'], producto['precio']

    return None


if __name__ == '__main__':
    producto_mas_caro = buscar_producto_mas_caro(productos)
    print(producto_mas_caro)
```


3. Ordenar los productos por precio de menor a mayor.
``` python
def productos_ordenados_de_menor_a_mayor(productos):

    lista_productos = []

    for producto in productos:
        precio = producto['precio']
        lista_productos.append(precio)

    lista_productos_ordenados = sorted(lista_productos)

    return lista_productos_ordenados


if __name__ == '__main__':
    productos_ordenados = productos_ordenados_de_menor_a_mayor(productos)
    print(productos_ordenados)
```


4. Aumentar el stock de todos los productos en un 10%.
``` python
def aumentar_diez_porciento_stock(productos):

    PORCENTAJE = 10

    for producto in productos:
        final = 0

        normal = producto['stock']
        porcentaje_calculado = normal * PORCENTAJE / 100
        final = normal + porcentaje_calculado
        producto['stock'] = final

    return productos


if __name__ == '__main__':
    productos_con_10_porciento_stock = aumentar_diez_porciento_stock(productos)
    print(productos_con_10_porciento_stock)
```


5. Eliminar todos los productos cuyo stock sea menor a 5 unidades.
``` python
def eliminar_stock_menor_a_5(productos):

    lista_sin_productos_stock_5 = []

    for producto in range(0, len(productos)):
        if productos[producto]['stock'] > 5:
            lista_sin_productos_stock_5.append(productos[producto])

    
    return lista_sin_productos_stock_5


if __name__ == '__main__':
    stock_mayor_o_igual_a_5 = eliminar_stock_menor_a_5(productos)
    print(stock_mayor_o_igual_a_5)
```


6. Buscar un producto por nombre (por ejemplo, "Camiseta") y mostrar su información.
``` python
def mostrar_informacion(productos, producto_buscado):

    for producto in productos:
        if producto['nombre'] == producto_buscado:
            return producto
        
    return None


if __name__ == '__main__':
    producto_a_buscar = input('Producto a buscar: ')
    if mostrar_informacion(productos, producto_a_buscar) == None:
        print('Lo siento, no se ha encontrado el producto')
    else:
        print(mostrar_informacion(productos, producto_a_buscar))
```


7. Modificar el precio de un producto específico (por ejemplo, aumentar el precio de "Laptop" en un 5%).
``` python
def modificar_precio_especifico(productos, producto_a_modificar, PORCENTAJE):

    for producto in productos:
        nombre_producto = producto['nombre']

        if (producto_a_modificar == nombre_producto):
            precio_normal = producto['precio']
            precio_aumentado = precio_normal + (precio_normal*PORCENTAJE) / 100
            producto['precio'] = precio_aumentado
            return producto
    
    return None

if __name__ == '__main__':
    print(modificar_precio_especifico(productos, 'Laptop', 5))

```


8. Agregar un nuevo producto a la lista, por ejemplo: "Televisor", con precio 400, stock 2 y categoría "Electrodomésticos".
``` python
def agregar_nuevo_elemento(productos, nombre, precio, stock, categoria):
    
    nuevo_producto = {'nombre': {nombre}, 'precio': {precio}, 'stock': {stock}, 'categoria': {categoria}}
    productos.append(nuevo_producto)
            
    return productos
    

if __name__ == '__main__':
    print(agregar_nuevo_elemento(productos, 'Televisor', 400, 2, 'Electrodomésticos'))
```


9. Mostrar los productos con un stock mayor a 10 unidades.
``` python
if __name__ == '__main__':
```


10. Calcular el valor total del inventario (precio * stock) para todos los productos.
``` python
if __name__ == '__main__':
```


11. Mostrar todos los productos que cuesten menos de 100.
``` python

```


12. Contar cuántos productos hay en la categoría "Ropa".
``` python

```


13. Eliminar un producto de la lista por nombre (por ejemplo, eliminar "Microondas").
``` python

```


14. Mostrar los productos con precio superior a 100, ordenados alfabéticamente por nombre.
``` python

```


15. Encontrar el producto con la cantidad más baja de stock y mostrar su nombre y stock.
``` python

```

