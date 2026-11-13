# Správce osobních financí

Napíšeš si program, kterému budeš zapisovat příjmy a výdaje. On ti řekne,
kolik ti zbývá, za co utrácíš nejvíc a jestli držíš rozpočet. Všechno běží
v terminálu a vystačíš si s tím, co umíš z lekcí 1 až 9.

```text
Správce osobních financí

1 – výpis transakcí
2 – zůstatek
3 – přidat transakci
4 – odebrat transakci
5 – přehled měsíce
6 – rozpočty
7 – nastavit rozpočet
8 – graf výdajů
0 – konec
Co chceš udělat? 8
bydleni    ██████████████████████████████   28000 Kč
jidlo      ████████                          8260 Kč
doprava    █                                 1100 Kč
zabava     █                                 1310 Kč
ostatni    █                                 1290 Kč
```

## Jak to bude probíhat

Projekt je rozdělený na kroky. Začneš malým programem, který umí dvě věci,
a v každém kroku mu něco přidáš. Nemusíš stihnout všechno. Do kroku 3 by
měla dojít každá, zbytek je navíc.

| Krok | Co přibude | Co si zopakuješ |
|---|---|---|
| [1 – Základ](cviceni/01_zaklad.md) | výpis transakcí, zůstatek, menu | cykly, podmínky, funkce, čtení ze slovníku |
| [2 – Přidání a odebrání](cviceni/02_pridani_a_odebrani.md) | nové transakce, kontrola vstupu | seznamy, řetězce, `while` |
| [3 – Přehledy](cviceni/03_prehledy.md) | výdaje podle kategorií, přehled měsíce | slovníky, stavění seznamu |
| [4 – Rozpočty](cviceni/04_rozpocty.md) | limity a upozornění na překročení | slovníky, skládání funkcí |
| [5 – Grafy](cviceni/05_grafy.md) | sloupcový graf ze znaků | řetězce, `max` |
| [6 – Uložení do souboru](cviceni/06_soubory.md) | data přežijí ukončení programu | nové: soubory a JSON |
| [Bonusy](bonusy/) | barvy v terminálu, hledání, řazení, HTML report a další | podle chuti |

Máš hotové kroky a zbývá čas? Vyber si, co tě láká. Bonusy na sebe
nenavazují a pořadí je na tobě.

U každého platí totéž co u kroků: logiku piš jako funkci do `finance.py`,
napiš k ní aspoň jeden test a teprve potom ji přidej do menu.

Každý krok má stejnou stavbu:

1. **Testy.** Zkopíruješ si je do `test_finance.py`. Budou červené, protože
   popisují funkce, které ještě nemáš.
2. **Funkce.** Píšeš je do `finance.py`, dokud testy nezezelenají.
3. **Menu.** Hotové funkce nabídneš uživatelce v `app.py`.

Zadání říká, co má funkce dělat. Jak to udělá, je na tobě. Hotový kód
v zadání nenajdeš, najdeš tam odkazy do taháků z lekcí.

## Soubory

| Soubor | K čemu je |
|---|---|
| `finance.py` | **logika**: funkce, které dostanou data a vrátí výsledek. Píšeš sem většinu kódu a tyhle funkce se testují. |
| `app.py` | **menu**: `while True`, `input()` a `print()`. Volá funkce z `finance.py`. Tenhle soubor spouštíš. |
| `test_finance.py` | testy. V každém kroku si sem zkopíruješ připravené a přidáš vlastní. |
| `ukazkova_data.py` | ukázkové transakce, kategorie a rozpočty, ať je od začátku s čím pracovat |
| `finance.json` | stejné transakce uložené v souboru, budeš ho potřebovat až v kroku 6 |
| `TAHAK.md` | tahák k testům a k souborům |

Proč dva soubory s kódem? Funkce, která se ptá přes `input()` a odpovídá
přes `print()`, se testovat nedá: test za tebe nic nenapíše na klávesnici
a nepřečte si obrazovku. Funkci, která dostane data a výsledek vrátí,
otestuješ na jednom řádku. Proto počítání bydlí ve `finance.py` a povídání
s uživatelkou v `app.py`.

## Jak vypadají data

Jedna transakce je slovník. Všechny transakce jsou seznam slovníků.

```python
transakce = [
    {"datum": "2026-11-01", "typ": "prijem", "castka": 32000, "kategorie": "vyplata", "popis": "výplata"},
    {"datum": "2026-11-02", "typ": "vydaj", "castka": 14000, "kategorie": "bydleni", "popis": "nájem"},
    {"datum": "2026-11-04", "typ": "vydaj", "castka": 1630, "kategorie": "jidlo", "popis": "velký nákup"},
]
```

- `castka` je v celých korunách a je vždycky kladná. Jestli jde o příjem,
  nebo výdaj, říká `typ`.
- `datum` je text ve tvaru `RRRR-MM-DD`. Takhle zapsaná data se dají
  porovnávat a řadit jako obyčejný text.
- Typy a kategorie jsou bez háčků a čárek, ať se dobře píšou do `input()`.

## Než začneš

1. V terminálu ve VS Code nainstaluj pytest: `pip install pytest`.
   Na Windows případně `py -m pip install pytest`.
2. Ve VS Code měj otevřenou složku celého workshopu (**File → Open Folder**),
   ne jen jeden soubor.
3. Otevři panel **Testing** (ikona baňky vlevo) a spusť testy. V
   `test_finance.py` je jeden a má být zelený. Když je, všechno funguje.
4. Spusť `app.py`. Má vypsat, kolik transakcí načetl.
5. Otevři [krok 1](cviceni/01_zaklad.md).

## Když se zasekneš

1. Přečti si chybovou hlášku odspodu. Tahák L7.
2. Podívej se do nápovědy na konci zadání a do taháku, na který odkazuje.
3. Zeptej se kolegyně ve dvojici nebo u stolu.
4. Zavolej kouče.

## Co s tím dál

Na závěrečném workshopu se k podobnému programu můžeš vrátit a přidat mu
to, co se naučíš v dalších lekcích: transakci jako třídu, načtení výpisu
z banky ze souboru CSV a ošetření chyb přes výjimky.
