# Raport evaluare

**Model**: `qwen2.5:3b-instruct-q8_0`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 98

## Metrici globale

- Refusal accuracy: **74%** (73/98)
- Breadcrumb recall@4 (excl. refusal cases): **95%** (78/82)
- Keyword coverage (cazuri non-refusal): **51%** (82 cazuri)
- Contract pass rate (R1..R6): **69%** (68/98)
- Latency medie: **15.4s** per întrebare
- JSON invalid / generări runaway: **1** cazuri (din care 0 forțate la refuz; cea mai lungă ieșire: 2916 caractere)

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 30 | 70% | 100% | 67% | 14.9s |
| locuire | 33 | 73% | 96% | 85% | 13.7s |
| nastere | 35 | 80% | 90% | 57% | 17.4s |

## Distribuția violărilor de contract

- `R7_OVERREFUSAL`: 12
- `R4_FABRICATED_DOC`: 12
- `R2_UNCITED`: 10
- `R3_BAD_CITATION`: 1

## Generări runaway / JSON invalid (1)

| Caz | Parse fail | Forțat la refuz | Caractere max | Încercări |
|---|---|---|---|---|
| casatorie-15 | 1 | nu | 2916 | 2 |

## Cazuri cu probleme (43)


### nastere-01 — nastere
**Întrebare**: Ce documente îmi trebuie pentru înregistrarea nașterii copilului meu, dacă sunt căsătorit cu partenera?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul']

### nastere-05 — nastere
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Documentele necesare pentru înregistrarea nașterii copilului, în cazul în care tatăl recunoaște copilul și părinții nu sunt căsătoriți, includ:
- Certificatul de naștere al mamei
- Actul de identitate al mamei
- Certificatul medical constat…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul']

