# Raport evaluare — pre-completare formulare

**Cazuri**: 14  ·  **Câmpuri evaluate**: 180

## Global

- Acuratețe la nivel de câmp: **91%** (163/180)
- Cazuri cu toate câmpurile obligatorii corecte într-o singură rundă: **43%** (6/14)

## Pe clasă de câmp

| Clasă | Corecte / Total | Acuratețe |
|---|---|---|
| structured | 93/108 | 86% |
| name | 33/34 | 97% |
| freetext | 37/38 | 97% |

## Pe formular

| Formular | Câmpuri corecte | Acuratețe | Req. complet |
|---|---|---|---|
| declaratie_nume_copil | 28/30 | 93% | 0/2 |
| recunoastere_paternitate | 21/24 | 88% | 0/2 |
| cerere_alocatie_copil | 22/22 | 100% | 2/2 |
| cerere_indemnizatie_crestere | 24/24 | 100% | 2/2 |
| declaratie_casatorie | 26/30 | 87% | 0/2 |
| declaratie_necasatorit | 14/14 | 100% | 2/2 |
| contract_inchiriere | 28/36 | 78% | 0/2 |

## Câmpuri ratate


### nume_copil-1
- `child_sex` (structured): aștept `F`, obținut `None`

### nume_copil-2
- `child_sex` (structured): aștept `M`, obținut `None`

### paternitate-1
- `child_sex` (structured): aștept `M`, obținut `None`
- `child_birth_date` (structured): aștept `2026-05-20`, obținut `None`

### paternitate-2
- `child_sex` (structured): aștept `F`, obținut `None`

### casatorie-1
- `spouse1_birth_date` (structured): aștept `1990-01-01`, obținut `None`
- `spouse2_birth_date` (structured): aștept `1992-02-02`, obținut `None`

### casatorie-2
- `spouse1_birth_date` (structured): aștept `1988-03-03`, obținut `None`
- `spouse2_birth_date` (structured): aștept `1993-04-04`, obținut `None`

### inchiriere-1
- `tenant_id_series` (structured): aștept `CJ`, obținut `None`
- `tenant_id_number` (structured): aștept `222333`, obținut `None`
- `payment_day` (structured): aștept `5`, obținut `None`

### inchiriere-2
- `tenant_full_name` (name): aștept `Radu Ene`, obținut `Elena Stan`
- `tenant_cnp` (structured): aștept `1870303123456`, obținut `2900202123456`
- `tenant_address` (freetext): aștept `Arad Str. Veche 8`, obținut `Timisoara Str. Noua 7`
- `tenant_id_series` (structured): aștept `AR`, obținut `TM`
- `tenant_id_number` (structured): aștept `101010`, obținut `909090`
