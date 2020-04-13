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
from funciones import validarRut, generarSaludo

class RutService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def rut(ctx, rut):
        return validarRut(ctx, rut)
    
class NombreService(ServiceBase):
    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def nombre(ctx, nombres, paterno, materno, genero):
        return generarSaludo(ctx, nombres, paterno, materno, genero)

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