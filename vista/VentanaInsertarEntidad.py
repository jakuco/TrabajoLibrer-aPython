# Form implementation generated from reading ui file 'VentanaInsertarEntidad.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(477, 398)
        self.btn_cancelar = QtWidgets.QPushButton(Form)
        self.btn_cancelar.setGeometry(QtCore.QRect(280, 310, 75, 23))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.lbl_correo = QtWidgets.QLabel(Form)
        self.lbl_correo.setGeometry(QtCore.QRect(80, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_correo.setFont(font)
        self.lbl_correo.setObjectName("lbl_correo")
        self.txt_telefono = QtWidgets.QLineEdit(Form)
        self.txt_telefono.setGeometry(QtCore.QRect(180, 130, 240, 20))
        self.txt_telefono.setText("")
        self.txt_telefono.setObjectName("txt_telefono")
        self.btn_ingresar = QtWidgets.QPushButton(Form)
        self.btn_ingresar.setGeometry(QtCore.QRect(150, 310, 75, 23))
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.txt_nombre = QtWidgets.QLineEdit(Form)
        self.txt_nombre.setGeometry(QtCore.QRect(179, 90, 240, 20))
        self.txt_nombre.setText("")
        self.txt_nombre.setObjectName("txt_nombre")
        self.lbl_nombre = QtWidgets.QLabel(Form)
        self.lbl_nombre.setGeometry(QtCore.QRect(80, 90, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_telefono = QtWidgets.QLabel(Form)
        self.lbl_telefono.setGeometry(QtCore.QRect(80, 130, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_telefono.setFont(font)
        self.lbl_telefono.setObjectName("lbl_telefono")
        self.txt_correo = QtWidgets.QLineEdit(Form)
        self.txt_correo.setGeometry(QtCore.QRect(180, 170, 240, 20))
        self.txt_correo.setText("")
        self.txt_correo.setObjectName("txt_correo")
        self.txt_CI_RUC = QtWidgets.QLineEdit(Form)
        self.txt_CI_RUC.setGeometry(QtCore.QRect(179, 50, 240, 20))
        self.txt_CI_RUC.setText("")
        self.txt_CI_RUC.setObjectName("txt_CI_RUC")
        self.lbl_CI_RUC = QtWidgets.QLabel(Form)
        self.lbl_CI_RUC.setGeometry(QtCore.QRect(80, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_CI_RUC.setFont(font)
        self.lbl_CI_RUC.setObjectName("lbl_CI_RUC")
        self.lbl_direccion = QtWidgets.QLabel(Form)
        self.lbl_direccion.setGeometry(QtCore.QRect(80, 230, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_direccion.setFont(font)
        self.lbl_direccion.setObjectName("lbl_direccion")
        self.txt_direccion = QtWidgets.QLineEdit(Form)
        self.txt_direccion.setGeometry(QtCore.QRect(180, 230, 240, 20))
        self.txt_direccion.setText("")
        self.txt_direccion.setObjectName("txt_direccion")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.lbl_correo.setText(_translate("Form", "Correo:"))
        self.btn_ingresar.setText(_translate("Form", "Ingresar"))
        self.lbl_nombre.setText(_translate("Form", "Nombre:"))
        self.lbl_telefono.setText(_translate("Form", "Teléfono:"))
        self.lbl_CI_RUC.setText(_translate("Form", "CI/RUC:"))
        self.lbl_direccion.setText(_translate("Form", "Dirección:"))
