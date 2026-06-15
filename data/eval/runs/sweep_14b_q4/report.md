# Raport evaluare

**Model**: `qwen2.5:14b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 68

## Metrici globale

- Refusal accuracy: **74%** (50/68)
- Breadcrumb recall@4 (excl. refusal cases): **93%** (52/56)
- Keyword coverage (cazuri non-refusal): **53%** (56 cazuri)
- Contract pass rate (R1..R6): **71%** (48/68)
- Latency medie: **47.0s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 22 | 68% | 100% | 64% | 61.0s |
| locuire | 22 | 82% | 100% | 82% | 37.8s |
| nastere | 24 | 71% | 80% | 67% | 42.7s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 36 | 78% | 88% | 81% |
| medium | 20 | 70% | 95% | 60% |
| hard | 12 | 67% | 100% | 58% |

## Distribuția violărilor de contract

- `R7_OVERREFUSAL`: 15
- `R2_UNCITED`: 4
- `R6_FORM_ID_IN_DOCS`: 1

## Cazuri cu probleme (27)


### nastere-01 — nastere / easy
**Întrebare**: Ce documente îmi trebuie pentru înregistrarea nașterii copilului meu, dacă sunt căsătorit cu partenera?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: Nașterea unui copil care s-a întâmplat într-un spital din România poate fi înregistrată la Primaria localității unde a avut loc nașterea. În acest caz, este necesar să prezentezi următoarele documente: certificatul medical constatator al na…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']

### nastere-04 — nastere / easy
**Întrebare**: Am născut acasă, nu într-un spital. Cum obțin certificatul medical constatator al nașterii?
**Răspuns**: Dacă ai născut acasă și nu la spital sau clinica, trebuie să contactezi medicul de familie sau un medic care a fost prezent la naștere pentru a obține certificatul medical constatator al nașterii. Acest document este necesar pentru înregist…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România']

### nastere-05 — nastere / easy
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-07 — nastere / easy
**Întrebare**: Cine eliberează certificatul de naștere al copilului meu?
**Răspuns**: Certificatul de naștere este eliberat de ofițerul de stare civilă la Primaria județului sau municipiului unde s-a întâmplat nașterea, bazându-se pe informațiile din certificatul medical constatator al nașterii și alte documente necesare.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Tatăl recunoaște copilul']

### nastere-08 — nastere / easy
**Întrebare**: Ce este certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii este un document pe care îl vei primi de la spital sau clinica unde s-a întâmplat nașterea. Acest document este emis în termen de 24 de ore și atestă faptul că s-a avut loc o naștere. Este import…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în străinătate']

### nastere-13 — nastere / medium
**Întrebare**: Am primit certificatul de naștere al copilului în străinătate. Cum îl transcriu pe cel românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Cel puțin un părinte are domiciliul în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România']

### nastere-15 — nastere / medium
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Dacă părinții copilului nascut nu au domiciliu în România, procedura de înregistrare a nașterii depinde de legi ale țării cetățeniei acestora. Poți să înregistrezi nașterea la ambasada sau consulatul țării cetățeniei părinților, dacă aceste…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-16 — nastere / medium
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-17 — nastere / hard
**Întrebare**: Nu sunt căsătorit cu mama copilului. Cum recunosc legal copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-19 — nastere / hard
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-20 — nastere / hard
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### casatorie-07 — casatorie / easy
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-09 — casatorie / medium
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Pentru a vă căsătoria în România, este necesar să depuneți documente precum declarația de căsătorie și actele de identitate la primăria locului de domiciliu sau reședință al unuia dintre voi. Sursele disponibile nu specifică detaliile exact…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-11 — casatorie / medium
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Pentru a vă căsători în străinătate, trebuie să urmați pași și condiții specificate de legi românești și internaționale. În general, aceste etape includ:

1. **Localizarea ambasadei sau consulatului român**: Căsătoria poate fi oficiată la s…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-12 — casatorie / medium
**Întrebare**: Care sunt pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-13 — casatorie / medium
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!', 'Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România']

### casatorie-14 — casatorie / medium
**Întrebare**: Am încheiat căsătoria în străinătate. Cum o transcriu/recunosc în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-15 — casatorie / hard
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Pentru căsătorire cu un cetățean străin, este necesar să îndepliniți anumite condiții și să furnizați documente specifice. Acest proces poate include:

1. **Documentele de identitate**: Partenerul dumneavoastră trebuie să prezinte actele sa…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-18 — casatorie / hard
**Întrebare**: Partenerul meu nu cunoaște limba română. Ce este obligatoriu la oficierea căsătoriei?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în România']

### casatorie-21 — casatorie / easy
**Întrebare**: Cum împart pensia de soț decedat?
**Răspuns**: Pentru a împărți pensia de soț decedat, este important să cunoașteți regimul matrimonial aplicabil. Dacă aveți bunuri comune (regimul comun al bunurilor), atunci pensia poate fi considerată o parte din bunurile comune și va fi împărțită în …
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Locuire', 'Căsătoria > Regimul matrimonial > 📌 Separația de bunuri', 'Căsătoria > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Relația de cuplu']

### casatorie-22 — casatorie / easy
**Întrebare**: Putem semna un contract prematrimonial înainte de căsătorie?
**Răspuns**: Da, puteți să alegeți să încheiate o convenție matrimonială (contract prematrimonial) înainte de căsătorie. Acesta poate fi încheiat înainte sau după oficierea căsătoriei și poate stabili regimul matrimonial al separației bunurilor sau comu…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Ne căsătorim în România']

### locuire-04 — locuire / easy
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: În conformitate cu prevederile legale, pentru a formaliza o închiriere de imobil este necesar să se încheie un contract scris care stabilește condițiile de închirie între proprietar și chiriaș. Acest document este esențial atât din punct de…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile proprietarului (locatorului)']

### locuire-05 — locuire / easy
**Întrebare**: Care sunt obligațiile proprietarului față de chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile chiriașului (locatarului)']

### locuire-08 — locuire / easy
**Întrebare**: Care sunt obligațiile chiriașului față de proprietar?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile chiriașului (locatarului)']

### locuire-11 — locuire / medium
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a descrie obligațiile chiriașului (locatarului) față de imobil.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Obligațiile chiriașului (locatarului)']

### locuire-20 — locuire / easy
**Întrebare**: Ce taxe plătesc dacă cumpăr o casă de vacanță în Bulgaria?
**Răspuns**: Conform sursei disponibile, nu am detalii specifice despre taxe care leversi dacă cumpără o casă de vacanță în Bulgaria. Informațiile din sursele noastre se referă la taxele aplicabile în România pentru un cumpărător, cum ar fi taxa de inta…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Drepturile și obligațiile mele în calitate de cumpărător', 'Locuire > Drepturile și obligațiile mele în calitate de vânzător', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Ne căsătorim în România']
