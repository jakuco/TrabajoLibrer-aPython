# Form implementation generated from reading ui file 'VentanaInsertarCaja.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 166)
        self.lbl_ingresar_caja = QtWidgets.QLabel(Form)
        self.lbl_ingresar_caja.setGeometry(QtCore.QRect(50, 50, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ingresar_caja.setFont(font)
        self.lbl_ingresar_caja.setObjectName("lbl_ingresar_caja")
        self.btn_aceptar = QtWidgets.QPushButton(Form)
        self.btn_aceptar.setGeometry(QtCore.QRect(180, 90, 75, 23))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.txt_ingresar_caja = QtWidgets.QLineEdit(Form)
        self.txt_ingresar_caja.setGeometry(QtCore.QRect(270, 50, 61, 20))
        self.txt_ingresar_caja.setObjectName("txt_ingresar_caja")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_ingresar_caja.setText(_translate("Form", "Ingrese el valor de la caja:"))
        self.btn_aceptar.setText(_translate("Form", "Aceptar"))
        self.txt_ingresar_caja.setText(_translate("Form", "1000000"))