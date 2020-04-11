import logging
logging.basicConfig(level=logging.DEBUG)
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive.number import Integer
from spyne.model.primitive.string import Unicode
from spyne.service import ServiceBase
from spyne import Iterable
from spyne.protocol.soap.soap11 import Soap11
from spyne.server.wsgi import WsgiApplication
from itertools import cycle
import re

class RutService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def rut(ctx, rut):
        rutConDv = rut
        rut = re.sub('-', '', rutConDv)[:-1]
        dv = rutConDv.strip()[-1].upper()
        if (rut.isnumeric() and dv.isnumeric()):
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
            return ('Por favor ingrese solo numeros.')

class NombreService(ServiceBase):
    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def nombre(ctx, nombres, paterno, materno, genero):
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

application = Application([RutService, NombreService],
    tns='spyne.webservice.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('localhost', 5051, wsgi_app)
    server.serve_forever()