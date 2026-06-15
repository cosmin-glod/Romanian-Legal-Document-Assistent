# Raport evaluare

**Model**: `rollama3ro`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 98

## Metrici globale

- Refusal accuracy: **82%** (80/98)
- Breadcrumb recall@4 (excl. refusal cases): **95%** (78/82)
- Keyword coverage (cazuri non-refusal): **71%** (82 cazuri)
- Contract pass rate (R1..R6): **56%** (55/98)
- Latency medie: **47.8s** per întrebare
- JSON invalid / generări runaway: **15** cazuri (din care 3 forțate la refuz; cea mai lungă ieșire: 3211 caractere)

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 30 | 80% | 100% | 50% | 46.4s |
| locuire | 33 | 79% | 96% | 48% | 53.4s |
| nastere | 35 | 86% | 90% | 69% | 43.9s |

## Distribuția violărilor de contract

- `R4_FABRICATED_DOC`: 41
- `R2_UNCITED`: 12
- `R6_FORM_ID_IN_DOCS`: 11

## Generări runaway / JSON invalid (15)

| Caz | Parse fail | Forțat la refuz | Caractere max | Încercări |
|---|---|---|---|---|
| casatorie-22 | 1 | nu | 3211 | 2 |
| nastere-x26 | 1 | nu | 3209 | 2 |
| locuire-x24 | 2 | da | 3141 | 1 |
| locuire-07 | 1 | nu | 3135 | 2 |
| locuire-01 | 1 | nu | 3101 | 2 |
| locuire-15 | 2 | da | 3098 | 1 |
| locuire-14 | 1 | nu | 3091 | 2 |
| nastere-05 | 1 | nu | 3012 | 2 |
| locuire-17 | 1 | nu | 2962 | 2 |
| casatorie-03 | 1 | nu | 2954 | 2 |
| locuire-09 | 1 | nu | 2954 | 2 |
| nastere-22 | 1 | nu | 2887 | 2 |
| casatorie-x23 | 2 | da | 2877 | 1 |
| nastere-09 | 1 | nu | 2840 | 2 |
| casatorie-21 | 1 | nu | 2838 | 2 |

## Cazuri cu probleme (54)


### nastere-05 — nastere
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Pentru a înregistra nașterea copilului, Serviciul de Stare Civilă al Primăriei îți va cere următoarele documente: Certificatul medical constatator al nașterii care trebuie să poarte număr de înregistrare, dată certă, sigiliul/ştampila unită…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul']

### nastere-09 — nastere
**Întrebare**: Am născut în străinătate. Ce trebuie să fac pentru ca nașterea să fie recunoscută în România?
**Răspuns**: Pentru a înregistra nașterea unui copil cetățean străin născut în România, Serviciul de Stare Civilă al Primăriei îți va cere următoarele documente: Certificatul de naștere al mamei; Actul de identitate al mamei; Certificatul medical consta…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul > Vreau să înregistrez nașterea la ambasada țării mele de origine']

### nastere-10 — nastere
**Întrebare**: Cine poate primi indemnizația pentru creșterea copilului?
**Răspuns**: Persoanele care pot primi indemnizația pentru creșterea copilului sunt cele care au venituri salariale supuse impozitului pe venit, conform Codului fiscal, timp de 12 luni în ultimele 24 luni anterioare nașterii copilului. Acestea includ pe…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-13 — nastere
**Întrebare**: Am primit certificatul de naștere al copilului în străinătate. Cum îl transcriu pe cel românesc?
**Răspuns**: Pentru a transcrie certificatul de naștere al copilului dvs. la autoritățile române, trebuie să urmați acești pași: 1. Obțineți un certificat de naștere în limba engleză sau traduceți-l în limba engleză dacă este într-o altă limbă. 2. Verif…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Cel puțin un părinte are domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România']

