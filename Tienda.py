class Tienda:
    acumulador = 0
    productos = []
    clientes = []

    def __init__(self):
        self.acumulador = 0
    
    def agregar_producto_a_carrito(self, producto, cantidad, cliente):
        
        if(not producto.tiene_unidades_disponibles(cantidad)):
             raise Exception('No se pueden agregar las unidades, stock no disponible')
        cliente.agregar_producto_a_carrito(producto,cantidad)
        
        print('Producto', producto.nombre , ' agregado con ', cantidad, 'por el cliente ', cliente.nombre)
                                                                            