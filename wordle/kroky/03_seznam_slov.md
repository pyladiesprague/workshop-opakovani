# Krok 3: Seznam slov

Tajné slovo teď vybere program. Na začátek `wordle.py` přidej:

```python
from random import randrange
from pomocnik import nacti_radky
```

`nacti_radky("hadana_slova.txt")` vrátí seznam slov ze souboru. `randrange(n)` vrátí náhodné celé číslo od 0 do n - 1.

## Logika

Rozšiř funkci na `chyba_slova(slovo, povolena)`. Slovo o pěti písmenech, které není v seznamu `povolena`, dostane chybu `"Takové slovo neznám."`.

## Testy

Funkce má teď dva parametry, takže test z minulého kroku spadne. Oprav volání ve třídě `TestVstup` a přidej dva testy:

```python
    def test_nezname_slovo(self):
        self.assertEqual(chyba_slova(___, ["kočka"]), "Takové slovo neznám.")

    def test_povolene_slovo(self):
        self.assertEqual(chyba_slova("kočka", ["kočka"]), ___)
```

## Program

1. Náhodně vyber tajné slovo ze souboru `hadana_slova.txt`.
2. Zadaná slova kontroluj podle souboru `povolena_slova.txt`. Seznam povolených slov pošli funkcím `zahraj` a `nacti_slovo` jako další parametr.
3. Po skončení hry se zeptej, jestli chce hráč hrát znovu.

Zasekla ses? Nápověda je v souboru [`napovedy/03_seznam_slov.md`](../napovedy/03_seznam_slov.md).
