# Wordle s řešičem

Postavíš českou verzi hry Wordle. Hráč má šest pokusů na uhodnutí slova o pěti
písmenech a po každém pokusu vidí, která písmena sedí. Nakonec napíšeš řešič:
program, který hru umí hrát sám. Vystačíš si s tím, co umíš z lekcí 1 až 9.

```text
             K   A   B   Á   T
             P   A   U   Z   A
             ·   ·   ·   ·   ·
             ·   ·   ·   ·   ·
             ·   ·   ·   ·   ·
             ·   ·   ·   ·   ·

         Ě   Š   Č   Ř   Ž   Ý   Á   Í   É
 Q   W   E   R   T   Z   U   I   O   P   Ú
   A   S   D   F   G   H   J   K   L   Ů
 Y   X   C   V   B   N   M   Ď   Ť   Ň   Ó

  Zkus: PAUZA

  Tvůj pokus:
```

Pracovat můžeš sama nebo ve dvojici.

## Jak to bude probíhat

Projekt je rozdělený na kroky. Začneš programem, který vyhodnotí jedno slovo,
a v každém kroku mu něco přidáš. Nemusíš stihnout všechno. Do kroku 3 by měla
dojít každá, to už je hra, která se dá hrát. Zbytek je navíc.

| Krok | Co přibude | Co si zopakuješ |
| --- | --- | --- |
| [1 – Jeden pokus](cviceni/01_jeden_pokus.md) | vyhodnocení jednoho slova | řetězce, seznamy, `for`, funkce |
| [2 – Celá hra](cviceni/02_cela_hra.md) | šest pokusů, kontrola vstupu, výhra a prohra | `while`, metody řetězců |
| [3 – Seznam slov](cviceni/03_seznam_slov.md) | náhodné slovo, jen skutečná slova | `in`, `randrange`, import |
| [4 – Barvy](cviceni/04_barvy.md) | barevná pole místo značek | seznam n-tic, rozbalování |
| [5 – Klávesnice](cviceni/05_klavesnice.md) | přehled písmen | slovníky, slovník ve funkci |
| [6 – Opakovaná písmena](cviceni/06_opakovana_pismena.md) | oprava chyby u slov se stejným písmenem dvakrát | měnění seznamu, testy jako první |
| [7 – Nápověda](cviceni/07_napoveda.md) | která slova ještě připadají v úvahu | stavění seznamu, skládání funkcí |
| [8 – Řešič](cviceni/08_resic.md) | program poradí nejlepší slovo | počítadlo, hledání největšího |
| [9 – Statistiky](cviceni/09_statistiky.md) | výsledky uložené v souboru | slovník ve slovníku |
| [10 – Herní obrazovka](cviceni/10_herni_obrazovka.md) | obrazovka, která zůstává na místě | rozdělení programu na funkce |

Kdo stihne všech deset kroků, najde další úkoly ve složce [`bonusy`](bonusy/)
a volné náměty v souboru [`napady.md`](napady.md).

Každý krok má stejnou stavbu:

1. **Funkce.** Zadání řekne, co má funkce dostat a co vrátit. Píšeš ji do
   `logika.py`.
2. **Testy.** V prvních krocích je dostaneš hotové a zkopíruješ si je do
   `test_logika.py`. Od kroku 6 je píšeš sama.
3. **Program.** Hotové funkce použiješ ve hře ve `wordle.py`.

Zadání říká, co má funkce dělat. Jak to udělá, je na tobě.

Po každém kroku ulož práci na GitHub: **Commit** a pak **Sync Changes**.

## Soubory

| Soubor | K čemu je |
| --- | --- |
| `logika.py` | **logika**: funkce s pravidly hry. Dostanou data a vrátí výsledek. Tyhle funkce se testují. |
| `wordle.py` | **hra**: `input()` a `print()`. Volá funkce z `logika.py`. Tenhle soubor spouštíš. |
| `test_logika.py` | testy funkcí z `logika.py` |
| `pomocnik.py` | hotové funkce na barvy a soubory. Nemusíš ho číst ani měnit. |
| `hadana_slova.txt` | 425 slov, která může program vybrat jako tajná |
| `povolena_slova.txt` | skoro 28 000 slov, která může hráč zadat |

Proč dva soubory s kódem? Funkce, která se ptá přes `input()` a odpovídá přes
`print()`, se testovat nedá: test za tebe nic nenapíše na klávesnici a
nepřečte si obrazovku. Funkci, která dostane data a výsledek vrátí, otestuješ
na jednom řádku. Proto pravidla hry bydlí v `logika.py` a povídání s hráčem ve
`wordle.py`.

## Jak vypadá test

```python
def test_uhodnute_slovo():
    assert logika.vyhodnot("panna", "panna") == [S, S, S, S, S]
```

Test je funkce, jejíž jméno začíná `test_`. Slovo `assert` znamená „tvrdím,
že“: nalevo je to, co funkce vrátila, napravo to, co vrátit měla. Když tvrzení
platí, test je zelený. Když ne, je červený a v hlášce uvidíš, co funkce
vrátila doopravdy.

Víc o testech je v lekci o testování, tahák najdeš v
[`lekce-testovani/TAHAK.md`](../lekce-testovani/TAHAK.md).

## Než začneš

1. Měj připravený počítač podle návodu [Před workshopem](../PRED-WORKSHOPEM.md):
   fork, clone a nainstalovaný pytest. Když pytest chybí, napiš v terminálu
   ve VS Code `pip install pytest`, na Windows případně `py -m pip install pytest`.
2. Ve VS Code měj otevřenou složku celého workshopu (**File → Open Folder**),
   ne jen složku projektu.
3. Otevři panel **Testing** (ikona baňky vlevo). Rozbal `projekt-wordle` a
   spusť jeho testy šipkou vedle názvu. V `test_logika.py` je jeden test a má
   být zelený. Když je, všechno funguje.
4. Spusť `wordle.py`. Má vypsat, kolik písmen slovo má a kolik máš pokusů.
5. Otevři [krok 1](cviceni/01_jeden_pokus.md).

## Když se zasekneš

1. Přečti si chybovou hlášku odspodu.
2. Otevři nápovědu ke kroku ve složce [`napovedy`](napovedy/). Jmenuje se
   stejně jako zadání.
3. Zeptej se kolegyně ve dvojici nebo u stolu.
4. Zavolej kouče.

## Na konci dne

Ukážeš ostatním, co jsi postavila. Stačí si zahrát jednu hru a říct, co ti
dalo nejvíc práce.
