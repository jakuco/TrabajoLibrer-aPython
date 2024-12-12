from PyQt6 import QtWidgets
from vista.VentanaMostrarEntidades import Ui_Form
from modelo import Archivo
from controlador.ControladorEditar_Eliminar_Entidades import ControladorEditar_Eliminar_Entidades

class ControladorMostrarEntidades(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(ControladorMostrarEntidades, self).__init__(parent)
        self.setupUi(self)

        self.btn_editar.clicked.connect(self.editar)
        self.btn_eliminar.clicked.connect(self.eliminar)

        self.controladorEditar_Eliminar_Entidades = ControladorEditar_Eliminar_Entidades()
        self.controladorEditar_Eliminar_Entidades.btn_aceptar.clicked.connect(self.actualizar_lista)
        self.entidades = Archivo.recuperar("entidades.dat")

        try:
            self.mostrar_lista_entidades()
        except:
            pass

    def editar(self):
        if self.jgd_tabla_entidades.currentRow() != -1:
            self.controladorEditar_Eliminar_Entidades.txt_CI_RUC.setText(self.entidades.lista_de_entidades[self.jgd_tabla_entidades.currentRow()].codigo)

            self.controladorEditar_Eliminar_Entidades.btn_eliminar.setVisible(False)
            self.controladorEditar_Eliminar_Entidades.btn_editar.setVisible(False)
            self.controladorEditar_Eliminar_Entidades.btn_buscar.setVisible(False)
            self.controladorEditar_Eliminar_Entidades.btn_buscar.setEnabled(True)

            self.controladorEditar_Eliminar_Entidades.btn_buscar.click()
            self.controladorEditar_Eliminar_Entidades.btn_editar.click()

            self.controladorEditar_Eliminar_Entidades.show()

    def eliminar(self):
        self.controladorEditar_Eliminar_Entidades.txt_CI_RUC.setText(self.entidades.lista_de_entidades[self.jgd_tabla_entidades.currentRow()].codigo)

        self.controladorEditar_Eliminar_Entidades.txt_nombre.setEnabled(False)
        self.controladorEditar_Eliminar_Entidades.txt_correo.setEnabled(False)
        self.controladorEditar_Eliminar_Entidades.txt_telefono.setEnabled(False)
        self.controladorEditar_Eliminar_Entidades.txt_direccion.setEnabled(False)

        self.controladorEditar_Eliminar_Entidades.btn_eliminar.setVisible(False)
        self.controladorEditar_Eliminar_Entidades.btn_editar.setVisible(False)
        self.controladorEditar_Eliminar_Entidades.btn_buscar.setVisible(False)
        self.controladorEditar_Eliminar_Entidades.btn_buscar.setEnabled(True)

        self.controladorEditar_Eliminar_Entidades.btn_eliminar.click()
        self.controladorEditar_Eliminar_Entidades.btn_buscar.click()
        self.controladorEditar_Eliminar_Entidades.show()

    def mostrar_lista_entidades(self):
        fila = 0
        self.jgd_tabla_entidades.clearContents()
        self.jgd_tabla_entidades.setRowCount(0)

        "Se ingresan cada uno de los atribitos de libros en la tabla"
        for entidad in self.entidades.lista_de_entidades:
            self.jgd_tabla_entidades.insertRow(fila)
            self.jgd_tabla_entidades.setItem(fila, 0, QtWidgets.QTableWidgetItem(entidad.codigo))
            self.jgd_tabla_entidades.setItem(fila, 1, QtWidgets.QTableWidgetItem(entidad.nombre))
            self.jgd_tabla_entidades.setItem(fila, 2, QtWidgets.QTableWidgetItem(entidad.telefono))
            self.jgd_tabla_entidades.setItem(fila, 3, QtWidgets.QTableWidgetItem(entidad.correo))
            self.jgd_tabla_entidades.setItem(fila, 4, QtWidgets.QTableWidgetItem(entidad.direccion))

            fila += 1
            if fila == len(self.entidades.lista_de_entidades)+1:
                break

    def actualizar_lista(self):
        self.mostrar_lista_entidades()