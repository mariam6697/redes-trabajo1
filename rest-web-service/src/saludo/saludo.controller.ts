import { Controller, Body, Get, Post, Param, Req, Res } from '@nestjs/common';
import { CreateNameDto } from './dto/create-name.dto';
import { PersonalizarService } from './personalizar.service';

@Controller('saludo')
export class SaludoController {
	constructor(private personalizarService: PersonalizarService){}

	@Post()
  	async create(@Body() createNameDto: CreateNameDto) {
    return this.personalizarService.personalizar(createNameDto);
	}

}
