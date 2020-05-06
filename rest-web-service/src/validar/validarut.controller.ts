import { Controller, Get, Post, Body, Param, Req, Res } from '@nestjs/common';
import { CreateRutDto } from './dto/create-rut.dto';
import { ValidaterutService } from './validaterut.service';

@Controller('validarut')
export class ValidarutController {
	constructor(private validarService: ValidaterutService){}

	@Post()
  	async create(@Body() createRutDto: CreateRutDto) {
    return this.validarService.validar(createRutDto);
  }

}
