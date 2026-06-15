# Raport evaluare — pre-completare formulare

**Cazuri**: 14  ·  **Câmpuri evaluate**: 180

## Global

- Acuratețe la nivel de câmp: **97%** (175/180)
- Cazuri cu toate câmpurile obligatorii corecte într-o singură rundă: **71%** (10/14)

## Pe clasă de câmp

| Clasă | Corecte / Total | Acuratețe |
|---|---|---|
| structured | 104/108 | 96% |
| name | 34/34 | 100% |
| freetext | 37/38 | 97% |

## Pe formular

| Formular | Câmpuri corecte | Acuratețe | Req. complet |
|---|---|---|---|
| declaratie_nume_copil | 30/30 | 100% | 2/2 |
| recunoastere_paternitate | 22/24 | 92% | 0/2 |
| cerere_alocatie_copil | 22/22 | 100% | 2/2 |
| cerere_indemnizatie_crestere | 24/24 | 100% | 2/2 |
| declaratie_casatorie | 30/30 | 100% | 2/2 |
| declaratie_necasatorit | 14/14 | 100% | 2/2 |
| contract_inchiriere | 33/36 | 92% | 0/2 |

## Câmpuri ratate


### paternitate-1
- `child_sex` (structured): aștept `M`, obținut `None`

### paternitate-2
- `child_sex` (structured): aștept `F`, obținut `None`

### inchiriere-1
- `payment_day` (structured): aștept `5`, obținut `None`

### inchiriere-2
- `property_address` (freetext): aștept `Timisoara Str. Mare 20`, obținut `Str. Noua 7, Timisoara`
- `payment_day` (structured): aștept `10`, obținut `None`
