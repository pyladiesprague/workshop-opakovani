# Wordle s řešičem

Během dne postavíš českou verzi hry Wordle. Hráč má šest pokusů na uhodnutí slova o pěti písmenech a po každém pokusu vidí, která písmena sedí. Na konci napíšeš program, který hru umí hrát sám.

Pracovat můžeš sama nebo ve dvojici.

## Jak začít

Ve VS Code otevři složku `wordle/moje_hra` přes **File → Open Folder**. Tady budeš pracovat celý den.

| Soubor | Co v něm je |
| --- | --- |
| `logika.py` | Funkce s pravidly hry. Tady se nic nevypisuje a na nic se neptá. |
| `wordle.py` | Samotná hra. Spouštíš ji tlačítkem Run. |
| `test_logika.py` | Testy funkcí z `logika.py`. |
| `pomocnik.py` | Hotové funkce na barvy a soubory. Nemusíš ho číst ani měnit. |
| `hadana_slova.txt` | 425 slov, která může program vybrat jako tajná. |
| `povolena_slova.txt` | Skoro 28 000 slov, která může hráč zadat. |

Hru máme ve dvou souborech kvůli testům. Test si soubor naimportuje a tím ho celý spustí, takže kdyby v něm byl `input()`, test by čekal na hráče.

## Jak spouštět testy

Vlevo klikni na ikonu zkumavky **Testing** a nahoře na dvě šipky **Run All Tests**. Zelená znamená, že test prošel, červená, že ne.

Test vypadá takhle:

```python
class TestVyhodnot(unittest.TestCase):
    def test_uhodnute_slovo(self):
        self.assertEqual(vyhodnot("panna", "panna"), [S, S, S, S, S])
```

Do `assertEqual` patří to, co funkce vrátila, a to, co vrátit měla. `S`, `J` a `N` jsou zkratky pro `"spravne"`, `"jinde"` a `"neni"`, najdeš je nahoře v souboru s testy. Slova `class` a `self` si zatím jen opiš, testy jsou v Pythonu uspořádané do tříd. Co přesně znamenají, se naučíme v lekci o třídách.

## Jak pracovat

Zadání je ve složce `kroky`, jeden soubor na jeden krok. Každý krok rozšiřuje stejný program.

1. Přečti si zadání kroku.
2. Doplň kód a testy.
3. Spusť testy a zahraj si.
4. Ulož práci na GitHub: **Commit** a pak **Sync Changes**. Do zprávy napiš, co přibylo, třeba „Hra má šest pokusů“.

Když se zasekneš, otevři si nápovědu ke kroku ve složce `napovedy`. Když nestačí, zeptej se kouče.

## Kroky

| Krok | Co přibude |
| --- | --- |
| [1](cviceni/01_jeden_pokus.md) | Vyhodnocení jednoho pokusu |
| [2](cviceni/02_cela_hra.md) | Šest pokusů, výhra a prohra |
| [3](cviceni/03_seznam_slov.md) | Náhodné slovo a kontrola zadaných slov |
| [4](cviceni/04_barvy.md) | Barevná pole |
| [5](cviceni/05_klavesnice.md) | Klávesnice s přehledem písmen |
| [6](cviceni/06_opakovana_pismena.md) | Slova se stejným písmenem dvakrát |
| [7](cviceni/07_napoveda.md) | Nápověda |
| [8](cviceni/08_resic.md) | Řešič |
| [9](cviceni/09_statistiky.md) | Statistiky uložené v souboru |
| [10](cviceni/10_herni_obrazovka.md) | Obrazovka, která zůstává na místě |

Kdo stihne všech deset kroků, pokračuje [bonusy](bonusy/).
