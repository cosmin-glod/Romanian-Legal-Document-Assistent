# Raport evaluare — pre-completare formulare

**Cazuri**: 14  ·  **Câmpuri evaluate**: 180

## Global

- Acuratețe la nivel de câmp: **94%** (170/180)
- Cazuri cu toate câmpurile obligatorii corecte într-o singură rundă: **57%** (8/14)

## Pe clasă de câmp

| Clasă | Corecte / Total | Acuratețe |
|---|---|---|
| structured | 99/108 | 92% |
| name | 34/34 | 100% |
| freetext | 37/38 | 97% |

## Pe formular

| Formular | Câmpuri corecte | Acuratețe | Req. complet |
|---|---|---|---|
| declaratie_nume_copil | 30/30 | 100% | 2/2 |
| recunoastere_paternitate | 20/24 | 83% | 0/2 |
| cerere_alocatie_copil | 22/22 | 100% | 2/2 |
| cerere_indemnizatie_crestere | 24/24 | 100% | 2/2 |
| declaratie_casatorie | 26/30 | 87% | 0/2 |
| declaratie_necasatorit | 14/14 | 100% | 2/2 |
| contract_inchiriere | 34/36 | 94% | 0/2 |

## Câmpuri ratate


### paternitate-1
- `child_sex` (structured): aștept `M`, obținut `None`
- `child_birth_date` (structured): aștept `2026-05-20`, obținut `None`

### paternitate-2
- `child_sex` (structured): aștept `F`, obținut `None`
- `child_birth_date` (structured): aștept `2026-04-10`, obținut `None`

### casatorie-1
- `spouse1_birth_date` (structured): aștept `1990-01-01`, obținut `None`
- `spouse2_birth_date` (structured): aștept `1992-02-02`, obținut `None`

### casatorie-2
- `spouse1_birth_date` (structured): aștept `1988-03-03`, obținut `None`
- `spouse2_birth_date` (structured): aștept `1993-04-04`, obținut `None`

### inchiriere-1
- `payment_day` (structured): aștept `5`, obținut `None`

### inchiriere-2
- `property_address` (freetext): aștept `Timisoara Str. Mare 20`, obținut `Str. Noua 7, Timisoara`
