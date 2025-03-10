1. Listar los nombres de los estudiantes que están matriculados en el curso de "Matemáticas".
```python
def listar_nombres_cursan_Matematicas(estudiantes):

    estudiantes_matematicas =[]

    for estudiante in estudiantes:
        if(estudiante[2] == 'Matemáticas'):
            estudiantes_matematicas.append(estudiante[0])

    return estudiantes_matematicas


if __name__ == '__main__':
    print(listar_nombres_cursan_Matematicas(estudiantes))
```

2. Calcular el promedio de las calificaciones de todos los estudiantes.
```python
def calcular_promedio_estudiantil(estudiantes):

    total = 0
    cantidad_estudiantes = len(estudiantes)

    for estudiante in estudiantes:
        total += estudiante[3]
    
    promedio = total / cantidad_estudiantes

    return promedio


if __name__ == '__main__':
    print(calcular_promedio_estudiantil(estudiantes))
```

3. Mostrar los estudiantes cuya calificación promedio es superior a 8.
```python
def mostrar_estudiantes_con_promedio_superior_a_8(estudiantes):

    estudiantes_promedio_mayor_a_8 = []

    for estudiante in estudiantes:
        if(estudiante[3] > 8):
            estudiantes_promedio_mayor_a_8.append(estudiante[0])

    return estudiantes_promedio_mayor_a_8


if __name__ == '__main__':
    print(mostrar_estudiantes_con_promedio_superior_a_8(estudiantes))
```

4. Contar cuántos estudiantes tienen más del 90% de asistencia.
```python
def mostrar_estudiantes_mayor_90_porciento_asistencia(estudiantes):

    estudiantes_mayor_80_porciento_asistencia = []

    for estudiante in estudiantes:
        if(estudiante[4] > 90):
            estudiantes_mayor_80_porciento_asistencia.append(estudiante[0])

    return estudiantes_mayor_80_porciento_asistencia


if __name__ == '__main__':
    print(mostrar_estudiantes_mayor_90_porciento_asistencia(estudiantes))
```

5. Encontrar el estudiante con la mayor calificación promedio y mostrar su nombre y calificación.
```python
def encontrar_mejor_estudiante(estudiantes):

    mejor_estudiante = estudiantes[0]

    for estudiante in estudiantes:
        nota = estudiante[3]
        
        if nota > mejor_estudiante[3]:
            mejor_estudiante = estudiante
            

    return mejor_estudiante[0], mejor_estudiante[3]

if __name__ == '__main__':
    print(encontrar_mejor_estudiante(estudiantes))
```

6. Listar los estudiantes cuyo nombre comienza con la letra "M".
```python
def listar_nombre_empiezan_por_M(estudiantes):

    lista_estudiantes_empiezan_con_la_M = []
    listado_nombres = []

    for estudiante in estudiantes:
        nombre = estudiante[0]
        listado_nombres.append(nombre)
    
    for nombre in listado_nombres:
        inicial = nombre[0]

        if(inicial == 'M'):
            lista_estudiantes_empiezan_con_la_M.append(nombre)

    return lista_estudiantes_empiezan_con_la_M


if __name__ == '__main__':
    print(listar_nombre_empiezan_por_M(estudiantes))
```

7. Calcular el porcentaje de estudiantes con más de 90% de asistencia.
```python

```

8. Mostrar los estudiantes que tienen una calificación promedio menor a 7.5.
```python

```

9. Ordenar los estudiantes por edad de menor a mayor y mostrar sus nombres y edades.
```python

```

10. Encontrar el estudiante con la menor asistencia y mostrar su nombre y número de asistencias.
```python

```

11. Agregar un nuevo estudiante a la base de datos: "Laura Martínez", 18 años, curso "Historia", calificación 9.0, asistencias 100.
```python

```

12. Eliminar los estudiantes cuyo curso sea "Historia".
```python

```

13. Calcular la calificación promedio general del curso "Física".
```python

```

14. Mostrar los estudiantes cuya calificación promedio sea mayor o igual a 8.
```python

```

15. Mostrar los nombres y edades de los estudiantes que tienen una calificación promedio mayor a 8 y menos de 95% de asistencias.
```python

```

16. Contar cuántos estudiantes están matriculados en el curso de "Química".
```python

```

17. Modificar la calificación promedio de "Carlos Sánchez" a 7.5.
```python

```

18. Ordenar los estudiantes por calificación promedio de mayor a menor y mostrar sus nombres y calificaciones.
```python

```

19. Contar cuántos estudiantes tienen menos de 90% de asistencia.
```python

```

20. Mostrar los estudiantes cuyo nombre contenga la letra "a".
```python

```
