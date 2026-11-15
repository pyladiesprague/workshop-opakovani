# Titanic

Dneska budeš datová analytička. Máš skutečný seznam pasažérů Titaniku a jednu
otázku, která se dá rozplést na spoustu menších:

**Kdo byl na palubě a jak dopadl?**

Kolik let bylo nejstaršímu cestujícímu? Kolik stál nejdražší lístek? Jak se
jmenovalo nejvíc mužů? A kdo měl největší šanci přežít? Odpovědi v zadání
nenajdeš, zjistíš je z dat. Na konci z nich sestavíš zprávu a přidáš k ní
otázku, kterou si vymyslíš sama. Vystačíš si s tím, co umíš z lekcí 1 až 9.

```text
TITANIC V ČÍSLECH
============================================

Pasažérů celkem:            ???
Přežilo:                    ??? (??.? %)
Průměrný věk:              ??.?
Nejstarší:                ????? (?? let)

Podle pohlaví             Přežilo  (lidí)
  ženy                     ??.? %  (???)
  muži                     ??.? %  (???)

Přežití podle třídy
  1. třída        ████████████████████████        ??.? %
  2. třída        ███████████████                 ??.? %
  3. třída        ███████                         ??.? %
```

Otazníky a délky sloupců v ukázkách jsou jen naznačené. Čísla ti vyjdou z dat.

Pracovat můžeš sama nebo ve dvojici.

## Jak přemýšlí analytička

Pořád dokola se opakuje pět kroků:

1. **Polož otázku.**
2. **Odhadni odpověď.**
3. **Spočítej ji.**
4. **Porovnej výsledek** s odhadem a s tím, co už víš.
5. **Zeptej se, co tě zajímá dál.**

A pět zvyků, které se ti budou hodit:

- **Nejdřív odhad.** Bez odhadu tě žádný výsledek nepřekvapí.
- **Porovnávej.** Samotné číslo moc neřekne. Vždycky se ptej: oproti čemu?
- **Dívej se, kolik lidí ve skupině je.** Procento z pěti lidí toho moc
  neříká.
- **Ptej se, co chybí.** Lidé bez údajů můžou být jiní než ostatní.
- **U „proč“ buď opatrná.** Když dvě věci vycházejí spolu, ještě to neznamená,
  že jedna způsobuje druhou. Někdy za tím stojí něco třetího a někdy je to jen
  náhoda.

Odhady, výsledky a další otázky si zapisuj do souboru `poznamky.md`.

## Jak to bude probíhat

Projekt je rozdělený na kroky a každý krok začíná otázkou. Nemusíš stihnout
všechno. Do kroku 6 by měla dojít každá, to už víš, kdo na lodi byl a kdo
přežil častěji. Zbytek je navíc.

| Krok | Otázka | Co si zopakuješ |
| --- | --- | --- |
| [1 – Načtení](cviceni/01_nacteni.md) | Co v souboru vlastně je? | seznam slovníků; nové: soubor CSV |
| [2 – Úklid](cviceni/02_uklid.md) | Co v datech chybí? | převod typů, měnění slovníku; nové: `None` |
| [3 – Kdo byl na palubě](cviceni/03_kdo_byl_na_palube.md) | Kdo byl nejstarší a nejmladší? | sčítání v cyklu, hledání největšího |
| [4 – Lístky](cviceni/04_listky.md) | Kolik stál lístek? | stavění seznamu, skládání funkcí |
| [5 – Jména](cviceni/05_jmena.md) | Co prozradí jména? | řetězce, `split`, počítadlo |
| [6 – Kdo přežil](cviceni/06_kdo_prezil.md) | Kdo přežil častěji? | procenta, podmínky |
| [7 – Přístavy](cviceni/07_pristavy.md) | Záleželo na tom, kde kdo nastoupil? | slovník seznamů |
| [8 – Přístav, nebo třída](cviceni/08_pristav_nebo_trida.md) | Co z toho rozhodovalo? | n-tice jako klíč |
| [9 – Graf](cviceni/09_graf.md) | Jak to ukázat na první pohled? | řetězce, zarovnání |
| [10 – Zpráva](cviceni/10_zprava.md) | Titanic v číslech | f-stringy, skládání funkcí |
| [11 – Průzkumník](cviceni/11_pruzkumnik.md) | Co dalšího se dá z dat zjistit? | kontrola vstupu, `while` |
| [12 – Moje otázka](cviceni/12_moje_otazka.md) | Co zajímá tebe? | všechno dohromady |

Kdo stihne všech dvanáct kroků, najde další úkoly ve složce
[`bonusy`](bonusy/) a volné náměty v souboru [`napady.md`](napady.md).

Každý krok má stejnou stavbu:

