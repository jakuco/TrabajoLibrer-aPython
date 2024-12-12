import sys
from PyQt6 import QtCore, QtWidgets

from controlador.ControladorMostrarEntidades import ControladorMostrarEntidades
from vista.VentanaPrincipal import Ui_MainWindow
from controlador.ControladorInsertarLibros import ControladorVistaInsertarLibros
from controlador.ControladorMostrarLibros import ControladorMostrarLibros
from controlador.ControladorEditar_Eliminar_Libros import ControladorEditarLibros
from controlador.ControladorIngresarEntidades import ControladorVistaInsertarEntidad
from controlador.ControladorEditar_Eliminar_Entidades import ControladorEditar_Eliminar_Entidades
from controlador.ControladorFacturar import ControladorFacturar
from controlador.ControladorMostrarTransacciones import ControladorMostrarTransacciones
from controlador.ControladorIngresarCaja import ControladorIngresarCaja

from modelo import Archivo
from modelo.Tienda_de_libros import Tienda_de_libros

class ControladorVistaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ControladorVistaPrincipal, self).__init__(parent)
        #self.tienda_de_libros = Archivo.recuperar("tienda.dat")
        self.setupUi(self)

        self.controladorIngresarCaja = ControladorIngresarCaja()
        self.controladorFacturar = ControladorFacturar()

        self.actionInsertarLibro.triggered.connect(self.ingreso_Libro)
        self.actionMostrar_todos_mis_libros.triggered.connect(self.mostrar_Libros)
        self.actionEditarLibro.triggered.connect(self.editar_libro)
        self.actionEliminarLibro.triggered.connect(self.eliminar_libro)

        self.actionEliminarComprador_Vendedor.triggered.connect(self.eliminar_Entidad)
        self.actionEditar_Comprador_Vendedor.triggered.connect(self.editar_Entidad)
        self.actionInsertar_Comprador_Venderor.triggered.connect(self.ingreso_Entidad)
        self.actionMostar_Compradores_y_Vendedores.triggered.connect(self.mostrar_Entidades)

        self.actionFacturar.triggered.connect(self.facturar)
        self.actionTodas_las_facturas.triggered.connect(self.mostrar_transacciones)

        self.btn_ingresar_caja.clicked.connect(self.ingresarCaja)

        self.controladorIngresarCaja.btn_aceptar.clicked.connect(self.actualizarCaja)
        self.controladorFacturar.btn_Facturar.clicked.connect(self.editarCaja)

        if Archivo.recuperar("tienda.dat") != None:
            tienda_de_libros = Archivo.recuperar("tienda.dat")
            #self.tienda_de_libros.caja = self.controladorIngresarCaja.caj
            self.txt_caja.setText(str(tienda_de_libros.caja))
        else:
            tienda_de_libros = Tienda_de_libros(0)
            self.txt_caja.setText(str(tienda_de_libros.caja))

        #self.txt_caja.setText(str(self.tienda_de_libros.caja))

    def ingresarCaja(self):
        self.controladorIngresarCaja.show()

    def actualizarCaja(self):
        #try:
            self.txt_caja.setText(str(round(Archivo.recuperar("tienda.dat").caja, 2)))
        #except Exception:

    def editarCaja(self):

        tienda_de_libros = Archivo.recuperar("tienda.dat")
        self.txt_caja.setText(str(round(tienda_de_libros.caja, 2)))
        #tienda_de_libros.caja = self.controladorIngresarCaja.caja
        #print(tienda_de_libros.caja)
        Archivo.guardar("tienda.dat", tienda_de_libros)


    """Controladores Relacionados a la biblioteca o libros"""
    def ingreso_Libro(self):
        self.controladorVistaInsertarLibros = ControladorVistaInsertarLibros()
        self.controladorVistaInsertarLibros.show()

    def mostrar_Libros(self):
        self.controladorMostrarLibros = ControladorMostrarLibros()
        self.controladorMostrarLibros.show()

    def editar_libro(self):
        self.controladorEditarLibros = ControladorEditarLibros()
        self.controladorEditarLibros.btn_eliminar.setVisible(False)
        self.controladorEditarLibros.btn_aceptar.setGeometry(QtCore.QRect(260, 320, 75, 23))
        self.controladorEditarLibros.btn_cancelar.setGeometry(QtCore.QRect(370, 320, 75, 23))
        self.controladorEditarLibros.show()

    def eliminar_libro(self):
        self.controladorEditarLibros = ControladorEditarLibros()
        self.controladorEditarLibros.btn_editar.setVisible(False)
        self.controladorEditarLibros.btn_eliminar.setGeometry(QtCore.QRect(150, 320, 75, 23))
        self.controladorEditarLibros.btn_aceptar.setGeometry(QtCore.QRect(260, 320, 75, 23))
        self.controladorEditarLibros.btn_cancelar.setGeometry(QtCore.QRect(370, 320, 75, 23))
        self.controladorEditarLibros.show()
    """===================================================================================="""

    """Controladores relacionados a las entidades, cliente y proveedores"""
    def ingreso_Entidad(self):
        self.controladoInsertarEntidad = ControladorVistaInsertarEntidad()
        self.controladoInsertarEntidad.show()

    def mostrar_Entidades(self):
        self.controladorMostrarEntidades = ControladorMostrarEntidades()
        self.controladorMostrarEntidades.show()

    def editar_Entidad(self):
        self.controladorEditarEntidad = ControladorEditar_Eliminar_Entidades()
        self.controladorEditarEntidad.btn_eliminar.setVisible(False)
        self.controladorEditarEntidad.btn_aceptar.setGeometry(QtCore.QRect(220, 320, 75, 23))
        self.controladorEditarEntidad.btn_cancelar.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.controladorEditarEntidad.show()

    def eliminar_Entidad(self):
        self.controladorEditarEntidad = ControladorEditar_Eliminar_Entidades()
        self.controladorEditarEntidad.btn_editar.setVisible(False)
        self.controladorEditarEntidad.btn_aceptar.setGeometry(QtCore.QRect(120, 320, 75, 23))
        self.controladorEditarEntidad.btn_cancelar.setGeometry(QtCore.QRect(220, 320, 75, 23))
        self.controladorEditarEntidad.btn_cancelar.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.controladorEditarEntidad.show()

    """===================================================================================="""
    def facturar(self):
        self.controladorFacturar.show()

    def mostrar_transacciones(self):
        self.controladorMostrarFacturas = ControladorMostrarTransacciones()
        self.controladorMostrarFacturas.show()
