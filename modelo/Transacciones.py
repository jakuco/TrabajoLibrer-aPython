from modelo.Transaccion import Transaccion
class Transacciones:
    def __init__(self):
        self.lista_transacciones = []

    def agregar_transaccion(self, transaccion):
        self.lista_transacciones.append(transaccion)

    def obtener_transaccion(self, indice):
        return self.lista_transacciones[indice]

    def obtener_Abastecimientos_Ventas(self, tipo_de_transaccion):
        return list(map(lambda n: type(n) == tipo_de_transaccion, self.lista_transacciones))

    def agregar_factura(self, codigo_entidad, nombre_entidad, forma_de_pago, IVA, lista_de_lista_de_atributos_detalles, tipo_transaccion):

        self.agregar_transaccion(Transaccion(len(self.lista_transacciones), codigo_entidad, nombre_entidad, forma_de_pago, IVA, lista_de_lista_de_atributos_detalles, tipo_transaccion))
