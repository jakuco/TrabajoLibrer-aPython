from PyQt6 import QtWidgets
from vista.VentanaBuscarEntidad import Ui_form_buscar_entidad
from modelo import Archivo

class ControladorBuscarEntidad(QtWidgets.QMainWindow, Ui_form_buscar_entidad):
    def __init__(self, parent=None):
        super(ControladorBuscarEntidad, self).__init__(parent)
        self.CI_RUC = ""
        self.nombre = ""

        self.setupUi(self)
        self.btn_buscar.clicked.connect(self.buscar_entidad)
        self.btn_aceptar.clicked.connect(self.aceptar_entidad)
        self.btn_cancelar.clicked.connect(self.cancelar)

    def buscar_entidad(self):
        entidades = Archivo.recuperar("entidades.dat")
        entidad = entidades.obtener_entidad_por_codigo(self.txt_CI_RUC.text())
        if entidad == None:
            pass
        else:
            self.txt_CI_RUC.setEnabled(False)
            self.txt_nombre.setText(entidad.nombre)

            self.btn_cancelar.setEnabled(True)
            self.btn_aceptar.setEnabled(True)

    def aceptar_entidad(self):
        self.nombre = self.txt_nombre.text()
        self.CI_RUC = self.txt_CI_RUC.text()

        self.limpiar_campos()
        self.close()

    def cancelar(self):
        self.limpiar_campos()
        self.close()

    def limpiar_campos(self):
        self.txt_CI_RUC.clear()
        self.txt_nombre.clear()

        self.btn_cancelar.setEnabled(False)
        self.btn_aceptar.setEnabled(False)
