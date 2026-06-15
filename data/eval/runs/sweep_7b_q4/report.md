# Raport evaluare

**Model**: `qwen2.5:7b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 68

## Metrici globale

- Refusal accuracy: **66%** (45/68)
- Breadcrumb recall@4 (excl. refusal cases): **93%** (52/56)
- Keyword coverage (cazuri non-refusal): **56%** (56 cazuri)
- Contract pass rate (R1..R6): **68%** (46/68)
- Latency medie: **32.9s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 22 | 50% | 100% | 55% | 32.0s |
| locuire | 22 | 77% | 100% | 73% | 27.1s |
| nastere | 24 | 71% | 80% | 75% | 39.0s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 36 | 72% | 88% | 75% |
| medium | 20 | 60% | 95% | 60% |
| hard | 12 | 58% | 100% | 58% |

## Distribuția violărilor de contract

- `R7_OVERREFUSAL`: 18
- `R4_FABRICATED_DOC`: 15
- `R6_FORM_ID_IN_DOCS`: 2
- `R5_REFUSAL_WITH_DOCS`: 2
- `R2_UNCITED`: 1

## Cazuri cu probleme (30)


### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: Nașterea va fi înregistrată la Serviciul de Stare Civilă din primăria localității unde a avut loc nașterea. Pentru acest proces, veți aveți nevoie să furnizați următoarele documente: Certificatul medical constatator al nașterii care trebuie…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']

### nastere-04 — nastere / easy
**Întrebare**: Am născut acasă, nu într-un spital. Cum obțin certificatul medical constatator al nașterii?
**Răspuns**: Dacă ai născut acasă, nu într-un spital, puteți solicita o declarație privind nașterea la primăria localității unde locuiești sau unde vrei să înregistrezi nașterea. Această declarație va fi suplimentar confirmată de autorități locale și va…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România']

### nastere-08 — nastere / easy
**Întrebare**: Ce este certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii este un document medical emis de medicul care a asistat, supravegheat sau constatat nașterea. Acest document nu înlocuiește certificatul de naștere și trebuie obținut de la spitalul unde a avut l…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în străinătate']

### nastere-11 — nastere / medium
**Întrebare**: Ce alocații financiare primesc părinții pentru un nou-născut?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre sumele de sprijin financiar acordate părinților pentru copiii născuți. Sursa necesară nu este menționată în documente disponibile.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Municipiul Constanța', 'Nașterea > Municipiul București', 'Nașterea > Municipiul Făgăraș', 'Nașterea > Copilul nu este încadrat într-un grad de handicap']

### nastere-12 — nastere / medium
**Întrebare**: Pe ce perioadă se acordă indemnizația pentru creșterea copilului?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre indemnizația lunară de creștere a copilului.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului']

### nastere-14 — nastere / medium
**Întrebare**: Ce este stimulentul de inserție și în ce condiții îl primesc?
**Răspuns**: Stimulentul de inserție este un ajutor financiar pentru părinți care se întorc la job după concediu de creștere a copilului. Pentru a primi acest stimulent, trebuie să îndeplinești unele condiții, cum ar fi a fi părinte și a fi aflat în con…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Stimulentul de inserție', 'Nașterea > Stimulentul de inserție', 'Nașterea > Stimulentul de inserție', 'Nașterea > Stimulente pentru nou-născut']

### nastere-15 — nastere / medium
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Da, puteți înregistra nașterea copilului dvs. la ambasada sau consulatul țării de cetățenie în România. Este important să verificați dacă țara dumneavoastră are o misiune diplomatice în România și să contactați direct această instituție pen…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-16 — nastere / medium
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la această întrebare. Vă rog să furnizați mai multe detalii sau documente specifice care să permită o răspuns mai precisă.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-17 — nastere / hard
**Întrebare**: Nu sunt căsătorit cu mama copilului. Cum recunosc legal copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dumneavoastră. Pentru recunoașterea legală a paternității, este necesar să consultați documentele și legi relevante din România.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-18 — nastere / hard
**Întrebare**: Părinții au nume de familie diferite. Ce nume va purta copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la această întrebare.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-19 — nastere / hard
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-21 — nastere / easy
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: Pentru a înregistra nașterea copilului, este necesar să furnizați următoarele documente, conform sursei 1 și 3:

- Actul de identitate al părintelui cetățean român (buletin, carte de identitate, etc.)
- Certificatul medical constatator al n…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### casatorie-03 — casatorie / easy
**Întrebare**: Sunt deja căsătorit. Pot încheia o nouă căsătorie?
**Răspuns**: Nu poți încheia o nouă căsătorie fiindcă ești deja căsătorit. Poligamia este interzisă în România.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Monogamie', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex']

### casatorie-04 — casatorie / easy
**Întrebare**: Pot să mă căsătoresc la 16 ani?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine privind vârsta de căsătorie. Te sfătuiesc să consultești un ofițer de stare civilă sau o autoritate locală pentru informații precise.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-07 — casatorie / easy
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre oficierea căsătoriei la ambasadele române din străinătate. Vă recomand să consultați site-ul oficial al Ministerului Internelor sau serviciile compet…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-10 — casatorie / medium
**Întrebare**: Ce nume de familie pot să aleg după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine. Poți lua fiecare numele pe care l-ați avut înainte de căsătorie, puteți lua amândoi numele unuia dintre soți sau puteți purta numele voastre reunite.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-11 — casatorie / medium
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre procedurile de căsătorie în străinătate. Vă recomand să consultați site-ul oficial al Ministerului Afacerilor Externe sau să vă adresați la sediul mi…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-12 — casatorie / medium
**Întrebare**: Care sunt pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu la întrebarea dvs. privind pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin. Surselor actuale nu le-am găsit în documentele …
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-13 — casatorie / medium
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre procedurile de apostilare sau legalizare a documentelor eliberate de statele membre ale Uniunii Europene în România. Vă recomand să consultați direct…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!', 'Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România']

### casatorie-15 — casatorie / hard
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dumneavoastră privind procedurile de căsătoria cu un partener cetățean străin. Vă recomand să consultați documentele oficiale sau să vă adresa…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-16 — casatorie / hard
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Pentru a vă căsătoriți, ambele părți trebuie să aveți cel puțin 18 ani, absența justificată de vârstă minimă fiind rară și necesitând permisiunea tutorelor sau a unui avocat. Dacă aveți amândoi peste 18 ani, puteți face o declarație de căsă…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED', 'R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-18 — casatorie / hard
**Întrebare**: Partenerul meu nu cunoaște limba română. Ce este obligatoriu la oficierea căsătoriei?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în România']

### casatorie-19 — casatorie / easy
**Întrebare**: Cum divorțez de partenerul meu?
**Răspuns**: Pentru divorț, trebuie să depuneti o cerere în primărie unde locuiești. Va trebui să furnizați documente precum actele de identitate, certificatul de naștere al copiilor dacă există și alte documente relevante. Dacă căsătoria a avut loc în …
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Proprietarul vrea să mă dea afară - ce pot face?', 'Căsătoria > Regimul matrimonial > 📌 Separația de bunuri', 'Căsătoria > Locuire', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-22 — casatorie / easy
**Întrebare**: Putem semna un contract prematrimonial înainte de căsătorie?
**Răspuns**: Da, puteți semna un contract prematrimonial înainte de căsătorie. În cazul în care alegeți ca regim matrimonial separaţia de bunuri sau comunitatea convenţională, este obligatoriu să prezentați în original, convenţia autentificată la un not…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Ne căsătorim în România']

### locuire-01 — locuire / easy
**Întrebare**: Sunt cetățean român și vreau să cumpăr un apartament. Care este primul pas?
**Răspuns**: Primul pas este de a duce-vă la notar, împreună cu vânzătorul, pentru achiziționarea imobilului. Notarul va asigura încheierea contractului și înregistrarea tranzacției.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Sunt cetățean român', 'Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Sunt cetățeanul unui alt stat']

### locuire-03 — locuire / easy
**Întrebare**: Ce trebuie să conțină un contract de închiriere între proprietar și chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu despre structura unui contract de închiriere. Sursa specifică nu conține aceste detalii.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Despre contractul de locațiune (închiriere)']

### locuire-04 — locuire / easy
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre contract de închiriere. Surselor nu mărește informații specifice privind cerințele legale sau procedurile asociate acestui tip de document.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile proprietarului (locatorului)']

### locuire-05 — locuire / easy
**Întrebare**: Care sunt obligațiile proprietarului față de chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dumneavoastră. Vă rog să furnizați mai multe detalii sau sursă specifică care să abordeze obligațiile proprietarului față de chiriaș.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile chiriașului (locatarului)']

### locuire-08 — locuire / easy
**Întrebare**: Care sunt obligațiile chiriașului față de proprietar?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre obligațiile chiriașului față de proprietar. Vă recomand să consultați documentul 'contract_inchiriere' pentru detalii specifice privind drepturile și…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R6_FORM_ID_IN_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Drepturile chiriașului (locatarului)']

### locuire-11 — locuire / medium
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu despre obligațiile chiriașului față de imobil. Sursa specifică acestea.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Obligațiile chiriașului (locatarului)']