1. **Odhad.** Než začneš počítat, zapiš si do `poznamky.md`, co čekáš.
2. **Funkce.** Zadání řekne, co má funkce dostat a co vrátit. Píšeš ji do
   `analyza.py`.
3. **Testy.** V prvních krocích je dostaneš hotové a zkopíruješ si je do
   `test_analyza.py`. Od kroku 7 je píšeš sama.
4. **Zpráva.** Výsledek vypíšeš v `zprava.py` a doplníš poznámky. Výpisy z
   předchozích kroků v souboru nech a nové přidávej pod ně.

Zadání říká, co má funkce dělat. Jak to udělá, je na tobě.

Po každém kroku ulož práci na GitHub: **Commit** a pak **Sync Changes**.

## Soubory

| Soubor | K čemu je |
| --- | --- |
| `analyza.py` | **analýza**: funkce, které počítají. Dostanou data a vrátí výsledek. Tyhle funkce se testují. |
| `zprava.py` | **zpráva**: `print()` a `input()`. Volá funkce z `analyza.py`. Tenhle soubor spouštíš. |
| `test_analyza.py` | testy funkcí z `analyza.py` |
| `Titanic-Dataset.csv` | data |
| `poznamky.md` | tvoje poznámky: odhady, výsledky a další otázky |
| `TAHAK.md` | tahák k tomu, co je v projektu nové: CSV, `None`, kopie slovníku |

Proč dva soubory s kódem? Funkce, která výsledek jen vypíše přes `print()`, se
testovat nedá: test si obrazovku nepřečte. Funkci, která dostane data a
výsledek vrátí, otestuješ na jednom řádku. Proto počítání bydlí v `analyza.py`
a vypisování v `zprava.py`.

## Jak vypadá test

```python
def test_pocet_prezivsich():
    assert analyza.pocet_prezivsich(ukazka()) == 3
```

Test je funkce, jejíž jméno začíná `test_`. Slovo `assert` znamená „tvrdím,
že“: nalevo je to, co funkce vrátila, napravo to, co vrátit měla. Když tvrzení
platí, test je zelený. Když ne, je červený a v hlášce uvidíš, co funkce
vrátila doopravdy.

Víc o testech je v lekci o testování, tahák najdeš v
[`lekce-testovani/TAHAK.md`](../lekce-testovani/TAHAK.md).

Na testy nepoužíváme celý soubor, stovky řádků z hlavy nespočítáš. Od kroku 3
budeš mít v testech funkci `ukazka()` s pěti vymyšlenými pasažéry, u kterých
výsledek snadno ověříš.

## Co je v datech

Každý řádek souboru je jeden pasažér. Nejsou to všichni lidé na palubě, takže
výsledky popisují jen tenhle soubor. Sloupce mají anglické názvy, jak to u
skutečných dat bývá.

| Sloupec | Význam |
| --- | --- |
| `PassengerId` | pořadové číslo |
| `Survived` | 1 = přežil, 0 = nepřežil |
| `Pclass` | třída: 1, 2 nebo 3 |
| `Name` | jméno ve tvaru `Příjmení, Titul. Jméno` |
| `Sex` | `female` nebo `male` |
| `Age` | věk; u některých pasažérů chybí |
| `SibSp` | kolik sourozenců a manželů měl pasažér na palubě |
| `Parch` | kolik rodičů a dětí měl pasažér na palubě |
| `Ticket` | číslo lístku |
| `Fare` | cena lístku v librách |
| `Cabin` | kajuta; u většiny pasažérů chybí |
| `Embarked` | přístav nástupu: `S` Southampton, `C` Cherbourg, `Q` Queenstown |

## Než začneš

1. V terminálu ve VS Code nainstaluj pytest: `pip install pytest`. Na Windows
   případně `py -m pip install pytest`.
2. Ve VS Code měj otevřenou složku celého workshopu (**File → Open Folder**),
   ne jen složku projektu.
3. Otevři panel **Testing** (ikona baňky vlevo). Rozbal `projekt-titanic` a
   spusť jeho testy šipkou vedle názvu. V `test_analyza.py` je jeden test a má
   být zelený. Když je, všechno funguje.
4. Spusť `zprava.py`. Má vypsat, ve kterém souboru jsou data.
5. Otevři [krok 1](cviceni/01_nacteni.md).

## Když se zasekneš

1. Přečti si chybovou hlášku odspodu.
2. Otevři nápovědu ke kroku ve složce [`napovedy`](napovedy/). Jmenuje se
   stejně jako zadání.
3. Zeptej se kolegyně ve dvojici nebo u stolu.
4. Zavolej kouče.

## Na konci dne

Ukážeš ostatním svůj nejzajímavější výsledek. Stačí tři věty: na co ses ptala,
co vyšlo a co tě překvapilo.
