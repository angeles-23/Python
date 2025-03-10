class Persona:
    numero_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona.numero_personas += 1
    
    @classmethod
    def imprimir_numero_personas(cls):
        ''' 
        Método para imprimir cuántas personas se han creado
        '''
        return f'Existen {cls.numero_personas} personas'


class Alumno(Persona):  
    def __init__(self, nombre, apellido, numero_estudiante):
        super().__init__(nombre, apellido)
        self.numero_estudiante = numero_estudiante
    
    def imprimir_informacion(self):
        return f'{self.nombre} {self.apellido} con numero estudiante: {self.numero_estudiante}'
    
    def añadir_alumno(): # self, nombre, apellido, dni
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        numero_estudiante = int(input('Numero_estudiante: '))

        Persona.numero_personas += 1
        print('Se ha creado un alumno\n')

        return nombre, apellido, numero_estudiante   # Esto se quedaría igual
    

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido)
        self.dni = dni

    def imprimir_informacion(self):
        return f'{self.nombre} {self.apellido} con DNI:{self.dni}'
    
    def añadir_profesor(): # self, nombre, apellido, dni
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        dni = input('DNI: ')
        Persona.numero_personas += 1
        print('Se ha creado un profesor\n')

        return nombre, apellido, dni     # Esto se quedaría igual



import os 
os.system('cls')

print(Persona.imprimir_numero_personas())

Alumno.añadir_alumno()          # Alumno.añadir_alumno(nombre, apellido, numero_estudiante)
Alumno.añadir_alumno()
Alumno.añadir_alumno()
print(Persona.imprimir_numero_personas())

Profesor.añadir_profesor()      # Profesor.añadir_profesor(nombre, apellido, dni)
print(Persona.imprimir_numero_personas())
