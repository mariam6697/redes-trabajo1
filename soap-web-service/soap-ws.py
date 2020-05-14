import logging
logging.basicConfig(level=logging.DEBUG)
from spyne.application import Application
from spyne.decorator import rpc
from cors import CorsService
from spyne.model.primitive.string import Unicode
from spyne.protocol.soap.soap11 import Soap11
from spyne.server.wsgi import WsgiApplication
from funciones import validar_rut, generar_saludo, Respuesta

class RutService(CorsService):
    @rpc(Unicode, _returns=Respuesta)
    def rut(ctx, rut):
        return validar_rut(ctx, rut)
    
class NombreService(CorsService):
    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=Respuesta)
    def nombre(ctx, nombres, paterno, materno, genero):
        return generar_saludo(ctx, nombres, paterno, materno, genero)

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