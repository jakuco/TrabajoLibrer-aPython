# Form implementation generated from reading ui file 'VentanaMostrarTransacciones.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_form_mostrar_transacciones(object):
    def setupUi(self, form_mostrar_transacciones):
        form_mostrar_transacciones.setObjectName("form_mostrar_transacciones")
        form_mostrar_transacciones.resize(727, 542)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_mostrar_transacciones.sizePolicy().hasHeightForWidth())
        form_mostrar_transacciones.setSizePolicy(sizePolicy)
        self.jgd_tabla_transacciones = QtWidgets.QTableWidget(form_mostrar_transacciones)
        self.jgd_tabla_transacciones.setGeometry(QtCore.QRect(30, 50, 671, 131))
        self.jgd_tabla_transacciones.setAutoFillBackground(False)
        self.jgd_tabla_transacciones.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.jgd_tabla_transacciones.setObjectName("jgd_tabla_transacciones")
        self.jgd_tabla_transacciones.setColumnCount(8)
        self.jgd_tabla_transacciones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_transacciones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_transacciones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_transacciones.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_transacciones.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_transacciones.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_transacciones.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_transacciones.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_transacciones.setHorizontalHeaderItem(7, item)
        self.jgd_tabla_detalles = QtWidgets.QTableWidget(form_mostrar_transacciones)
        self.jgd_tabla_detalles.setGeometry(QtCore.QRect(30, 220, 471, 271))
        self.jgd_tabla_detalles.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.jgd_tabla_detalles.setObjectName("jgd_tabla_detalles")
        self.jgd_tabla_detalles.setColumnCount(4)
        self.jgd_tabla_detalles.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_detalles.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_detalles.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_detalles.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jgd_tabla_detalles.setHorizontalHeaderItem(3, item)
        self.lbl_transacciones = QtWidgets.QLabel(form_mostrar_transacciones)
        self.lbl_transacciones.setGeometry(QtCore.QRect(30, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_transacciones.setFont(font)
        self.lbl_transacciones.setObjectName("lbl_transacciones")
        self.lbl_detalles_transaccion = QtWidgets.QLabel(form_mostrar_transacciones)
        self.lbl_detalles_transaccion.setGeometry(QtCore.QRect(30, 190, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_detalles_transaccion.setFont(font)
        self.lbl_detalles_transaccion.setObjectName("lbl_detalles_transaccion")
        self.lbl_Total = QtWidgets.QLabel(form_mostrar_transacciones)
        self.lbl_Total.setGeometry(QtCore.QRect(580, 280, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Total.setFont(font)
        self.lbl_Total.setObjectName("lbl_Total")
        self.lbl_error_4 = QtWidgets.QLabel(form_mostrar_transacciones)
        self.lbl_error_4.setGeometry(QtCore.QRect(460, 300, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_error_4.setFont(font)
        self.lbl_error_4.setText("")
        self.lbl_error_4.setObjectName("lbl_error_4")
        self.txt_total = QtWidgets.QLineEdit(form_mostrar_transacciones)
        self.txt_total.setEnabled(False)
        self.txt_total.setGeometry(QtCore.QRect(550, 320, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_total.setFont(font)
        self.txt_total.setObjectName("txt_total")

        self.retranslateUi(form_mostrar_transacciones)
        QtCore.QMetaObject.connectSlotsByName(form_mostrar_transacciones)

    def retranslateUi(self, form_mostrar_transacciones):
        _translate = QtCore.QCoreApplication.translate
        form_mostrar_transacciones.setWindowTitle(_translate("form_mostrar_transacciones", "Form"))
        item = self.jgd_tabla_transacciones.horizontalHeaderItem(0)
        item.setText(_translate("form_mostrar_transacciones", "Año"))
        item = self.jgd_tabla_transacciones.horizontalHeaderItem(1)
        item.setText(_translate("form_mostrar_transacciones", "mes"))
        item = self.jgd_tabla_transacciones.horizontalHeaderItem(2)
        item.setText(_translate("form_mostrar_transacciones", "día"))
        item = self.jgd_tabla_transacciones.horizontalHeaderItem(3)
        item.setText(_translate("form_mostrar_transacciones", "CI/RUC"))
        item = self.jgd_tabla_transacciones.horizontalHeaderItem(4)
        item.setText(_translate("form_mostrar_transacciones", "Nombre"))
        item = self.jgd_tabla_transacciones.horizontalHeaderItem(5)
        item.setText(_translate("form_mostrar_transacciones", "Forma de pago"))
        item = self.jgd_tabla_transacciones.horizontalHeaderItem(6)
        item.setText(_translate("form_mostrar_transacciones", "Tipo de transacción"))
        item = self.jgd_tabla_transacciones.horizontalHeaderItem(7)
        item.setText(_translate("form_mostrar_transacciones", "IVA"))
        item = self.jgd_tabla_detalles.horizontalHeaderItem(0)
        item.setText(_translate("form_mostrar_transacciones", "Codigo libro"))
        item = self.jgd_tabla_detalles.horizontalHeaderItem(1)
        item.setText(_translate("form_mostrar_transacciones", "Nombre libro"))
        item = self.jgd_tabla_detalles.horizontalHeaderItem(2)
        item.setText(_translate("form_mostrar_transacciones", "Cantidad"))
        item = self.jgd_tabla_detalles.horizontalHeaderItem(3)
        item.setText(_translate("form_mostrar_transacciones", "Precio de venta"))
        self.lbl_transacciones.setText(_translate("form_mostrar_transacciones", "Transacciones"))
        self.lbl_detalles_transaccion.setText(_translate("form_mostrar_transacciones", "Detalles de la transación"))
        self.lbl_Total.setText(_translate("form_mostrar_transacciones", "Total"))