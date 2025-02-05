class Animal:
    def __init__(self, especie):
        self.especie = especie      # Atributo de instancia / Atributo común para toda las clases hijas
    
    def hacer_sonidos(self):
        print('Este animal hace un sonido genérico.')

    def escribir_habitat(self):
        print(f'El {self.especie} puede vivir en diversos hábitats.')


class Perro(Animal):
    def __init__(self):
        super().__init__('perro')