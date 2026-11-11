# Tahák – Správce osobních financí

Věci, které v projektu potřebuješ a v tahácích z lekcí nejsou.

## Vlastní soubor jako zdroj funkcí

Funkce z jiného souboru ve stejné složce si půjčíš stejně jako z `random`:

```python
from finance import zustatek            # jen vybrané funkce

print(zustatek(transakce))
```

```python
import finance                          # celý soubor

print(finance.zustatek(transakce))      # funkce se volá s tečkou
```

Oba zápisy dělají totéž. V `app.py` se hodí první, v testech druhý: do
souboru s testy pak můžeš přidávat další testy a import neměníš.

Při importu se soubor celý provede. Proto ve `finance.py` nesmí být žádný
`input()` ani `print()` mimo funkce.

## Testy

```python
import finance


def test_zustatek_bez_transakci():        # jméno funkce začíná test_
    assert finance.zustatek([]) == 0      # assert = „tvrdím, že“
```

- Soubor s testy se jmenuje `test_něco.py`, funkce `test_něco`.
- Jméno testu říká, co test ověřuje.
- Jeden test ověřuje jednu věc.
- Spouští se v panelu **Testing** (ikona baňky), nebo v terminálu:
  `python -m pytest`.

Tvary `assert`, se kterými si vystačíš:

```python
assert vysledek == 100              # rovná se
assert vysledek == {"jidlo": 750}   # jde porovnat i slovník nebo seznam
assert vysledek is None             # funkce nic nenašla
assert je_platna_castka("250")      # má být True
assert not je_platna_castka("abc")  # má být False
assert "nájem" in text              # obsahuje
assert len(transakce) == 5          # délka
```

### Když test neprojde

```text
    def test_zustatek():
>       assert finance.zustatek(ukazka()) == 100
E       assert 1900 == 100
```

Řádek s `>` je tvrzení, které neplatí. Řádek s `E` ukazuje, co doopravdy
vyšlo: funkce vrátila 1900 a test čekal 100.

| Hláška | Co se většinou stalo |
|---|---|
| `AttributeError: module 'finance' has no attribute 'zustatek'` | funkce ve `finance.py` chybí, nebo se jmenuje jinak |
| `TypeError: zustatek() takes 1 positional argument but 2 were given` | funkce má jiný počet parametrů, než s kolika ji test volá |
| `assert None == 100` | funkce nic nevrací, chybí `return` |
| `KeyError: 'castka'` | překlep v klíči slovníku |

### Co testovat

- obyčejný případ, který si umíš spočítat ručně,
- okraje: prázdný seznam, nula, jediná položka,
- špatný vstup: číslo, které neexistuje, kategorie, která chybí.

Funkce s `input()` a `print()` se takhle testovat nedají. Proto je
v projektu logika ve `finance.py` a menu v `app.py`.

Každý test si má připravit vlastní data. V `test_finance.py` k tomu slouží
funkce `ukazka()`, která pokaždé vrátí nový seznam. Kdyby testy sdílely
jeden seznam, test, který do něj něco přidá, by rozbil ty ostatní.

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
