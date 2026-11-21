"""Sprawdza pliki tłumaczeń: poprawny JSON, same teksty, te same {parametry} co po angielsku, spis w index.json."""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARAMS = re.compile(r"\{(\w+)\}")
errors = []
en = json.loads((ROOT / "en.json").read_text(encoding="utf-8"))
index = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
listed = {l["code"] for l in index["languages"]}
for f in sorted(ROOT.glob("*.json")):
    if f.name == "index.json":
        continue
    code = f.stem
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"{f.name}: niepoprawny JSON / invalid JSON: {e}"); continue
    if not isinstance(data, dict) or any(not isinstance(v, str) for v in data.values()):
        errors.append(f"{f.name}: wartości muszą być tekstami / values must be strings"); continue
    if "_language" not in data:
        errors.append(f"{f.name}: brak _language / missing _language")
    if code not in listed:
        errors.append(f"{f.name}: brak w index.json / not listed in index.json")
    for key, text in data.items():
        if key.startswith("plural."):
            if set(PARAMS.findall(text)) - {"n"}:
                errors.append(f"{f.name}: {key}: tylko {{n}} / only {{n}} allowed")
            continue
        if key not in en:
            errors.append(f"{f.name}: nieznany klucz / unknown key: {key}"); continue
        if set(PARAMS.findall(text)) != set(PARAMS.findall(en[key])):
            errors.append(f"{f.name}: {key}: inne parametry niż w en.json / placeholders differ from en.json")
for code in listed:
    if not (ROOT / f"{code}.json").exists():
        errors.append(f"index.json: brak pliku / missing file {code}.json")
print("\n".join(errors) or "OK")
sys.exit(1 if errors else 0)
