# Krok 1: Co v souboru vlastně je?

CSV je tabulka uložená v textovém souboru. Otevři si `Titanic-Dataset.csv` ve VS Code: první řádek jsou názvy sloupců a každý další řádek je jeden pasažér.

Python umí takový soubor přečíst modulem `csv`, který je jeho součástí, takže nic neinstalujeme:

```python
import csv

with open(SOUBOR, encoding="utf-8") as f:
    radky = list(csv.DictReader(f))
```

`SOUBOR` je cesta k datům. Máš ji připravenou nahoře v `analyza.py`, takže program soubor najde, ať máš ve VS Code otevřenou jakoukoliv složku.

- `open` otevře soubor a `with` se postará, aby se zase zavřel.
- `csv.DictReader` čte soubor řádek po řádku a z každého udělá slovník, kde klíče jsou názvy sloupců.
- `list` z toho udělá seznam.

Práci se soubory si podrobně projdeme v lekci 13, teď ti stačí tohle.

## Logika

V `analyza.py` je připravená prázdná funkce `nacti_pasazery(soubor)`. Dopiš ji tak, aby vrátila seznam slovníků.

## Testy

Testy pro tenhle krok máš hotové v `test_analyza.py`. Spusť je v panelu Testing. Jsou červené, protože funkce zatím nic nedělá. Napiš ji tak, aby zezelenaly.

## Zpráva

Do `zprava.py` si naimportuj funkci i cestu k datům:

```python
from analyza import SOUBOR, nacti_pasazery
```

Načti pasažéry a vypiš:

1. Kolik jich je.
2. Názvy sloupců. Klíče slovníku jako seznam získáš takhle: `list(pasazeri[0])`.
3. Prvního pasažéra.

Všimni si, že i čísla jsou v uvozovkách. Z CSV přijde všechno jako text.
