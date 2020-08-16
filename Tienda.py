class Tienda:
    acumulado = ""

    def __init__(self, acumulador):
        self.acumulador = acumulador
    
    def agregar_producto_a_carrito(self, producto, cantidad, cliente):
        print('Producto', self.producto , ' agregado con ', self.cantidad, 'por el cliente ', self.cliente)
                        