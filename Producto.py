class Producto:
    sku = ""
    nombre = ""
    descripcion = ""
    unidades_disponibles = ""
    precio = ""

    def __init__(self, sku, nombre, descripcion, unidades_disponibles, precio):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.unidades_disponibles = unidades_disponibles
        self.precio = precio
    
    def tiene_unidades_disponibles(self, cantidad):

        if cantidad > self.unidades_disponibles:
            return False

        return True

    def get_precio(self):
        return self.precio