### nastere-15 — nastere
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Nu, părinții trebuie să aibă un domiciliu legal în România pentru ca nașterea copilului lor să poată fi înregistrată la primărie. Dacă nu au domiciliul în România, va trebui să verificați procedurile de înregistrare a nașterii în țara părin…
**Status**: recall=False · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-16 — nastere
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Pentru a obține certificatul de naștere al copilului tău românesc, trebuie să depui o cerere la primăria din România în care ai domiciliul. Trebuie să furnizezi documente justificative, cum ar fi actul de identitate, pașaportul sau permisul…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-20 — nastere
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Pentru a obține un certificat de naștere românesc pentru copilul tău, trebuie să urmezi aceste pași: 
1. Solicitați un certificat de naștere francez original sau o copie legalizată.
2. Traduceți certificatul în limba română și obțineți o tr…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-21 — nastere
**Întrebare**: Cum îmi schimb buletinul la 14 ani după naștere?
**Răspuns**: Pentru a vă schimba buletinul de identitate la 14 ani, trebuie să solicitați un nou certificat de naștere. Pentru a face acest lucru, puteți vizita serviciul public comunitar local de evidență a persoanelor (SPCLEP) sau primăria din localit…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Cel puțin un părinte are domiciliul în România']

### nastere-22 — nastere
**Întrebare**: Vreau să adopt un copil cu vârsta de peste 5 ani. Procedura?
**Răspuns**: Pentru înregistrarea nașterii, veți avea nevoie de o declarație privind numele copilului (declaratie_nume_copil). Această declarație este necesară atunci când părinții au nume diferite și trebuie să decidă ce nume va purta copilul. În cazul…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în România > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-23 — nastere
**Întrebare**: Cum primesc pensie alimentară de la fostul soț pentru copilul nostru?
**Răspuns**: Pentru a primi pensia alimentară de la fostul soț, trebuie să depuneți o cerere la tribunalul în care aveți domiciliul sau reședința. În cererea dvs., trebuie să furnizați informații despre venitul și situația financiară a dumneavoastră, pr…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție']

### nastere-24 — nastere
**Întrebare**: Cât costă un test DNA pentru stabilirea paternității?
**Răspuns**: Costurile unui test de ADN pentru stabilirea paternității pot varia în funcție de furnizor și de tipul de test efectuat. În general, costurile pot începe de la aproximativ 200 $ și pot ajunge până la câteva sute de dolari. Este important să…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul București', 'Nașterea > Ajutor financiar > Stimulente pentru nou-născut > Municipiul Constanța', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în străinătate > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap']

### nastere-x27 — nastere
**Întrebare**: Cum transcriu în România certificatul de naștere al copilului emis în străinătate?
**Răspuns**: Pentru a transcrie un certificat de naștere al copilului emis în străinătate, trebuie să urmați acești pași: 

1. Verificați dacă certificatul de naștere este scris în limba română sau tradus în limba română.
2. Dacă certificatul de naștere…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Cel puțin un părinte are domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România']

### nastere-x29 — nastere
**Întrebare**: Ce valoare are alocația de stat pentru copii și cine o poate solicita?
**Răspuns**: Alocația de stat pentru copii are o valoare de 719 RON pentru copiii cu vârste între 0 și 2 ani, iar pentru cei cu vârsta de peste 2 ani, este de 292 RON. Alocația poate fi solicitată de către unul dintre părinți sau reprezentantul legal al…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în străinătate > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în România > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în străinătate > Copilul nu este încadrat într-un grad de handicap']

### nastere-x35 — nastere
**Întrebare**: Cum îmi reînnoiesc permisul de conducere?
**Răspuns**: Pentru a vă reînnoi permisul de conducere, trebuie să urmați acești pași:
1. Verificați eligibilitatea: Asigurați-vă că aveți toate cerințele necesare pentru reînnoire, cum ar fi vârsta minimă și experiența de conducere.
2. Colectarea docum…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-02 — casatorie
**Întrebare**: Două persoane de același sex se pot căsători în România?
**Răspuns**: Nu, două persoane de același sex nu se pot căsători în România. Căsătoria dintre persoanele de același sex este interzisă și căsătoriile dintre persoanele de același sex încheiate în străinătate de cetățeni români sau de cetățeni străini nu…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie > 📌 Căsătoria între rude > 📌 Persoana pusă sub o măsură de ocrotire specială > 📌 Căsătoria dintre persoanele de același sex', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-05 — casatorie
**Întrebare**: Pot să iau numele partenerului ca nume de familie după căsătorie?
**Răspuns**: Da, puteți lua numele partenerului ca nume de familie după căsătorie. În declarația de căsătorie, puteți menționa că veți purta numele vostru reunite și va fi recunoscut oficial după încheierea căsătoriei dvs.

