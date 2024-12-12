
from PyQt6 import QtWidgets

from vista.VentanaInsertarEntidad import Ui_Form
from modelo.Entidades import Entidades
from modelo import Archivo, Validar
from controlador.ControladorErrores import ControladorErrores

class ControladorVistaInsertarEntidad(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(ControladorVistaInsertarEntidad, self).__init__(parent)
        self.setupUi(self)
        self.btn_ingresar.clicked.connect(self.ingresar)
        self.btn_cancelar.clicked.connect(self.close)
        self.controladorErrores = ControladorErrores()

    def ingresar(self):
        if (Validar.validar("RUC")(self.txt_CI_RUC.text()) or Validar.validar("cedula")(self.txt_CI_RUC.text())):
            entidades = Archivo.recuperar("entidades.dat")
            if entidades != None:
                self.agregar_entidad(entidades)

            else:
                entidades = Entidades()
                self.agregar_entidad(entidades)

            if entidades != None:
                Archivo.guardar("entidades.dat", entidades)

            self.borrar_campos()
        elif ((Validar.validar("RUC")(self.txt_CI_RUC.text()) or Validar.validar("cedula")(self.txt_CI_RUC.text()))) == False:
            self.controladorErrores.lbl_error.setText("Error: RUC o CI mal ingresado")
            self.controladorErrores.show()

    def cancelar(self):
        self.close()

    def borrar_campos(self):
        self.txt_nombre.clear()
        self.txt_CI_RUC.clear()
        self.txt_correo.clear()
        self.txt_telefono.clear()
        self.txt_direccion.clear()

    def agregar_entidad(self, entidades):
        entidades.agregar_entidad([self.txt_nombre.text(), self.txt_direccion.text(), self.txt_telefono.text(),
                                   self.txt_correo.text(), self.txt_CI_RUC.text()])
