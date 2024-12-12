from modelo import Archivo
from vista.VentanaMostrarTransacciones import Ui_form_mostrar_transacciones
from PyQt6 import QtWidgets


class ControladorMostrarTransacciones(QtWidgets.QMainWindow, Ui_form_mostrar_transacciones):
    def __init__(self, parent=None):
        super(ControladorMostrarTransacciones, self).__init__(parent)
        self.setupUi(self)
        self.jgd_tabla_transacciones.clicked.connect(self.mostrar_detalles_total_transaccion)

        """Recuperamos el archivo de transacciones"""
        self.transacciones = Archivo.recuperar("transacciones.dat")
        try:

            fila = 0
            self.jgd_tabla_transacciones.clearContents()
            self.jgd_tabla_transacciones.setRowCount(0)

            "Se ingresan cada uno de los atribitos de libros en la tabla"
            for transaccion in self.transacciones.lista_transacciones:

                self.jgd_tabla_transacciones.insertRow(fila)
                self.jgd_tabla_transacciones.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(transaccion.factura.fecha.year)))
                self.jgd_tabla_transacciones.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(transaccion.factura.fecha.month)))
                self.jgd_tabla_transacciones.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(transaccion.factura.fecha.day)))
                self.jgd_tabla_transacciones.setItem(fila, 3, QtWidgets.QTableWidgetItem(transaccion.factura.codigo_entidad))
                self.jgd_tabla_transacciones.setItem(fila, 4, QtWidgets.QTableWidgetItem(transaccion.factura.nombre_entidad))
                self.jgd_tabla_transacciones.setItem(fila, 5, QtWidgets.QTableWidgetItem(transaccion.factura.forma_de_pago))
                self.jgd_tabla_transacciones.setItem(fila, 6, QtWidgets.QTableWidgetItem(transaccion.tipo_de_transaccion))
                self.jgd_tabla_transacciones.setItem(fila, 7, QtWidgets.QTableWidgetItem(str(transaccion.factura.IVA)))

                self.jgd_tabla_transacciones.resizeColumnsToContents()
                fila += 1
                if fila == len(self.transacciones.lista_transacciones) + 1:
                    break
        except:
            pass

    def mostrar_detalles_total_transaccion(self):
        indice_transaccion = self.jgd_tabla_transacciones.currentRow()

        fila = 0
        self.jgd_tabla_detalles.clearContents()
        self.jgd_tabla_detalles.setRowCount(0)

        total = float(0)

        "Se ingresan cada uno de los atribitos de libros en la tabla"
        for detalle in self.transacciones.lista_transacciones[indice_transaccion].factura.lista_de_detalles:

            self.jgd_tabla_detalles.insertRow(fila)
            self.jgd_tabla_detalles.setItem(fila, 0, QtWidgets.QTableWidgetItem(detalle.codigo_libro))
            self.jgd_tabla_detalles.setItem(fila, 1, QtWidgets.QTableWidgetItem(detalle.nombre_libro))
            self.jgd_tabla_detalles.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(detalle.cantidad_libros)))
            self.jgd_tabla_detalles.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(detalle.precio_de_venta)))

            self.jgd_tabla_detalles.resizeColumnsToContents()

            """Se crea el total según se muestren los detalles"""
            total = float(total + detalle.precio_de_venta*detalle.cantidad_libros)

            fila += 1
            if fila == len(self.transacciones.lista_transacciones[indice_transaccion].factura.lista_de_detalles) + 1:
                break

        """Se muestra el total de la transacción"""
        self.txt_total.setText(str(total + total*self.transacciones.lista_transacciones[indice_transaccion].factura.IVA/100))