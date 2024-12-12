class Detalle_factura:
    def __init__(self, codigo_libro, nombre_libro, cantidad_libros, precio_de_venta):
        self.cantidad_libros = cantidad_libros
        self.codigo_libro = codigo_libro
        self.nombre_libro = nombre_libro
        self.precio_de_venta = precio_de_venta

    def calcular_costo_detalle(self):
        return float(self.precio_de_venta*self.cantidad_libros)
