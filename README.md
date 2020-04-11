# redes-trabajo1
Servicios web SOAP y REST, con clientes

## Servicio web SOAP
Admite peticiones SOAP 1.1 y responde en el mismo protocolo. Previamente instalado Python3 y PIP, para levantar el servidor:
* Situarse en la carpeta `soap-web-service`
* En la línea de comandos, ejecutar `pip install -r requirements.txt`
* Finalmente ejecutar `python soap-ws.py`
* El servicio web se encontrará disponible en la dirección `http://localhost:5051/`

Nótese que si se tiene instalado Python2 y Python3 simultáneamente (como en sistemas Linux), el comando `python` se reemplaza por `python3` y `pip` por `pip3`.
El servicio cuenta con dos métodos: `rut` y `nombre`:
* `rut` recibe el parámetro `rut` que puede (o no) tener un guión para separar el dígito verificador. No admite caracteres distintos a números o guión.
* `nombre` recibe cuatro parámetros que son cadenas de texto: `nombres`, `paterno`, `materno` y `genero`. Este último corresponde a `M` o `F` y no es sensible a mayúsculas.
Ambos métodos responden un mensaje que indican si el dígito verificador es válido (en caso de `rut`) o un saludo personalizado (en caso de `nombre`).
