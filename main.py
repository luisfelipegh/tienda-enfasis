from Tienda import Tienda
from Producto import Producto
from Cliente import Cliente

def main():
    
    tienda = Tienda()
    producto1 = Producto('1', 'berenjena', 'a orozco le encanta', 20, 1000)
    producto2 = Producto('1', 'banano', 'tambien a orozco le encanta', 10, 300)

    cliente_1 = Cliente('Luis Felipe')
    cliente_2 = Cliente('Andres Orozco')
    cliente_3 = Cliente('Sebastian Moncada')
    
    tienda.agregar_producto_a_carrito(producto1,5,cliente_1)
    tienda.agregar_producto_a_carrito(producto2,3,cliente_1)
    
    
    tienda.agregar_producto_a_carrito(producto1,2,cliente_2)
    tienda.agregar_producto_a_carrito(producto2,4,cliente_2)
    
    tienda.agregar_producto_a_carrito(producto1,7,cliente_3)
    tienda.agregar_producto_a_carrito(producto2,10,cliente_3)
    
    #5900
    print('Precio Final del Carrito de ',cliente_1.nombre,' es ' ,cliente_1.carritoDeCompras.calcular_total())
    #3200
    print('Precio Final del Carrito de ',cliente_2.nombre,' es ' ,cliente_2.carritoDeCompras.calcular_total())
    #10000 
    print('Precio Final del Carrito de ',cliente_3.nombre,' es ' ,cliente_3.carritoDeCompras.calcular_total())

    
if __name__=="__main__": 
    main()