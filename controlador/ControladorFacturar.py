from PyQt6 import QtWidgets

from vista.VentanaFacturar import Ui_form_facturar

from modelo.Transacciones import Transacciones
from modelo import Archivo
from modelo import Validar

from controlador.ControladorBuscarLibro import ControladorBuscarLibro
from controlador.ControladorBuscarEntidad import ControladorBuscarEntidad
from controlador.ControladorIngresarEntidades import ControladorVistaInsertarEntidad
from controlador.ControladorErrores import ControladorErrores

class ControladorFacturar(QtWidgets.QMainWindow, Ui_form_facturar):
    def __init__(self, parent=None):
        super(ControladorFacturar, self).__init__(parent)
        self.setupUi(self)

        self.btn_Ingresar_libro.clicked.connect(self.ingresar_libro)
        self.btn_buscar.clicked.connect(self.ingresar_entidad)
        self.btn_Facturar.clicked.connect(self.facturar)
        self.btn_anular_facturar.clicked.connect(self.anular_facturacion)
        self.btn_eliminar_detalle.clicked.connect(self.eliminar_detalle)

        self.jgd_tabla_detalles.clicked.connect(self.activar_boton)
        self.cbx_tipo_transaccion.activated.connect(self.elegir_tipo_transaccion)

        self.controladorBuscarLibro = ControladorBuscarLibro()
        self.controladorBuscarLibro.abastecimiento = True

        self.controladorBuscarEntidad = ControladorBuscarEntidad()
        self.controladorBuscarLibro.btn_aceptar.clicked.connect(self.actualizar_detalles)
        self.error = ControladorErrores()

        self.lista_detalles = []

    def ingresar_libro(self):
        self.controladorBuscarLibro.show()

    def ingresar_entidad(self):
        entidades = Archivo.recuperar("entidades.dat")
        entidad = entidades.obtener_entidad_por_codigo(self.txt_CI_RUC.text())

        if entidad == None:

            self.controladorIngresarEntidad = ControladorVistaInsertarEntidad()
            self.controladorIngresarEntidad.show()
        else:
            self.txt_nombre.setText(entidad.nombre)
        pass

    def actualizar_detalles(self):

        if self.controladorBuscarLibro.cantidad > 0 and self.controladorBuscarLibro.precio_venta > 0 \
                and self.controladorBuscarLibro.ISBN_libro != "" and self.controladorBuscarLibro.nombre_libro != ""\
                and (self.controladorBuscarLibro.ISBN_libro not in [self.jgd_tabla_detalles.item(i, 0).text() for i in range(self.jgd_tabla_detalles.rowCount())])\
                and Validar.validar("IVA")(self.txt_IVA.text()):

            fila = self.jgd_tabla_detalles.rowCount()

            self.jgd_tabla_detalles.insertRow(fila)
            self.jgd_tabla_detalles.setItem(fila, 0, QtWidgets.QTableWidgetItem(self.controladorBuscarLibro.ISBN_libro))
            self.jgd_tabla_detalles.setItem(fila, 1, QtWidgets.QTableWidgetItem(self.controladorBuscarLibro.nombre_libro))
            self.jgd_tabla_detalles.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(self.controladorBuscarLibro.cantidad)))
            self.jgd_tabla_detalles.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(self.controladorBuscarLibro.precio_venta)))
            self.jgd_tabla_detalles.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(self.controladorBuscarLibro.precio_venta * self.controladorBuscarLibro.cantidad)))


            self.lista_detalles.append([self.controladorBuscarLibro.ISBN_libro, self.controladorBuscarLibro.nombre_libro,
                                        self.controladorBuscarLibro.cantidad, self.controladorBuscarLibro.precio_venta])

            self.actualizar_subtotal_total()

            self.cbx_tipo_transaccion.setEnabled(False)
            self.txt_IVA.setEnabled(False)
        else:
            """Me dice cual es el error"""
            if self.controladorBuscarLibro.ISBN_libro in [self.jgd_tabla_detalles.item(i, 0).text() for i in range(self.jgd_tabla_detalles.rowCount())]:
                self.error.lbl_error.setText("Error: Libro ya ingreado")

            elif self.controladorBuscarLibro.cantidad <= 0:
                self.error.lbl_error.setText("Error: Cantidad mal ingresada")

            elif Validar.validar("IVA")(self.txt_IVA.text()) == False:
                self.error.lbl_error.setText("Error: IVA mal ingresado")

            else:
                self.error.lbl_error.setText("Error: Cantidad supera al stock")

            self.error.show()

    def facturar(self):
        if self.cbx_tipo_transaccion.currentText() == "Abastecimiento":
        #if self.controladorBuscarLibro.abastecimiento:
            #print("Es un Abastecimiento")
            tienda = Archivo.recuperar("tienda.dat")
            if Validar.transaccion("Abastecimiento")((float(self.txt_Total.text())), tienda.caja):
                #print("Abastecimineto válido****")
                #print("Total:" , self.txt_Total.text(), "|Caja:", tienda.caja)
                self.actualizar_transacciones_biblioteca()
            else:
                self.error.lbl_error.setText("Error: El total es mayor a la caja")
                self.error.show()

        elif self.cbx_tipo_transaccion.currentText() == "Venta":
            #print("Es una venta válida****")
            self.actualizar_transacciones_biblioteca()

        self.reiniciar_campos()

    def anular_facturacion(self):
        self.controladorBuscarLibro.abastecimiento = self.controladorBuscarLibro.venta = False
        self.reiniciar_campos()
        self.close()

    def activar_boton(self):
        self.btn_eliminar_detalle.setEnabled(True)

    def eliminar_detalle(self):
        fila = self.jgd_tabla_detalles.currentRow()
        self.jgd_tabla_detalles.removeRow(fila)
        self.lista_detalles.pop(fila)
        self.btn_eliminar_detalle.setEnabled(False)
        self.actualizar_subtotal_total()

    def actualizar_subtotal_total(self):
        self.txt_subtotal.setText(str(sum([int(self.jgd_tabla_detalles.item(i, 4).text()) for i in range(self.jgd_tabla_detalles.rowCount())])))
        self.txt_Total.setText(str((float(self.txt_subtotal.text())*(float(self.txt_IVA.text()))/100) + float(self.txt_subtotal.text())))
        pass

    def actualizar_transacciones_biblioteca(self):
        if self.txt_CI_RUC.text() != "" and len(self.lista_detalles) > 0:

            transacciones = Archivo.recuperar("transacciones.dat")
            if transacciones != None:
                print("CI/RUC:", self.txt_CI_RUC.text())
                transacciones.agregar_factura(self.txt_CI_RUC.text(), self.txt_nombre.text(),
                                              self.cbx_Efectivo.currentText(),
                                              float(self.txt_IVA.text()),
                                              self.lista_detalles,
                                              self.cbx_tipo_transaccion.currentText())
            else:
                transacciones = Transacciones()
                transacciones.agregar_factura(self.txt_CI_RUC.text(), self.txt_nombre.text(),
                                              self.cbx_Efectivo.currentText(),
                                              float(self.txt_IVA.text()), self.lista_detalles,
                                              self.cbx_tipo_transaccion.currentText())

            if transacciones != None:
                Archivo.guardar("transacciones.dat", transacciones)

                biblioteca = Archivo.recuperar("libros.dat")
                for n in range(self.jgd_tabla_detalles.rowCount()):
                    #self.jgd_tabla_detalles.item()
                    biblioteca.actualizar_biblioteca(self.jgd_tabla_detalles.item(n, 0).text(),
                                                     int(self.jgd_tabla_detalles.item(n, 2).text()),
                                                     self.cbx_tipo_transaccion.currentText())

                    #print((self.jgd_tabla_detalles.item(0, n).text()), int(self.jgd_tabla_detalles.item(n, 2).text()),self.cbx_tipo_transaccion.currentText())
                Archivo.guardar("libros.dat", biblioteca)

            """Modificamos el valor de la caja apartir deel tipo de transacción"""
            tienda = Archivo.recuperar("tienda.dat")

            if self.cbx_tipo_transaccion.currentText() == "Abastecimiento":
                tienda.caja = tienda.caja - float(self.txt_Total.text())
            elif self.cbx_tipo_transaccion.currentText() == "Venta":
                tienda.caja = tienda.caja + float(self.txt_Total.text())

            Archivo.guardar("tienda.dat", tienda)

            """Reiniciamos al tipo de transacción que se va a hacer"""
            self.controladorBuscarLibro.abastecimiento = self.controladorBuscarLibro.venta = False
            self.close()

        elif len(self.txt_CI_RUC.text()) <= 0:
            self.error.lbl_error.setText("Error: RUC/CI incorrecto")
            self.error.show()

        elif len(self.lista_detalles) <= 0:
            self.error.lbl_error.setText("Error: Lista de detalles vacía")
            self.error.show()

    def reiniciar_campos(self):
        #print("Si entra")
        self.cbx_tipo_transaccion.setEnabled(True)
        self.txt_IVA.setText("0")
        self.txt_IVA.setEnabled(True)
        self.jgd_tabla_detalles.clearContents()
        self.jgd_tabla_detalles.setRowCount(0)
        self.txt_CI_RUC.clear()
        self.txt_nombre.clear()
        self.txt_Total.clear()
        self.txt_subtotal.clear()
        self.lista_detalles = []

    def elegir_tipo_transaccion(self):
        print(self.cbx_tipo_transaccion.currentText())
        if self.cbx_tipo_transaccion.currentText() == "Abastecimiento":
            self.controladorBuscarLibro.abastecimiento = True
            self.controladorBuscarLibro.venta = False
        elif self.cbx_tipo_transaccion.currentText() == "Venta":
            self.controladorBuscarLibro.abastecimiento = False
            self.controladorBuscarLibro.venta = True

