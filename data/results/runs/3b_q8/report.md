# Raport evaluare

**Model**: `qwen2.5:3b-instruct-q8_0`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 98

## Metrici globale

- Refusal accuracy: **74%** (73/98)
- Breadcrumb recall@4 (excl. refusal cases): **95%** (78/82)
- Keyword coverage (cazuri non-refusal): **53%** (82 cazuri)
- Contract pass rate (R1..R6): **68%** (67/98)
- Latency medie: **16.0s** per întrebare
- JSON invalid / generări runaway: **1** cazuri (din care 1 forțate la refuz; cea mai lungă ieșire: 2914 caractere)

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 30 | 70% | 100% | 63% | 15.4s |
| locuire | 33 | 76% | 96% | 70% | 14.0s |
| nastere | 35 | 77% | 90% | 71% | 18.4s |

## Distribuția violărilor de contract

- `R4_FABRICATED_DOC`: 26
- `R7_OVERREFUSAL`: 10
- `R2_UNCITED`: 6
- `R3_BAD_CITATION`: 6
- `R6_FORM_ID_IN_DOCS`: 4
- `R5_REFUSAL_WITH_DOCS`: 1

## Generări runaway / JSON invalid (1)

| Caz | Parse fail | Forțat la refuz | Caractere max | Încercări |
|---|---|---|---|---|
| casatorie-x26 | 1 | da | 2914 | 1 |

## Cazuri cu probleme (44)


### nastere-01 — nastere
**Întrebare**: Ce documente îmi trebuie pentru înregistrarea nașterii copilului meu, dacă sunt căsătorit cu partenera?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul']

### nastere-05 — nastere
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Documentele necesare pentru înregistrarea nașterei copilului, în cazul în care tatăl recunoaște copilul și părinții nu sunt căsătoriți, includ:
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
**Răspuns**: Indemnizația pentru creșterea copilului poate fi primită de persoane care au fost încadrate într-o situație care le acordă dreptul la această indemnizare, conform regulilor și condițiilor specifice ale programului. În cazul dat, se pot incl…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-12 — nastere
**Întrebare**: Pe ce perioadă se acordă indemnizația pentru creșterea copilului?
**Răspuns**: Indemnizația pentru creșterea copilului este acordată în perioada concediului de maternitate sau din momentul intrării concediului de maternitate, dacă acesta nu a fost îndeplinit. De asemenea, poate fi acordată și în cazuri precum: trimis …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-15 — nastere
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-16 — nastere
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Ca fiind cetățean român și având domiciliul în Franța, dacă copilul tău a fost născut la Franța, trebuie să obții certificatul de naștere al copilului datorită facturilor de locuință sau alte documente care indică că aveți domiciliul în Fra…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-19 — nastere
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-20 — nastere
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Din întrebarea dvs., rezultă că copilul are două părți de origine româno-francese, având ambele cetățeniile. În acest caz, procedura pentru a obține certificatul românesc va include următoarele etape:

1. **Certificatul de Naștere**: Copilu…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-21 — nastere
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: Pentru schimbarea buletinului la vârsta de 14 ani după naștere, este necesar să consultați serviciul public comunitar local de evidențiere a persoanelor sau primăria localității de domiciliu. Documentele necesare sunt:

- Certificatul de na…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Cel puțin un părinte are domiciliul în România']

### nastere-22 — nastere
**Întrebare**: Vreau să adopt un copil cu vârsta de peste 5 ani. Procedura?
**Răspuns**: Procedurile pentru adoptarea unui copil sunt diferite în funcție de statutul acestuia (cetățean străin sau cetățean român) și al situației familiale ale părinților. Pentru un copil cu vârsta de peste 5 ani, care este cetățean străin cu reșe…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în România > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-23 — nastere
**Întrebare**: Cum primesc pensie alimentară de la fostul soț pentru copilul nostru?
**Răspuns**: Pentru a primi pensia alimentară de la fostul soț pentru copilul tău, trebuie să te adresezi Direcției Generale de Asistență Socială și Protecția Copilului (DGASPC) din județul sau sectorul unde locuiești. Trebuie să fiți într-una dintre si…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție']

