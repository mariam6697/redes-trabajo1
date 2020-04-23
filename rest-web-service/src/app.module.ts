import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ValidarutController } from './validarut/validarut.controller';
import { ValidaterutService } from './validaterut/validaterut.service';
import { SaludoController } from './saludo/saludo.controller';
import { PersonalizarService } from './personalizar/personalizar.service';

@Module({
  imports: [],
  controllers: [AppController, ValidarutController, SaludoController],
  providers: [AppService, ValidaterutService, PersonalizarService],
})
export class AppModule {}
