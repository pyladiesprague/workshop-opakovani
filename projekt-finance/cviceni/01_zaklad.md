# Krok 1 – Základ: výpis a zůstatek

Na konci tohohle kroku bude tvůj program umět tohle:

```text
Správce osobních financí

1 – výpis transakcí
2 – zůstatek
0 – konec
Co chceš udělat? 1
  1. 2026-10-01  + 32000 Kč  vyplata  výplata
  2. 2026-10-02  - 14000 Kč  bydleni  nájem
  3. 2026-10-05  -  1850 Kč  jidlo    velký nákup
  ...

1 – výpis transakcí
2 – zůstatek
0 – konec
Co chceš udělat? 2
Zůstatek: 25540 Kč
```

Nejdřív si otevři `ukazkova_data.py` a prohlédni si, jak data vypadají.

## Funkce

Funkce píšeš do `finance.py`.

| Funkce | Co vrátí |
|---|---|
| `soucet_prijmu(transakce)` | součet částek všech transakcí, které mají typ `"prijem"` |
| `soucet_vydaju(transakce)` | součet částek všech transakcí, které mají typ `"vydaj"` |
| `zustatek(transakce)` | příjmy mínus výdaje |

Funkce nic nevypisují a na nic se neptají. Dostanou seznam transakcí a vrátí
číslo. Ve funkci `zustatek` použij ty dvě předchozí.

## Testy

Otevři `test_finance.py` a tyhle testy zkopíruj na jeho konec:

```python
def test_soucet_prijmu():
    assert finance.soucet_prijmu(ukazka()) == 1000


def test_soucet_vydaju():
    assert finance.soucet_vydaju(ukazka()) == 900


def test_zustatek():
    assert finance.zustatek(ukazka()) == 100


def test_zustatek_bez_transakci():
    assert finance.zustatek([]) == 0
```

Spusť je v panelu **Testing**. Budou červené a v hlášce uvidíš
`AttributeError: module 'finance' has no attribute 'soucet_prijmu'`. To je
v pořádku: testy popisují funkce, které ještě neexistují. Tvůj úkol je napsat
je tak, aby testy zezelenaly.

Spočítej si na papíře, proč má z dat ve funkci `ukazka()` vyjít zrovna 1000,
900 a 100. Uvidíš tak, co přesně testy kontrolují.

Po každé funkci pusť testy. Zelených bude přibývat.

**Vlastní test:** zůstatek může vyjít i záporný. Napiš test se seznamem,
ve kterém je jediná transakce, a to výdaj. Seznam si napiš přímo v testu.

## Program

Menu je v `app.py`.

Funkce máš, teď je potřeba je někomu nabídnout.

1. Napiš funkci `vypis(transakce)`, která vypíše každou transakci na jeden
   řádek: pořadové číslo od jedničky, datum, plus nebo mínus podle typu,
   částku, kategorii a popis. Sloupce zarovnej, ať je to čitelné.
   Když je seznam prázdný, vypiš o tom zprávu.
2. Pod ni napiš nekonečný cyklus, který vypíše menu, zeptá se na volbu
   a podle ní zavolá `vypis`, vypíše zůstatek, nebo skončí.
3. Když uživatelka napíše něco jiného než `1`, `2` nebo `0`, řekni jí to
   a menu ukaž znovu.

Funkce z `finance.py` si do `app.py` naimportuj stejně, jako importuješ
z `random`:

```python
from finance import zustatek
```

Zasekla ses? Nápověda je v souboru [`napovedy/01_zaklad.md`](../napovedy/01_zaklad.md).

## Hotovo, když

- [ ] všech pět testů a tvůj vlastní jsou zelené
- [ ] `app.py` vypíše transakce v čitelných sloupcích
- [ ] zůstatek z ukázkových dat vyjde 25540 Kč
- [ ] neznámá volba program neshodí a `0` ho ukončí
