from modelo import Archivo
from PyQt6 import QtWidgets, QtGui
from vista.VentanaMostrarLibros import Ui_form_mostrar_libros
from controlador.ControladorEditar_Eliminar_Libros import ControladorEditarLibros


class ControladorMostrarLibros(QtWidgets.QMainWindow, Ui_form_mostrar_libros):
    def __init__(self, parent=None):
        super(ControladorMostrarLibros, self).__init__(parent)
        self.setupUi(self)
        self.jgd_tabla_libros.clicked.connect(self.mostrar)
        self.btn_editar.clicked.connect(self.editar)
        self.btn_eliminar.clicked.connect(self.eliminar)

        self.controladorEditar_Eliminar_Libros = ControladorEditarLibros()
        self.biblioteca = Archivo.recuperar("libros.dat")

        try:
            fila = 0
            self.jgd_tabla_libros.clearContents()
            self.jgd_tabla_libros.setRowCount(0)

            "Se ingresan cada uno de los atribitos de libros en la tabla"
            for libro in self.biblioteca.lista_de_libros:
                self.jgd_tabla_libros.insertRow(fila)
                self.jgd_tabla_libros.setItem(fila, 0, QtWidgets.QTableWidgetItem(libro.ISBN))
                self.jgd_tabla_libros.setItem(fila, 1, QtWidgets.QTableWidgetItem(libro.titulo))
                self.jgd_tabla_libros.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(libro.precio_de_compra)))
                self.jgd_tabla_libros.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(libro.precio_de_venta)))
                self.jgd_tabla_libros.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(libro.cantidad)))
                self.jgd_tabla_libros.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(libro.transacciones_abastecimiento)))

                fila += 1
                if fila == len(self.biblioteca.lista_de_libros)+1:
                    break

            self.jgd_tabla_libros.resizeColumnsToContents()
            self.txt_libro_barato.setText(self.biblioteca.obtener_libro_menos_costoso().ISBN+"  |   "+self.biblioteca.obtener_libro_menos_costoso().titulo)
            self.txt_libro_costoso.setText(self.biblioteca.obtener_libro_mas_costoso().ISBN+"   |   "+self.biblioteca.obtener_libro_mas_costoso().titulo)
            self.txt_libro_mas_vendido.setText(self.biblioteca.obtener_libro_mas_vendido().ISBN + "    |   "+ self.biblioteca.obtener_libro_mas_vendido().titulo)

        except:
            pass

    def mostrar(self):
        fila = self.jgd_tabla_libros.currentRow()
        try:
            """Se muestar la imagen según la ruta"""
            self.lbl_imagen_libro.setPixmap(QtGui.QPixmap(self.biblioteca.lista_de_libros[fila].ruta_imagen))
        except:
            pass

    def editar(self):
        if self.jgd_tabla_libros.currentRow() != -1:
            self.controladorEditar_Eliminar_Libros.txt_ISBN.setText(self.biblioteca.lista_de_libros[self.jgd_tabla_libros.currentRow()].ISBN)

            self.controladorEditar_Eliminar_Libros.btn_eliminar.setVisible(False)
            self.controladorEditar_Eliminar_Libros.btn_editar.setVisible(False)
            self.controladorEditar_Eliminar_Libros.btn_buscar.setVisible(False)
            self.controladorEditar_Eliminar_Libros.btn_buscar.setEnabled(True)

            self.controladorEditar_Eliminar_Libros.btn_buscar.click()
            self.controladorEditar_Eliminar_Libros.btn_editar.click()

            self.controladorEditar_Eliminar_Libros.show()

    def eliminar(self):
        if self.jgd_tabla_libros.currentRow() != -1:
            self.controladorEditar_Eliminar_Libros.txt_ISBN.setText(self.biblioteca.lista_de_libros[self.jgd_tabla_libros.currentRow()].ISBN)

            self.controladorEditar_Eliminar_Libros.txt_precio_compra.setEnabled(False)
            self.controladorEditar_Eliminar_Libros.txt_precio_venta.setEnabled(False)
            self.controladorEditar_Eliminar_Libros.txtCantidad.setEnabled(False)
            self.controladorEditar_Eliminar_Libros.btn_eliminar.setVisible(False)
            self.controladorEditar_Eliminar_Libros.btn_editar.setVisible(False)
            self.controladorEditar_Eliminar_Libros.btn_buscar.setVisible(False)
            self.controladorEditar_Eliminar_Libros.btn_elegir_ruta.setVisible(False)
            self.controladorEditar_Eliminar_Libros.btn_buscar.setEnabled(True)

            self.controladorEditar_Eliminar_Libros.btn_buscar.click()
            self.controladorEditar_Eliminar_Libros.btn_eliminar.click()
            self.controladorEditar_Eliminar_Libros.show()
