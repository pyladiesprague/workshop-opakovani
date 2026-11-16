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
| [Bonusy](bonusy/) | barvy v terminálu, hledání, řazení, HTML report | podle chuti |
| [Nápady na rozšíření](napady.md) | další nápady bez řešení, třeba na doma | podle chuti |

Máš hotové kroky a zbývá čas? Vyber si, co tě láká. Bonusy na sebe
nenavazují a pořadí je na tobě.

U každého platí totéž co u kroků: logiku piš jako funkci do `finance.py`,
napiš k ní aspoň jeden test a teprve potom ji přidej do menu.

Každý krok má stejnou stavbu:

1. **Funkce.** Co mají nové funkce v `finance.py` dělat.
2. **Testy.** V krocích 1 až 3 a v kroku 6 je dostaneš hotové a zkopíruješ si
   je do `test_finance.py`. V krocích 4 a 5 je píšeš sama podle seznamu, co
   vyzkoušet. Testy budou červené, protože popisují funkce, které ještě nemáš.
   Funkce píšeš, dokud nezezelenají.
3. **Program.** Hotové funkce nabídneš uživatelce v menu v `app.py`.
4. **Hotovo, když.** Podle seznamu na konci poznáš, že je krok hotový.

Zadání říká, co má funkce dělat. Jak to udělá, je na tobě. Hotový kód
v zadání nenajdeš, najdeš tam odkazy do taháků z lekcí.

## Soubory

| Soubor | K čemu je |
|---|---|
| `finance.py` | **logika**: funkce, které dostanou data a vrátí výsledek. Píšeš sem většinu kódu a tyhle funkce se testují. |
| `app.py` | **menu**: `while True`, `input()` a `print()`. Volá funkce z `finance.py`. Tenhle soubor spouštíš. |
| `test_finance.py` | testy. Hotové sem zkopíruješ, vlastní sem napíšeš. |
| `ukazkova_data.py` | ukázkové transakce, kategorie a rozpočty, ať je od začátku s čím pracovat |
| `finance.json` | stejné transakce uložené v souboru, budeš ho potřebovat až v kroku 6 |
| `TAHAK.md` | tahák k tomu, co je v projektu nové: import z `finance.py`, data pro testy, soubory a JSON |
| `cviceni/` | zadání kroků, jeden soubor na krok |
| `napovedy/` | nápověda ke kroku, soubor se jmenuje stejně jako krok |
| `bonusy/` | bonusy, jeden soubor na bonus |
| `napady.md` | nápady na rozšíření bez řešení |

Proč dva soubory s kódem? Funkce, která se ptá přes `input()` a odpovídá
přes `print()`, se testovat nedá: test za tebe nic nenapíše na klávesnici
a nepřečte si obrazovku. Funkci, která dostane data a výsledek vrátí,
otestuješ na jednom řádku. Proto počítání bydlí ve `finance.py` a povídání
s uživatelkou v `app.py`.

## Jak vypadá test

```python
def test_zustatek_bez_transakci():
    assert finance.zustatek([]) == 0
```

Test je funkce, jejíž jméno začíná `test_`. Slovo `assert` znamená „tvrdím,
že“: nalevo je to, co funkce vrátila, napravo to, co vrátit měla. Když tvrzení
platí, test je zelený. Když ne, je červený a v hlášce uvidíš, co funkce
vrátila doopravdy.

Víc o testech je v lekci o testování, tahák najdeš v
[`lekce-testovani/TAHAK.md`](../lekce-testovani/TAHAK.md).

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

1. Měj připravený počítač podle návodu [Před workshopem](../PRED-WORKSHOPEM.md):
   fork, clone a nainstalovaný pytest. Když pytest chybí, napiš v terminálu
   ve VS Code `pip install pytest`, na Windows případně `py -m pip install pytest`.
2. Ve VS Code měj otevřenou složku celého workshopu (**File → Open Folder**),
   ne jen složku projektu.
3. Otevři panel **Testing** (ikona baňky vlevo). Rozbal `projekt-finance` a
   spusť jeho testy šipkou vedle názvu. V `test_finance.py` je jeden test a má
   být zelený. Když je, všechno funguje.
4. Spusť `app.py`. Má vypsat, kolik transakcí načetl.
5. Otevři [krok 1](cviceni/01_zaklad.md).

## Když se zasekneš

1. Přečti si chybovou hlášku odspodu. Tahák L7, *Jak číst chybovou hlášku*.
2. Otevři nápovědu ke kroku. Odkaz na ni je v zadání nad „Hotovo, když“,
   soubory jsou ve složce `napovedy/`. Nápověda tě pošle i do taháku.
3. Zeptej se kolegyně ve dvojici nebo u stolu.
4. Zavolej kouče.

## Na konci dne

Ukážeš ostatním, co jsi postavila. Stačí ukázat přehled nebo graf ze svých
dat a říct, co ti dalo nejvíc práce.
