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

### Cliente
Previamente instalados NodeJS y NPM:
* Situarse en la carpeta `soap-web-client`.
* En la línea de comandos, ejecutar `npm install` para instalar los paquetes requeridos.
* Finalmente ejecutar `npm run serve` para levantar el cliente.
* Una aplicación web se encontrará disponible en la dirección `http://localhost:8080/`. En caso de estar ocupado dicho puerto, se utilizará otro que se indicará en la terminal respectiva.

## Servicio web REST
REST es una interfaz para conectar varios sistemas basados en el protocolo HTTP y sirve para obtener, generar datos y operaciones, devolviendo esos datos en un formato JSON.
Para poder levantar el servidor es necesario tener una version de Nodejs superior a 10.13.0 y NPM instalado.
* Situarse en la carpeta `rest-web-service`
* Abrir una terminal en la carpeta
* Instalar dependencias ejecutando `npm install`
* Finalmente ejecutar `npm run start`
* EL servicio web se encontrará disponible en la dirección `http://localhost:3000`

En la ruta `validarut` podemos encontrarnos con el primer método para la validación de un rut ingresado por el método `Post` desde el `body`. Este método recibe cualquier tipo de dato y es verificado dentro del servicio. El `rut` ingresado puede (o no) tener un guión para separar el dígito verificado. Finalmente nos otorgará la informacin acerca de si el `rut` ingresado es válido o no.

En la ruta `saludo` podemos encontrarnos con el segundo servicio que tiene la función de retornar un saludo personalizado en función del género del usuario. Ingresado por el método `Post` desde el `body`.  Los parámetros a ingresar son `nombres` que corresponde a los nombres del usuario. Los apellidos se ingresan en `materno` y `paterno`, mientras que el `genero` debe ser "M" ó "m"

### Cliente
Previamente instalados NodeJS y NPM:
* Situarse en la carpeta `rest-web-client`.
* En la línea de comandos, ejecutar `npm install` para instalar los paquetes requeridos.
* Finalmente ejecutar `npm run serve` para levantar el cliente.
* Una aplicación web se encontrará disponible en la dirección `http://localhost:8080/`. En caso de estar ocupado dicho puerto, se utilizará otro que se indicará en la terminal respectiva.