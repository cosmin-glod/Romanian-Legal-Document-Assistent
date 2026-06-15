# Raport evaluare

**Model**: `qwen2.5:3b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 68

## Metrici globale

- Refusal accuracy: **53%** (36/68)
- Breadcrumb recall@4 (excl. refusal cases): **93%** (52/56)
- Keyword coverage (cazuri non-refusal): **31%** (56 cazuri)
- Contract pass rate (R1..R6): **50%** (34/68)
- Latency medie: **68.9s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 22 | 41% | 100% | 45% | 147.1s |
| locuire | 22 | 50% | 100% | 59% | 9.9s |
| nastere | 24 | 67% | 80% | 46% | 51.2s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 36 | 56% | 88% | 56% |
| medium | 20 | 50% | 95% | 45% |
| hard | 12 | 50% | 100% | 42% |

## Distribuția violărilor de contract

- `R7_OVERREFUSAL`: 23
- `R4_FABRICATED_DOC`: 13
- `R2_UNCITED`: 3
- `R3_BAD_CITATION`: 2
- `R1_EMPTY`: 1

## Cazuri cu probleme (43)


### nastere-01 — nastere / easy
**Întrebare**: Ce documente îmi trebuie pentru înregistrarea nașterii copilului meu, dacă sunt căsătorit cu partenera?
**Răspuns**: Pentru înregistrarea nașterii copilului dvs., următoarele documente sunt necesare:
1. Actele de identitate (în calitate de părinți) - pentru ambele persoane.
2. Certificatul medical constatator al nașterii care trebuie să poată fi înregistr…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: Nu am suficiente informațiuni în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']

### nastere-04 — nastere / easy
**Întrebare**: Am născut acasă, nu într-un spital. Cum obțin certificatul medical constatator al nașterii?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România']

### nastere-05 — nastere / easy
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-07 — nastere / easy
**Întrebare**: Cine eliberează certificatul de naștere al copilului meu?
**Răspuns**: Certificatul de naștere al copilului este eliberat de spitalul sau medicul de familie.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Tatăl recunoaște copilul']

### nastere-08 — nastere / easy
**Întrebare**: Ce este certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii e un document medical pe care îl vei primi de la spitalul sau clinica unde ai născut. Este un document care este eliberal în termen de 24 de ore de către medicul care a asistat, a supravegheat sa…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în străinătate']

### nastere-11 — nastere / medium
**Întrebare**: Ce alocații financiare primesc părinții pentru un nou-născut?
**Răspuns**: Părinții pot primi următoarele alocați financiare pentru un nou-născut în funcție de locația lor și condițiile specifice ale fiecărui program:
- În Constanța: 2000 RON (prin intermediul cardului securizat)
- În București: 2500 RON
- În Făgă…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Municipiul Constanța', 'Nașterea > Municipiul București', 'Nașterea > Municipiul Făgăraș', 'Nașterea > Copilul nu este încadrat într-un grad de handicap']

### nastere-12 — nastere / medium
**Întrebare**: Pe ce perioadă se acordă indemnizația pentru creșterea copilului?
**Răspuns**: Nu am suficiente informațiuni în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului']

### nastere-13 — nastere / medium
**Întrebare**: Am primit certificatul de naștere al copilului în străinătate. Cum îl transcriu pe cel românesc?
**Răspuns**: 
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R1_EMPTY', 'R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Cel puțin un părinte are domiciliul în România', 'Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România']

### nastere-15 — nastere / medium
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-17 — nastere / hard
**Întrebare**: Nu sunt căsătorit cu mama copilului. Cum recunosc legal copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-19 — nastere / hard
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: <p>În România, pentru a stabili paternitatea legală pentru un copil născut în afara căsătoriei, tatăl trebuie să recunoască copilul sau mama copilului (care este mamă singură) trebuie să solicite o hotărâre judecătorească. Această hotărâre …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul']

### nastere-20 — nastere / hard
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Pentru a obține un certificat de naștere românesc pentru copilul dumneavoastră care s-a născut în Franța, cu ambele cetăți (româna și franceză), urmați pasurile de mai jos. Este important să vă asigurați că certificatul este transcris la Am…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României']

### nastere-21 — nastere / easy
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: Pentru a schimba buletinul la 14 ani după naștere în România, trebuie să urmați pasurile deaselețenie. Aceasta implică prezentarea unor documente specificate și potențial o traducere legalizată pentru datele tale de identificare dacă aceste…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Tatăl nu recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-23 — nastere / easy
**Întrebare**: Cum primesc pensie alimentară de la fostul soț pentru copilul nostru?
**Răspuns**: Pentru a prim pensia alimentară de la fostul soț pentru copilul tău, trebuie să îndeplinești cerințele specifice ale sistemului de pensii alimentare. Acestea includ: 

1. Afișarea înainte de judecător și aprobarea penitentiei.
2. Încarcarea…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului', 'Nașterea > Indemnizația pentru creșterea copilului']

### casatorie-03 — casatorie / easy
**Întrebare**: Sunt deja căsătorit. Pot încheia o nouă căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Monogamie', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex']

### casatorie-04 — casatorie / easy
**Întrebare**: Pot să mă căsătoresc la 16 ani?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-05 — casatorie / easy
**Întrebare**: Pot să iau numele partenerului ca nume de familie după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Suntem căsătoriți', 'Căsătoria > Ne căsătorim în România']

### casatorie-06 — casatorie / easy
**Întrebare**: Există rude apropiate cu care nu mă pot căsători?
**Răspuns**: Rudenia este în linie colaterală atunci când rezultă din faptul că mai multe persoane au un ascendent comun. Rudenia se stabilește astfel: în linie dreaptă, după numărul naşterilor; iar în linie colaterală, după numărul naşterilor, urcând d…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria între rude', 'Căsătoria > Condiții pentru a te căsători > 📌 Persoana pusă sub o măsură de ocrotire specială', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex', 'Căsătoria > Condiții pentru a te căsători > 📌 Monogamie']

### casatorie-07 — casatorie / easy
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-08 — casatorie / easy
**Întrebare**: Pot purta un nume compus din numele ambilor soți?
**Răspuns**: Nu, în România, copiii născuți de părinți căsătoriți nu pot purta un nume compus din numele ambilor soți. Dacă ați convenit să purtați un nume diferit, atunci acesta va fi folosit pentru nașterea copilului.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Tatăl recunoaște copilul', 'Căsătoria > Ne căsătorim în România']

### casatorie-10 — casatorie / medium
**Întrebare**: Ce nume de familie pot să aleg după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Relația de cuplu', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România']

### casatorie-11 — casatorie / medium
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
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
**Răspuns**: Suplimentar pentru un partener cetățean străin, veți avea nevoie să știeți câteva aspecte importante înainte de căsătoria. Acestea includ: 

1. **Cetățenia și legislația**: Voi trebui să știți dacă partenerul dumneavoastră are cetățenie sau…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']

### casatorie-16 — casatorie / hard
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-18 — casatorie / hard
**Întrebare**: Partenerul meu nu cunoaște limba română. Ce este obligatoriu la oficierea căsătoriei?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Partenerul este cetățean străin > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în România']

### casatorie-20 — casatorie / easy
**Întrebare**: Cât costă oficierea unei căsătorii la primărie?
**Răspuns**: În România, costurile de oficieri de căsătământ nu sunt specificate în documentele disponibile. Costurile pot varia în funcție de diverse factori, cum ar fi localitatea unde se desfășoară oficierile și numărul de martori necesari. În genera…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Ne căsătorim în România', 'Căsătoria > Partenerul este cetățean străin > 📌 PASUL 2 - Oficierea căsătoriei']

### casatorie-21 — casatorie / easy
**Întrebare**: Cum împart pensia de soț decedat?
**Răspuns**: Pensia de soț decedat nu este în regimul matrimonial, ci reprezintă o sumă care se pune la dispoziția unui singur persoană. Nu există documente sau proceduri specific pentru împărțirea pensiei de soț. Pentru informații precise, este recoman…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Locuire', 'Căsătoria > Regimul matrimonial > 📌 Separația de bunuri', 'Căsătoria > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Relația de cuplu']

### locuire-02 — locuire / easy
**Întrebare**: Ce acte îmi trebuie ca cumpărător al unui imobil în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Nu am reședința în România > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Sunt cetățeanul unui alt stat > 📌 De ce acte am nevoie?', 'Locuire > Am reședința în România > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Am reședința în România > 📌 De ce acte am nevoie?']

### locuire-04 — locuire / easy
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
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

### locuire-10 — locuire / medium
**Întrebare**: Sunt cetățean al unui stat non-UE. Pot cumpăra un imobil în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Partenerul este cetățean străin > ⚠️ ATENȚIE!']

### locuire-11 — locuire / medium
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Drepturile proprietarului (locatorului)', 'Locuire > Obligațiile proprietarului (locatorului)', 'Locuire > Obligațiile chiriașului (locatarului)', 'Locuire > Obligațiile chiriașului (locatarului)']

### locuire-12 — locuire / medium
**Întrebare**: Sunt cetățean turc. Pot cumpăra un apartament în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Sunt cetățean român']

### locuire-14 — locuire / medium
**Întrebare**: Care sunt drepturile mele ca membru al unei asociații de proprietari?
**Răspuns**: Ca membru al unei asociații de proprietari, ai următoarele drepturi:
- Să participi și să votezi la adunarea generală a respectivei asociații;
- Să îți înscrii candidatura, să candidezi, să alegi și să fii ales în structura organizatorică a…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R3_BAD_CITATION', 'R3_BAD_CITATION', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌Atribuțiile asociației de proprietari sunt:', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari?']

### locuire-15 — locuire / hard
**Întrebare**: Care sunt drepturile mele dacă sunt proprietarul unui apartament și membru al asociației de proprietari?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌Atribuțiile asociației de proprietari sunt:', 'Locuire']

### locuire-16 — locuire / hard
**Întrebare**: Vreau să închiriez locuința altcuiva și nu vrem să încheiem contract în scris. E legal?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Despre contractul de locațiune (închiriere)', 'Locuire > Proprietarul vrea să mă dea afară - ce pot face?', 'Locuire > Despre contractul de comodat (împrumut de folosință)', 'Locuire']

### locuire-17 — locuire / hard
**Întrebare**: Sunt cetățean român, vreau să cumpăr un imobil împreună cu un partener cetățean turc. Există restricții?
**Răspuns**: Nu am suficiente informațiilor în surse disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Condiții pentru a te căsători > 📌 Căsătoria dintre persoanele de același sex', 'Locuire > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?']

### locuire-21 — locuire / easy
**Întrebare**: Cum obțin un certificat de urbanism pentru a construi o casă pe terenul meu?
**Răspuns**: Obținându-vă un certificat de urbanism pentru a construi o casă pe terenul vău implică câteva etape importante. Înainte de a continua cu procesul, vă recomandăm să consultați autoritățile locale pentru informații specifice și regulamentele …
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > În ce condiții pot să vând un imobil? > 📌 De ce acte am nevoie?', 'Locuire > Nu am reședința în România > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Am reședința în România > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Sunt cetățean român > 📌 Ce acte trebuie să aducă vânzătorul?']
