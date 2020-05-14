from itertools import cycle
from spyne.model.complex import ComplexModel
from spyne import Boolean, String
import re

class Respuesta(ComplexModel):
    estado = Boolean
    mensaje = String
    def __init__(self, estado, mensaje):
        super(Respuesta, self).__init__()
        self.estado = estado
        self.mensaje = mensaje

def validar_rut(ctx, rut):
    rut_con_dv = rut
    rut = re.sub('-', '', rut_con_dv)[:-1].replace('.', '')
    print("RUT ingresado", rut)
    dv = rut_con_dv.strip()[-1].upper()
    if (rut.isnumeric() and (dv.isnumeric() or dv == 'K')):
        reversa = map(int, reversed(rut))
        factores = cycle(range(2, 8))
        suma = sum(d * f for d, f in zip(reversa, factores))
        dv_real = str((-suma) % 11)
        if (dv == dv_real):
            return Respuesta(True, 'El dígito verificador ' + dv + ' es correcto para el RUT ' + rut)
        elif (dv == 'K' and dv_real == '10'):
            return Respuesta(True, 'El dígito verificador ' + dv + ' es correcto para el RUT ' + rut)
        else:
            return Respuesta(False, 'El dígito verificador ' + dv + ' es incorrecto para el RUT ' + rut)
    else:
        return Respuesta(False, 'Ingrese sólo números, guión y K')

def generar_saludo(ctx, nombres, paterno, materno, genero):
    if (nombres != None and paterno != None and materno != None and genero != None):
        nombre_completo = (nombres + ' ' + paterno + ' ' + materno).title()
        mujer = False
        genero = genero.upper() if genero != None else None
        if (genero == 'F'):
            mujer = True
            saludo = 'Sra.'
        elif (genero == 'M'):
            saludo = 'Sr.'
        else:
            return Respuesta(False, 'Género no válido. Intente nuevamente.')
        return Respuesta(True, ('Bienvenida' if mujer else 'Bienvenido') + ' ' + saludo + ' ' + nombre_completo)
    elif (genero == None):
        return Respuesta(False, 'Ingrese un género.')
    else:
        return Respuesta(False, 'Por favor rellene todos los campos.')