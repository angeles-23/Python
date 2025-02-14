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