class Item:
    cantidad = ""
    producto = []

    def __init__(self,producto,cantidad):
        self.cantidad = cantidad
        self.producto = producto
        
    def calcular_total(self):
        #agregar los condicionales o refactorizacion 
        return self.producto.get_precio() * self.cantidad