### nastere-09 — nastere
**Întrebare**: Am născut în străinătate. Ce trebuie să fac pentru ca nașterea să fie recunoscută în România?
**Răspuns**: În România, pentru a recunoași nașterea unui copil străin născut în România, trebuie să faci următoarele documente: Certificatul de naştere al mamei; Actele de identitate ale tale și ale partenerului/partenerei (buletin sau carte de identit…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul > Vreau să înregistrez nașterea la ambasada țării mele de origine']

### nastere-10 — nastere
**Întrebare**: Cine poate primi indemnizația pentru creșterea copilului?
**Răspuns**: Indemnizația pentru creșterea copilului poate fi primită de persoane care au fost încadrate într-o situație care le acordă dreptul la această indemnizare, conform regulilor și condițiilor specifice. În cazul dat, acesta include persoanele c…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-11 — nastere
**Întrebare**: Ce alocații financiare primesc părinții pentru un nou-născut?
**Răspuns**: Părinții pot primi stimulente financiare pentru nou-născut în sume diferite, dependând de localitatea. În București suma este de 2500 RON, în Constanța 2000 RON (cu card securizat) și în Făgăraș 1500 RON. Nu există informații despre alte su…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul București', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul Constanța', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul Făgăraș']

### nastere-12 — nastere
**Întrebare**: Pe ce perioadă se acordă indemnizația pentru creșterea copilului?
**Răspuns**: Indemnizația pentru creșterea copilului este acordată în perioada concediului de maternitate sau din momentul intrării în concediu de creștere copil, fără încetarea raportului de muncă. De asemenea, poate fi acordată și în cazuri precum îna…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-14 — nastere
**Întrebare**: Ce este stimulentul de inserție și în ce condiții îl primesc?
**Răspuns**: Stimulantul de inserție este un ajutor financiar disponibil pentru părinți care se întorc la serviciu sau la muncă după ce copilul împlinește 6 luni. Este aprobabil pentru persoanele care sunt în concediu de creștere, adoptori, cel căruia i…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut']

### nastere-15 — nastere
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-16 — nastere
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Sunt cetățean român cu domiciliul în Franța și am născut acolo. În acest caz, pentru a obține un certificat de naștere al copilului românesc, trebuie să respectăm regulile legale din România privind recunoașterea paternității în afara căsăt…
**Status**: recall=False · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-19 — nastere
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-20 — nastere
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: În acest caz, există pași care trebuie urmat pentru a obține un certificat de naștere în România. În special, reușiți să ne spuneți că am cetățenie dublă română și franceză, iar copilul s-a născut în Franța. Aici e o listă a pașilor complet…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-21 — nastere
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: Pentru a schimba buletinul la 14 ani după naștere, trebuie să consultați serviciul public comunitar local de evidență a persoanelor sau primăria localității de domiciliu. Voi fi solicitată următoarele documente:

- Buletinul de naștere
- Ac…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Cel puțin un părinte are domiciliul în România']

### nastere-23 — nastere
**Întrebare**: Cum primesc pensie alimentară de la fostul soț pentru copilul nostru?
**Răspuns**: Pentru a primi pensia alimentară de la fostul soț pentru copilul tău, consulteți Direcția Generală de Asistență Socială și Protecția Copilului (DGASPC) în județul sau sectorul unde locuiești. Informațiile specifici se pot găsi pe site-ul of…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție']

### nastere-x27 — nastere
**Întrebare**: Cum transcriu în România certificatul de naștere al copilului emis în străinătate?
**Răspuns**: Pentru a transcrie un certificat de naștere al copilului emis în străinătate, urmați pașii de mai jos:

1. Vă rugăm să introduceți detalii despre cererii dvs., inclusiv numele și prenume copilei, datimea născării, locul născării și statul d…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Cel puțin un părinte are domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România']

### nastere-x28 — nastere
**Întrebare**: Sunt cetățean străin; ce documente cere primăria pentru a înregistra nașterea copilului?
**Răspuns**: Pentru a înregistra nașterea copilului ca și cetățean străin, Primăria va solicita următoarele documente:

- Actele de identitate ale tale și ale partenerului/partenera (buletin sau carte de identitate, etc.);
- Certificatul medical constat…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul']

### nastere-x29 — nastere
**Întrebare**: Ce valoare are alocația de stat pentru copii și cine o poate solicita?
**Răspuns**: Alocația de stat pentru copii are valoarea de 719 RON pentru copiii cu vârste între 0 și 2 ani și 292 RON pentru copiii cu vârsta de peste 2 ani. Acesta poate fi solicitat:
1. De către copil înainte de a împlini vârsta de 18 ani, dacă este …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în străinătate > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în România > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în străinătate > Copilul nu este încadrat într-un grad de handicap']

### nastere-x32 — nastere
**Întrebare**: Ce hârtii îmi trebuie ca să declar oficial venirea pe lume a bebelușului meu?
**Răspuns**: Pentru a declară oficial venirea pe lume a bebelușului tău în România, vei avea nevoie de următoarele hârtii și documente:

1. Certificatul de naștere al mamei (încălcți)
2. Actul de identitate al mamei
3. Declarația privind numele pe care …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-x33 — nastere
**Întrebare**: Ce ajutoare bănești pot lua de la stat după ce mi se naște un copil?
**Răspuns**: După ce un copil este născut, părinții pot lua stimulant financiar pentru nou-născuți din Municipiul Constanța (2000 RON) - condiții specifice se referesc la domiciliul stabil sau reședința aflat pe raza Municipiului Constanța de cel puțin …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Stimulente pentru nou-născut', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul Constanța', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul București', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-x34 — nastere
**Întrebare**: Părintele necăsătorit poate trece numele lui pe micuț?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România']

### casatorie-03 — casatorie
**Întrebare**: Sunt deja căsătorit. Pot încheia o nouă căsătorie?
**Răspuns**: Nu, dacă ești deja căsătorit sau căsătoară, nu poți încheia o altă căsătorie. Poligamia este interzisă în România.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-05 — casatorie
**Întrebare**: Pot să iau numele partenerului ca nume de familie după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-06 — casatorie
**Întrebare**: Există rude apropiate cu care nu mă pot căsători?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu exactitudine dacă există rude apropiate cu care nu poți căsătorești.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie > 📌 Căsătoria între rude', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie > 📌 Căsătoria între rude > 📌 Persoana pusă sub o măsură de ocrotire specială', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie > 📌 Căsătoria între rude > 📌 Persoana pusă sub o măsură de ocrotire specială > 📌 Căsătoria dintre persoanele de același sex', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie']

### casatorie-07 — casatorie
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-09 — casatorie
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Pentru a depune la primăria documentele necesare pentru căsătoria în România, următoarele documente sunt necesare și trebuie să le depunăteți în funcție de tipul partenerului dumneavoastră:

