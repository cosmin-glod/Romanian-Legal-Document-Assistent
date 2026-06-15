# Raport evaluare

**Model**: `qwen2.5:7b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 98

## Metrici globale

- Refusal accuracy: **69%** (68/98)
- Breadcrumb recall@4 (excl. refusal cases): **95%** (78/82)
- Keyword coverage (cazuri non-refusal): **57%** (82 cazuri)
- Contract pass rate (R1..R6): **68%** (67/98)
- Latency medie: **28.3s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 30 | 57% | 100% | 57% | 29.4s |
| locuire | 33 | 70% | 96% | 64% | 26.3s |
| nastere | 35 | 80% | 90% | 83% | 29.3s |

## Distribuția violărilor de contract

- `R7_OVERREFUSAL`: 24
- `R5_REFUSAL_WITH_DOCS`: 8
- `R6_FORM_ID_IN_DOCS`: 5
- `R2_UNCITED`: 3
- `R4_FABRICATED_DOC`: 2

## Cazuri cu probleme (36)


### nastere-05 — nastere
**Întrebare**: Părinții nu sunt căsătoriți. Tatăl recunoaște copilul. Ce documente trebuie depuse la primărie?
**Răspuns**: Pentru a înregistra nașterea copilului atunci când părinții nu sunt căsătoriți și tatăl recunoaște copilul, trebuie depuse următoarele documente la primărie:
- Certificatul medical constatator al nașterii care trebuie să poarte număr de înr…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul']

### nastere-10 — nastere
**Întrebare**: Cine poate primi indemnizația pentru creșterea copilului?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre indemnizația pentru creșterea copilului.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-12 — nastere
**Întrebare**: Pe ce perioadă se acordă indemnizația pentru creșterea copilului?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre indemnizația de creștere a copilului. Sursa specifică nu conține aceste detalii.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-15 — nastere
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: În România, puteți înregistra nașterea copilului dvs. la primărie, deoarece nu sunteți căsătoriți și tatăl recunoaște copilul. Serviciul de Stare Civilă va cere următoarele documente: Certificatul medical constatator al nașterii care trebui…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-16 — nastere
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre procedurile de obținere a certificatului de naștere al copilului. Vă recomand să consultați site-ul oficial al Biroului Național de Statut Civil sau …
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-18 — nastere
**Întrebare**: Părinții au nume de familie diferite. Ce nume va purta copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la această întrebare.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Suntem căsătoriți']

### nastere-19 — nastere
**Întrebare**: Sunt mamă singură, tatăl copilului nu recunoaște copilul. Cum stabilesc paternitatea legal?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre stabilirea paternității. Pentru mai multe detalii, vă recomand să consultați legi privind dreptul de familie sau să vă adresați unui avocat specializ…
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-20 — nastere
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre procedurile specifice de obținere a certificatului de naștere românesc pentru copil născut în Franța. Pentru mai multe detalii, vă recomand să consul…
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-x29 — nastere
**Întrebare**: Ce valoare are alocația de stat pentru copii și cine o poate solicita?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre alocația de stat pentru copii. Vă recomand să consultați site-ul oficial al Ministerului Dezvoltării Sociale sau un serviciu local de asistență socia…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în străinătate > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în România > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în străinătate > Copilul nu este încadrat într-un grad de handicap']

### casatorie-03 — casatorie
**Întrebare**: Sunt deja căsătorit. Pot încheia o nouă căsătorie?
**Răspuns**: Dacă ești deja căsătorit, nu poți încheia o altă căsătorie. Poligamia este interzisă în România.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie', 'Căsătoria > Condiții pentru a te căsători', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-05 — casatorie
**Întrebare**: Pot să iau numele partenerului ca nume de familie după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre această opțiune. Vă recomand să consultați documentul oficial de declarate de căsătorie sau altă sursă legală specifică procedurii de căsătorie.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R6_FORM_ID_IN_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-07 — casatorie
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre oficierea căsătoriei la ambasade/consulate române din străinătate. Vă sfătuiesc să consultați site-ul oficial al Ministerului Afacerilor Externe sau …
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-10 — casatorie
**Întrebare**: Ce nume de familie pot să aleg după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre numele de familie după căsătorie.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-11 — casatorie
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu despre procedurile de căsătorie în străinătate. Vă pot oferi următoarele informații generale:

1. Puteți căsători la sediul misiunii diplomatice ale României (a…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate']

### casatorie-12 — casatorie
**Întrebare**: Care sunt pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la această întrebare.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!']

### casatorie-13 — casatorie
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la această întrebare. Te sfătuiesc să contactezi autoritățile competente pentru informații precise și actualizate privind procesul de legalizare sau apostil…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România']

### casatorie-15 — casatorie
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dumneavoastră. Vă rog să furnizați mai multe detalii sau sursă legată de procedurile de căsătorie.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-16 — casatorie
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Pentru căsătorire, trebuie să depuneti o declarație de căsătorie la primăria locului de domiciliu sau reședință al unuia dintre voi. Dacă nu aveți amândoi 18 ani, va fi necesar avizul medical și încuviințarea părinților sau tutorelui, dacă …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R6_FORM_ID_IN_DOCS']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-17 — casatorie
**Întrebare**: Sunt minor de 16 ani și vreau să mă căsătoresc. Care sunt pașii legali completi?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dvs. Desigur, puteți consulta primăria locală sau Serviciul Public Comunitar Local de Evidență a Persoanelor (SPCLEP) pentru informații detali…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-18 — casatorie
**Întrebare**: Partenerul meu nu cunoaște limba română. Ce este obligatoriu la oficierea căsătoriei?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-19 — casatorie
**Întrebare**: Cum divorțez de partenerul meu?
**Răspuns**: Pentru divorț, trebuie să depuneti o cerere în primărie unde locuiești. Va trebui să furnizați documente precum actele de identitate, certificatul de naștere al copiilor dacă există, și alte documente relevante. Dacă partenerul tău nu este …
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Proprietarul vrea să mă dea afară - ce pot face?', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală > 📌 Comunitatea Convențională > 📌 Separația de bunuri', 'Căsătoria > Drepturile și obligațiile soților > Locuire', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-22 — casatorie
**Întrebare**: Putem semna un contract prematrimonial înainte de căsătorie?
**Răspuns**: Da, puteți semna un contract prematrimonial înainte de căsătorie. Acest contract poate fi încheiat înainte sau în timpul căsătoriei și produce efecte de la data încheierii sale. Dacă alegeți acest regim matrimonial, va trebui să prezentați …
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie > 📌 Căsătoria între rude > 📌 Persoana pusă sub o măsură de ocrotire specială', 'Căsătoria > Condiții pentru a te căsători']

### casatorie-x24 — casatorie
**Întrebare**: Unde trebuie să depun declarația de căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre debunarea declarației de căsătorie. Vă recomand să consultați site-ul oficial al Primăriei sau serviciul de stare civilă din locul dumneavoastră de r…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.']

### casatorie-x28 — casatorie
**Întrebare**: Ce buletine ne cer la primărie când vrem să facem nunta?
**Răspuns**: Pentru a efectua declarația de căsătorie, va trebui să prezentați următoarele documente în original: actele voastre de identitate (cartea de identitate, buletin sau carte de identitate provizorie).
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### locuire-02 — locuire
**Întrebare**: Ce acte îmi trebuie ca cumpărător al unui imobil în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dumneavoastră. Poate fi necesar să consultați documentele administrative locale sau să contactați autoritățile relevante pentru instrucțiuni s…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-03 — locuire
**Întrebare**: Ce trebuie să conțină un contract de închiriere între proprietar și chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu despre structura unui contract de închiriere. Sursa specifică nu conține aceste detalii.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)']

### locuire-04 — locuire
**Întrebare**: Vreau să închiriez un apartament. Trebuie obligatoriu să facem contract în scris?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre contractul de închiriere. Vă recomand să consultați legi și regulamente specifice privind închirieri imobiliare din România, sau să vă adresați unui …
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-05 — locuire
**Întrebare**: Care sunt obligațiile proprietarului față de chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre obligațiile proprietarului față de chiriaș. Vă recomand să consultați documentul oficial 'Contract de închiriere (locațiune)' pentru detalii precise.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R6_FORM_ID_IN_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-06 — locuire
**Întrebare**: Care sunt drepturile mele ca chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre drepturile chiriașului. Vă recomand să consultați un avocat sau documentele administrative relevante pentru acest subiect.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-08 — locuire
**Întrebare**: Care sunt obligațiile chiriașului față de proprietar?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu la această întrebare. Poți consulta documentul 'contract_inchiriere' pentru mai multe detalii despre obligațiile chiriașului față de proprietar.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R6_FORM_ID_IN_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-09 — locuire
**Întrebare**: Sunt cetățean al unui stat UE. În ce condiții pot cumpăra o casă în România?
**Răspuns**: Dacă ești cetățean al unui stat membru al Uniunii Europene sau al Spațiului Economic European și vrei să cumperi un imobil în România, poți face acest lucru în aceleași condiții ca un cetățean român. Pentru că ești nerezident, va trebui să …
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-10 — locuire
**Întrebare**: Sunt cetățean al unui stat non-UE. Pot cumpăra un imobil în România?
**Răspuns**: Poți cumpăra un imobil în România ca cetățean al unui stat non-UE, dar cel mai rapid mod este prin înființarea unei firme SRL cu asociat unic pe teritoriul României și achiziționarea imobiliarului de către respectivul SRL. Este important să…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-11 — locuire
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu despre obligațiile chiriașului față de imobil. Sursa specifică obligațiile chiriașului, dar nu conține detalii specifice.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)']

### locuire-13 — locuire
**Întrebare**: Care sunt drepturile proprietarului asupra unui imobil închiriat?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine despre drepturile proprietarului asupra unui imobil închiriat. Vă recomand să consultați documentul oficial de contract de închiriere sau o consultanță juri…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R6_FORM_ID_IN_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-x29 — locuire
**Întrebare**: Pot să las pe cineva să stea în apartamentul meu gratis, cu acte?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu certitudine la întrebarea dumneavoastră. Cu toate acestea, în general, este recomandat să formalizați situația de locare prin un contract de închiriere pentru a proteja…
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']

### locuire-x30 — locuire
**Întrebare**: Ce scrie într-o înțelegere de chirie între proprietar și cel care stă?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde cu detaliu despre structura contractului de închiriere. Cu toate acestea, pot menționa câteva elemente esențiale care ar trebui să apară în acest document, bazându-mă pe c…
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R5_REFUSAL_WITH_DOCS', 'R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)']
