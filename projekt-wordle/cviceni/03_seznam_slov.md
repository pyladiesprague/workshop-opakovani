# Krok 3 – Seznam slov

Na konci tohohle kroku vybírá tajné slovo program a hráč smí hádat jen
skutečná slova:

```text
Tvůj pokus: xyzab
Takové slovo neznám.
Tvůj pokus: kabát
k a b á t
- + - - -
...
Došly pokusy. Tajné slovo bylo pauza.
Hrát znovu? (ano/ne)
```

Ve složce projektu jsou dva soubory se slovy. V `hadana_slova.txt` je 425
slov, ze kterých program vybírá tajné slovo. V `povolena_slova.txt` je skoro
28 000 slov, která smí hráč zadat.

Na začátek `wordle.py` přidej:

```python
from random import randrange
from pomocnik import nacti_radky
```

`nacti_radky("hadana_slova.txt")` vrátí seznam slov ze souboru. `randrange(n)`
vrátí náhodné celé číslo od 0 do n - 1. Soubor `pomocnik.py` je hotový,
nemusíš ho číst ani měnit.

## Funkce

Funkce píšeš do `logika.py`.

| Funkce | Co vrátí |
| --- | --- |
| `chyba_slova(slovo, povolena)` | to co dřív, a navíc `"Takové slovo neznám."`, když slovo o pěti písmenech není v seznamu `povolena` |

## Testy

Funkce má teď dva parametry, takže testy z minulého kroku spadnou. Oprav v
nich volání a přidej dva nové testy. Místo `___` doplň, co chybí:

```python
def test_nezname_slovo():
    assert logika.chyba_slova(___, ["kočka"]) == "Takové slovo neznám."


def test_povolene_slovo():
    assert logika.chyba_slova("kočka", ["kočka"]) == ___
```

## Program

Program píšeš do `wordle.py`.

1. Náhodně vyber tajné slovo ze souboru `hadana_slova.txt`.
2. Zadaná slova kontroluj podle souboru `povolena_slova.txt`. Seznam
   povolených slov pošli funkcím `zahraj` a `nacti_slovo` jako další parametr.
3. Po skončení hry se zeptej, jestli chce hráč hrát znovu.

Zasekla ses? Nápověda je v souboru [`napovedy/03_seznam_slov.md`](../napovedy/03_seznam_slov.md).

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] tajné slovo je při každé hře jiné
- [ ] slovo, které neexistuje, hra odmítne
- [ ] po hře jde hrát znovu, nebo skončit
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
