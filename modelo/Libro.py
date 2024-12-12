class Libro:
    def __init__(self, ISBN, titulo, ruta_imagen, precio_de_compra, precio_de_venta, cantidad):
        self.ISBN = ISBN
        self.titulo = titulo
        self.ruta_imagen = ruta_imagen
        self.precio_de_compra = precio_de_compra
        self.precio_de_venta = precio_de_venta
        self.cantidad = cantidad
        self.transacciones_abastecimiento = 0
        self.cantidad_de_ventas = 0