Surse: [1, 3]
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-07 — casatorie
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Pentru a oficia căsătoria la ambasada sau consulatul român, trebuie să urmați aceste instrucțiuni: 1) Depuneți cererea de căsătorie la ambasadă sau consulat cu cel puțin 10 zile înainte de data propusă pentru ceremonia de nuntă. 2) Asiguraț…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-08 — casatorie
**Întrebare**: Pot purta un nume compus din numele ambilor soți?
**Răspuns**: Da, puteți alege să vă căsătoriți cu numele vostru reunite. Acest lucru înseamnă că veți lua amândoi numele unuia dintre soții dvs. după căsătorie. În declarația de căsătorie, puteți menționa acest lucru și vă puteți căsători cu numele vost…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-09 — casatorie
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Pentru a căsători în România, vi se vor solicita următoarele documente: 1. Declarația de căsătorie; 2. Actul de identitate (pentru cetățenii Uniunii Europene) sau pașaportul (pentru cetățenii altor state); 3. Certificatul de naștere, tradus…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.']

### casatorie-10 — casatorie
**Întrebare**: Ce nume de familie pot să aleg după căsătorie?
**Răspuns**: După căsătorie, puteți alege din următoarele opțiuni pentru numele dvs. de familie: păstrați fiecare nume pe care l-ați avut înainte de căsătorie; luați amândoi numele unuia dintre soții; sau purtați numele vostru reunite.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-13 — casatorie
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu, nu trebuie să traduceți documente atunci când vă căsătoriți în România dacă sunteți cetățean român și partenerul dvs. este un cetățean UE. Documentele eliberate de statele membre ale Uniunii Europene sunt scutite de apostilare sau orice…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România']

### casatorie-16 — casatorie
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu, nu puteți căsători dacă sunteți verișori primari. Conform legii române, este interzisă căsătoria între persoane care sunt într-un grad de consangvinizare mai apropiat decât al patrulea (adică verișorul primar). În cazul în care aveți vâ…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-17 — casatorie
**Întrebare**: Sunt minor de 16 ani și vreau să mă căsătoresc. Care sunt pașii legali completi?
**Răspuns**: Pentru a te căsători legal la vârsta de 16 ani, trebuie să urmați acești pași: 
1. Obțineți consimțământul părinților sau al tutorelui dvs., dacă nu sunteți încă major.
2. Depuneți o cerere de permisiune la tribunal, care va fi examinată și…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-19 — casatorie
**Întrebare**: Cum divorțez de partenerul meu?
**Răspuns**: Pentru a divorța, trebuie să depuneți o cerere la tribunal. Cererea poate fi completată online sau în persoană la tribunal. Odată ce cererea este depusă, va trebui să plătiți taxele judiciare și să furnizați documente justificative, cum ar …
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Proprietarul vrea să mă dea afară - ce pot face?', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală > 📌 Comunitatea Convențională > 📌 Separația de bunuri', 'Căsătoria > Drepturile și obligațiile soților > Locuire', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-20 — casatorie
**Întrebare**: Cât costă oficierea unei căsătorii la primărie?
**Răspuns**: Oficierea unei căsătorii la primărie este gratuită pentru cetățenii români, în timp ce cetățenii străini trebuie să plătească o taxă de 20 lei (aproximativ 4 euro) pe persoană. Acest lucru se poate găsi în Legea nr. 105/2006 privind căsător…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-21 — casatorie
**Întrebare**: Cum împart pensia de soț decedat?
**Răspuns**: Pensia de soț decedat este acordată în mod automat viitoarei soții, indiferent dacă aceasta are sau nu un loc de muncă. Dacă viitorul soț a avut și el o pensie, atunci se va adăuga la pensia viitoarei soții. În cazul în care viitorul soț nu…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Locuire', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală > 📌 Comunitatea Convențională > 📌 Separația de bunuri', 'Căsătoria > Drepturile și obligațiile soților > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Drepturile și obligațiile soților > Relația de cuplu']

