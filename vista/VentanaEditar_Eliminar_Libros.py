# Form implementation generated from reading ui file 'VentanaEditar_Eliminar_Libros.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_form_editar_libros(object):
    def setupUi(self, form_editar_libros):
        form_editar_libros.setObjectName("form_editar_libros")
        form_editar_libros.resize(655, 378)
        self.txt_ISBN = QtWidgets.QLineEdit(form_editar_libros)
        self.txt_ISBN.setEnabled(True)
        self.txt_ISBN.setGeometry(QtCore.QRect(220, 50, 180, 20))
        self.txt_ISBN.setObjectName("txt_ISBN")
        self.lbl_precio_venta = QtWidgets.QLabel(form_editar_libros)
        self.lbl_precio_venta.setGeometry(QtCore.QRect(60, 170, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio_venta.setFont(font)
        self.lbl_precio_venta.setObjectName("lbl_precio_venta")
        self.btn_elegir_ruta = QtWidgets.QPushButton(form_editar_libros)
        self.btn_elegir_ruta.setEnabled(False)
        self.btn_elegir_ruta.setGeometry(QtCore.QRect(220, 250, 180, 23))
        self.btn_elegir_ruta.setObjectName("btn_elegir_ruta")
        self.lbl_precio_compra = QtWidgets.QLabel(form_editar_libros)
        self.lbl_precio_compra.setGeometry(QtCore.QRect(60, 130, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio_compra.setFont(font)
        self.lbl_precio_compra.setObjectName("lbl_precio_compra")
        self.txt_precio_compra = QtWidgets.QLineEdit(form_editar_libros)
        self.txt_precio_compra.setEnabled(False)
        self.txt_precio_compra.setGeometry(QtCore.QRect(220, 130, 180, 20))
        self.txt_precio_compra.setObjectName("txt_precio_compra")
        self.lbl_cantidad = QtWidgets.QLabel(form_editar_libros)
        self.lbl_cantidad.setGeometry(QtCore.QRect(60, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cantidad.setFont(font)
        self.lbl_cantidad.setObjectName("lbl_cantidad")
        self.txt_titulo = QtWidgets.QLineEdit(form_editar_libros)
        self.txt_titulo.setEnabled(True)
        self.txt_titulo.setGeometry(QtCore.QRect(220, 90, 180, 20))
        self.txt_titulo.setObjectName("txt_titulo")
        self.btn_cancelar = QtWidgets.QPushButton(form_editar_libros)
        self.btn_cancelar.setEnabled(False)
        self.btn_cancelar.setGeometry(QtCore.QRect(480, 320, 75, 23))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.lbl_portada = QtWidgets.QLabel(form_editar_libros)
        self.lbl_portada.setGeometry(QtCore.QRect(60, 250, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_portada.setFont(font)
        self.lbl_portada.setObjectName("lbl_portada")
        self.txt_precio_venta = QtWidgets.QLineEdit(form_editar_libros)
        self.txt_precio_venta.setEnabled(False)
        self.txt_precio_venta.setGeometry(QtCore.QRect(220, 170, 180, 20))
        self.txt_precio_venta.setObjectName("txt_precio_venta")
        self.lbl_ISBN = QtWidgets.QLabel(form_editar_libros)
        self.lbl_ISBN.setGeometry(QtCore.QRect(60, 50, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ISBN.setFont(font)
        self.lbl_ISBN.setObjectName("lbl_ISBN")
        self.lbl_titulo = QtWidgets.QLabel(form_editar_libros)
        self.lbl_titulo.setGeometry(QtCore.QRect(60, 90, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.txtCantidad = QtWidgets.QLineEdit(form_editar_libros)
        self.txtCantidad.setEnabled(False)
        self.txtCantidad.setGeometry(QtCore.QRect(220, 210, 180, 20))
        self.txtCantidad.setObjectName("txtCantidad")
        self.btn_buscar = QtWidgets.QPushButton(form_editar_libros)
        self.btn_buscar.setGeometry(QtCore.QRect(40, 320, 75, 23))
        self.btn_buscar.setObjectName("btn_buscar")
        self.btn_editar = QtWidgets.QPushButton(form_editar_libros)
        self.btn_editar.setEnabled(False)
        self.btn_editar.setGeometry(QtCore.QRect(150, 320, 75, 23))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_aceptar = QtWidgets.QPushButton(form_editar_libros)
        self.btn_aceptar.setEnabled(False)
        self.btn_aceptar.setGeometry(QtCore.QRect(370, 320, 75, 23))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.lbl_imagen_libro = QtWidgets.QLabel(form_editar_libros)
        self.lbl_imagen_libro.setGeometry(QtCore.QRect(460, 60, 161, 191))
        self.lbl_imagen_libro.setText("")
        self.lbl_imagen_libro.setPixmap(QtGui.QPixmap("imagenes_iconos/21735.png"))
        self.lbl_imagen_libro.setScaledContents(True)
        self.lbl_imagen_libro.setObjectName("lbl_imagen_libro")
        self.btn_eliminar = QtWidgets.QPushButton(form_editar_libros)
        self.btn_eliminar.setEnabled(False)
        self.btn_eliminar.setGeometry(QtCore.QRect(260, 320, 75, 23))
        self.btn_eliminar.setObjectName("btn_eliminar")

        self.retranslateUi(form_editar_libros)
        QtCore.QMetaObject.connectSlotsByName(form_editar_libros)
        form_editar_libros.setTabOrder(self.txt_ISBN, self.txt_titulo)
        form_editar_libros.setTabOrder(self.txt_titulo, self.txt_precio_compra)
        form_editar_libros.setTabOrder(self.txt_precio_compra, self.txt_precio_venta)
        form_editar_libros.setTabOrder(self.txt_precio_venta, self.txtCantidad)
        form_editar_libros.setTabOrder(self.txtCantidad, self.btn_elegir_ruta)
        form_editar_libros.setTabOrder(self.btn_elegir_ruta, self.btn_buscar)
        form_editar_libros.setTabOrder(self.btn_buscar, self.btn_editar)
        form_editar_libros.setTabOrder(self.btn_editar, self.btn_aceptar)
        form_editar_libros.setTabOrder(self.btn_aceptar, self.btn_cancelar)

    def retranslateUi(self, form_editar_libros):
        _translate = QtCore.QCoreApplication.translate
        form_editar_libros.setWindowTitle(_translate("form_editar_libros", "Form"))
        self.lbl_precio_venta.setText(_translate("form_editar_libros", "Precio de venta:"))
        self.btn_elegir_ruta.setText(_translate("form_editar_libros", "Elegir ruta imagen"))
        self.lbl_precio_compra.setText(_translate("form_editar_libros", "Precio de compra:"))
        self.lbl_cantidad.setText(_translate("form_editar_libros", "Cantidad:"))
        self.btn_cancelar.setText(_translate("form_editar_libros", "Cancelar"))
        self.lbl_portada.setText(_translate("form_editar_libros", "Portada:"))
        self.lbl_ISBN.setText(_translate("form_editar_libros", "ISBN:"))
        self.lbl_titulo.setText(_translate("form_editar_libros", "Título:"))
        self.btn_buscar.setText(_translate("form_editar_libros", "Buscar"))
        self.btn_editar.setText(_translate("form_editar_libros", "Editar"))
        self.btn_aceptar.setText(_translate("form_editar_libros", "Aceptar"))
        self.btn_eliminar.setText(_translate("form_editar_libros", "Eliminar"))
