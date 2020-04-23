import { Injectable } from '@nestjs/common';
import { Nombre } from './interfaces/nombre.interface'

@Injectable()
export class PersonalizarService {

	// Función para Proper Name
	toTitleCase(str) {
    return str.replace(/\w\S*/g, function(txt){
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}
	/* 
	El siguiente algoritmo de Personalizar solicita los siguientes requerimientos:
	- Debe recibir en una variable los Nombres, luego Paterno, Materno y Género son otras variables.
	- Debe retornar un saludo que inicie con "Sr" o "Sra" dependiendo del género.
	- El nombre debe retornarse finalmente con las iniciales de cada nombre o apellido en mayúscula. (El resto en minus)
	- El ingreso por el usuario puede incluír tanto minúsculas como mayúsculas
	*/
	personalizar(name: Nombre){
		//Verificar datos correctos.

		if(typeof(name.nombres) && typeof(name.paterno) && typeof(name.materno) && typeof(name.genero) == "string"){
			var nombres = this.toTitleCase(name.nombres.toLowerCase());
			var paterno = this.toTitleCase(name.paterno.toLowerCase());
			var materno = this.toTitleCase(name.materno.toLowerCase());
			var genero = name.genero.toLowerCase();
			if(genero ==  "m" || genero ==  "f"){
				// Creamos el saludo y comenzamos a hacer las transformaciones correspondientes.
				var saludo = "Bienvenid";
				if(genero == "m"){
					saludo = saludo + "o Sr"
				}else{
					saludo = saludo + "a Sra"
				}

				return `${saludo} ${nombres} ${paterno} ${materno}`

			}else{
				return 'Genero invalido'
			
}		}else{
			return 'Formato incorrecto'
		}
 }
}
