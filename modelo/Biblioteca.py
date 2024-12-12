from modelo.Libro import Libro
class Biblioteca:
    def __init__(self):
        self.lista_de_libros = []

    def agregar_libro(self, atributos_libro):
        self.lista_de_libros.append(Libro(atributos_libro[0],
                                          atributos_libro[1],
                                          atributos_libro[2],
                                          atributos_libro[3],
                                          atributos_libro[4],
                                          atributos_libro[5]))

    def obtener_libro(self, indice):
        return self.lista_de_libros[indice]

    def actualizar_cantidad_ventas_libro(self, ISBN, cantidad):
        self.obtener_libro_ISBN(ISBN).cantidad_de_ventas = \
            self.obtener_libro_ISBN(ISBN).cantidad_de_ventas + cantidad

    def actualizar_transacciones_abastecimiento(self, ISBN):
        self.obtener_libro_ISBN(ISBN).transacciones_abastecimiento = \
            self.obtener_libro_ISBN(ISBN).transacciones_abastecimiento + 1

    def eliminar_libro(self, ISBN):
        """Obtiene el índice de un libro previamente buscado por si ISBN y lo elimina de la lista"""
        self.lista_de_libros.pop(self.lista_de_libros.index(self.obtener_libro_ISBN(ISBN)))

    def editar_libro(self, ISBN, ruta, titulo, precio_compra, precio_venta, cantidad):
        self.lista_de_libros[self.lista_de_libros.index(self.obtener_libro_ISBN(ISBN))] = Libro(ISBN, titulo, ruta, precio_compra, precio_venta, cantidad)

    def obtener_libro_ISBN(self, ISBN):
        """Obtenemos una lista de los ISBN de los libros,
        filtramos para el valor de nuestro ISBN y enviamos el único elemento de nuestra lista"""
        if ISBN in list(map(lambda n: n.ISBN, self.lista_de_libros)):
            return list(filter(lambda n: n.ISBN == ISBN, self.lista_de_libros))[0]
        else:
            return None

    def obtener_libro_titulo(self, titulo):
        """Obtiene una lista de todos los libros con el mismo título, en este caso regresa el primero"""
        if titulo in list(map(lambda n: n.titulo, self.lista_de_libros)):
            return list(filter(lambda n: n.titulo == titulo, self.lista_de_libros))[0]
        else:
            return None

    def obtener_libro_mas_vendido(self):
        return self.obtener_libro(list(map(lambda n: n.cantidad_de_ventas,
                                           self.lista_de_libros)).index(max(list(map(lambda n: n.cantidad_de_ventas,
                                                                                     self.lista_de_libros)))))

    def obtener_libro_mas_costoso(self):
        """Obtenemos una lista con los precios de los libros, vemos cual es el más alto y obtenemos su posición """
        return self.obtener_libro(list(map(lambda n: n.precio_de_venta,
                 self.lista_de_libros)).index(max(list(map(lambda n: n.precio_de_venta,
                                                           self.lista_de_libros)))))

    def obtener_libro_menos_costoso(self):
        return self.obtener_libro(list(map(lambda n: n.precio_de_venta,
                                           self.lista_de_libros)).index(min(list(map(lambda n: n.precio_de_venta,
                                                                                     self.lista_de_libros)))))

    def actualizar_biblioteca(self, ISBN, cantidad, tipo_transaccion):
        if tipo_transaccion == "Abastecimiento":
            self.obtener_libro_ISBN(ISBN).cantidad = self.obtener_libro_ISBN(ISBN).cantidad + cantidad
            self.actualizar_transacciones_abastecimiento(ISBN)
        elif tipo_transaccion == "Venta":
            self.obtener_libro_ISBN(ISBN).cantidad = self.obtener_libro_ISBN(ISBN).cantidad - cantidad
            self.actualizar_cantidad_ventas_libro(ISBN, cantidad)

