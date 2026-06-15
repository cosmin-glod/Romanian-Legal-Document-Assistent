# Raport evaluare

**Model**: `qwen2.5:7b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 68

## Metrici globale

- Refusal accuracy: **71%** (48/68)
- Breadcrumb recall@4 (excl. refusal cases): **93%** (52/56)
- Keyword coverage (cazuri non-refusal): **55%** (56 cazuri)
- Contract pass rate (R1..R6): **88%** (60/68)
- Latency medie: **60.0s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 22 | 50% | 100% | 100% | 58.1s |
| locuire | 22 | 86% | 100% | 86% | 53.0s |
| nastere | 24 | 75% | 80% | 79% | 68.3s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 36 | 75% | 88% | 86% |
| medium | 20 | 65% | 95% | 90% |
| hard | 12 | 67% | 100% | 92% |

## Distribuția violărilor de contract

- `R5_REFUSAL_WITH_DOCS`: 3
- `R2_UNCITED`: 3
- `R4_FABRICATED_DOC`: 2

## Cazuri cu probleme (26)


### casatorie-02 — casatorie / easy
**Întrebare**: Două persoane de același sex se pot căsători în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Condiții pentru a te căsători > 📌 Monogamie', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-03 — casatorie / easy
**Întrebare**: Sunt deja căsătorit. Pot încheia o nouă căsătorie?
**Răspuns**: Nu poți încheia o nouă căsătorie fiindcă ești deja căsătorit. Poligamia este interzisă în România.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Monogamie', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex']

### casatorie-09 — casatorie / medium
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-11 — casatorie / medium
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre procedurile de căsătorie în străinătate. Vă rog să furnizați mai multe detalii sau sursă specifică pentru această procedură.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-12 — casatorie / medium
**Întrebare**: Care sunt pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu despre procedurile de căsătorie când partenerul este cetățean străin. Vă rog să furnizați mai multe detalii sau sursă specifică pentru acest subiect.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-13 — casatorie / medium
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine dacă trebuie sau nu traduceri pentru actele lui. Surselor citate nu oferă detalii specifice despre cazul dumneavoastră, căsătorit cu un cetățean UE. Pentru …
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!', 'Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România']

### casatorie-14 — casatorie / medium
**Întrebare**: Am încheiat căsătoria în străinătate. Cum o transcriu/recunosc în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dvs. Vă rog să furnizați mai multe detalii sau sursă specifică pentru a putea oferi un răspuns corect.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-15 — casatorie / hard
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dumneavoastră privind procedurile de căsătorie cu un cetățean străin. Vă recomand să consultați un consul sau un avocat specializat în dreptul…
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-18 — casatorie / hard
**Întrebare**: Partenerul meu nu cunoaște limba română. Ce este obligatoriu la oficierea căsătoriei?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în România']

### casatorie-19 — casatorie / easy
**Întrebare**: Cum divorțez de partenerul meu?
**Răspuns**: Pentru divorț, există câteva pași de urmat:

1. Dacă aveți un regim matrimonial convențional (comunitatea de bune), puteți solicita divorțul la ofițerul de stare civilă.
2. În cazul în care alegeți regimul separației de bunuri, trebuie să e…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Proprietarul vrea să mă dea afară - ce pot face?', 'Căsătoria > Regimul matrimonial > 📌 Separația de bunuri', 'Căsătoria > Locuire', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-22 — casatorie / easy
**Întrebare**: Putem semna un contract prematrimonial înainte de căsătorie?
**Răspuns**: Da, puteți semna un contract prematrimonial înainte sau în timpul căsătoriei. Dacă alegeți un alt regim matrimonial decât cel al comunității legale, veți prezenta o copie a convenției matrimoniale, autentificată de către notarul public. Con…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Ne căsătorim în România']

### locuire-04 — locuire / easy
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile proprietarului (locatorului)']

### locuire-05 — locuire / easy
**Întrebare**: Care sunt obligațiile proprietarului față de chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre obligațiile proprietarului față de chiriaș. Vă recomand să consultați documentul contractului de închiriere sau un avocat pentru informații precise.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile chiriașului (locatarului)']

### locuire-11 — locuire / medium
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre obligațiile chiriașului față de imobil. Vă recomand să consultați un avocat sau documentele contractuale de închiriere pentru informații precise.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Obligațiile chiriașului (locatarului)']

### locuire-17 — locuire / hard
**Întrebare**: Sunt cetățean român, vreau să cumpăr un imobil împreună cu un partener cetățean turc. Există restricții?
**Răspuns**: Există restricții pentru căsătoria dintre persoane de același sex în România, dar acestea nu afectează achiziționarea unui imobil. Ca cetățean român și partener turc, puteți cumpăra un imobil prin înființarea unei firme SRL cu asociat unic …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?']

### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: Nașterea va fi înregistrată la Serviciul de Stare Civilă al Primăriei unde locuiești. Documentele necesare includ: certificatul medical constatator al nașterii, actele de identitate ale părinților și, dacă aveți nume de familie diferite, de…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']

### nastere-04 — nastere / easy
**Întrebare**: Am născut acasă, nu într-un spital. Cum obțin certificatul medical constatator al nașterii?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine dacă există un alt mecanism de obținere a certificatului medical constatator al nașterii în cazul născerii acasă. În general, certificatul medical constatat…
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS']
**Top breadcrumbs**: ['Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România']

### nastere-05 — nastere / easy
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Pentru a înregistra nașterea copilului atunci când părinții nu sunt căsătoriți și tatăl recunoaște copilul, trebuie depuse următoarele documente la primărie:

- Certificatul de naştere al mamei;
- Actele de identitate ale tale și ale parten…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-08 — nastere / easy
**Întrebare**: Ce este certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii este un document medical emis de medicul care a asistat la nașterea copilului sau de medicul șef de secție. Acesta nu înlocuiește certificatul de naștere și trebuie obținut din spitalul unde a av…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în străinătate']

### nastere-13 — nastere / medium
**Întrebare**: Am primit certificatul de naștere al copilului în străinătate. Cum îl transcriu pe cel românesc?
**Răspuns**: Pentru a transcrie certificatul de naștere al copilului pe cel românesc, trebuie să urmăriți unul dintre următorii pași, în funcție de situația părinților:

1. Dacă părinții au avut niciodată domiciliu în România: Poți cere transcrierea cer…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Cel puțin un părinte are domiciliul în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România']

### nastere-15 — nastere / medium
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Da, puteți înregistra nașterea copilului dvs. la ambasada sau consulatul țării de origine, chiar dacă părinții nu au avut niciodată domiciliu în România. Acest lucru se poate face pentru că procesul de înregistrare a nașterii unui copil str…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-16 — nastere / medium
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dumneavoastră. Vă rog să furnizați mai multe detalii sau sursă care să ofere informații despre procedurile de înregistrare a nașterii copilulu…
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-18 — nastere / hard
**Întrebare**: Părinții au nume de familie diferite. Ce nume va purta copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-20 — nastere / hard
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dvs. Desigur, puteți consulta direct siteurile oficiale ale autorităților române sau ambasadele/consulatelor române din Franța pentru instrucț…
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-21 — nastere / easy
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: Pentru a înregistra nașterea copilului, este necesar să furnizați următoarele documente:

- Actul de identitate al părintelui cetățean român (buletin, carte de identitate, etc.)
- Certificatul medical constatator al nașterii care trebuie să…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-22 — nastere / easy
**Întrebare**: Vreau să adopt un copil cu vârsta de peste 5 ani. Procedura?
**Răspuns**: Procedura pentru adoptarea unui copil cu vârsta de peste 5 ani este mai complexă și implică multe etape. În primul rând, ar trebui să consultați o asistență juridică sau o organizație specializată în adoptiile sociale pentru a obține inform…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Stimulentul de inserție', 'Nașterea > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Copilul nu este încadrat într-un grad de handicap']
