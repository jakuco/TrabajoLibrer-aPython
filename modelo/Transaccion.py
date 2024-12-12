from modelo.Factura import Factura
class Transaccion:
    def __init__(self, id_factura, codigo_entidad, nombre_entidad,forma_de_pago, IVA, lista_de_lista_de_atributos_detalles, tipo_de_transaccion):
        self.factura = Factura(id_factura, codigo_entidad, nombre_entidad, forma_de_pago, IVA)
        self.tipo_de_transaccion = tipo_de_transaccion
        for detalles in lista_de_lista_de_atributos_detalles: self.factura.adicionar_detalles(detalles[0], detalles[1], detalles[2], detalles[3])
