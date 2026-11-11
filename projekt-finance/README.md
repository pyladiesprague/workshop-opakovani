# Projekt: Správce osobních financí

> **Rozpracovaný návrh** – zadání se ještě ladí, podrobný plán je zatím v mých poznámkách.

Napíšeš si program, kterému budeš zapisovat příjmy a výdaje a on ti řekne,
kolik ti zbývá, za co utrácíš nejvíc a jestli držíš rozpočet. Všechno běží
v terminálu, přesně tak, jak to umíš z lekcí 1–9.

Projekt je rozdělený na **kroky**. Každý krok má zadání, nápovědu, které věci
z taháků se hodí, a **testy**, které ti řeknou, že máš hotovo. Začni krokem 1
a pokračuj svým tempem. Nemusíš stihnout všechno – do kroku 3 by měla dojít
každá, zbytek je navíc.

## Co budeš potřebovat

- Python a VS Code jako na lekcích.
- `pytest` na spouštění testů: v terminálu ve VS Code spusť `pip install pytest`
  (na Windows případně `py -m pip install pytest`).
- Složku tohoto repozitáře otevřenou ve VS Code (**File → Open Folder**), aby
  fungoval panel **Testing** (ikona baňky vlevo).

## Soubory

| Soubor | K čemu je |
|---|---|
| `finance.py` | **logika** – funkce, které dostanou data a vrátí výsledek; sem píšeš většinu kódu a tohle se testuje |
| `app.py` | **menu** – `while True`, `input()`, `print()`; jen volá funkce z `finance.py` |
| `test_finance.py` | testy; ke každému kroku si sem zkopíruješ ty připravené a přidáš vlastní |
| `data.py` | ukázkové transakce, aby bylo s čím začít a testy měly stejná data |

## Jak vypadají data

Jedna transakce je slovník, všechny transakce jsou seznam slovníků:

```python
transakce = [
    {"datum": "2026-11-01", "typ": "prijem", "castka": 32000, "kategorie": "vyplata", "popis": "výplata"},
    {"datum": "2026-11-02", "typ": "vydaj",  "castka": 15000, "kategorie": "bydleni", "popis": "nájem"},
    {"datum": "2026-11-03", "typ": "vydaj",  "castka": 250,   "kategorie": "jidlo",   "popis": "oběd"},
]
```

Částky jsou celé koruny. Datum je text ve tvaru `RRRR-MM-DD` – takhle se dá
řadit i porovnávat jako obyčejný text.

## Kroky

1. **Základ** – výpis transakcí a zůstatek, menu s volbami 1 / 2 / 0.
2. **Přidání a odebrání** transakce, kontrola vstupu v cyklu.
3. **Přehledy** – výdaje podle kategorií, přehled měsíce, největší výdaj.
4. **Rozpočty** – limit na kategorii, varování při překročení.
5. **Grafy v terminálu** – sloupce z `█` podle kategorií.
6. **Uložení do souboru** (JSON) – data přežijí ukončení programu.

Bonusy pro rychlé: HTML report do prohlížeče, hledání v popisu, řazení podle
částky, cíl spoření, opakující se platby, export do CSV, krok zpět…

*(Podrobná zadání kroků, nápovědy a testy doplním.)*
