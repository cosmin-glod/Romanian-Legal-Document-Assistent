# Raport evaluare

**Model**: `qwen2.5:14b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 98

## Metrici globale

- Refusal accuracy: **66%** (65/98)
- Breadcrumb recall@4 (excl. refusal cases): **95%** (78/82)
- Keyword coverage (cazuri non-refusal): **47%** (82 cazuri)
- Contract pass rate (R1..R6): **71%** (70/98)
- Latency medie: **37.0s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 30 | 43% | 100% | 60% | 38.7s |
| locuire | 33 | 82% | 96% | 79% | 31.5s |
| nastere | 35 | 71% | 90% | 74% | 40.9s |

## Distribuția violărilor de contract

- `R7_OVERREFUSAL`: 26
- `R2_UNCITED`: 2

## Cazuri cu probleme (35)


### nastere-10 — nastere
**Întrebare**: Cine poate primi indemnizația pentru creșterea copilului?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-12 — nastere
**Întrebare**: Pe ce perioadă se acordă indemnizația pentru creșterea copilului?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-13 — nastere
**Întrebare**: Am primit certificatul de naștere al copilului în străinătate. Cum îl transcriu pe cel românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Cel puțin un părinte are domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România']

### nastere-15 — nastere
**Întrebare**: Părinții mei nu au avut niciodată domiciliul în România. Pot înregistra nașterea copilului meu aici?
**Răspuns**: Dacă părinții copilului sunt cetățeni străini și nu au domiciliu în România, înregistrarea nașterii se poate face la ambasada sau consulatul țării de origine a părinților. Verifică lista misiunilor diplomatice din România pentru a afla care…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-16 — nastere
**Întrebare**: Sunt cetățean român cu domiciliul în Franța. Am născut acolo. Cum obțin certificatul de naștere al copilului meu românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-18 — nastere
**Întrebare**: Părinții au nume de familie diferite. Ce nume va purta copilul?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Suntem căsătoriți']

### nastere-20 — nastere
**Întrebare**: Am cetățenie dublă, română și franceză, iar copilul s-a născut în Franța. Care e procedura completă pentru a-i obține certificatul românesc?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=False · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl nu recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean străin > Vreau să înregistrez nașterea la autoritățile române > Nu suntem căsătoriți > Tatăl recunoaște copilul']

### nastere-22 — nastere
**Întrebare**: Vreau să adopt un copil cu vârsta de peste 5 ani. Procedura?
**Răspuns**: Procedura de adoptare pentru un copil cu vârsta peste 5 ani implică pași complexi care sunt gestionai de către autorități competente, cum ar fi Comisia Națională pentru Protecția Copiilor. În general, aceste etape includ:

1. **Informații P…
**Status**: recall=None · refusal_correct=False · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului > Stimulentul de inserție', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în România > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap > Indemnizația de maternitate > Indemnizația pentru creșterea copilului']

### nastere-x27 — nastere
**Întrebare**: Cum transcriu în România certificatul de naștere al copilului emis în străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la ambasada / oficiul consular al României', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Cel puțin un părinte are domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu mai stau în România, dar cel puțin un părinte a avut domiciliul în România', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în străinătate > Vreau să transcriu certificatul de naștere la autoritățile române > Părinții nu au avut niciodată domiciliul în România']

### nastere-x28 — nastere
**Întrebare**: Sunt cetățean străin; ce documente cere primăria pentru a înregistra nașterea copilului?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl recunoaște copilul', 'Nașterea > Certificatul de naștere > Sunt cetățean român > Nașterea a avut loc în România > Partenerul este cetățean român > Suntem căsătoriți', 'Nașterea > Certificatul de naștere > Sunt cetățean străin > Vreau să înregistrez nașterea la primărie > Nu suntem căsătoriți > Tatăl nu recunoaște copilul']

### nastere-x29 — nastere
**Întrebare**: Ce valoare are alocația de stat pentru copii și cine o poate solicita?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean străin cu reședința în România și nu este beneficiar al protecției temporare > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în străinătate > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în România > Părinții muncesc în România > Copilul nu este încadrat într-un grad de handicap', 'Nașterea > Ajutor financiar > Alocația de stat pentru copii > Copilul este cetățean român > Copilul s-a născut în străinătate > Copilul nu este încadrat într-un grad de handicap']

### casatorie-05 — casatorie
**Întrebare**: Pot să iau numele partenerului ca nume de familie după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-07 — casatorie
**Întrebare**: Putem să oficiem căsătoria la o ambasadă a României din străinătate?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-09 — casatorie
**Întrebare**: Ce documente trebuie să depun la primărie pentru căsătorie în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.']

### casatorie-10 — casatorie
**Întrebare**: Ce nume de familie pot să aleg după căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Relația de cuplu', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România']

### casatorie-11 — casatorie
**Întrebare**: Vreau să mă căsătoresc în străinătate. Ce procedură există?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate']

### casatorie-12 — casatorie
**Întrebare**: Care sunt pașii pentru depunerea declarației de căsătorie când partenerul este cetățean străin?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!']

### casatorie-13 — casatorie
**Întrebare**: Sunt cetățean român căsătorit cu un cetățean UE. Trebuie traduceri pentru actele lui?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România']

### casatorie-14 — casatorie
**Întrebare**: Am încheiat căsătoria în străinătate. Cum o transcriu/recunosc în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate']

### casatorie-15 — casatorie
**Întrebare**: Partenerul meu este cetățean străin. Ce trebuie să știu suplimentar înainte de căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-16 — casatorie
**Întrebare**: Sunt verișor primar cu partenera. Putem să ne căsătorim?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie']

### casatorie-17 — casatorie
**Întrebare**: Sunt minor de 16 ani și vreau să mă căsătoresc. Care sunt pașii legali completi?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-18 — casatorie
**Întrebare**: Partenerul meu nu cunoaște limba română. Ce este obligatoriu la oficierea căsătoriei?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat. > ⚠️ ATENȚIE!', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### casatorie-21 — casatorie
**Întrebare**: Cum împart pensia de soț decedat?
**Răspuns**: Pentru a împărți pensia de soț decedat, este important să cunoașteți regimul matrimonial aplicabil. În cazul comunității legale sau convențională (care presupune că toate bunurile dobândite în timpul căsătoriei sunt comune), pensia de soț d…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Drepturile și obligațiile soților > Locuire', 'Căsătoria > Regimul matrimonial > 📌 Comunitatea legală > 📌 Comunitatea Convențională > 📌 Separația de bunuri', 'Căsătoria > Drepturile și obligațiile soților > Bunuri și datorii comune > 📌 Bunurile și datoriile comune', 'Căsătoria > Drepturile și obligațiile soților > Relația de cuplu']

### casatorie-22 — casatorie
**Întrebare**: Putem semna un contract prematrimonial înainte de căsătorie?
**Răspuns**: Da, puteți semna un contract prematrimonial (convenție matrimonială) înainte de căsătorie. Acesta poate fi încheiat înainte sau după oficierea căsătoriei și poate stabili regimul matrimonial ales de către soți, cum ar fi separarea bunurilor…
**Status**: recall=None · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în străinătate', 'Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie > 📌 Monogamie > 📌 Căsătoria între rude > 📌 Persoana pusă sub o măsură de ocrotire specială', 'Căsătoria > Condiții pentru a te căsători']

### casatorie-x24 — casatorie
**Întrebare**: Unde trebuie să depun declarația de căsătorie?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.']

### casatorie-x26 — casatorie
**Întrebare**: Ce documente îmi trebuie pentru a mă căsători ca cetățean român?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie > 📌 PASUL 2 - Oficierea căsătoriei > 🗂 În cazul cetăţenilor străini care nu cunosc limba română, la oficierea căsătoriei este obligatorie prezenţa unui interpret autorizat.', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în străinătate']

### casatorie-x28 — casatorie
**Întrebare**: Ce buletine ne cer la primărie când vrem să facem nunta?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean străin > 📌 PASUL 1 - Declarația de căsătorie', 'Căsătoria > Procedură și acte necesare > Sunt cetățean străin > Partenerul este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean român > Ne căsătorim în România', 'Căsătoria > Procedură și acte necesare > Sunt cetățean român > Partenerul / partenera este cetățean străin > Ne căsătorim în România']

### locuire-02 — locuire
**Întrebare**: Ce acte îmi trebuie ca cumpărător al unui imobil în România?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Nu am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Sunt cetățean român > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui stat membru UE sau al Spațiului Economic European > Am reședința în România > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie?']

### locuire-05 — locuire
**Întrebare**: Care sunt obligațiile proprietarului față de chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-06 — locuire
**Întrebare**: Care sunt drepturile mele ca chiriaș?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-08 — locuire
**Întrebare**: Care sunt obligațiile chiriașului față de proprietar?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a descrie obligațiile chiriașului (locatarului) față de proprietar.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-11 — locuire
**Întrebare**: Care sunt obligațiile chiriașului față de imobil?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a descrie obligațiile chiriașului (locatarului) față de imobil.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)']

### locuire-13 — locuire
**Întrebare**: Care sunt drepturile proprietarului asupra unui imobil închiriat?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=False
**Violations**: ['R7_OVERREFUSAL']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Drepturile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Drepturile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)']

### locuire-x29 — locuire
**Întrebare**: Pot să las pe cineva să stea în apartamentul meu gratis, cu acte?
**Răspuns**: În cazul în care dorești ca cineva să ocupe gratuit un apartament tău, este recomandat să încheie un contract formal de închiriere pentru a stabili condițiile acestui acord și pentru a proteja interesele ambilor părți. Acest lucru poate pre…
**Status**: recall=False · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile proprietarului (locatorului) > Obligațiile proprietarului (locatorului)', 'Locuire > Vreau să închiriez un imobil > Drepturile și obligațiile chiriașului (locatarului) > Obligațiile chiriașului (locatarului)', 'Locuire > Vreau să închiriez un imobil > Despre contractul de locațiune (închiriere)', 'Locuire > Vreau să cumpăr un imobil > În ce condiții pot să cumpăr un imobil? > Nu sunt cetățean român > Sunt cetățeanul unui alt stat > 📌 În ce condiții pot cumpăra un imobil? > 📌 De ce acte am nevoie? > 📌 Ce acte trebuie să aducă vânzătorul?']
