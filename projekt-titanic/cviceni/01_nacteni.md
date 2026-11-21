# Krok 1 – Co v souboru vlastně je?

Na konci tohohle kroku program načte data a ukáže, co v nich je:

```text
Pasažérů: ???
Sloupce: ['PassengerId', 'Survived', 'Pclass', ...]
{'PassengerId': '1', 'Survived': '0', 'Pclass': '3', ...}
```

Otazníky v ukázkách znamenají číslo, které ti vyjde. Odpovědi v zadání
nenajdeš, zjistíš je z dat.

CSV je tabulka uložená v textovém souboru. Otevři si `Titanic-Dataset.csv` ve
VS Code: první řádek jsou názvy sloupců a každý další řádek je jeden pasažér.

Python umí takový soubor přečíst modulem `csv`, který je jeho součástí, takže
nic neinstalujeme:

```python
import csv

with open(SOUBOR, encoding="utf-8") as f:
    radky = list(csv.DictReader(f))
```

- `SOUBOR` je cesta k datům. Máš ji připravenou nahoře v `analyza.py`.
- `open` otevře soubor a `with` se postará, aby se zase zavřel.
- `csv.DictReader` čte soubor řádek po řádku a z každého udělá slovník, kde
  klíče jsou názvy sloupců.
- `list` z toho udělá seznam.

Práci se soubory si podrobně projdeme v lekci 13, teď ti stačí tohle. Stejný
recept je i v [taháku projektu](../TAHAK.md).

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `nacti_pasazery(soubor)` | seznam slovníků, jeden slovník na každý řádek souboru |

## Testy

Otevři `test_analyza.py` a tyhle testy zkopíruj na jeho konec:

```python
def test_pocet_pasazeru():
    pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)
    assert len(pasazeri) == 891


def test_kazdy_pasazer_ma_dvanact_sloupcu():
    pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)
    assert len(pasazeri[0]) == 12


def test_jmeno_prvniho_pasazera():
    pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)
    assert pasazeri[0]["Name"] == "Braund, Mr. Owen Harris"
```

Spusť je v panelu **Testing**. Budou červené a v hlášce uvidíš
`AttributeError: module 'analyza' has no attribute 'nacti_pasazery'`. To je v
pořádku: testy popisují funkci, která ještě neexistuje. Napiš ji tak, aby
zezelenaly.

## Program

Výpisy píšeš do `zprava.py`.

Na začátku `zprava.py` už je `import analyza`. Funkce a cestu k datům
z `analyza.py` proto voláš s tečkou, stejně jako v testech:

```python
pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)
```

Import už nikdy měnit nemusíš. Každá funkce, kterou do `analyza.py` přidáš,
je ve `zprava.py` hned k dispozici jako `analyza.jmeno_funkce`.

Vypiš:

1. Kolik jich je.
2. Názvy sloupců. Klíče slovníku jako seznam získáš takhle:
   `list(pasazeri[0].keys())`.
3. Prvního pasažéra.

Všimni si, že i čísla jsou v uvozovkách. Z CSV přijde všechno jako text.

Zasekla ses? Nápověda je v souboru [`napovedy/01_nacteni.md`](../napovedy/01_nacteni.md).

## Hotovo, když

- [ ] všechny čtyři testy jsou zelené
- [ ] program vypíše počet pasažérů, názvy sloupců a prvního pasažéra
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
