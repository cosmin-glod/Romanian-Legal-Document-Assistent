# Asistent conversațional pentru proceduri administrative din România

Aplicația este un asistent de tip RAG care funcționează integral local, fără transmiterea datelor către servicii externe. Sistemul răspunde la întrebări privind proceduri administrative (naștere, căsătorie, locuire), pe baza unui corpus de pe cezicelegea.ro, și poate pre-completa formulare administrative sub formă de PDF.

Peste modelul de limbaj este adăugat un strat de verificare pe bază de contract, care validează structura și semantica răspunsului. Modelul emite o schemă JSON tipizată, iar regulile de mai jos verifică ulterior conținutul:

- R1: răspunsul nu poate fi gol.
- R2: un răspuns care nu este refuz trebuie să citeze cel puțin o sursă.
- R3: indicii de citare trebuie să corespundă surselor regăsite.
- R4: documentele menționate trebuie să fie ancorate în sursele citate, nu inventate.
- R5: un refuz nu poate lista documente.
- R6: un identificator de formular nu poate apărea în lista de documente.
- R7: modelul nu poate refuza atunci când sursele conțin răspunsul.

Descrierea completă a metodei, a experimentelor și a rezultatelor se regăsește în [lucrarea de licență](Asistent%20conversational%20pentru%20proceduri%20administrative%20din%20Romania%20folosind%20RAG%20si%20local%20LLMs.pdf) din rădăcina depozitului.

## Componente principale

- `src/licenta/` : biblioteca (scraper, chunker, index, retriever, generator, contracts, forms, extractor, prefill, evaluate).
- `scripts/` : utilitare de linie de comandă și experimente (evaluare, ablații, grafice).
- `streamlit_app.py` : interfața web.
- `data/` : corpusul scrapat, indexul generat, formularele generate și rezultatele evaluării.
- `kaggle/` : notebook-uri pentru evaluare pe GPU.

Regăsirea folosește modelul de embedding BAAI/bge-m3 cu index Chroma, iar generarea se face prin Ollama, cu modelul ales de utilizator.

## Instalare

Sunt necesare Python 3.13 sau mai nou, uv și Ollama.

```bash
uv sync
ollama pull qwen2.5:3b-instruct-q8_0
uv run python -m licenta.index
```

Ultima comandă construiește indexul din `data/cezicelegea_dump.json`. La prima rulare se descarcă modelul bge-m3 (aproximativ 2,3 GB).

Înainte de utilizare, serverul Ollama trebuie să fie pornit (`ollama serve`). Alternativ, scriptul `scripts/demo.sh` pornește automat Ollama, construiește aplicația și o expune la o adresă publică temporară printr-un tunel Cloudflare, generarea rămânând integral locală.

Precizăm că modelele de dimensiuni mari nu au putut fi rulate local pe echipamentul avut la dispoziție, motiv pentru care evaluarea acestora s-a realizat pe platforma Kaggle, prin notebook-urile din directorul `kaggle/`. Utilizatorii care dispun de o configurație hardware corespunzătoare pot rula întregul sistem exclusiv local, prin Ollama, fără a recurge la Kaggle.

## Utilizare

```bash
# Interfața web
uv run streamlit run streamlit_app.py

# Chat în linia de comandă
uv run python scripts/chat.py "Care este vârsta minimă pentru căsătorie?"

# Doar regăsirea
uv run python scripts/query.py -k 3 -s casatorie "varsta minima"

# Test al motorului de formulare, fără model de limbaj
uv run python scripts/form.py
```

## Evaluare

```bash
uv run python scripts/eval.py            # gold set complet
uv run python scripts/eval.py --limit 3  # test rapid
uv run python scripts/eval_forms.py      # extracția de formulare
```

Rezultatele se salvează în `data/results/runs/`. Tabelul de mai jos prezintă comparația între modele pe gold set-ul de 98 de cazuri:

| Configurație | Acuratețe refuz | Recall@4 | Acoperire cuvinte-cheie | Contract (R1-R6) | Latență |
|---|---|---|---|---|---|
| 3B-Q4 | 62% | 95% | 41% | 53% | 13s |
| 3B-Q8 (recomandat) | 74% | 95% | 53% | 68% | 16s |
| 3B-fp16 | 79% | 95% | 55% | 68% | 27s |
| 7B-Q4 | 69% | 95% | 57% | 68% | 28s |
| 14B-Q4 | 66% | 95% | 47% | 71% | 37s |
| RoLlama3-8B-Q4 | 82% | 95% | 71% | 56% | 48s |

Regăsirea are un recall practic independent de model (95%), astfel încât diferențele apar la calibrarea refuzului și la respectarea contractului, în raport cu latența. Configurația recomandată pentru rulare locală este qwen2.5:3b-instruct-q8_0, ca echilibru între calitate și latență. Detalii complete privind metricile se găsesc în lucrare.

## Variabile de mediu

- `LICENTA_MODEL` : modelul de generare (implicit qwen2.5:3b-instruct-q4_K_M).
- `LICENTA_CHROMA_DIR` : locația indexului Chroma.
- `OLLAMA_HOST` : endpoint Ollama, pentru rulare pe un server remote.

Indexul din `data/chroma_db/` și formularele din `data/forms/` nu sunt versionate, întrucât se pot regenera din corpus și din scripturi.