### nastere-x31 — nastere
**Întrebare**: Nu suntem căsătoriți și tatăl vrea să recunoască copilul; ce declarație este necesară?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-x33 — nastere
**Întrebare**: Ce ajutoare bănești pot lua de la stat după ce mi se naște un copil?
**Răspuns**: După ce un copil este născut, părinții pot lua stimulant financiar de 2000 RON la Municipiul Constanța (condiții: unul dintre părinți are cetățenia română și domiciliul stabil sau reședința pe raza Municipiului Constanța de cel puțin 1 an î…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Stimulente pentru nou-născut', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul Constanța', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul București', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-x34 — nastere
**Întrebare**: Părintele necăsătorit poate trece numele lui pe micuț?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România']

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
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliere despre procedurile de căsătoria la ambasadă sau consulatul român din străinătate.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-09 — casatorie
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Pentru a depune la primăria documentele necesare pentru a se călători cu un soț străin, următoarea listă de documente este necesară și trebuie să le depună pe formatul original:

1. Act de identitate (pentru cetățenii Uniunii Europene) sau …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.']

### casatorie-10 — casatorie
**Întrebare**: Ce nume de familie pot să aleg după căsătorie?
**Răspuns**: După căsătorie, părțile sunt obligați să menționeze un nume de familie. În cazul în care nu au acordat un nume de familie la nascere, pot alege un nume de familie personal. Această informație se poate găsi în documentele de căsătorie sau de…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R6_FORM_ID_IN_DOCS', 'R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-11 — casatorie
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Procedura pentru căsătoria în străinătate, cum ar fi cazul cu un cetățean român și un alt cetățean (străin) include următoarele documente:

1. Certificatul de naștere pentru ambele persoane.
2. Actele de identitate în formă originală, aflat…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate']

### casatorie-13 — casatorie
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informațiuni în sursele disponibile pentru a răspunde direct la întrebarea dvs., dar în baza documentelor de care aveți nevoie, nu pare că ar fi necesare traduceri. Documentele eliberate de statele membre ale Uniunii Europe…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România']

### casatorie-14 — casatorie
**Întrebare**: Am încheiat căsătoria în străinătate. Cum o transcriu/recunosc în România?
**Răspuns**: Pentru a recunoaște și a transcrivi căsătoria în România după încheierea acesteia în străinătate, urmează pasii:

1. Îndată că s-a încheiat căsătoria în străinătate, solicitați un certificat de căsătorie oficial eliberat de autoritățile din…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R3_BAD_CITATION', 'R3_BAD_CITATION']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate']

### casatorie-15 — casatorie
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Pentru un partener cetățean străin, au următoarele aspecte suplimentare care ar trebui să știe:

1. **Regimul matrimonial**: Alegeți regimul matrimonial al separației de bunuri sau al comunității convenționale.
2. **Convenția autentificată*…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R3_BAD_CITATION']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-16 — casatorie
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-17 — casatorie
**Întrebare**: Sunt minor de 16 ani și vreau să mă căsătoresc. Care sunt pașii legali completi?
**Răspuns**: Pentru a-ți căsătura, fiind minor de 16 ani, trebuie să respecteți pașii următori:

1. Deși vrei să mă căsătoresc, nu ai dreptul legal să faci asta.
2. Trebuie să te întrebi pentru adevărarea acestui dorință și să-ți asiguri că este ceva pe…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-x26 — casatorie
**Întrebare**: Ce documente îmi trebuie pentru a mă căsători ca cetățean român?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-x28 — casatorie
**Întrebare**: Ce buletine ne cer la primărie când vrem să facem nunta?
**Răspuns**: La primăria pentru a realiza o nuntă, va fi necesară următoarele buletinuri de identitate în original:
1. Carte de Identitate
2. Buletin sau carte de identitate provizorie (daca este cazul)
3. Pașaport pentru cetățenii străini care au domic…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-x29 — casatorie
**Întrebare**: Cum se împart agoniseala și averea strânse în timpul mariajului?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală', 'Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală > 📌 Comunitatea Convențională > 📌 Separația de bunuri']

### locuire-01 — locuire
**Întrebare**: Sunt cetățean român și vreau să cumpăr un apartament. Care este primul pas?
**Răspuns**: Primul pas este să aduni toate documentele necesare pentru a confirma că esti cu adevărat proprietarul aceluiași imobil și că are voie să îl vândă: actul tău de identitate; actul de proprietate al imobilului (care poate să fie, după caz, co…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat']

### locuire-03 — locuire
**Întrebare**: Ce trebuie să conțină un contract de închiriere între proprietar și chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)']

