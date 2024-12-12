from PyQt6 import QtWidgets
from vista.VentanaDeErrores import Ui_Form


class ControladorErrores(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(ControladorErrores, self).__init__(parent)
        self.setupUi(self)
        self.btn_aceptar.clicked.connect(self.aceptar)

    def aceptar(self):
        self.close()