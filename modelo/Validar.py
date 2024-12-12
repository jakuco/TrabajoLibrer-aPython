
def validar(tipo):

    def cedula(cedula):
        return sum([int(cedula[i]) if i % 2 != 0 else int(cedula[i])*2 if int(cedula[i])*2 < 9 else int(cedula[i])*2-9
                    for i in range(len(cedula))])%10 == 0 and len(cedula) == 10 and (int(cedula[:2]) < 25 or int(cedula[:2]) == 30) and cedula.isdigit()

    def ISBN(ISBN):
        """Existen dos froma de validar, el uno es para 10 y el otro es para los 13 dígitos, tener en cuenta eso al calcular"""
        """En este caso solo se tomó encuenta el de 10 dígitos con caracteres - intermedio de manera: 84-206-8186-5"""
        return sum([int(list(filter(lambda n: n != "-", ISBN))[i])*(i+1) for i in range(len(list(filter(lambda n: n != "-", ISBN))))]) % 11 ==0

    def RUC(RUC):
        verificador = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
        verificador_publicos = [3, 2, 7, 6, 5, 4, 3, 2, 1]

        if len(RUC) == 13 and int(RUC[2]) >= 0 and int(RUC[2]) <= 5:
            return True
        elif len(RUC) == 13 and int(RUC[2]) == 6 and sum([int(RUC[i])*verificador_publicos[i] for i in range(9)]) % 11 == 0:
            return True
        elif len(RUC) == 13 and int(RUC[2]) == 9 and sum([int(RUC[i])*verificador[i] for i in range(10)]) % 11 == 0:
            return True

        return False

    def telefono(telefono):
        """El teléfono tiene que empezar por 09 en el caso de celular siendo su largo de 10"""
        """Para convencionales puede ser 02, 03, 04, 05, 06, 07 con longitud de 9"""
        return (telefono.isdigit() and len(telefono) > 0 and len(telefono) == 10) if telefono[:2] =="09" else \
            (telefono.isdigit() and len(telefono) > 0 and len(telefono) == 9 and int(telefono[:2]) < 8 and int(telefono[:2]) > 1)

    def IVA(IVA):
        if IVA.isdecimal():
            if int(IVA) >= 0:
                return True

        return False
    def cantidad(cantidad):
        if cantidad.isdigit():
            if int(cantidad) > 0:
                return True

        return False

    diccionario_validaciones = {
        "ISBN": ISBN,
        "cedula": cedula,
        "telefona": telefono,
        "RUC": RUC,
        "IVA":IVA,
        "cantidad":cantidad
    }
    return diccionario_validaciones[tipo]

def transaccion(tipo):

    def venta(cantidad, stock):
        if cantidad <= stock:
            return True
        return False

    def abastecimiento(total, caja):
        if total <= caja:
            return True
        return False

    diccionario_validaciones = {
        "Abastecimiento": abastecimiento,
        "Venta": venta
    }
    return diccionario_validaciones[tipo]

print(validar("cedula")("1101160032"))