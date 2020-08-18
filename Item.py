class Item:
    cantidad = ""
    producto = []

    def __init__(self,producto,cantidad):
        self.cantidad = cantidad
        self.producto = producto
        
    def calcular_total(self):
        
        if (self.producto.get_sku()[0:2].upper() == 'EA'):
            return self.producto.get_precio() * self.cantidad
        if (self.producto.get_sku()[0:2].upper() == 'WE'):
            return self.producto.get_precio() * self.cantidad
        if (self.producto.get_sku()[0:2].upper() == 'SP'):
            return self.producto.get_precio() * self.cantidad
        return 0