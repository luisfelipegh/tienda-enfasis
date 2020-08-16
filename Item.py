class Item:
    cantidad = ""
    producto = []

    def __init__(self,cantidad,producto):
        self.cantidad = cantidad
        self.producto = producto
        
    def calcular_total(self):
        
        #agregar los condicionales o refactorizacion 
        
        return self.producto.precio * self.cantidad