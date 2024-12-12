from modelo.Transaccion import Transaccion


class Venta(Transaccion):
    def __init__(self, id_factura, codigo_entidad, forma_de_pago, IVA, lista_de_lista_de_atributos_detalles):
        Transaccion.__init__(self, id_factura, codigo_entidad, forma_de_pago, IVA, lista_de_lista_de_atributos_detalles)