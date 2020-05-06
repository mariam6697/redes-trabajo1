import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ValidarModule } from './validar/validar.module';
import { SaludoModule } from './saludo/saludo.module';

@Module({
  imports: [ValidarModule, SaludoModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
