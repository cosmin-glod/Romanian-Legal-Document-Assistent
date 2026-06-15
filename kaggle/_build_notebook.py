"""Generate the all-in-one Kaggle notebook (kaggle/licenta_gpu_all.ipynb)."""
import json
from pathlib import Path

cells = []
def md(s): cells.append({"cell_type": "markdown", "metadata": {}, "source": s.splitlines(keepends=True)})
def code(s): cells.append({"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": s.strip("\n").splitlines(keepends=True)})

md("""# Licență — toate evaluările GPU (un singur notebook)

Rulează pe **Kaggle GPU T4 × 2** tot ce nu poate rula pe laptop:

1. **Eval multi-model** pe setul de aur (68 cazuri): sweep de cuantizare (3B Q4/Q8/FP16) + scară (3B → 7B → 14B).
2. **LLM-judge faithfulness** — un model mare judecă fidelitatea fiecărui răspuns față de surse (metrică reală, nu proxy lexical).
3. **R7 recovery** — măsoară câte refuzuri spurioase recuperează reîncercarea cu sursă numită.
4. **Bundle** — arhivează toate rezultatele în `/kaggle/working/results.zip` de descărcat.

**Înainte de Run All:** Accelerator = **GPU T4 ×2**, Internet = **On**, Dataset = `licenta` (glodcosmin).
Alege ce rulezi din cellula de config (Secțiunea 9). Sweep-ul complet durează ~1–2h; pornește cu un subset.
""")

md("## 1. Mediu + Ollama (2 instanțe, una per GPU)")
code("!pip uninstall -y torchvision torchaudio >/dev/null 2>&1; !sudo apt-get install -y zstd >/dev/null 2>&1; !curl -fsSL https://ollama.com/install.sh | sh")
code("!nvidia-smi")
code("""
import subprocess, time, os, urllib.request
subprocess.run(['pkill', '-f', 'ollama serve'], capture_output=True); time.sleep(3)
HOSTS = []
for gpu_id, port in [(0, 11434), (1, 11435)]:
    env = os.environ.copy()
    env['CUDA_VISIBLE_DEVICES'] = str(gpu_id)
    env['OLLAMA_HOST'] = f'127.0.0.1:{port}'
    env['OLLAMA_NUM_PARALLEL'] = '2'
    env['OLLAMA_MAX_LOADED_MODELS'] = '1'
    log = open(f'/tmp/ollama_gpu{gpu_id}.log', 'w')
    subprocess.Popen(['ollama', 'serve'], env=env, stdout=log, stderr=log)
    HOSTS.append(f'http://127.0.0.1:{port}')
for host in HOSTS:
    for i in range(60):
        try:
            urllib.request.urlopen(f'{host}/api/version', timeout=2); print(f'{host}: UP'); break
        except Exception: time.sleep(1)
    else:
        !tail -30 /tmp/ollama_gpu*.log
        raise RuntimeError(f'{host} down')
""")

md("## 2. Cod + date + dependențe")
code("""
import shutil, sys, os
from pathlib import Path
SRC = Path('/kaggle/input/datasets/glodcosmin/licenta')
if not SRC.exists():  # dataset may mount under a different root
    cands = list(Path('/kaggle/input').glob('**/src/licenta'))
    SRC = cands[0].parents[1] if cands else SRC
WORK = Path('/kaggle/working/licenta')
if WORK.exists(): shutil.rmtree(WORK)
WORK.mkdir()
shutil.copytree(SRC / 'src', WORK / 'src')
(WORK / 'data' / 'eval' / 'runs').mkdir(parents=True)
shutil.copy(SRC / 'data' / 'cezicelegea_dump.json', WORK / 'data' / 'cezicelegea_dump.json')
shutil.copy(SRC / 'data' / 'eval' / 'gold_set.json', WORK / 'data' / 'eval' / 'gold_set.json')
sys.path.insert(0, str(WORK / 'src')); os.chdir(WORK)
print('Working dir:', os.getcwd())
""")
code("!pip install -q 'chromadb>=1.5' 'sentence-transformers<4' 'pydantic>=2.13' 'ollama>=0.6' 'fpdf2'")

md("## 3. Index Chroma (bge-m3) + rutare per-thread")
code("""
import logging; logging.basicConfig(level=logging.WARNING, format='%(message)s')
from licenta.index import build_index
build_index()
""")
code("""
import threading, ollama
_tls = threading.local(); _orig_chat = ollama.chat
def _routing_chat(*a, **k):
    host = getattr(_tls, 'host', None)
    return ollama.Client(host=host).chat(*a, **k) if host else _orig_chat(*a, **k)
ollama.chat = _routing_chat

def pull_and_warm(model):
    c = ollama.Client(host=HOSTS[0])
    print('pull', model, '...', flush=True)
    os.environ['OLLAMA_HOST'] = '127.0.0.1:11434'
    subprocess.run(['ollama', 'pull', model], check=True)
    for host in HOSTS:
        ollama.Client(host=host).chat(model=model, messages=[{'role':'user','content':'hi'}])
    print('warm OK:', model)
""")

