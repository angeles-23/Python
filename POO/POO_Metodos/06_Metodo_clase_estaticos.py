# ✔️ **Objetivo:** Implementar un sistema de registro de usuarios con métodos de clase y estáticos.

# 🔹 **Ejercicio:**  
# Crea una clase `Usuario` que tenga:
# - Un atributo de clase `usuarios_registrados`, que almacene un contador de usuarios creados.
# - Un constructor que reciba el nombre del usuario e incremente `usuarios_registrados`.
# - Un método de instancia `mostrar_usuario` que devuelva el nombre del usuario.
# - Un método de clase `cantidad_usuarios` que devuelva el número total de usuarios registrados.
# - Un método estático `validar_nombre_usuario` que reciba un nombre y devuelva `True` si tiene más de 3 caracteres, `False` en caso contrario.

# Crea varias instancias de `Usuario` y prueba los métodos.

class Usuario:
    usuarios_registrados = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.usuarios_registrados += 1

    def mostrar_usuario(self):
        return self.nombre
    
    @classmethod
    def cantidad_usuarios(cls):
        return cls.usuarios_registrados

    @staticmethod
    def validar_nombre (nombreValidado):
        if len(nombreValidado) > 3:
            return True
        else:
            return False
              
u1 = Usuario('Pedro')
u2 = Usuario('Gavi')

print(u1.mostrar_usuario())
print(u2.mostrar_usuario())

print(Usuario.cantidad_usuarios())

print(Usuario.validar_nombre('Adrian'))
print(Usuario.validar_nombre('Ana'))