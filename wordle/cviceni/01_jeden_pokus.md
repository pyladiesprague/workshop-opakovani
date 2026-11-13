# Krok 1: Jeden pokus

V `logika.py` je připravená prázdná funkce `vyhodnot(hadane, tajne)`. Dostane dvě slova o pěti písmenech a má vrátit seznam pěti řetězců, jeden pro každé písmeno hádaného slova:

| Hodnota | Význam |
| --- | --- |
| `"spravne"` | Písmeno je ve slově a stojí na správném místě. |
| `"jinde"` | Písmeno ve slově je, ale na jiném místě. |
| `"neni"` | Písmeno ve slově není. |

```python
vyhodnot("kabát", "kočka")
# ["spravne", "jinde", "neni", "neni", "neni"]
```

Nahoře v `logika.py` jsou dvě konstanty, `DELKA_SLOVA` a `POCET_POKUSU`. Konstanta je obyčejná proměnná, kterou program nikde nemění. Velká písmena v názvu to dávají najevo. Používej je místo čísel 5 a 6.

## Testy

Testy pro tenhle krok už máš hotové v `test_logika.py`. Spusť je v panelu Testing. Jsou červené, protože funkce zatím nic nedělá.

Napiš funkci tak, aby všechny zezelenaly. Slova se stejným písmenem dvakrát teď neřeš, přijdou na řadu v kroku 6.

Zasekla ses? Nápověda je v souboru [`napovedy/01_jeden_pokus.md`](../napovedy/01_jeden_pokus.md), část Funkce.

## Program

Ve `wordle.py` napiš funkci `vypis_pokus(hadane, vysledek)`, která vypíše slovo a pod něj značky `+`, `?` a `-`:

```
k a b á t
+ ? - - -
```

Tajné slovo si zatím napiš přímo do kódu. Zeptej se hráče na slovo, vyhodnoť ho a vypiš. Funkci si do `wordle.py` naimportuješ takhle:

```python
from logika import vyhodnot
```

Zasekla ses? Nápověda je v souboru [`napovedy/01_jeden_pokus.md`](../napovedy/01_jeden_pokus.md), část Program.
