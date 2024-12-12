from PyQt6 import QtCore, QtWidgets, QtGui
from vista.VentanaInsertarCaja import Ui_Form
from modelo import Validar
from controlador.ControladorErrores import ControladorErrores

class ControladorIngresarCaja(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(ControladorIngresarCaja, self).__init__(parent)
        self.setupUi(self)
        self.caja = 0
        self.btn_aceptar.clicked.connect(self.aceptar)

    def aceptar(self):
        if Validar.validar("cantidad")(self.txt_ingresar_caja.text()):
            self.caja = float(self.txt_ingresar_caja.text())
        else:
            self.controladorError = ControladorErrores()
            self.controladorError.lbl_error.setText("Error: cantidad mal imgresada")

        self.close()