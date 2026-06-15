# Raport evaluare

**Model**: `qwen2.5:3b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 30

## Metrici globale

- Refusal accuracy: **67%** (20/30)
- Breadcrumb recall@4 (excl. refusal cases): **75%** (18/24)
- Keyword coverage (cazuri non-refusal): **32%** (24 cazuri)
- Contract pass rate (R1..R6): **70%** (21/30)
- Latency medie: **90.0s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 10 | 60% | 88% | 80% | 162.1s |
| locuire | 10 | 70% | 88% | 80% | 30.2s |
| nastere | 10 | 70% | 50% | 50% | 77.5s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 15 | 87% | 78% | 73% |
| medium | 9 | 56% | 56% | 56% |
| hard | 6 | 33% | 100% | 83% |

## Distribuția violărilor de contract

- `R4_FABRICATED_DOC`: 10
- `R2_UNCITED`: 3

## Cazuri cu probleme (19)


### nastere-01 — nastere / easy
**Întrebare**: Ce documente îmi trebuie pentru înregistrarea nașterii copilului meu, dacă sunt căsătorit cu partenera?
**Răspuns**: Nașterea copilului este înregistrată în conformitate cu procedurile specificate pentru părinți care sunt căsătoriți. Documentele necesare includ:
- Actele de identitate ale tale și ale partenerului/partenerei (buletin sau carte de identitat…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-02 — nastere / easy
**Întrebare**: Cine eliberează certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii este eliberați de medicul care a asistat la naștere sau de medicul șef de secție de obstetrică-ginecologie.
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate']

### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: Nașterea unui copil care a fost născut într-un spital în România se înregistrează la Serviciul de Stare Civil al primăriei unde locuiește parintii. Dacă parțenerul/partenera nu locuiește în aceeași primarie, procedura poate varia.
**Status**: recall=False · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']

### nastere-04 — nastere / medium
**Întrebare**: Am născut în străinătate. Ce trebuie să fac pentru ca nașterea să fie recunoscută în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul']

### nastere-05 — nastere / medium
**Întrebare**: Cine poate primi indemnizația pentru creșterea copilului?
**Răspuns**: Părinții firești ai copilului, adoptatorii, persoana căreia i s-a încredințat copilul în vederea adopției sau care are copilul în plasament sau regim de urgență, asistentul maternal și tutorele pot primi indemnizația pentru creșterea copilu…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Stimulentul de inserție']

### nastere-06 — nastere / medium
**Întrebare**: Ce alocații financiare primesc părinții pentru un nou-născut?
**Răspuns**: 719 RON pentru copiii cu vârste între 0 și 2 ani; 292 RON pentru copiii cu vârsta de peste 2 ani.
**Status**: recall=False · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Municipiul Constanța', 'Nașterea > Municipiul București', 'Nașterea > Municipiul Făgăraș', 'Nașterea > Copilul nu este încadrat într-un grad de handicap']

### nastere-07 — nastere / hard
**Întrebare**: Nu sunt căsătorit cu mama copilului. Cum recunosc legal copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-09 — nastere / easy
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: În România, pentru a schimba un buletin la vârsta de 14 ani după născut, părinții trebuie să își prezinte documentele corespunzătoare Serviciului de Stare Civil. Acestea includ:

- Actul de identitate al părintelui (buletin, carte de identi…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### casatorie-03 — casatorie / easy
**Întrebare**: Sunt deja căsătorit. Pot încheia o nouă căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Monogamie', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex']

### casatorie-04 — casatorie / medium
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Pentru căsătoria, la primăria localității unde îşi are domiciliul sau reședința unul dintre voi (și chiar și în afara sediului, de exemplu, la grădini publice, parcuri, muzee, plaje etc.) trebuie depusă următoarele documente în original: De…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-05 — casatorie / medium
**Întrebare**: Ce nume de familie pot să aleg după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-06 — casatorie / medium
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-07 — casatorie / hard
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Pentru căsătoria cu un partener cetățean străin, veți necesita informațiile următoare înainte de căsătorie:

1. Documente necesare pentru declarația de căsătorie: 
- Declarația de căsătorie
- Dovadă a domiciliului sau a reședinței cetățeanu…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-08 — casatorie / hard
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### locuire-03 — locuire / easy
**Întrebare**: Ce trebuie să conțină un contract de închiriere între proprietar și chiriaș?
**Răspuns**: Un contract de închiriere între proprietar și chiriaș ar trebui să conțină următoarele informații:
1. Identitatea locatorului și a locatarului (nume, cod de identificare personal, date de contact).
2. Descrierea imobilului care urmează să f…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Despre contractul de locațiune (închiriere)']

### locuire-04 — locuire / medium
**Întrebare**: Sunt cetățean al unui stat UE. În ce condiții pot cumpăra o casă în România?
**Răspuns**: Pentru a cumpăra o casă în România fiind cetățean al unui stat membru al Uniunii Europene, obiectul contractului trebuie să se poată determina (în acest caz respectivul imobil - casă) și cauza pentru care se încheie contractul trebuie să fi…
**Status**: recall=False · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil?']

### locuire-05 — locuire / medium
**Întrebare**: Sunt cetățean al unui stat non-UE. Pot cumpăra un imobil în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!']

### locuire-07 — locuire / hard
**Întrebare**: Care sunt drepturile mele dacă sunt proprietarul unui apartament?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire', 'Locuire > Relația cu asociația de proprietari > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Obligațiile proprietarului (locatorului)']

### locuire-08 — locuire / hard
**Întrebare**: Vreau să închiriez locuința altcuiva. Trebuie să încheiem contract în scris?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Despre contractul de locațiune (închiriere)']
