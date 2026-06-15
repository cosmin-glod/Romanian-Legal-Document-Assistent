# Raport evaluare

**Model**: `qwen2.5:3b-instruct-fp16`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 68

## Metrici globale

- Refusal accuracy: **78%** (53/68)
- Breadcrumb recall@4 (excl. refusal cases): **93%** (52/56)
- Keyword coverage (cazuri non-refusal): **53%** (56 cazuri)
- Contract pass rate (R1..R6): **68%** (46/68)
- Latency medie: **22.9s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 22 | 73% | 100% | 59% | 23.7s |
| locuire | 22 | 77% | 100% | 77% | 20.5s |
| nastere | 24 | 83% | 80% | 67% | 24.3s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 36 | 75% | 88% | 72% |
| medium | 20 | 90% | 95% | 70% |
| hard | 12 | 67% | 100% | 50% |

## Distribuția violărilor de contract

- `R4_FABRICATED_DOC`: 17
- `R7_OVERREFUSAL`: 6
- `R2_UNCITED`: 2
- `R6_FORM_ID_IN_DOCS`: 1

## Cazuri cu probleme (33)


### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: În România, nașterea unui copil născut într-un spital trebuie înregistrată la Primăria locală unde se desfășoară evenimentul. Documentele necesare includ: Actele de identitate ale părinților; Certificatul medical constatator al nașterii car…
**Status**: recall=False · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']

### nastere-04 — nastere / easy
**Întrebare**: Am născut acasă, nu într-un spital. Cum obțin certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii trebuie eliberați de la medicul de familie sau spitalul pe raza căruia a avut loc nașterea. Documentele necesare sunt: Actele tale de identitate și ale partenerului/partenerei (părinții); Certifi…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România']

### nastere-05 — nastere / easy
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Certificatul de naștere al mamei; Actele de identitate ale tale și ale partenerului/partenerei (buletin sau carte de identitate, etc.). Aceste documente sunt necesare pentru înregistrarea nașterii. De asemenea, este recomandabil să solicita…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-08 — nastere / easy
**Întrebare**: Ce este certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii este un document medical pe care îl vei primi de la spitalul sau clinica unde ai născut. Este eliberați de către medicul care a asistat la nașterea și nu ține loc loc certificatului de naștere.
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în străinătate']

### nastere-09 — nastere / medium
**Întrebare**: Am născut în străinătate. Ce trebuie să fac pentru ca nașterea să fie recunoscută în România?
**Răspuns**: În România, pentru a recunoaște nașterea unui copil străin născut în România, va trebui să faci următoarele documente și proceduri: Certificatul medical constatator al nașterii care trebuie să poarte număr de înregistrare, dată certă, sigil…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul']

### nastere-14 — nastere / medium
**Întrebare**: Ce este stimulentul de inserție și în ce condiții îl primesc?
**Răspuns**: Stimulantul de inserție este un ajutor financiar disponibil la nivel local, nu național. Este acordat părinților care se întorc la serviciu sau la job după ce copilul împlinește 6 luni. Valoarea stimulentului variază în funcție de perioada …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
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

### nastere-18 — nastere / hard
**Întrebare**: Părinții au nume de familie diferite. Ce nume va purta copilul?
**Răspuns**: Pentru a determina numele pe care îl va avea copilul, părinții trebuie să stabilească un acord în privința acestui aspect sau să solicite ajutor la instanță de tutelă pentru a lua decizia finală. Nu am suficiente informații în sursele dispo…
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-19 — nastere / hard
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: În acest caz, pentru a stabili paternitatea legală, mama copilului trebuie să își prezinte următoarele documente:

