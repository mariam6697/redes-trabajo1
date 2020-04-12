import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ValidarutController } from './validarut/validarut.controller';
import { ValidaterutService } from './validaterut/validaterut.service';

@Module({
  imports: [],
  controllers: [AppController, ValidarutController],
  providers: [AppService, ValidaterutService],
})
export class AppModule {}
