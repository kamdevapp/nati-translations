# Nati translations

Translations of the [Nati](https://github.com/kamdevapp/nati) music player. The app downloads languages
from here (Settings → Language → Download more languages) – no new app version needed.

## Add your language
1. Copy `en.json` to `<code>.json` – e.g. `de.json`, `ja.json` (two-letter ISO 639-1 code).
2. Translate the **values**, never the keys. Set `"_language"` to the language's own name (`"Deutsch"`, `"日本語"`).
3. Keep the placeholders in braces exactly as they are: `{name}`, `{minutes}`, `{n}`…
4. Plurals: keys `plural.<thing>.one / few / many / other` with `{n}` – use the forms your language needs
   (English: one, other; Polish: one, few, many; Japanese: other).
5. Add your language to `index.json` and open a **Pull Request**. Missing texts are shown in English,
   so a partial translation is welcome too.

`server.*` texts are messages from the Nati cloud, `storage.*` are names on the “storage” screen.
Checks run automatically on every Pull Request (`tools/check.py`).

---

## 🇵🇱 Po polsku
Tłumaczenia odtwarzacza Nati. Aplikacja pobiera stąd języki (Ustawienia → Język → Pobierz więcej języków).
Nowy język: skopiuj `en.json` jako `<kod>.json`, przetłumacz wartości (nie klucze), zostaw `{parametry}`,
dopisz język do `index.json` i zgłoś **Pull Request**. Brakujące teksty pokazują się po angielsku.
