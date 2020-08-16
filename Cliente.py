import CarritoDeCompra

class Cliente:
    nombre = ""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.carritoDeCompra = CarritoDeCompra()
        
    
    def agregar_producto_a_carrito(self,producto,cantidad):
        self.carritoDeCompra.agregar_item(producto,cantidad)