### casatorie-22 — casatorie
**Întrebare**: Putem semna un contract prematrimonial înainte de căsătorie?
**Răspuns**: Da, puteți semna un contract prematrimonial înainte de căsătorie. Acesta este cunoscut sub numele de convenția matrimonială și poate fi încheiat înainte sau în timpul căsătoriei. Convenția produce efecte de la data încheierii sale, iar părț…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie > 📌 Căsătoria între rude > 📌 Persoana pusă sub o măsură de ocrotire specială', 'Căsătoria > Condiții pentru a te căsători']

### casatorie-x23 — casatorie
**Întrebare**: Ce condiții trebuie îndeplinite ca să mă pot căsători?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-x24 — casatorie
**Întrebare**: Unde trebuie să depun declarația de căsătorie?
**Răspuns**: Declarația de căsătorie trebuie depusă la primăria locului de domiciliu sau reședință a unuia dintre viitorii soți. Prin excepție, căsătoria poate fi oficiată și la o altă primărie decât cea de domiciliu sau reședință, cu aprobarea primarul…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED', 'R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.']

### casatorie-x29 — casatorie
**Întrebare**: Cum se împart agoniseala și averea strânse în timpul mariajului?
**Răspuns**: Averile dobândite în timpul căsătoriei de oricare dintre soți sunt, de la data dobândirii lor, bunuri comune ale soților. Acestea includ salarii, venituri din proprietate intelectuală, imobile sau mașini achiziționate în timpul căsătoriei. …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală', 'Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală > 📌 Comunitatea Convențională > 📌 Separația de bunuri']

### casatorie-x30 — casatorie
**Întrebare**: Ce taxe plătesc pentru înmatricularea unei mașini?
**Răspuns**: Pentru înregistrarea unei mașini, trebuie să plătiți taxa de intabulare (înscriere în cartea funciară) către Oficiul de Cadastru și Publicitate Imobiliară. Această taxă este de 0,15% din prețul vânzării imobilului. Conform legii, vânzarea u…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > Drepturile și obligațiile mele în calitate de cumpărător', 'Locuire > Vreau să vând un imobil > Drepturile și obligațiile mele în calitate de vânzător', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție']

### locuire-02 — locuire
**Întrebare**: Ce acte îmi trebuie ca cumpărător al unui imobil în România?
**Răspuns**: Ca cumpărător, este nevoie să aduci doar actul de identitate, pentru ca notarul să poată verifica cine ești. De asemenea, dacă ești căsătorit(ă), este nevoie și de certificatul de căsătorie.
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-03 — locuire
**Întrebare**: Ce trebuie să conțină un contract de închiriere între proprietar și chiriaș?
**Răspuns**: Un contract de închiriere (locațiune) între proprietar și chiriaș ar trebui să includă următoarele informații: identitatea locatorului și a locatarului (nume, cod de identificare personal, date de contact); descrierea imobilului care urmeaz…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)']

### locuire-04 — locuire
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: Nu, nu este neapărat necesar ca contractul de închiriere (locațiune) să fie făcut în scris. Cu toate acestea, recomandăm să se facă un astfel de contract pentru a evita orice confuzie sau litigii viitoare. În plus, dacă doriți ca contractul…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-05 — locuire
**Întrebare**: Care sunt obligațiile proprietarului față de chiriaș?
**Răspuns**: Obligațiile unui proprietar față de un chiriaș includ furnizarea unei locuințe în stare bună, efectuarea oricăror reparații necesare și asigurarea garanției împotriva problemelor care apar. De asemenea, trebuie să permită accesul chiriașulu…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED', 'R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-06 — locuire
**Întrebare**: Care sunt drepturile mele ca chiriaș?
**Răspuns**: Drepturile tale ca chiriaș includ: 

