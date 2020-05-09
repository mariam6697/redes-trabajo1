import { Test, TestingModule } from '@nestjs/testing';
import { ValidarutController } from './validarut.controller';

describe('Validarut Controller', () => {
  let controller: ValidarutController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [ValidarutController],
    }).compile();

    controller = module.get<ValidarutController>(ValidarutController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
