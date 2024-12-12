import datetime
from modelo.Detalle_factura import Detalle_factura

class Factura:
    def __init__(self, id_factura, codigo_entidad, nombre_entidad,forma_de_pago, IVA):
        self.id_factura = id_factura
        self.codigo_entidad = codigo_entidad
        self.nombre_entidad = nombre_entidad
        self.forma_de_pago = forma_de_pago
        self.lista_de_detalles = []
        self.IVA = IVA
        self.fecha = datetime.datetime.now()

    def adicionar_detalles(self, cantidad, codigo_libro, nombre_libro, precio_de_venta_unitario):
        self.lista_de_detalles.append(Detalle_factura(cantidad, codigo_libro, nombre_libro, precio_de_venta_unitario))

    def eliminar_detalle(self, indice):
        self.lista_de_detalles.pop(indice)

    def obtener_detalle(self, indice):
        return self.lista_de_detalles[indice]

    def calcular_total_factura(self):
        total = 0
        for detalle in self.lista_de_detalles:
            total = total + detalle.calcular_costo_detalle()

        return (total*self.IVA)

