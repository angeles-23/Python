# ### 📌 **Ejercicio 7: Sistema de Facturación con Métodos de Instancia, Clase y Estáticos**
# ✔️ **Objetivo:** Aplicar los tres tipos de métodos en una simulación de facturación.

# 🔹 **Ejercicio:**  
# Crea una clase `Factura` que tenga:
# - Un atributo de clase `tasa_iva`, que almacene el porcentaje de IVA aplicado a las facturas.
# - Un constructor que reciba el número de factura y el monto base.
# - Un método de instancia `calcular_total` que devuelva el monto con IVA incluido.
# - Un método de clase `cambiar_tasa_iva` que permita modificar el valor del IVA.
# - Un método estático `formatear_monto` que reciba un monto y lo devuelva formateado con dos decimales y el símbolo de moneda.

# Crea facturas, cambia la tasa de IVA y prueba los métodos.

class Factura:
    tasa_iva = 0.21

    def __init__(self, numero_factura, monto):
        self.numero_factura = numero_factura
        self.monto = monto
        
    def calcular_total(self):
        '''Devuelve el monto con IVA incluido'''
        total = self.monto*Factura.tasa_iva+self.monto   # 20 + (20*0.21)
        return total
    
    @classmethod
    def cambiar_tasa_iva(cls, nueva_tasa):
        '''Modifica el valor del IVA'''
        cls.tasa_iva = nueva_tasa

    @staticmethod
    def formatear_monto(monto):
        '''Recibe un monto y lo devuelve formateado con dos decimales y el símbolo de moneda'''
        return f'El monto total es {monto:.2f}€'
    

factura1 = Factura(1, 500)
factura2 = Factura(1, 500)
factura3 = Factura(1, 500)

print(factura1.calcular_total())