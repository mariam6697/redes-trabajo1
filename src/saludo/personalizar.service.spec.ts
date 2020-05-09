import { Test, TestingModule } from '@nestjs/testing';
import { PersonalizarService } from './personalizar.service';

describe('PersonalizarService', () => {
  let service: PersonalizarService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [PersonalizarService],
    }).compile();

    service = module.get<PersonalizarService>(PersonalizarService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
