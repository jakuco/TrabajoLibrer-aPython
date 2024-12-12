from modelo.Entidad import Entidad
class Entidades:
    def __init__(self):
        self.lista_de_entidades = []

    def agregar_entidad(self, lista_de_atributos_entidad):
        self.lista_de_entidades.append(Entidad(lista_de_atributos_entidad[0],
                                               lista_de_atributos_entidad[1],
                                               lista_de_atributos_entidad[2],
                                               lista_de_atributos_entidad[3],
                                               lista_de_atributos_entidad[4]))

    def obtener_entidad(self, indice):
        return self.lista_de_entidades[indice]

    def eliminar_entidad(self, codigo):
        """Obtiene la entidad por medio de su código, encuentra cuál es el índice de esta en la lista
            y la elimina de la lista"""
        self.lista_de_entidades.pop(self.lista_de_entidades.index(self.obtener_entidad_por_codigo(codigo)))

    def editar_entidad(self, atributos_entidad):
        self.lista_de_entidades[self.lista_de_entidades.index(self.obtener_entidad_por_codigo(atributos_entidad[4]))] = \
            Entidad(atributos_entidad[0], atributos_entidad[1], atributos_entidad[2],  atributos_entidad[3], atributos_entidad[4])

    def obtener_entidad_por_codigo(self, codigo):
        if codigo in list(map(lambda n: n.codigo, self.lista_de_entidades)):
            return list(filter(lambda n: n.codigo == codigo, self.lista_de_entidades))[0]
        else:
            return None