1. Accesul la locuință și utilizarea acesteia cu grijă, fără a provoca daune.
2. Plata chiriei conform termenilor contractului de închiriere (locațiune).
3. Utilizarea utilităților și plata acestora pe p…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-07 — locuire
**Întrebare**: Care sunt obligațiile mele ca proprietar într-o asociație de proprietari?
**Răspuns**: Ca proprietar ai obligația: Să anunți președintele asociației cu privire la orice schimbare intervenită la structura și numărul membrilor familiei, a persoanelor luate în spațiu sau a chiriașilor/comodatarilor, în termen de 10 zile de la sc…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt:', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt: > 📌 Situația financiară a asociației de proprietari', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari?']

### locuire-08 — locuire
**Întrebare**: Care sunt obligațiile chiriașului față de proprietar?
**Răspuns**: Obligațiile unui chiriaș față de proprietar includ plata chiriei, plata utilităților, repararea oricăror daune care rezultă din utilizarea normală a imobilului și asigurarea faptului că locuința este menținută într-o stare bună. În plus, ch…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-09 — locuire
**Întrebare**: Sunt cetățean al unui stat UE. În ce condiții pot cumpăra o casă în România?
**Răspuns**: Dacă ești cetățean al unui stat membru al Uniunii Europene sau al Spațiului Economic European și vrei să cumperi o casă în România, poți face asta în aceleași condiții ca un cetățean român. Pentru ca orice contract să fie valabil, este nevo…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-11 — locuire
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Obligațiile unui chiriaș (locatar) față de imobil includ: 

1. Plata chiriei la termenul stabilit în contract.
2. Plata utilităților pe perioada de închiriere a imobilului.
3. Repararea oricăror daune cauzate de utilizare normală a imobilul…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)']

### locuire-13 — locuire
**Întrebare**: Care sunt drepturile proprietarului asupra unui imobil închiriat?
**Răspuns**: Drepturile proprietarului (locatorului) asupra unui imobil închiriat includ: 
1. Dreptul de a verifica periodic imobilul, dar cu notificare prealabilă și acordul chiriașului.
2. Dreptul de a accesa imobilul pentru vizionări cu viitori chiri…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-14 — locuire
**Întrebare**: Care sunt drepturile mele ca membru al unei asociații de proprietari?
**Răspuns**: Ca membru al unei asociații de proprietari, ai următoarele drepturi: Să participi și să votezi la adunarea generală a respectivei asociații; Să îți înscrii candidatura, să candidezi, să alegi și să fii ales în structura organizatorică a aso…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt:', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt: > 📌 Situația financiară a asociației de proprietari']

### locuire-15 — locuire
**Întrebare**: Care sunt drepturile mele dacă sunt proprietarul unui apartament și membru al asociației de proprietari?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt: > 📌 Situația financiară a asociației de proprietari', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt:']

### locuire-17 — locuire
**Întrebare**: Sunt cetățean român, vreau să cumpăr un imobil împreună cu un partener cetățean turc. Există restricții?
**Răspuns**: Dacă sunteți cetățean român și doriți să cumpărați un imobil împreună cu un partener cetățean turc, nu există restricții specifice în acest sens. Cu toate acestea, este important de remarcat faptul că vânzarea unui imobil este valabilă numa…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-19 — locuire
**Întrebare**: Cum obțin un credit ipotecar de la bancă?
**Răspuns**: Pentru a obține un împrumut ipotecar de la o bancă, trebuie să urmați acești pași:
1. Alegeți o bancă: Cercetați și comparați ofertele diferitelor bănci pentru a găsi cea care se potrivește cel mai bine nevoilor dvs.
2. Colectarea documente…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat']

### locuire-20 — locuire
**Întrebare**: Ce taxe plătesc dacă cumpăr o casă de vacanță în Bulgaria?
**Răspuns**: Dacă cumpărați o casă de vacanță în Bulgaria, veți trebui să plătiți taxa pe vânzarea imobiliară (taxa pe transferul proprietății), care este de 1% din valoarea vânzării. În plus, ar putea fi impozitul pe venit dacă aveți un venit anual mai…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC', 'R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > Drepturile și obligațiile mele în calitate de cumpărător', 'Locuire > Vreau să vând un imobil > Drepturile și obligațiile mele în calitate de vânzător', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### locuire-21 — locuire
**Întrebare**: Cum obțin un certificat de urbanism pentru a construi o casă pe terenul meu?
**Răspuns**: Pentru a obține un certificat de urbanism pentru a construi o casă pe terenul dvs., urmați acești pași: 

