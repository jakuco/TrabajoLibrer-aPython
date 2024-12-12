import pickle


def guardar(nombre, objeto):
    archivo = open(nombre, "wb")
    pickle.dump(objeto, archivo)
    archivo.close()

def recuperar(nombre):
    try:
        return pickle.load(open(nombre, "rb"))
    except:
        return None
