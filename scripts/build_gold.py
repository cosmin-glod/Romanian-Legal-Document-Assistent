"""Build the expanded gold set on top of the corrected (tree) corpus.

Adds, to the validated 68 seed cases:
  - new in-domain cases covering deep-tree branches surfaced by the scraper fix
    (certificat medical constatator, transcriere, alocație/stimulente, etc.);
  - synonym-paraphrase variants whose wording deliberately AVOIDS cezicelegea
    vocabulary (cununie/bebeluș/hârtii ...), to stress semantic retrieval and the
    exact-substring keyword metric;
  - extra out-of-domain refusal cases.

Every expected_breadcrumb_contains / expected_keyword is validated against the
live corpus (case-insensitive substring); ungrounded ones are reported so they
can be fixed rather than silently penalising the model.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOLD = ROOT / "data" / "eval" / "gold_set.json"
DUMP = ROOT / "data" / "cezicelegea_dump.json"


def _corpus_text() -> tuple[str, str]:
    """Return (all breadcrumb text, all body text), lowercased, for grounding."""
    d = json.loads(DUMP.read_text())
    bcs, bodies = [], []
    for ev in d:
        for s in ev["sections"]:
            bcs.append(" > ".join(s["breadcrumb"]))
            bodies.append(s["text"] + " " + " ".join(s["bullets"]))
    return " || ".join(bcs).lower(), " || ".join(bodies).lower()


# --- new in-domain cases (grounded in pulled leaf texts) --------------------
NEW_INDOMAIN = [
    # nastere
    ("nastere", "Cine îmi eliberează certificatul medical constatator al nașterii dacă am născut într-un spital?",
     ["Certificatul medical constatator"], ["certificatul medical constatator", "spital"]),
    ("nastere", "Certificatul medical constatator ține locul certificatului de naștere?",
     ["Certificatul medical constatator"], ["document medical", "certificatului de naștere"]),
    ("nastere", "Cum transcriu în România certificatul de naștere al copilului emis în străinătate?",
     ["transcri"], ["transcrise", "străine"]),
    ("nastere", "Sunt cetățean străin; ce documente cere primăria pentru a înregistra nașterea copilului?",
     ["Sunt cetățean străin"], ["certificatul medical constatator", "identitate"]),
    ("nastere", "Ce valoare are alocația de stat pentru copii și cine o poate solicita?",
     ["Alocația de stat"], ["alocația de stat", "reprezentantul"]),
    ("nastere", "Ce stimulent financiar primesc pentru nou-născut dacă am domiciliul în București?",
     ["Municipiul București"], ["stimulent", "domiciliu"]),
    ("nastere", "Nu suntem căsătoriți și tatăl vrea să recunoască copilul; ce declarație este necesară?",
     ["Tatăl recunoaște copilul"], ["declarația", "numele copilului"]),
    # casatorie
    ("casatorie", "Ce condiții trebuie îndeplinite ca să mă pot căsători?",
     ["Condiții pentru a te căsători"], ["acordul", "condiții"]),
    ("casatorie", "Unde trebuie să depun declarația de căsătorie?",
     ["Procedură și acte"], ["declaraţie de căsătorie", "primăria"]),
    ("casatorie", "Ce înseamnă regimul comunității legale a bunurilor?",
     ["Regimul matrimonial"], ["bunurile", "comune"]),
    ("casatorie", "Ce documente îmi trebuie pentru a mă căsători ca cetățean român?",
     ["Procedură și acte"], ["identitate", "căsătorie"]),
    # locuire
    ("locuire", "Trebuie să merg la notar dacă vreau să cumpăr un apartament?",
     ["cumpăr un imobil"], ["notar", "imobil"]),
    ("locuire", "Ce trebuie să fac dacă vreau să vând o casă?",
     ["vând un imobil"], ["notar", "imobil"]),
    ("locuire", "Contractul de închiriere trebuie autentificat la notar?",
     ["închiriez un imobil"], ["contract", "scrisă"]),
    ("locuire", "Ce este contractul de comodat?",
     ["comodat"], ["folosință", "comodat"]),
    ("locuire", "Cum se înființează o asociație de proprietari?",
     ["asociația de proprietari"], ["proprietarilor", "acordul scris"]),
]

# --- synonym paraphrases: wording NOT in cezicelegea (cununie/bebeluș/hârtii) -
PARAPHRASES = [
    ("nastere", "Ce hârtii îmi trebuie ca să declar oficial venirea pe lume a bebelușului meu?",
     ["Sunt cetățean străin"], ["certificatul medical constatator", "identitate"]),
    ("nastere", "Ce ajutoare bănești pot lua de la stat după ce mi se naște un copil?",
     ["Alocația de stat"], ["alocația de stat"]),
    ("nastere", "Părintele necăsătorit poate trece numele lui pe micuț?",
     ["Tatăl recunoaște copilul"], ["declarația", "numele copilului"]),
    ("casatorie", "De la ce vârstă am voie să mă cunun?",
     ["Vârsta minimă"], ["aviz medical"]),
    ("casatorie", "Ce buletine ne cer la primărie când vrem să facem nunta?",
     ["Procedură și acte"], ["identitate"]),
    ("casatorie", "Cum se împart agoniseala și averea strânse în timpul mariajului?",
     ["Regimul matrimonial"], ["bunurile", "comune"]),
    ("locuire", "Sunt obligat să apelez la un notar când îmi iau o locuință proprie?",
     ["cumpăr un imobil"], ["notar"]),
    ("locuire", "Pot să las pe cineva să stea în apartamentul meu gratis, cu acte?",
     ["comodat"], ["folosință"]),
    ("locuire", "Ce scrie într-o înțelegere de chirie între proprietar și cel care stă?",
     ["închiriez un imobil"], ["chiriei", "locatar"]),
    ("locuire", "Cum pun bazele unei organizații a locatarilor din bloc?",
     ["asociația de proprietari"], ["proprietarilor"]),
]

# --- extra out-of-domain refusals -------------------------------------------
NEW_REFUSE = [
    ("nastere", "Cum îmi reînnoiesc permisul de conducere?"),
    ("casatorie", "Ce taxe plătesc pentru înmatricularea unei mașini?"),
    ("locuire", "Cum îmi fac pașaport pentru o vacanță în străinătate?"),
    ("locuire", "Unde mă programez pentru un control la medicul de familie?"),
]


def main() -> None:
    seed = json.loads(GOLD.read_text())
    bc_text, body_text = _corpus_text()

    by_cat: dict[str, list[dict]] = {"nastere": [], "casatorie": [], "locuire": []}
    for c in seed:
        by_cat[c["category"]].append(c)

    issues: list[str] = []

    def ground(case_id: str, bcs: list[str], kws: list[str]) -> None:
        for b in bcs:
            if b.lower() not in bc_text:
                issues.append(f"{case_id}: breadcrumb '{b}' NOT in corpus")
        for k in kws:
            if k.lower() not in body_text:
                issues.append(f"{case_id}: keyword '{k}' NOT in corpus body")

    def add(cat, q, bcs, kws, refuse=False, variant="new"):
        cid = f"{cat}-x{len(by_cat[cat]) + 1:02d}"
        case = {
            "id": cid, "category": cat, "should_refuse": refuse, "question": q,
            "expected_breadcrumb_contains": bcs, "expected_keywords": kws,
            "variant": variant,
        }
        if not refuse:
            ground(cid, bcs, kws)
        by_cat[cat].append(case)

    for cat, q, bcs, kws in NEW_INDOMAIN:
        add(cat, q, bcs, kws)
    for cat, q, bcs, kws in PARAPHRASES:
        add(cat, q, bcs, kws, variant="paraphrase")
    for cat, q in NEW_REFUSE:
        add(cat, q, [], [], refuse=True)

    merged = by_cat["nastere"] + by_cat["casatorie"] + by_cat["locuire"]
    indomain = sum(1 for c in merged if not c["should_refuse"])
    refuse = sum(1 for c in merged if c["should_refuse"])

    print(f"total={len(merged)}  in-domain={indomain}  refuse={refuse}")
    for cat in by_cat:
        print(f"  {cat}: {len(by_cat[cat])}")
    if issues:
        print("\nGROUNDING ISSUES (fix before writing):")
        for i in issues:
            print("  ", i)
        print(f"\n{len(issues)} issues -> NOT writing.")
        return

    GOLD.rename(GOLD.with_name("gold_set_pre_expand.json"))
    GOLD.write_text(json.dumps(merged, ensure_ascii=False, indent=2))
    print(f"\nOK, wrote {GOLD}")


if __name__ == "__main__":
    main()
