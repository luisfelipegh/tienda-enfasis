import Item

class CarritoDeCompra:
    items = []

    def agregar_item(self, producto, cantidad):
        self.items.append(Item(producto,cantidad))

    def calcular_total(self):
        total = 0
        
        for item in self.items:
           total += item.calcular_total()
    
        return total
