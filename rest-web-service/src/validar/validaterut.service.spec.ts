import { Test, TestingModule } from '@nestjs/testing';
import { ValidaterutService } from './validaterut.service';

describe('ValidaterutService', () => {
  let service: ValidaterutService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [ValidaterutService],
    }).compile();

    service = module.get<ValidaterutService>(ValidaterutService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
