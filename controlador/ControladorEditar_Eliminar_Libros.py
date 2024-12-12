import shutil
import os
from PyQt6 import QtWidgets, QtGui
from vista.VentanaEditar_Eliminar_Libros import Ui_form_editar_libros
from modelo import Archivo, Validar
from controlador.ControladorErrores import ControladorErrores


class ControladorEditarLibros(QtWidgets.QMainWindow, Ui_form_editar_libros):
    def __init__(self, parent=None):
        super(ControladorEditarLibros, self).__init__(parent)
        self.setupUi(self)
        self.btn_buscar.clicked.connect(self.buscar_libro)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.btn_eliminar.clicked.connect(self.eliminar_libro)
        self.btn_editar.clicked.connect(self.editar_libro)
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_elegir_ruta.clicked.connect(self.obtener_ruta)
        self.estadoEliminar = False
        self.estadoEditar = False
        self.ruta = ""
        self.controladorError =ControladorErrores()
    def buscar_libro(self):
        self.biblioteca = Archivo.recuperar("libros.dat")
        libro = self.biblioteca.obtener_libro_ISBN(self.txt_ISBN.text())
        if libro == None:
            pass
        else:
            self.txt_titulo.setEnabled(False)
            self.txt_titulo.setText(libro.titulo)
            self.txtCantidad.setText(str(libro.cantidad))
            self.txt_precio_venta.setText(str(libro.precio_de_venta))
            self.txt_precio_compra.setText(str(libro.precio_de_compra))
            self.lbl_imagen_libro.setPixmap(QtGui.QPixmap(libro.ruta_imagen))
            self.btn_editar.setEnabled(True)
            self.btn_eliminar.setEnabled(True)
            self.btn_cancelar.setEnabled(True)
            self.ruta = libro.ruta_imagen

    def eliminar_libro(self):
        self.btn_buscar.setEnabled(False)
        self.txt_ISBN.setEnabled(False)
        self.btn_aceptar.setEnabled(True)
        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)
        self.estadoEliminar = True

    def editar_libro(self):
        self.btn_buscar.setEnabled(False)
        self.txt_ISBN.setEnabled(False)
        self.txt_titulo.setEnabled(True)
        self.txtCantidad.setEnabled(True)
        self.txt_precio_venta.setEnabled(True)
        self.txt_precio_compra.setEnabled(True)
        self.btn_aceptar.setEnabled(True)
        self.btn_editar.setEnabled(False)
        self.btn_elegir_ruta.setEnabled(True)
        self.estadoEditar = True

    def aceptar(self):
        if self.estadoEditar:
            if Validar.validar("ISBN")(self.txt_ISBN.text()) and Validar.validar("cantidad")(self.txtCantidad.text()) \
                    and Validar.validar("cantidad")(self.txt_precio_venta.text()) and Validar.validar("cantidad")(self.txt_precio_compra.text()) \
                    and len(self.txt_titulo.text()) > 0:

                self.biblioteca.editar_libro(self.txt_ISBN.text(), self.ruta,
                                             self.txt_titulo.text(), int(self.txt_precio_compra.text()),
                                             int(self.txt_precio_venta.text()), int(self.txtCantidad.text()))
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


        if self.estadoEliminar:
            """Primero se elimina la imagen y luego el libro, para eso utilizamos la ruta de la imagen """
            os.remove(self.biblioteca.obtener_libro_ISBN(self.txt_ISBN.text()).ruta_imagen)
            self.biblioteca.eliminar_libro(self.txt_ISBN.text())

        Archivo.guardar("libros.dat", self.biblioteca)

        self.limpiar_campos()

        self.txt_ISBN.setEnabled(True)
        self.txt_titulo.setEnabled(True)
        self.btn_buscar.setEnabled(True)
        self.btn_aceptar.setEnabled(False)
        self.btn_cancelar.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.txtCantidad.setEnabled(False)
        self.txt_precio_compra.setEnabled(False)
        self.txt_precio_venta.setEnabled(False)
        self.btn_elegir_ruta.setEnabled(False)
        self.estadoEliminar = self.estadoEditar = False

    def cancelar(self):
        self.txt_ISBN.setEnabled(True)
        self.btn_cancelar.setEnabled(False)
        self.btn_buscar.setEnabled(True)
        self.btn_aceptar.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.txtCantidad.setEnabled(False)
        self.txt_precio_compra.setEnabled(False)
        self.txt_precio_venta.setEnabled(False)
        self.limpiar_campos()
        self.estadoEliminar = self.estadoEditar = False

    def limpiar_campos(self):
        self.txtCantidad.clear()
        self.txt_precio_compra.clear()
        self.txt_precio_venta.clear()
        self.txt_titulo.clear()
        self.txt_ISBN.clear()
        self.lbl_imagen_libro.setPixmap(QtGui.QPixmap("imagenes_iconos/21735"))

    def obtener_ruta(self):
        if self.txt_ISBN.text() != "":
            ruta_origen, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Seleccionar imagen', '', 'Imágenes (*.jpg *.png)')
            ruta_destino = "imagenes_libros/"+self.txt_ISBN.text()+".png"
            shutil.copy(ruta_origen, ruta_destino)
            self.ruta = ruta_destino

        self.lbl_imagen_libro.setPixmap(QtGui.QPixmap(self.ruta))
