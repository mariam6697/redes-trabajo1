import { Module } from '@nestjs/common';
import { SaludoController } from './saludo.controller';
import { PersonalizarService } from './personalizar.service';


@Module({
	controllers: [SaludoController],
	providers: [PersonalizarService],
	})

export class SaludoModule {}
