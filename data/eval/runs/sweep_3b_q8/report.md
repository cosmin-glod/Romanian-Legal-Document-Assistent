# Raport evaluare

**Model**: `qwen2.5:3b-instruct-q8_0`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 68

## Metrici globale

- Refusal accuracy: **79%** (54/68)
- Breadcrumb recall@4 (excl. refusal cases): **93%** (52/56)
- Keyword coverage (cazuri non-refusal): **52%** (56 cazuri)
- Contract pass rate (R1..R6): **74%** (50/68)
- Latency medie: **15.1s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 22 | 77% | 100% | 73% | 18.0s |
| locuire | 22 | 82% | 100% | 86% | 11.8s |
| nastere | 24 | 79% | 80% | 62% | 15.6s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 36 | 81% | 88% | 83% |
| medium | 20 | 80% | 95% | 60% |
| hard | 12 | 75% | 100% | 67% |

## Distribuția violărilor de contract

- `R4_FABRICATED_DOC`: 10
- `R7_OVERREFUSAL`: 8
- `R3_BAD_CITATION`: 6
- `R6_FORM_ID_IN_DOCS`: 4
- `R2_UNCITED`: 2
- `R5_REFUSAL_WITH_DOCS`: 1

## Cazuri cu probleme (26)


### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: În România, nașterea unui copil născut într-un spital trebuie înregistrată la Primăria locală unde se desfășoară evenimentul. Documentele necesare includ: Actele de identitate ale părinților; Certificatul medical constatator al nașterii car…
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']

### nastere-04 — nastere / easy
**Întrebare**: Am născut acasă, nu într-un spital. Cum obțin certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii trebuie eliberați de la medicul de familie sau spitalul pe raza căruia a avut loc nașterea. Documentele necesare sunt: Actele tale de identitate și ale partenerului/partenerei (părinții); Certifi…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România']

### nastere-05 — nastere / easy
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-08 — nastere / easy
**Întrebare**: Ce este certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii este un document medical pe care îl vei primi de la spitalul sau clinica unde ai născut. Este eliberați de către medicul care a asistat la nașterea și nu ține loc certificatului de naștere.
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în străinătate']

### nastere-09 — nastere / medium
**Întrebare**: Am născut în străinătate. Ce trebuie să fac pentru ca nașterea să fie recunoscută în România?
**Răspuns**: În România, pentru a recunoaște nașterea unui copil străin născut în România, va trebui să faci următoarele documente și proceduri: Certificatul medical constatator al nașterii care trebuie să poarte număr de înregistrare, dată certă, sigil…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul']

### nastere-11 — nastere / medium
**Întrebare**: Ce alocații financiare primesc părinții pentru un nou-născut?
**Răspuns**: Părinții pentru un nou-născut pot primi alocațiile financiare următoare: 

- Municipiul Constanța: 2000 RON prin card securizat.
- Municipiul București: 2500 RON dacă cel puțin un părinte are domiciliu sau reședința în municipiul București …
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Municipiul Constanța', 'Nașterea > Municipiul București', 'Nașterea > Municipiul Făgăraș', 'Nașterea > Copilul nu este încadrat într-un grad de handicap']

### nastere-14 — nastere / medium
**Întrebare**: Ce este stimulentul de inserție și în ce condiții îl primesc?
**Răspuns**: Stimulantul de inserție este un ajutor financiar disponibil la nivel local, nu național. Este acordat părinților care se întorc la serviciu sau la job după ce copilul împlinește 6 luni. Valoarea stimulentului variază în funcție de perioada …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Stimulentul de inserție', 'Nașterea > Stimulentul de inserție', 'Nașterea > Stimulentul de inserție', 'Nașterea > Stimulente pentru nou-născut']

### nastere-15 — nastere / medium
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Înregistrarea nașterei unui copil străin născut în România se poate face la ambasada sau consulatul țării de cetățenie și depinde de legile acesteia. Dacă țara de cetățenie nu are o ambasadă sau un consulat în România, va trebui să verifici…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-17 — nastere / hard
**Întrebare**: Nu sunt căsătorit cu mama copilului. Cum recunosc legal copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-19 — nastere / hard
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: În acest caz, părinții pot stabili paternitatea prin hotărâre judecătorească. Mama are dreptul de a porni o acțiune în stabilirea paternității în numele copilului.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-20 — nastere / hard
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Pentru a obține un certificat de naștere românesc pentru copilul dumneavoastră născut în Franța, procedura este următoarea:

