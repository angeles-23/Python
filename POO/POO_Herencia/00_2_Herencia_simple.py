import os
os.system('cls')

class Persona:      # Clase padre
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentacion(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."
    
    def obtener_nombre(self):
        return f'Me llamo {self.nombre}.'


class Estudiante(Persona):      # Clase hija, herencia Persona
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Se repite la asignación de atributos de la clase padre
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def presentacion(self):
        return f"{super().presentacion()} Estudio {self.carrera}."
    
    def estudios(self):
        return f'Mis estudios son {self.carrera}.'


estudiante = Estudiante("Pedro", 22, "DAW")
print(estudiante.presentacion())  # Salida: Me llamo Pedro y tengo 22 años. Estudio Ingeniería Informática.
print(estudiante.obtener_nombre())
print(estudiante.estudios())

persona = Persona('Marta', 23, )
print(persona.presentacion())