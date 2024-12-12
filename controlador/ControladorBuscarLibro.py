from PyQt6 import QtWidgets, QtGui
from vista.VentanaBuscarLibro import Ui_form_buscar_libro
from modelo import Archivo
from modelo import Validar
from controlador.ControladorErrores import ControladorErrores


class ControladorBuscarLibro(QtWidgets.QMainWindow, Ui_form_buscar_libro):
    def __init__(self, parent=None):
        super(ControladorBuscarLibro, self).__init__(parent)
        self.setupUi(self)

        self.ISBN_libro = ""
        self.nombre_libro = ""
        self.cantidad = 0
        self.precio_venta = 0
        self.precio_unitario = 0
        self.venta = False
        self.abastecimiento = False

        self.btn_buscar.clicked.connect(self.buscar_libro)
        self.btn_aceptar.clicked.connect(self.aceptar_libro)
        self.btn_cancelar.clicked.connect(self.cancelar)

        self.controladorErrores = ControladorErrores()

    def buscar_libro(self):

        biblioteca = Archivo.recuperar("libros.dat")
        libro = biblioteca.obtener_libro_ISBN(self.txt_ISBN.text())
        if libro == None:
            pass
        else:
            self.txt_titulo.setEnabled(False)
            self.txt_titulo.setText(libro.titulo)
            self.txt_precio_venta.setText(str(libro.precio_de_venta))
            self.txt_en_stock.setText(str(libro.cantidad))
            self.txt_precio_compra.setText(str(libro.precio_de_compra))
            self.lbl_icono_libro.setPixmap(QtGui.QPixmap(libro.ruta_imagen))
            self.btn_cancelar.setEnabled(True)
            self.btn_aceptar.setEnabled(True)

    def aceptar_libro(self):
        if Validar.validar("cantidad")(self.txtCantidad.text()):
            tipo_transaccion = "Abastecimiento" if self.abastecimiento == True else "Venta"
            if tipo_transaccion == "Venta" and Validar.transaccion(tipo_transaccion)(int(self.txtCantidad.text()), int(self.txt_en_stock.text())):

                self.ISBN_libro = self.txt_ISBN.text()
                self.nombre_libro = self.txt_titulo.text()
                self.cantidad = int(self.txtCantidad.text())
                self.precio_venta = int(self.txt_precio_venta.text())

            if tipo_transaccion == "Abastecimiento":

                self.ISBN_libro = self.txt_ISBN.text()
                self.nombre_libro = self.txt_titulo.text()
                self.cantidad = int(self.txtCantidad.text())
                self.precio_venta = int(self.txt_precio_compra.text())

            self.limpiar_campos()
            self.close()
        else:
            self.controladorErrores.lbl_error.setText("Error: Cantidad mal ingresada")
            self.controladorErrores.show()

    def cancelar(self):
        self.limpiar_campos()
        self.close()

    def limpiar_campos(self):
        self.txt_ISBN.clear()
        self.txt_titulo.clear()
        self.txt_precio_venta.clear()
        self.txtCantidad.clear()
        self.txt_precio_compra.clear()
        self.txt_en_stock.clear()

        self.lbl_icono_libro.setPixmap(QtGui.QPixmap("imagenes_iconos/21735"))

        self.btn_cancelar.setEnabled(False)
        self.btn_aceptar.setEnabled(False)

        self.abastecimiento = self.venta = False