1. Cereri de transcriere la Ambasada României din Franța sau Consularul României din Franța.
2. Documente necesare:…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-23 — nastere / easy
**Întrebare**: Cum primesc pensie alimentară de la fostul soț pentru copilul nostru?
**Răspuns**: Pentru a primi pensie alimentară de la fostul soț pentru copilul tău, este recomandabil să consultați documentele oferite de Agenția pentru Plăți și Inspecție Socială (APIS). Această instituție va oferi informații despre procesul de solicit…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului']

### casatorie-04 — casatorie / easy
**Întrebare**: Pot să mă căsătoresc la 16 ani?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-05 — casatorie / easy
**Întrebare**: Pot să iau numele partenerului ca nume de familie după căsătorie?
**Răspuns**: Nu, după căsătoria, nu puteți lua numele partenerului ca nume de familie. Acest lucru trebuie să fie declarat în scris în fața ofițerului de stare civilă sau a notarului.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Suntem căsătoriți', 'Căsătoria > Ne căsătorim în România']

### casatorie-09 — casatorie / medium
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Pentru a oferi declarația de căsătorie și alte documente necesare pentru căsătoria în România, veți trebui să depuneti la primăria locală unde îl are domiciliul sau reședința unul dintre voi. Documentele necesare includ:
1. Declarația de că…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-12 — casatorie / medium
**Întrebare**: Care sunt pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin?
**Răspuns**: Pașii pentru depunerea declarației de căsătorie sunt următoresi:

1. Prezentați declarația de căsătorie.
2. Prima dovadă a domiciliului sau a reședinței cetățeanului român în străinătate.
3. Actele voastră de identitate (carte de identitate…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R3_BAD_CITATION', 'R3_BAD_CITATION', 'R3_BAD_CITATION', 'R3_BAD_CITATION', 'R3_BAD_CITATION', 'R3_BAD_CITATION']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-13 — casatorie / medium
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!', 'Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România']

### casatorie-14 — casatorie / medium
**Întrebare**: Am încheiat căsătoria în străinătate. Cum o transcriu/recunosc în România?
**Răspuns**: Pentru recunoaștere a căsătoriei în România după încheierea acesteia în străinătate, este recomandat să folosiți un document scris în limba română care să includă informațiile necesare. Nu există o formular oficial de recunoaștere a căsător…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R6_FORM_ID_IN_DOCS', 'R6_FORM_ID_IN_DOCS', 'R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-16 — casatorie / hard
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-20 — casatorie / easy
**Întrebare**: Cât costă oficierea unei căsătorii la primărie?
**Răspuns**: În cazul României, costurile unei căsătørile la primăria nu sunt specificate și pot varia. Este recomandat să consultați serviciul local pentru informații precise.
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 2 - Oficierea căsătoriei']

### casatorie-21 — casatorie / easy
**Întrebare**: Cum împart pensia de soț decedat?
**Răspuns**: Pensia de soț decedat nu poate fi imputată pe partea fiecărui dintre soți. În cazul în care unul dintre soți este decedat, pensia se împarte întotdeauna la celălalt soț.[S1]
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Locuire', 'Căsătoria > Regimul matrimonial > 📌 Separația de bunuri', 'Căsătoria > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Relația de cuplu']

### locuire-05 — locuire / easy
**Întrebare**: Care sunt obligațiile proprietarului față de chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile chiriașului (locatarului)']

### locuire-11 — locuire / medium
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu exactitate despre plata chiriei în contractele de închiriere (locațiune). Pentru detalii precise, este recomandat să consultați documentul oficial sau să contactați aut…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Obligațiile chiriașului (locatarului)']

### locuire-12 — locuire / medium
**Întrebare**: Sunt cetățean turc. Pot cumpăra un apartament în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Sunt cetățean român']

### locuire-16 — locuire / hard
**Întrebare**: Vreau să închiriez locuința altcuiva și nu vrem să încheiem contract în scris. E legal?
**Răspuns**: Contractul de închiriere nu trebuie să fie încheiat în fața unui notar. Este suficient dacă proprietarul (locatorul) și chiriașul (locatarul) au un contract în formă scrisă și semnat de amândoi. Atenție! Începând cu 1 ianuarie 2023, proprie…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Proprietarul vrea să mă dea afară - ce pot face?', 'Locuire > Despre contractul de comodat (împrumut de folosință)', 'Locuire']

### locuire-17 — locuire / hard
**Întrebare**: Sunt cetățean român, vreau să cumpăr un imobil împreună cu un partener cetățean turc. Există restricții?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?']