1. Contactați primăria sau consiliul local pentru a verifica dacă zona este zonată rezidențială și pentru a obține informații despre c…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']

### locuire-x24 — locuire
**Întrebare**: Ce trebuie să fac dacă vreau să vând o casă?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să vând un imobil > În ce condiții pot să vând un imobil?', 'Locuire > Vreau să vând un imobil > În ce condiții pot să vând un imobil? > 📌 De ce acte am nevoie?', 'Locuire > Vreau să vând un imobil > În ce condiții pot să vând un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă cumpărătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil?']

### locuire-x25 — locuire
**Întrebare**: Contractul de închiriere trebuie autentificat la notar?
**Răspuns**: Nu, un contract de închiriere (locațiune) nu trebuie să fie autentificat la notar. Este suficient dacă proprietarul (locatorul) și chiriașul (locatarul) au un contract în formă scrisă și semnat de amândoi.

Cu toate acestea, este important …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să vând un imobil > În ce condiții pot să vând un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Sunt cetățean român', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)']

### locuire-x29 — locuire
**Întrebare**: Pot să las pe cineva să stea în apartamentul meu gratis, cu acte?
**Răspuns**: Da, poți lăsa pe cineva să stea în apartamentul tău gratuit, dar trebuie să ai un contract de închiriere scris și semnat de ambele părți. Acest contract ar trebui să includă informații despre identitatea dvs., a locatarului și a imobilului,…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']

### locuire-x30 — locuire
**Întrebare**: Ce scrie într-o înțelegere de chirie între proprietar și cel care stă?
**Răspuns**: O înțelegere de chirie între proprietar și cel care stă, cunoscută și sub numele de contract de locațiune, conține informații importante pentru ambele părți implicate. Acestea includ identitatea locatorului și a locatarului, descrierea imob…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)']

### locuire-x31 — locuire
**Întrebare**: Cum pun bazele unei organizații a locatarilor din bloc?
**Răspuns**: Pentru a înființa o asociație de proprietari, trebuie să obțineți acordul scris al cel puțin jumătate plus unu dintre numărul proprietarilor dintr-un imobil cu mai multe locuințe, cu condiția ca acesta să aibă minim 3 proprietari. În cadrul…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari?', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari? > 📌 Ce obligații am ca membru al unei asociații de proprietari? > 📌Atribuțiile asociației de proprietari sunt: > 📌 Situația financiară a asociației de proprietari', 'Locuire > Relația cu asociația de proprietari > 📌 Cum se înființează asociația de proprietari? > 📌 Ce drepturi am ca membru al unei asociații de proprietari?']

### locuire-x32 — locuire
**Întrebare**: Cum îmi fac pașaport pentru o vacanță în străinătate?
**Răspuns**: Pentru a obține un pașaport, trebuie să urmați acești pași:
1. Accesați site-ul oficial al Ministerului Afacerilor Interne (MAI) la https://www.mai.gov.ro/.
2. Faceți clic pe linkul „Pașapoarte” din meniul principal.
3. Selectați opțiunea c…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate']

### locuire-x33 — locuire
**Întrebare**: Unde mă programez pentru un control la medicul de familie?
**Răspuns**: Pentru a vă programa pentru o verificare la medicul dumneavoastră, puteți contacta direct cabinetul medical sau puteți utiliza serviciile online ale furnizorului dumneavoastră de asistență medicală. Asigurați-vă că aveți numărul de telefon …
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul medical constatator al nașterii > Am născut acasă > Am domiciliul în România', 'Nașterea > Certificatul medical constatator al nașterii > Am născut într-un spital / într-o clinică > Am domiciliul în România', 'Nașterea > Certificatul medical constatator al nașterii > Am născut acasă > Am domiciliul în străinătate', 'Nașterea > Certificatul medical constatator al nașterii > Am născut într-un spital / într-o clinică > Am domiciliul în străinătate']
