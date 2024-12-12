import sys
from PyQt6 import QtCore, QtWidgets
from controlador.ControladorPricipal import ControladorVistaPrincipal

app = QtWidgets.QApplication(sys.argv)
miVentanaPrincipal = ControladorVistaPrincipal
myApp = ControladorVistaPrincipal()
myApp.show()
app.exec()