- Certificatul de naștere al mamei;
- Actele de identitate ale tale și ale partenerului/partenerei (buletin sau carte de iden…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-20 — nastere / hard
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Pentru a obține un certificat de naștere românesc pentru copilul dumneavoastră născut în Franța, cu ambele cetățeniile (românească și franceză), urmează procedura următoare:

1. Cereri de transcriere la Ambasada României din Franța sau Cons…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-21 — nastere / easy
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: Pentru a schimba un buletin la vârsta de 14 ani după naștere, trebuie să consultați Serviciul de Stare Civilă al Primăriei în care aveți domiciliu. Voi fi solicitat să prezentați următoarele documente:

- Actul de identitate (buletin sau ca…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-23 — nastere / easy
**Întrebare**: Cum primesc pensie alimentară de la fostul soț pentru copilul nostru?
**Răspuns**: Pentru a primi pensie alimentară de la fostul soț pentru copilul tău, este necesar să urmăriți procesul legal specific al statelor/turismului în care locuiți. În general, această procedură include următoarele etape:

1. Declararea că fostul…
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
**Răspuns**: Nu, după căsătoria, nu puteți lua numele partenerului pe nume de familie. Acest lucru este specificat în [S2] [Căsătoria > Relația de cuplu].
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Suntem căsătoriți', 'Căsătoria > Ne căsătorim în România']

### casatorie-07 — casatorie / easy
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-08 — casatorie / easy
**Întrebare**: Pot purta un nume compus din numele ambilor soți?
**Răspuns**: Da, puteți purta un nume compus din numele ambilor soți. În declarația de recunoaștere a copilului, veți declara acest lucru în fața notarului sau a ofițerului de stare civilă.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Tatăl recunoaște copilul', 'Căsătoria > Ne căsătorim în România']

### casatorie-09 — casatorie / medium
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Pentru a oferi declarația de căsătorie și alte documente necesare pentru căsătoria în România, veți trebui să depuneti la primăria locului de domiciliu sau de reședință al unuia dintre voi. Documentele necesare includ:
1. Declarația de căsă…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-11 — casatorie / medium
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Vine aici o descriere a procedurii de căsătorește în străinătate, bazată pe informațiile furnizate și despre care sunt disponibil. Această descriere ar include detalii precum:

1. Certificatul de naștere pentru ambele persoane.
2. Actele de…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-12 — casatorie / medium
**Întrebare**: Care sunt pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin?
**Răspuns**: Pașii pentru depunerea declarației de căsătorie sunt următoresi:

1. Prezentați declarația de căsătorie.
2. Prima dovadă a domiciliului sau a reședinței cetățeanului român în străinătate.
3. Actele voastră de identitate (carte de identitate…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-13 — casatorie / medium
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!', 'Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România']

### casatorie-15 — casatorie / hard
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Pentru un partener cetățean străin, este important să verifice legislația națională și să alege regimul matrimonial.

1. **Legislația națională**: Verifică-le pentru a vedea dacă partenerul are drepturi speciale sau impedimente legale pentr…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-16 — casatorie / hard
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-20 — casatorie / easy
**Întrebare**: Cât costă oficierea unei căsătorii la primărie?
**Răspuns**: În cazul României, costurile unei căsătørile la primăria nu sunt specificate și pot varia. Este recomandat să consultați serviciul local al primăriei pentru informații precise despre costurile actuale.
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 2 - Oficierea căsătoriei']

### casatorie-21 — casatorie / easy
**Întrebare**: Cum împart pensia de soț decedat?
**Răspuns**: Pensia de soț decedat nu poate fi imputată pe partea fiecărui dintre soți. În cazul în care unul dintre voi este acordat cu o persoană pentru a-l ajuta, aceasta va primi pensia. Pentru alte cazuri, pensia de soț decedat nu poate fi imputată…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Locuire', 'Căsătoria > Regimul matrimonial > 📌 Separația de bunuri', 'Căsătoria > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Relația de cuplu']

### locuire-04 — locuire / easy
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: Da, este obligatoriu să faci un contract în scris pentru a proteja ambele părți ale acordului și pentru a clarifica condițiile de închiriere. Un exemplu de document care poate fi folosit este un contract de închiriere.
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

### locuire-12 — locuire / medium
**Întrebare**: Sunt cetățean turc. Pot cumpăra un apartament în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Sunt cetățean român']

### locuire-15 — locuire / hard
**Întrebare**: Care sunt drepturile mele dacă sunt proprietarul unui apartament și membru al asociației de proprietari?
**Răspuns**: Ca membru al unei asociații de proprietari, ai următoarele drepturi: Să participi și să votezi la adunarea generală a respectivei asociații; Să îți înscrii candidatura, să candidezi, să alegi și să fii ales în structura organizatorică a aso…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌Atribuțiile asociației de proprietari sunt:', 'Locuire']

### locuire-16 — locuire / hard
**Întrebare**: Vreau să închiriez locuința altcuiva și nu vrem să încheiem contract în scris. E legal?
**Răspuns**: Contractul de închiriere nu trebuie să fie încheiat în fața unui notar. Este suficient dacă proprietarul (locatorul) și chiriașul (locatarul) au un contract în formă scrisă și semnat de amândoi. Atenție! Începând cu 1 ianuarie 2023, proprie…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Proprietarul vrea să mă dea afară - ce pot face?', 'Locuire > Despre contractul de comodat (împrumut de folosință)', 'Locuire']

### locuire-17 — locuire / hard
**Întrebare**: Sunt cetățean român, vreau să cumpăr un imobil împreună cu un partener cetățean turc. Există restricții?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?']

### locuire-21 — locuire / easy
**Întrebare**: Cum obțin un certificat de urbanism pentru a construi o casă pe terenul meu?
**Răspuns**: Obținându-ți un certificat de urbanism pentru a construi o casă pe terenul tău implică următoarele etape principale:

1. Contactează autoritățile locale: Începe cu contactarea autorităților locale responsabile pentru planificarea și urbanis…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > În ce condiții pot să vând un imobil? > 📌 De ce acte am nevoie?', 'Locuire > Nu am reședința în România > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Am reședința în România > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Sunt cetățean român > 📌 Ce acte trebuie să aducă vânzătorul?']
