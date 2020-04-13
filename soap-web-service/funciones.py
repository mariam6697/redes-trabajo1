from itertools import cycle
import re

def validarRut(ctx, rut):
    rutConDv = rut
    rut = re.sub('-', '', rutConDv)[:-1]
    rut = rut.replace('.', '')
    print(rut)
    dv = rutConDv.strip()[-1].upper()
    if (rut.isnumeric() and (dv.isnumeric() or dv == 'K')):
        reversa = map(int, reversed(rut))
        factores = cycle(range(2, 8))
        suma = sum(d * f for d, f in zip(reversa, factores))
        dvReal = str((-suma) % 11)
        if (dv == dvReal):
            return ('El digito verificador ' + dv + ' es correcto para el RUT ' + rut)
        elif (dv == 'K' and dvReal == '10'):
            return ('El digito verificador ' + dv + ' es correcto para el RUT ' + rut)
        else:
            return ('El digito verificador ' + dv + ' es incorrecto para el RUT ' + rut)
    else:
        return ('Por favor ingrese solo numeros, guión o K.')

def generarSaludo(ctx, nombres, paterno, materno, genero):
    mujer = False
    genero = genero.upper() if genero != None else None
    if (genero == 'F'):
        mujer = True
        saludo = 'Sra.'
    elif (genero == 'M'):
        saludo = 'Sr.'
    else:
        return ('Genero no valido. Intente nuevamente.')
    if (nombres != None and paterno != None and materno != None):
        nombreCompleto = (nombres + ' ' + paterno + ' ' + materno).title()
        return (('Bienvenida' if mujer else 'Bienvenido') + ' ' + saludo + ' ' + nombreCompleto)
    return ('Por favor rellene todos los campos.')