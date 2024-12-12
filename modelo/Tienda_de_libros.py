#from Transacciones import Transacciones
from modelo.Entidades import Entidades
from modelo.Biblioteca import Biblioteca
from modelo.Transacciones import Transacciones

class Tienda_de_libros:
    def __init__(self, caja):
        self.caja = caja
        self.transacciones = Transacciones()
        self.entidades = Entidades()
        self.biblioteca = Biblioteca()
        self.nroFacturas = 0

    def obtener_clientes_proveedores(self, tipo_transaccion): # Me devuelve una lista de clientes o proveedores,
                                                              # según el tipo de transacción que ingrese
        """ Filtramos de la lista de entidades las entidades del tipo que queremos 'Abastecimiento' o 'Venta',
            después mapeamos para obtener el atributo de 'factura' de 'Transacción',
            repetimos el proceso con 'codigo_entidad' que se encuentra dentro de 'factura' aplicamos set eliminar repeticiones,
            finalizamos mapeando 'codigo_entidad' con la función 'obtener_entidad_por_codigo' que nos devuelve la entidad a la que corresponde un código"""

        return list(map(self.entidades.obtener_entidad_por_codigo,
                        list(set(list(map(lambda n: n.codigo_entidad,
                                          list(map(lambda n: n.factura,
                                                   list(filter(type(tipo_transaccion),
                                                               self.transacciones.lista_transacciones))))))))))

    def facturar(self, codigo_entidad, forma_de_pago, IVA, lista_de_lista_de_atributos_detalles, tipo_transaccion):
        self.transacciones.agregar_factura(codigo_entidad, forma_de_pago, IVA, lista_de_lista_de_atributos_detalles, tipo_transaccion)


    def obtener_libro_mas_vendido(self):
        # Me regresa el libro y si código
        #list(map(lambda n:if n.cantidad_libros, list(map(lambda n: n.lista_de_detalles, list(map(lambda n: n.factura, list(filter(type("Venta"), self.transacciones.lista_transacciones))))))))
        #lista_codigos_de_libros_con_cantidad_libros = list(map(lambda n:[n.codigo_libro, n.cantidad_libros], list(map(lambda n: n.lista_de_detalles, list(map(lambda n: n.factura, list(filter(type("Venta"), self.transacciones.lista_transacciones))))))))

        lista_definitiva = {}
        #for lista in lista_codigos_de_libros_con_cantidad_libros:
            #if lista.codigo_libro in lista_definitiva.keys():
            #    lista_definitiva.
        #    pass
        print("Si entra en el libro más vendido *************+")
        #list(filter(type("Venta"), self.transacciones.lista_transacciones))
        print(list(filter(lambda n: n.tipo_de_transaccion == "Venta", self.transacciones.lista_transacciones)))
        print(list(map(lambda n: n.factura, list(filter(lambda n: n.tipo_de_transaccion == "Venta", self.transacciones.lista_transacciones)))))

        """Lista de lista de detalles"""
        print(list(map(lambda n: n.lista_de_detalles, list(map(lambda n: n.factura, list(filter(lambda n: n.tipo_de_transaccion == "Venta", self.transacciones.lista_transacciones)))))))
        lista_de_lista_detalles = list(map(lambda n: n.lista_de_detalles, list(map(lambda n: n.factura, list(filter(lambda n: n.tipo_de_transaccion == "Venta", self.transacciones.lista_transacciones))))))

        lista_de_todos_los_detalles = [lista_de_lista_detalles[i][j] for i in range(len(lista_de_lista_detalles)) for j in range(len(lista_de_lista_detalles[i]))]

        for i in range(len(lista_de_todos_los_detalles)):
            print(lista_de_todos_los_detalles[i].cantidad_libros, lista_de_todos_los_detalles[i].nombre_libro)

        lista_de_codigos = list(set([lista_de_todos_los_detalles[i].codigo_libro for i in range(len(lista_de_todos_los_detalles))]))

        print(lista_de_codigos)
        """"""
        print("Salí del 'Obtener libro mas vendido'")
        return list(map(lambda n: [n.codigo_libro, n.cantidad_libros], list(map(lambda n: n.lista_de_detalles, list(map(lambda n: n.factura, list(filter(lambda n: n.tipo_de_transaccion == "Venta", self.transacciones.lista_transacciones))))))))