1. Buletin / Carte de identitate / Pașaport (pent…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.']

### casatorie-13 — casatorie
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Pentru înregistrarea nașterii, actul de identitate sau pașaport este necesar pentru partenerul vostro. Dacă este cetățean al Uniunii Europene, va fi suficient actul de identitate. În caz contrar, pașaportul sau certificatul de identitate di…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România']

### casatorie-14 — casatorie
**Întrebare**: Am încheiat căsătoria în străinătate. Cum o transcriu/recunosc în România?
**Răspuns**: Dacă au fost încheiate actele de căsătorie în străinătate, pentru a le recunoaște sau asemănării acestora cu legile românești și pentru a le transcrie în România, urmează să respectați aceste pași:

1. Declararea de căsătorie: Acest documen…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate']

### casatorie-15 — casatorie
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Naștere — declarația privind numele copilului este necesară.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-16 — casatorie
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-17 — casatorie
**Întrebare**: Sunt minor de 16 ani și vreau să mă căsătoresc. Care sunt pașii legali completi?
**Răspuns**: Nu am suficiente informațiilor în sursele disponibile pentru a răspunde la întrebarea dvs. referitoare la tratamentul legal de căsătorește pentru minori cu mai puțin de 16 ani în România. Vă recomand să consultați un avocat pentru a afla ma…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-x26 — casatorie
**Întrebare**: Ce documente îmi trebuie pentru a mă căsători ca cetățean român?
**Răspuns**: Pentru a mă căsătoși ca cetățean român, următoarele documente sunt necesare și valabile la data depunerii declarației de căsătorie și la data oficierii căsătoriei:
1. Act de identitate (pentru viitorul soț);
2. Dovada domiciliului sau a reș…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-x28 — casatorie
**Întrebare**: Ce buletine ne cer la primărie când vrem să facem nunta?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-x29 — casatorie
**Întrebare**: Cum se împart agoniseala și averea strânse în timpul mariajului?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală', 'Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală > 📌 Comunitatea Convențională > 📌 Separația de bunuri']

### locuire-02 — locuire
**Întrebare**: Ce acte îmi trebuie ca cumpărător al unui imobil în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-07 — locuire
**Întrebare**: Care sunt obligațiile mele ca proprietar într-o asociație de proprietari?
**Răspuns**: Ca proprietar ai obligațiile următoare:
- Să anunți președintele asociației cu privire la orice schimbare intervenită la structura și numărul membrilor familiei, a persoanelor luate în spațiu sau a chiriașilor/comodatarilor, în termen de 10…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R3_BAD_CITATION']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt:', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt: > 📌 Situația financiară a asociației de proprietari', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari?']

### locuire-08 — locuire
**Întrebare**: Care sunt obligațiile chiriașului față de proprietar?
**Răspuns**: Nu am suficiente informațiuni în sursele disponibile pentru a răspunde cu detaliere despre obligațiile chiriașului față de proprietar.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-09 — locuire
**Întrebare**: Sunt cetățean al unui stat UE. În ce condiții pot cumpăra o casă în România?
**Răspuns**: Sunt cetățean al unui stat membru al Uniunii Europene și vreau să cumpăr o casă în România. În aceste condiții, pot face achiziționarea imobiliar pe baza acordului internațional reciproc între România și respectivul stat membru UE/SEE. Pent…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-12 — locuire
**Întrebare**: Sunt cetățean turc. Pot cumpăra un apartament în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']

### locuire-16 — locuire
**Întrebare**: Vreau să închiriez locuința altcuiva și nu vrem să încheiem contract în scris. E legal?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Proprietarul vrea să mă dea afară - ce pot face?', 'Locuire > Vreau să închei un contract de comodat > Despre contractul de comodat (împrumut de folosință)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)']

### locuire-17 — locuire
**Întrebare**: Sunt cetățean român, vreau să cumpăr un imobil împreună cu un partener cetățean turc. Există restricții?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-x29 — locuire
**Întrebare**: Pot să las pe cineva să stea în apartamentul meu gratis, cu acte?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detalii despre documentele necesare pentru oferirea locuinței gratuită unui vânzator.
Pentru a putea furniza aceste informații, este nevoie de mai multe detalii despre …
**Status**: recall=False · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']

### locuire-x31 — locuire
**Întrebare**: Cum pun bazele unei organizații a locatarilor din bloc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt: > 📌 Situația financiară a asociației de proprietari', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari?']

### locuire-x32 — locuire
**Întrebare**: Cum îmi fac pașaport pentru o vacanță în străinătate?
**Răspuns**: Pașaportul nu este necesar pentru o vacanță în străinătate. Dacă doriți să aplicați pașaport, vă recomand să contactați oficiul consular al statului de cetățenie dumneavoastră sau misiunea diplomatică din țara destinată pentru informații pr…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate']

### locuire-x33 — locuire
**Întrebare**: Unde mă programez pentru un control la medicul de familie?
**Răspuns**: Procesul de eliberare a certificatului medical constatator al nașterii se realizează la medicul de familie sau spitalul unde a avut loc nașterea. Dacă a fost născut acasă, procesul se desfășoară la medicul de familie. Acesta este un documen…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul medical constatator al nașterii > Am născut acasă > Am domiciliul în România', 'Nașterea > Certificatul medical constatator al nașterii > Am născut într-un spital / într-o clinică > Am domiciliul în România', 'Nașterea > Certificatul medical constatator al nașterii > Am născut acasă > Am domiciliul în străinătate', 'Nașterea > Certificatul medical constatator al nașterii > Am născut într-un spital / într-o clinică > Am domiciliul în străinătate']