### locuire-04 — locuire
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: Da, este obligatoriu să se facă un contract în scris pentru a proteja ambele părți ale acordului și pentru a clarifica condițiile de închiriere. Un exemplu de document care ar putea fi folosit este un contract de închiriere.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-09 — locuire
**Întrebare**: Sunt cetățean al unui stat UE. În ce condiții pot cumpăra o casă în România?
**Răspuns**: Sunt cetățean al unui stat membru al Uniunii Europene și vreau să cumpăr o casă în România. Pentru această activitate, sunt obligat să aduc doar actul de identitate pentru ca notarul să poată verifica cine ești. De asemenea, dacă sunt căsăt…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-10 — locuire
**Întrebare**: Sunt cetățean al unui stat non-UE. Pot cumpăra un imobil în România?
**Răspuns**: În cazul în care nu ești cetățean român sau al vreunui stat membru UE/SEE, poți achiziționa un imobil pe baza unui acord internațional reciproc între România și respectiva țară. Cetățenii statelor terțe pot dobândi drept de proprietate asup…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-12 — locuire
**Întrebare**: Sunt cetățean turc. Pot cumpăra un apartament în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']

### locuire-15 — locuire
**Întrebare**: Care sunt drepturile mele dacă sunt proprietarul unui apartament și membru al asociației de proprietari?
**Răspuns**: Drepturile dvs. ca proprietar și membru al asociației de proprietari includ: 
- Să anunți președintele asociației cu privire la orice schimbare intervenită la structura și numărul membrilor familiei, a persoanelor luate în spațiu sau a chir…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R3_BAD_CITATION']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt: > 📌 Situația financiară a asociației de proprietari', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt:']

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

### locuire-18 — locuire
**Întrebare**: Care e diferența între un cetățean UE și unul non-UE când vine vorba despre cumpărarea unui imobil în România?
**Răspuns**: Diferența între un cetățean al Uniunii Europene (UE) și unul care nu este cetățean român în ceea ce privește cumpărarea unui imobil în România se referă la necesitatea de a obține NIF (număr de înregistrare fiscală) pentru cetățenii non-UE.…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']

### locuire-x29 — locuire
**Întrebare**: Pot să las pe cineva să stea în apartamentul meu gratis, cu acte?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']

### locuire-x30 — locuire
**Întrebare**: Ce scrie într-o înțelegere de chirie între proprietar și cel care stă?
**Răspuns**: Într-o înțelegere de chirie între proprietar și cel care stă, contractul trebuie să conțină următoarele informații: identitatea locatorului și a locatarului (nume, cod de identificare personal, date de contact); descrierea imobilului care u…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R3_BAD_CITATION', 'R3_BAD_CITATION']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)']

### locuire-x31 — locuire
**Întrebare**: Cum pun bazele unei organizații a locatarilor din bloc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt: > 📌 Situația financiară a asociației de proprietari', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari?']

### locuire-x32 — locuire
**Întrebare**: Cum îmi fac pașaport pentru o vacanță în străinătate?
**Răspuns**: Pașaportul nu este necesar pentru o vacanță în străinătate. Dacă doriți să vă dea un document oficial care să permită accesul la spațiile UE, puteți căuta o carte de identitate temporară sau o carte de viitor personal. De asemenea, pentru a…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate']

### locuire-x33 — locuire
**Întrebare**: Unde mă programez pentru un control la medicul de familie?
**Răspuns**: Procesul de eliberare a certificatului medical constatator al nașterii se realizează în spitalul sau clinica unde a avut loc nașterea. Acest document trebuie să fie prezentat la medicul de familie sau personalul spitalului.
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul medical constatator al nașterii > Am născut acasă > Am domiciliul în România', 'Nașterea > Certificatul medical constatator al nașterii > Am născut într-un spital / într-o clinică > Am domiciliul în România', 'Nașterea > Certificatul medical constatator al nașterii > Am născut acasă > Am domiciliul în străinătate', 'Nașterea > Certificatul medical constatator al nașterii > Am născut într-un spital / într-o clinică > Am domiciliul în străinătate']
