# Raport evaluare

**Model**: `qwen2.5:3b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 68

## Metrici globale

- Refusal accuracy: **65%** (44/68)
- Breadcrumb recall@4 (excl. refusal cases): **93%** (52/56)
- Keyword coverage (cazuri non-refusal): **37%** (56 cazuri)
- Contract pass rate (R1..R6): **74%** (50/68)
- Latency medie: **77.3s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 22 | 55% | 100% | 77% | 84.3s |
| locuire | 22 | 68% | 100% | 82% | 59.9s |
| nastere | 24 | 71% | 80% | 62% | 86.8s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 36 | 78% | 88% | 83% |
| medium | 20 | 60% | 95% | 60% |
| hard | 12 | 33% | 100% | 67% |

## Distribuția violărilor de contract

- `R4_FABRICATED_DOC`: 28
- `R3_BAD_CITATION`: 3
- `R2_UNCITED`: 1

## Cazuri cu probleme (42)


### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: Nașterea unui copil care a fost născut într-un spital în România se poate înregistra la Primaria unde locuiește părinții sau la Serviciul de Stare Civil al acesteia. Dacă Țara de cetățenie nu are ambasadă sau consulat în România, procedura …
**Status**: recall=False · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']

### nastere-04 — nastere / easy
**Întrebare**: Am născut acasă, nu într-un spital. Cum obțin certificatul medical constatator al nașterii?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România']

### nastere-05 — nastere / easy
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Certificatul de naștere al mamei; Actele de identitate ale tale și ale partenerului/partenerei (buletin sau carte de identitate, etc.); Certificatul medical constatator al nașterii care trebuie să poarte număr de înregistrare, dată certă, s…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-08 — nastere / easy
**Întrebare**: Ce este certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii este un document medical pe care îl vei primi de la spitalul sau clinica unde ai născut. Este eliberal în termen de 24 ore de către medic care a asistat la naștere, sau de către medicul șef de se…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în străinătate']

### nastere-09 — nastere / medium
**Întrebare**: Am născut în străinătate. Ce trebuie să fac pentru ca nașterea să fie recunoscută în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul']

### nastere-10 — nastere / medium
**Întrebare**: Cine poate primi indemnizația pentru creșterea copilului?
**Răspuns**: Părinții firești ai copilului, adoptatorii și persoana căreia i s-a încredințat copilul în vederea adopției pot primi indemnizația pentru creșterea copilului.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Stimulentul de inserție']

### nastere-11 — nastere / medium
**Întrebare**: Ce alocații financiare primesc părinții pentru un nou-născut?
**Răspuns**: 719 RON pentru copiii cu vârste între 0 și 2 ani; 292 RON pentru copiii cu vârsta de peste 2 ani.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Municipiul Constanța', 'Nașterea > Municipiul București', 'Nașterea > Municipiul Făgăraș', 'Nașterea > Copilul nu este încadrat într-un grad de handicap']

### nastere-13 — nastere / medium
**Întrebare**: Am primit certificatul de naștere al copilului în străinătate. Cum îl transcriu pe cel românesc?
**Răspuns**: Pentru a-ți transcrea certificatul de naștere al copilului, urmați pașii de mai jos:

1. Încercați să obțineți autorizare pentru eliberarea unui extras multilingv a actelor de stare civilă din baza Convenției nr. 16 a Comisiei Internațional…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R3_BAD_CITATION', 'R3_BAD_CITATION', 'R3_BAD_CITATION', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Cel puțin un părinte are domiciliul în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România']

### nastere-14 — nastere / medium
**Întrebare**: Ce este stimulentul de inserție și în ce condiții îl primesc?
**Răspuns**: Stimulantul de inserție este un ajutor financiar care poate fi obținut de părinți care se întorc la serviciu sau la job după ce copilul împlinește 6 luni. Este valabil în unele localități României, decât au decis să îl acorde prin hotărâre …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Stimulentul de inserție', 'Nașterea > Stimulentul de inserție', 'Nașterea > Stimulentul de inserție', 'Nașterea > Stimulente pentru nou-născut']

### nastere-15 — nastere / medium
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-16 — nastere / medium
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Pentru a obține un certificat de naștere al copilului românesc, urmați pasurile de mai jos. Nu am suficiente informații în surse disponibile pentru a răspunde cu detalii specifice ale cazului dumneavoastră.

1. Cereri Transcriere: Dacă copi…
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-17 — nastere / hard
**Întrebare**: Nu sunt căsătorit cu mama copilului. Cum recunosc legal copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-18 — nastere / hard
**Întrebare**: Părinții au nume de familie diferite. Ce nume va purta copilul?
**Răspuns**: Pentru a determina numele pe care îl va avea copila, părinții trebuie să stabilească un acord în această privință. Dacă nu pot forma un acord, cazul va fi transmis la instanță de tutelă pentru a decide numele.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-19 — nastere / hard
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-20 — nastere / hard
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Pentru a obține un certificat de naștere românesc pentru copil care s-a nascut în Franța, având ambele cetăți (românească și franceză), procedura completă ar trebui să include următoarele etape:

1. Cerere de transcriere la Ambasada Românie…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-21 — nastere / easy
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: În România, pentru a schimba un buletin la vârsta de 14 ani după născut, părinții trebuie să își înregistreze modificarea în Serviciul de Stare Civil. Această acțiune implică prezentarea următoarelor documente și informațiilor:

**Documente…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### casatorie-03 — casatorie / easy
**Întrebare**: Sunt deja căsătorit. Pot încheia o nouă căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Monogamie', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex']

### casatorie-04 — casatorie / easy
**Întrebare**: Pot să mă căsătoresc la 16 ani?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-05 — casatorie / easy
**Întrebare**: Pot să iau numele partenerului ca nume de familie după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Suntem căsătoriți', 'Căsătoria > Ne căsătorim în România']

### casatorie-06 — casatorie / easy
**Întrebare**: Există rude apropiate cu care nu mă pot căsători?
**Răspuns**: Rudele apropiate cu care nu poți să te căsătorești sunt părinții, bunici, descendenți, naturali sau adoptivi. Rudenia se stabilește astfel: în linie dreaptă, după numărul nașterilor; iar în linie colaterală, după numărul nașterilor, urcând …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria între rude', 'Căsătoria > Condiții pentru a te căsători > 📌 Persoana pusă sub o măsură de ocrotire specială', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex', 'Căsătoria > Condiții pentru a te căsători > 📌 Monogamie']

### casatorie-07 — casatorie / easy
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-08 — casatorie / easy
**Întrebare**: Pot purta un nume compus din numele ambilor soți?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Tatăl recunoaște copilul', 'Căsătoria > Ne căsătorim în România']

### casatorie-09 — casatorie / medium
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Pentru a depune la primăria în România, următoarele documente sunt necesare și recomandate:

1. Declarația de căsătorie (deși aceasta este obligatorie)
2. Actele de identitate ale celor doi căștiți (carte de identitate, buletin sau carte de…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-10 — casatorie / medium
**Întrebare**: Ce nume de familie pot să aleg după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-11 — casatorie / medium
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Vă recomandăm să depuiți certificatul de naștere și certificatele medicale prenupțiale (în cazul în care există) pentru a putea continua procedura.

Vă recomandăm să consultați autoritățile române pentru a obține certificatul de căsătoreanț…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-12 — casatorie / medium
**Întrebare**: Care sunt pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin?
**Răspuns**: Când partenerul este cetățean străin, pașii pentru depunerea declarației de căsătământ sunt următores:
1. Prezentarea declarației de căsătământ
2. Prima dovadă a domiciliului sau a reședinței cetățeanului român în străinătate
3. Actele voșt…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-13 — casatorie / medium
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!', 'Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România']

### casatorie-15 — casatorie / hard
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Pentru căsătoria cu un partener cetățean străin, sunt necesare următoarele documente suplimentare:

1. Carte de Identitate sau Pașaport pentru ambele persoane.
2. Certificatul de Naștere al cetățeanului român, în original și traducere legal…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-16 — casatorie / hard
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-17 — casatorie / hard
**Întrebare**: Sunt minor de 16 ani și vreau să mă căsătoresc. Care sunt pașii legali completi?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători']

### casatorie-18 — casatorie / hard
**Întrebare**: Partenerul meu nu cunoaște limba română. Ce este obligatoriu la oficierea căsătoriei?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în România']

### locuire-03 — locuire / easy
**Întrebare**: Ce trebuie să conțină un contract de închiriere între proprietar și chiriaș?
**Răspuns**: Un contract de închiriere între proprietar și chiriaș ar trebui să conțină următoarele informații:

- identitatea locatorului și a locatarului (nume, cod de identificare personal, date de contact);
- descrierea imobilului care urmează să fi…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Despre contractul de locațiune (închiriere)']

### locuire-04 — locuire / easy
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile proprietarului (locatorului)']

### locuire-07 — locuire / easy
**Întrebare**: Care sunt obligațiile mele ca proprietar într-o asociație de proprietari?
**Răspuns**: Să anunți președintele asociației cu privire la orice schimbare intervenită la structura și numărul membrilor familiei, a persoanelor luate în spațiu sau a chiriașilor/comodatarilor, în termen de 10 zile de la schimbare, în scris; Să menții…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌Atribuțiile asociației de proprietari sunt:', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari?']

### locuire-09 — locuire / medium
**Întrebare**: Sunt cetățean al unui stat UE. În ce condiții pot cumpăra o casă în România?
**Răspuns**: Pentru a cumpăra o casă în România fiind cetățean al unui stat membru al Uniunii Europene, este necesar să fie capabile să contracteze, să dea consimțământul în momentul contractării, obiectul contractului trebuie să se poată determina (în …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil?']

### locuire-10 — locuire / medium
**Întrebare**: Sunt cetățean al unui stat non-UE. Pot cumpăra un imobil în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!']

### locuire-11 — locuire / medium
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Obligațiile chiriașului (locatarului)']

### locuire-12 — locuire / medium
**Întrebare**: Sunt cetățean turc. Pot cumpăra un apartament în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Sunt cetățean român']

### locuire-15 — locuire / hard
**Întrebare**: Care sunt drepturile mele dacă sunt proprietarul unui apartament și membru al asociației de proprietari?
**Răspuns**: Ca proprietar al unui apartament și membru al asociației de proprietari, ai următoarele drepturi:
- Să participi și să votezi la adunarea generală a respectivei asociații;
- Să îți înscrii candidatura, să candidezi, să alegi și să fii ales …
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌Atribuțiile asociației de proprietari sunt:', 'Locuire']

### locuire-16 — locuire / hard
**Întrebare**: Vreau să închiriez locuința altcuiva și nu vrem să încheiem contract în scris. E legal?
**Răspuns**: Nu am suficiente informațiilor în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Proprietarul vrea să mă dea afară - ce pot face?', 'Locuire > Despre contractul de comodat (împrumut de folosință)', 'Locuire']

### locuire-17 — locuire / hard
**Întrebare**: Sunt cetățean român, vreau să cumpăr un imobil împreună cu un partener cetățean turc. Există restricții?
**Răspuns**: Nu am suficiente informațiilor în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?']

### locuire-18 — locuire / hard
**Întrebare**: Care e diferența între un cetățean UE și unul non-UE când vine vorba despre cumpărarea unui imobil în România?
**Răspuns**: Cetățenii statelor terțe (non-UE) pot dobânda drept de proprietate asupra construcțiilor și drept de superficie (un drept de folosință pe durata existenței construcției) asupra terenurilor, în situația în care doresc să cumpere imobile în R…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European']