md("""## 4. Helper: rulare paralelă a evaluării pentru un model
Salvează `data/eval/runs/<label>/results.json` + `report.md`.""")
code("""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from tqdm.auto import tqdm
import json, time
from licenta.evaluate import load_gold_set, evaluate_case, _build_report
from licenta.retriever import Retriever

retriever = Retriever()
cases = load_gold_set(Path('data/eval/gold_set.json'))

def run_eval(label, model, k=4, temperature=0.0, few_shot=False):
    pull_and_warm(model)
    def worker(ic):
        idx, case = ic
        _tls.host = HOSTS[idx % len(HOSTS)]
        try: return evaluate_case(case, retriever, model, k=k, temperature=temperature, few_shot=few_shot)
        except Exception as e: print('ERR', case.id, e); return None
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=len(HOSTS)*2) as ex:
        results = [r for r in tqdm(ex.map(worker, enumerate(cases)), total=len(cases)) if r]
    out = Path('data/eval/runs') / label; out.mkdir(parents=True, exist_ok=True)
    (out/'results.json').write_text(json.dumps([asdict(r) for r in results], ensure_ascii=False, indent=2))
    (out/'report.md').write_text(_build_report(results, model, k))
    print(f'{label}: {len(results)} cazuri in {time.time()-t0:.0f}s -> {out}')
    return results
""")

md("## 5. Config — alege ce rulezi")
code("""
# (label, ollama_tag). Comentează ce nu vrei. FP16 3B ~6GB, 14B Q4 ~9GB (intră pe un T4).
MODELS = [
    ('3b_q4',  'qwen2.5:3b-instruct-q4_K_M'),
    ('3b_q8',  'qwen2.5:3b-instruct-q8_0'),     # sweep cuantizare
    ('3b_fp16','qwen2.5:3b-instruct-fp16'),     # sweep cuantizare
    ('7b_q4',  'qwen2.5:7b-instruct-q4_K_M'),
    ('14b_q4', 'qwen2.5:14b-instruct-q4_K_M'),  # al 3-lea punct de scară
    # ('rollama8b', 'TAG_VALID_OLLAMA'),        # model RO: pune un tag valid din ollama.com/library
]
JUDGE_MODEL = '14b_q4'   # cheia din MODELS folosită ca judecător de fidelitate
RUN_FEWSHOT = False      # True -> adaugă o rulare few-shot pe 3B
RUN_R7_RECOVERY = True
""")

md("## 6. Rulează eval pentru toate modelele")
code("""
all_results = {}
for label, tag in MODELS:
    try:
        all_results[label] = run_eval(label, tag)
    except Exception as e:
        print(f'SKIP {label} ({tag}): {e}')
if RUN_FEWSHOT:
    all_results['3b_q4_fewshot'] = run_eval('3b_q4_fewshot', dict(MODELS)['3b_q4'], few_shot=True)
""")

md("""## 7. Tabel comparativ (sweep + scară)
refusal accuracy, recall@4, lexical recall, contract pass, latency.""")
code("""
import statistics as st
def summarize(results):
    n=len(results)
    ref=sum(r.refusal_correct for r in results)/n
    rr=[r for r in results if r.breadcrumb_recall is not None]
    rec=sum(1 for r in rr if r.breadcrumb_recall)/len(rr)
    kw=[r.keyword_coverage for r in results if r.keyword_coverage is not None]
    con=sum(r.contract_valid for r in results)/n
    lat=sum(r.latency_s for r in results)/n
    return dict(n=n, refusal=round(100*ref), recall=round(100*rec),
                kw=round(100*sum(kw)/len(kw)) if kw else 0, contract=round(100*con), lat=round(lat))
import pandas as pd
df = pd.DataFrame({lab: summarize(res) for lab,res in all_results.items()}).T
print(df.to_string())
df.to_csv('data/eval/runs/summary.csv')
df
""")

