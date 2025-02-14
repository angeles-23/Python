class Factura:
    tasa_iva = 0.21

    def __init__(self, numero_factura, monto):
        self.numero_factura = numero_factura
        self.monto = monto

    def calcular_total(self, total_factura):
        total_factura *= Factura.tasa_iva
        return f'El monto total es {total_factura}'
    
    @classmethod
    def cambiar_tasa_iva(cls, nueva_tasa):
        cls.tasa_iva = nueva_tasa

    @staticmethod
    def formatear_monto(monto):
        return f'El monto formateado es:{monto:.2f}€'
    

factura1 = Factura(1, 500)
factura2 = Factura(1, 500)
factura3 = Factura(1, 500)

print(factura1.calcular_total())