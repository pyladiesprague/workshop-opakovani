# Tahák – Titanic

Věci, které v projektu potřebuješ a v tahácích z lekcí nejsou.

## CSV

CSV je tabulka uložená jako text. První řádek jsou názvy sloupců, každý další
řádek je jeden záznam a hodnoty odděluje čárka.

```python
import csv

with open(SOUBOR, encoding="utf-8") as f:
    radky = list(csv.DictReader(f))

print(radky[0]["Name"])
```

| Zápis | Co znamená |
| --- | --- |
| `open(SOUBOR, ...)` | otevři soubor pro čtení |
| `encoding="utf-8"` | kódování textu; piš ho vždycky, jinak se pokazí háčky a čárky |
| `with ... as f:` | uvnitř odsazeného bloku je soubor otevřený, na konci se sám zavře |
| `csv.DictReader(f)` | čte řádek po řádku a z každého udělá slovník; klíče jsou názvy sloupců |
| `list(...)` | udělá z toho seznam slovníků |

Všechno, co z CSV přijde, je text. I `"22"` a `"7.25"`. Čísla si musíš převést
sama funkcemi `int` a `float`.

## None

`None` je hodnota, která znamená „nic tu není“. Hodí se pro údaj, který chybí.

```python
vek = None

if vek is None:
    print("Věk neznáme")
```

- Ptáme se přes `is None`, případně `is not None`.
- S `None` se nedá počítat ani ho porovnávat s čísly. `None < 16` skončí
  chybou `TypeError`.
- Nula není `None`. Nula je číslo, `None` znamená, že číslo neznáme.

## Kopie slovníku

Přiřazení slovník nezkopíruje, jen mu dá druhé jméno. Tahák L9, *Slovník ve
funkci*.

```python
puvodni = {"Age": "22"}
kopie = puvodni.copy()
kopie["Age"] = 22.0

print(puvodni["Age"])   # "22", původní slovník se nezměnil
```

## Desetinná čísla v testech

Desetinná čísla se v počítači ukládají nepřesně, takže `100 / 3` nemusí vyjít
do posledního místa stejně dvakrát. V testech je proto porovnávej přes
`pytest.approx`:

```python
import pytest


def test_prezivani_muzu():
    miry = analyza.prezivani_podle(ukazka(), "Sex")
    assert miry["male"] == pytest.approx(100 / 3)
```

## N-tice jako klíč slovníku

Klíčem slovníku může být i n-tice. Hodí se, když skupinu určují dvě hodnoty
najednou.

```python
miry = {(1, "female"): 10.0, (3, "male"): 20.0}

print(miry[(1, "female")])
```

Seznam klíčem být nemůže, protože se dá měnit.