md("""## 8. LLM-judge faithfulness
Un model mare judecă, per caz non-refuz, dacă răspunsul e susținut de sursele citate:
**corect / parțial / incorect**. Metrică reală de fidelitate (vs proxy-ul lexical).""")
code("""
import json, re
from licenta.generator import DEFAULT_MODEL

JUDGE_TAG = dict(MODELS)[JUDGE_MODEL]
pull_and_warm(JUDGE_TAG)

JUDGE_SYS = ('Ești un evaluator strict. Primești o ÎNTREBARE, un RĂSPUNS și SURSELE citate. '
 'Decide dacă răspunsul este susținut DOAR de surse. Răspunde cu un singur cuvânt: '
 '"corect" (tot ce afirmă e în surse), "partial" (parțial susținut sau incomplet) sau '
 '"incorect" (afirmă lucruri absente din surse sau greșite).')

def judge_one(case_result):
    if case_result['is_refusal'] or not case_result.get('cited_sources_text'):
        return None
    srcs = '\\n'.join(f'[S{i+1}] {t}' for i,t in enumerate(case_result['cited_sources_text']))
    msg = f"ÎNTREBARE: {case_result['question']}\\n\\nRĂSPUNS: {case_result['answer_text']}\\n\\nSURSE:\\n{srcs}"
    _tls.host = HOSTS[0]
    r = ollama.chat(model=JUDGE_TAG, messages=[{'role':'system','content':JUDGE_SYS},{'role':'user','content':msg}],
                    options={'temperature':0})
    w = r['message']['content'].strip().lower()
    return 'corect' if 'corect' in w else ('partial' if 'partial' in w or 'parțial' in w else 'incorect')

def judge_model(label):
    rows = json.loads(Path(f'data/eval/runs/{label}/results.json').read_text())
    verdicts = [v for v in (judge_one(r) for r in rows) if v]
    from collections import Counter; c = Counter(verdicts)
    n = len(verdicts) or 1
    print(f'{label}: judge n={len(verdicts)} | corect {100*c["corect"]//n}% partial {100*c["partial"]//n}% incorect {100*c["incorect"]//n}%')
    Path(f'data/eval/runs/{label}/judge.json').write_text(json.dumps(dict(c), ensure_ascii=False))
    return c

for label in all_results:
    try: judge_model(label)
    except Exception as e: print('judge skip', label, e)
""")

md("""## 9. R7 recovery (refuz spurious recuperat)
Rulează cazurile spurioase + control prin bucla cu R7 activ; câte refuzuri spurioase devin răspunsuri,
fără a sparge refuzurile corecte.""")
code("""
if RUN_R7_RECOVERY:
    base_label = '3b_q4'
    base = json.loads(Path(f'data/eval/runs/{base_label}/results.json').read_text())
    spur = [r['case_id'] for r in base if r['is_refusal'] and not r['should_refuse']]
    ctrl = [r['case_id'] for r in base if r['should_refuse']]
    gold = {c.id: c for c in cases}
    from licenta.generator import generate
    tag = dict(MODELS)['3b_q4']; pull_and_warm(tag)
    rows=[]
    def w(ic):
        idx,cid = ic; _tls.host = HOSTS[idx % len(HOSTS)]
        case = gold[cid]; hits = retriever.query(case.question, k=4)
        a = generate(case.question, hits, model=tag, temperature=0.0)
        return dict(id=cid, subset=('control' if case.should_refuse else 'spurious'),
                    base_refused=(cid in spur or cid in [r['case_id'] for r in base if r['is_refusal']]),
                    final_refused=a.schema.is_refusal, attempts=a.attempts)
    with ThreadPoolExecutor(max_workers=len(HOSTS)*2) as ex:
        rows = list(tqdm(ex.map(w, enumerate(spur+ctrl)), total=len(spur+ctrl)))
    sp=[r for r in rows if r['subset']=='spurious']; ct=[r for r in rows if r['subset']=='control']
    rec=sum(1 for r in sp if not r['final_refused'])
    kept=sum(1 for r in ct if r['final_refused'])
    print(f'R7 recovery: spurious recuperate {rec}/{len(sp)} | control pastrate {kept}/{len(ct)}')
    Path('data/eval/runs/r7_recovery.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
""")

md("## 10. Bundle rezultatele (descarcă results.zip)")
code("""
import shutil
shutil.make_archive('/kaggle/working/results', 'zip', 'data/eval/runs')
print('Gata -> /kaggle/working/results.zip')
!ls -la /kaggle/working/results.zip
""")

nb = {"cells": cells,
      "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                   "language_info": {"name": "python"}, "accelerator": "GPU"},
      "nbformat": 4, "nbformat_minor": 5}
Path('kaggle/licenta_gpu_all.ipynb').write_text(json.dumps(nb, indent=1))
print('wrote kaggle/licenta_gpu_all.ipynb with', len(cells), 'cells')
