# Analiza: ce ar fi „scăpat" fără stratul de contracte

Întrebare: din cazurile evaluate, în câte răspunsul s-ar fi părut valid pentru utilizator (refuz sau răspuns afirmativ) dar a fost marcat ca incorect de cel puțin o regulă R1..R6?

## Tabel sintetic

| Model | Total cazuri | Cazuri cu violare | Eșecuri silențioase | Reducerea ratei silențioase față de 3B |
|---|---|---|---|---|
| 3B (M1 local) | 68 | 18 (26%) | 18 (26%) | — |
| 7B (Kaggle T4) | 68 | 8 (12%) | 8 (12%) | 15 pp |

## Distribuția violărilor pe regulă

| Regulă | 3B (M1 local) | 7B (Kaggle T4) |
|---|---|---|
| `R2_UNCITED` | 1 | 3 |
| `R3_BAD_CITATION` | 3 | 0 |
| `R4_FABRICATED_DOC` | 28 | 2 |
| `R5_REFUSAL_WITH_DOCS` | 0 | 3 |

## Headline numbers pentru teză

- **3B (M1 local)**: fără stratul de contracte, **18 din 68** răspunsuri (26%) ar fi fost servite cetățeanului ca informație autoritară, deși conțin fabricare, lipsă de citații sau pollution de formulare în documente.
- **7B (Kaggle T4)**: fără stratul de contracte, **8 din 68** răspunsuri (12%) ar fi fost servite cetățeanului ca informație autoritară, deși conțin fabricare, lipsă de citații sau pollution de formulare în documente.

## Exemple concrete (max 3 per regulă, per model)


### 3B (M1 local)

**R2_UNCITED** (1 apariții total):
- `casatorie-11` — "Vreau să mă căsătoresc în străinătate. Ce procedură există?"
  > Vă recomandăm să depuiți certificatul de naștere și certificatele medicale prenupțiale (în cazul în care există) pentru a putea continua procedura.

Vă recomandăm să consultați autoritățile române pen…

**R4_FABRICATED_DOC** (28 apariții total):
- `nastere-03` — "Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?"
  > Nașterea unui copil care a fost născut într-un spital în România se poate înregistra la Primaria unde locuiește părinții sau la Serviciul de Stare Civil al acesteia. Dacă Țara de cetățenie nu are amba…
- `nastere-05` — "Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?"
  > Certificatul de naștere al mamei; Actele de identitate ale tale și ale partenerului/partenerei (buletin sau carte de identitate, etc.); Certificatul medical constatator al nașterii care trebuie să poa…
- `nastere-05` — "Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?"
  > Certificatul de naștere al mamei; Actele de identitate ale tale și ale partenerului/partenerei (buletin sau carte de identitate, etc.); Certificatul medical constatator al nașterii care trebuie să poa…


### 7B (Kaggle T4)

**R2_UNCITED** (3 apariții total):
- `nastere-05` — "Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?"
  > Pentru a înregistra nașterea copilului atunci când părinții nu sunt căsătoriți și tatăl recunoaște copilul, trebuie depuse următoarele documente la primărie:

- Certificatul de naştere al mamei;
- Act…
- `nastere-21` — "Cum îmi schimb buletinul la 14 ani după naștere?"
  > Pentru a înregistra nașterea copilului, este necesar să furnizați următoarele documente:

- Actul de identitate al părintelui cetățean român (buletin, carte de identitate, etc.)
- Certificatul medical…
- `nastere-22` — "Vreau să adopt un copil cu vârsta de peste 5 ani. Procedura?"
  > Procedura pentru adoptarea unui copil cu vârsta de peste 5 ani este mai complexă și implică multe etape. În primul rând, ar trebui să consultați o asistență juridică sau o organizație specializată în …

**R4_FABRICATED_DOC** (2 apariții total):
- `locuire-17` — "Sunt cetățean român, vreau să cumpăr un imobil împreună cu un partener cetățean turc. Există restricții?"
  > Există restricții pentru căsătoria dintre persoane de același sex în România, dar acestea nu afectează achiziționarea unui imobil. Ca cetățean român și partener turc, puteți cumpăra un imobil prin înf…
- `nastere-13` — "Am primit certificatul de naștere al copilului în străinătate. Cum îl transcriu pe cel românesc?"
  > Pentru a transcrie certificatul de naștere al copilului pe cel românesc, trebuie să urmăriți unul dintre următorii pași, în funcție de situația părinților:

1. Dacă părinții au avut niciodată domicili…

**R5_REFUSAL_WITH_DOCS** (3 apariții total):
- `locuire-05` — "Care sunt obligațiile proprietarului față de chiriaș?"
  > Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre obligațiile proprietarului față de chiriaș. Vă recomand să consultați documentul contractului de închiriere s…
- `locuire-11` — "Care sunt obligațiile chiriașului față de imobil?"
  > Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre obligațiile chiriașului față de imobil. Vă recomand să consultați un avocat sau documentele contractuale de î…
- `nastere-04` — "Am născut acasă, nu într-un spital. Cum obțin certificatul medical constatator al nașterii?"
  > Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine dacă există un alt mecanism de obținere a certificatului medical constatator al nașterii în cazul născerii acasă. În…

