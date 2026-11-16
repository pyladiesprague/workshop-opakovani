# Tahák – Správce osobních financí

Věci, které v projektu potřebuješ a v tahácích z lekcí nejsou. Testy a
import z vlastního souboru najdeš v tahácích lekcí workshopu:

- [`lekce-testovani/TAHAK.md`](../lekce-testovani/TAHAK.md): jak napsat
  test, jak číst test, který neprošel, časté hlášky, co testovat,
- [`lekce-moduly/TAHAK.md`](../lekce-moduly/TAHAK.md): *Dva zápisy importu*
  a *Vlastní modul*.

## Import z finance.py

```python
from finance import zustatek    # v app.py: jen vybrané funkce
import finance                  # v testech: celý soubor, volá se finance.zustatek(...)
```

Při importu se `finance.py` celý provede. Proto v něm mimo funkce nesmí
být žádný `input()` ani `print()`.

## Vlastní data pro každý test

Každý test si má připravit vlastní data. V `test_finance.py` k tomu slouží
funkce `ukazka()`, která pokaždé vrátí nový seznam. Kdyby testy sdílely
jeden seznam, test, který do něj něco přidá, by rozbil ty ostatní.

```python
def test_pridani_transakce():
    transakce = ukazka()
    finance.pridej_transakci(transakce, "2026-11-21", "vydaj", 90, "jidlo", "koláč")
    assert len(transakce) == 6
```

## Soubory a JSON

Budeš potřebovat v kroku 6. JSON je formát, který umí zapsat seznamy
a slovníky jako text. Vypadá skoro stejně jako v Pythonu.

Zápis do souboru:

```python
import json

nakup = [{"co": "rohlíky", "kusu": 5}, {"co": "máslo", "kusu": 1}]

with open("nakup.json", "w", encoding="utf-8") as soubor:
    json.dump(nakup, soubor, ensure_ascii=False, indent=2)
```

Čtení ze souboru:

```python
import json

with open("nakup.json", encoding="utf-8") as soubor:
    nakup = json.load(soubor)

print(nakup[0]["co"])       # rohlíky
```

| Zápis | Co znamená |
|---|---|
| `open("nakup.json", "w", ...)` | otevři soubor pro zápis (`w` jako write); když neexistuje, vytvoří se, když existuje, přepíše se |
| `open("nakup.json", ...)` | bez `"w"` se soubor otevře pro čtení; když neexistuje, je to `FileNotFoundError` |
| `encoding="utf-8"` | kódování textu; piš ho vždycky, jinak se pokazí háčky a čárky |
| `with ... as soubor:` | uvnitř odsazeného bloku je soubor otevřený, na konci se sám zavře |
| `json.dump(data, soubor)` | zapiš data do souboru |
| `ensure_ascii=False` | nech háčky a čárky čitelné |
| `indent=2` | odsaď zápis, ať se soubor dá číst |
| `json.load(soubor)` | přečti soubor a vrať, co v něm je |

Do JSON jdou seznamy, slovníky, texty, čísla, `True`, `False` a `None`.
N-tice se uloží jako seznam.

Samotné jméno souboru jako `"nakup.json"` se hledá ve složce, ze které
program spouštíš. Soubor vedle programu najdeš odkudkoli takhle:

```python
from pathlib import Path

SOUBOR = Path(__file__).parent / "nakup.json"   # složka programu + jméno souboru

with open(SOUBOR, encoding="utf-8") as soubor:
    nakup = json.load(soubor)
```
