import { Injectable } from '@nestjs/common';
import { Rut } from './interfaces/rut.interface';

@Injectable()
export class ValidaterutService {

	validar(rut: Rut){

	var factores = [2,3,4,5,6,7];
	var trueDV;
	// Validar que sea un número y válido
	var DV = rut.rut.substr(-1);
	var rutTmp = rut.rut.substring(0, rut.rut.length - 1);
	rutTmp = rutTmp.replace("-","");
	if(isNaN(Number(rutTmp)) || isNaN(Number(DV)) && DV.toUpperCase()!="K"){
		return `Ingrese un rut valido`
	}else{
		// Invertir rut
		var rutInvertido = 0;
		var suma = 0;
		var resto = Number(rutTmp);
		do{
			rutInvertido = rutInvertido * 10 + (resto %10);
			resto = Math.floor(resto / 10);
		}while(resto > 0)
		//Se aplica el algoritmo
		var cont = 0;
		for(let i = 0; i < rutInvertido.toString().length; i++){
			if(cont == 5){
				suma = suma + Number(rutInvertido.toString()[i])*factores[cont];
				cont = 0;	
			}else{
				suma = suma + Number(rutInvertido.toString()[i])*factores[cont];
				cont++;
			}
		}
		trueDV = 11 - suma%11;
		if(trueDV == 10){
			trueDV = "K";
			if(trueDV == DV.toUpperCase()){
				return `El rut es valido`
			}
			else{
				return `El rut no es valido`
			}
		}
		if(trueDV == 11){
			trueDV == 0;
		}
		if(trueDV == DV){
			return `El rut es valido`
		}else{
			return `El rut no es valido`
		}



	}

}
}