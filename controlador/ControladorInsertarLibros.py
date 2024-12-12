#import sys
import pickle
import shutil
from PyQt6 import QtWidgets

from vista.VentanaInsertarLibros import Ui_form_insertar_libro
from modelo.Biblioteca import Biblioteca
from modelo import Archivo, Validar
from controlador.ControladorErrores import ControladorErrores

class ControladorVistaInsertarLibros(QtWidgets.QMainWindow, Ui_form_insertar_libro):
    def __init__(self, parent=None):
        super(ControladorVistaInsertarLibros, self).__init__(parent)
        self.setupUi(self)
        self.ruta = ""
        self.btn_ingresar.clicked.connect(self.ingresar)
        self.btn_cancelar.clicked.connect(self.close)
        self.btn_elegir_ruta.clicked.connect(self.obtener_ruta)
        self.controladorError = ControladorErrores()

    def ingresar(self):
        if Validar.validar("ISBN")(self.txt_ISBN.text()) and Validar.validar("cantidad")(self.txtCantidad.text()) \
                and Validar.validar("cantidad")(self.txt_precio_venta.text()) and Validar.validar("cantidad")(self.txt_precio_compra.text()) \
                and len(self.txt_titulo.text()) > 0:

            if self.ruta != "":

                biblioteca = Archivo.recuperar("libros.dat")

                if biblioteca != None:
                    biblioteca.agregar_libro([self.txt_ISBN.text(), self.txt_titulo.text(),
                                              self.ruta, int(self.txt_precio_compra.text()),
                                              int(self.txt_precio_venta.text()), int(self.txtCantidad.text())])

                else:
                    biblioteca = Biblioteca()
                    biblioteca.agregar_libro([self.txt_ISBN.text(), self.txt_titulo.text(),
                                              self.ruta, int(self.txt_precio_compra.text()),
                                              int(self.txt_precio_venta.text()), int(self.txtCantidad.text())])

                if biblioteca != None:
                    Archivo.guardar("libros.dat", biblioteca)

                self.borrar_campos()
            else:
                self.controladorError.lbl_error.setText("Error: Imagen no seleccionada")
                self.controladorError.show()

        elif Validar.validar("ISBN")(self.txt_ISBN.text()) != True:
            self.controladorError.lbl_error.setText("Error: ISBN incorrecto")
            self.controladorError.show()

        elif Validar.validar("cantidad")(self.txtCantidad.text()) != True:
            self.controladorError.lbl_error.setText("Error: cantidad mal ingresada")
            self.controladorError.show()

        elif Validar.validar("cantidad")(self.txt_precio_venta.text()) != True:
            self.controladorError.lbl_error.setText("Error: precio venta mal ingresado")
            self.controladorError.show()

        elif Validar.validar("cantidad")(self.txt_precio_compra.text()) != True:
            self.controladorError.lbl_error.setText("Error: precio compra mal ingresado")
            self.controladorError.show()

        elif len(self.txt_titulo.text()) <= 0:
            self.controladorError.lbl_error.setText("Error: Debe ingresar un título")
            self.controladorError.show()

        self.ruta = ""

    def cancelar(self):
        self.close()

    def obtener_ruta(self):
        if self.txt_ISBN.text() != "":
            ruta_origen, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Seleccionar imagen', '', 'Imágenes (*.jpg *.png)')
            ruta_destino = "imagenes_libros/"+self.txt_ISBN.text()+".png"
            shutil.copy(ruta_origen, ruta_destino)
            self.ruta = ruta_destino

    def borrar_campos(self):
        self.txt_ISBN.clear()
        self.txt_titulo.clear()
        self.txt_precio_compra.clear()
        self.txt_precio_venta.clear()
        self.txtCantidad.clear()
