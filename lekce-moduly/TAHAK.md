# Tahák – Moduly

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Modul

Modul je soubor s Pythonem, ze kterého si jiné soubory půjčují funkce.

- **Standardní knihovna:** moduly, které má Python s sebou (`random`,
  `math`, `statistics`, `datetime`, `time`). Stačí je importovat.
- **Knihovny z PyPI:** moduly od jiných lidí (`cowsay`, `pytest`). Nejdřív
  je nainstaluješ přes `pip`, pak importuješ.
- **Vlastní modul:** tvůj soubor `.py` ve stejné složce.

## Dva zápisy importu

```python
from random import randrange, choice    # vybrané funkce
randrange(1, 7)

import random                           # celý modul
random.randrange(1, 7)                  # funkce se volá s tečkou
```

Oba dělají totéž. Importy piš nahoru do souboru.

## Instalace knihovny

V terminálu ve VS Code (**Terminal → New Terminal**):

```text
pip install pytest
```

| Systém | Když `pip` nefunguje |
|---|---|
| Windows | `py -m pip install pytest` |
| macOS | `python3 -m pip install pytest` |

Instaluje se jednou na počítač. Import píšeš do každého souboru, kde
knihovnu používáš.

## Pytest

```text
python -m pytest --version      # je nainstalovaný?
python -m pytest                # spusť všechny testy
```

Pytest najde soubory `test_něco.py` a v nich funkce `test_něco` a spustí je.
Ve VS Code je spouštíš v panelu **Testing** (ikona baňky).

## Vlastní modul

```text
prevody.py          logika: jen funkce, žádný input() ani print()
program.py          program: input(), print(), volá funkce z prevody.py
test_prevody.py     testy: kontrolují funkce z prevody.py
```

```python
import prevody                          # bez .py
print(prevody.na_fahrenheity(30))
```

- Modul leží ve stejné složce jako soubor, který ho importuje.
- Jméno: malá písmena, číslice a podtržítka, nezačíná číslicí, bez mezer,
  pomlček a háčků.
- Nepojmenuj ho jako existující modul (`random.py`, `pytest.py`).
- Při importu se celý soubor provede. Co je mimo funkce, spustí se.

Funkce třídíš do modulů stejně jako kód do funkcí: co k sobě patří, dej
dohromady a pojmenuj.

## Časté chyby

| Hláška | Co se většinou stalo |
|---|---|
| `NameError: name 'randrange' is not defined` | chybí import, nebo je pod místem použití |
| `NameError: name 'sqrt' is not defined` | `import math` a pak `sqrt` místo `math.sqrt` |
| `ModuleNotFoundError: No module named 'cowsay'` | knihovna není nainstalovaná, nebo je překlep ve jméně |
| `ModuleNotFoundError: No module named 'prevody'` | `prevody.py` neleží ve stejné složce, nebo je překlep ve jméně |
| `ModuleNotFoundError: No module named 'prevody.py'` | v importu je `.py` navíc, piš jen `import prevody` |
| `ImportError: cannot import name 'na_kelviny' from 'prevody'` | taková funkce v modulu není (překlep, nebo není uložený soubor) |
| `AttributeError: module 'random' has no attribute 'randrange'` | tvůj soubor se jmenuje `random.py` a schoval skutečný modul |
| program se při importu na něco ptá nebo něco vypíše | v modulu je `input()` nebo `print()` mimo funkci |
| `pip` hlásí `externally-managed-environment` | zavolej kouče |
