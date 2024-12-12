
from PyQt6 import QtWidgets
from vista.VentanaEditar_Eliminar_Entidades import Ui_Form
from modelo import Archivo, Validar
from controlador.ControladorErrores import ControladorErrores

class ControladorEditar_Eliminar_Entidades(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(ControladorEditar_Eliminar_Entidades, self).__init__(parent)
        self.setupUi(self)
        self.btn_buscar.clicked.connect(self.buscar_entidad)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.btn_eliminar.clicked.connect(self.eliminar_entidad)
        self.btn_editar.clicked.connect(self.editar_entidad)
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.estadoEliminar = self.estadoEditar = False
        self.ruta = ""

        self.controladorErrores = ControladorErrores()
    def buscar_entidad(self):

        self.entidades = Archivo.recuperar("entidades.dat")
        entidad = self.entidades.obtener_entidad_por_codigo(self.txt_CI_RUC.text())
        if entidad == None:
            pass
        else:
            self.txt_CI_RUC.setEnabled(False)
            self.txt_nombre.setText(entidad.nombre)
            self.txt_telefono.setText(entidad.telefono)
            self.txt_correo.setText(entidad.correo)
            self.txt_direccion.setText(entidad.direccion)
            self.habilitar_botones_editar_eliminar(True)

    def eliminar_entidad(self):
        self.txt_correo.setEnabled(False)
        self.txt_CI_RUC.setEnabled(False)

        self.habilitar_botones_editar_eliminar(False)
        self.habilitar_botones_aceptar_cancelar_deshabilitar_buscar(True)
        self.estadoEliminar = True

    def editar_entidad(self):
        self.txt_CI_RUC.setEnabled(False)
        self.txt_nombre.setEnabled(True)
        self.txt_telefono.setEnabled(True)
        self.txt_correo.setEnabled(True)
        self.txt_direccion.setEnabled(True)

        self.habilitar_botones_aceptar_cancelar_deshabilitar_buscar(True)
        self.habilitar_botones_editar_eliminar(False)
        self.estadoEditar = True

    def aceptar(self):

        if self.estadoEditar:
            if (Validar.validar("RUC")(self.txt_CI_RUC.text()) or Validar.validar("cedula")(self.txt_CI_RUC.text())) and \
                len(self.txt_correo.text()) > 0 and len(self.txt_nombre.text()) > 0 and len(self.txt_telefono.text()) and \
                len(self.txt_direccion.text()) > 0:
                self.entidades.editar_entidad([self.txt_nombre.text(), self.txt_direccion.text(),
                                          self.txt_telefono.text(), self.txt_correo.text(),
                                          self.txt_CI_RUC.text()])


            elif Validar.validar("RUC")(self.txt_CI_RUC.text()) == False:
                self.controladorErrores.lbl_error.setText("Error: RUC mal ingresado")

            elif Validar.validar("cedula")(self.txt_CI_RUC.text()) == False:
                self.controladorErrores.lbl_error.setText("Error: cedula mal ingresada")

            elif len(self.txt_correo.text()) <= 0:
                self.controladorErrores.lbl_error.setText("Error: Correo mal ingresado")

            elif len(self.txt_nombre.text()) <= 0:
                self.controladorErrores.lbl_error.setText("Error: Nombre mal ingresado")

            elif len(self.txt_telefono.text()) <= 0:
                self.controladorErrores.lbl_error.setText("Error: teléfono mal ingresado")

            elif len(self.txt_direccion.text()) <= 0:
                self.controladorErrores.lbl_error.setText("Error: dirección mal ingresado")

        if self.estadoEliminar:
            self.entidades.eliminar_entidad(self.txt_CI_RUC.text())

        Archivo.guardar("entidades.dat", self.entidades)
        self.reiniciar_campos()
        self.limpiar_campos()

        self.estadoEliminar = self.estadoEditar = False

    def cancelar(self):
        self.reiniciar_campos()
        self.limpiar_campos()
        self.estadoEliminar = self.estadoEditar = False

    def limpiar_campos(self):
        self.txt_CI_RUC.clear()
        self.txt_nombre.clear()
        self.txt_telefono.clear()
        self.txt_correo.clear()
        self.txt_direccion.clear()

    def reiniciar_campos(self):
        self.txt_CI_RUC.setEnabled(True)
        self.txt_correo.setEnabled(False)
        self.txt_nombre.setEnabled(False)
        self.txt_telefono.setEnabled(False)
        self.txt_direccion.setEnabled(False)
        self.habilitar_botones_aceptar_cancelar_deshabilitar_buscar(False)

    def habilitar_botones_aceptar_cancelar_deshabilitar_buscar(self, estado):
        self.btn_aceptar.setEnabled(estado)
        self.btn_cancelar.setEnabled(estado)
        if estado: self.btn_buscar.setEnabled(False)
        else: self.btn_buscar.setEnabled(True)

    def habilitar_botones_editar_eliminar(self, estado):
        self.btn_eliminar.setEnabled(estado)
        self.btn_editar.setEnabled(estado)
