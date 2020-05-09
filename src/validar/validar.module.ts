import { Module } from '@nestjs/common';
import { ValidarutController } from './validarut.controller';
import { ValidaterutService } from './validaterut.service';


@Module({
	controllers: [ValidarutController],
	providers: [ValidaterutService],
	})
export class ValidarModule {}
