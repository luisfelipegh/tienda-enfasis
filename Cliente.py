from CarritoDeCompras import CarritoDeCompras

class Cliente:
    nombre = ""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.carritoDeCompras = CarritoDeCompras()
        
    
    def agregar_producto_a_carrito(self,producto,cantidad):
        
        self.carritoDeCompras.agregar_item(producto,cantidad)