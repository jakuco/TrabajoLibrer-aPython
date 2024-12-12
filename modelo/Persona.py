from Entidad import  Entidad


class Persona(Entidad):
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        Entidad.__init__(self, nombre, direccion, telefono, correo)
        self.cedula = cedula
