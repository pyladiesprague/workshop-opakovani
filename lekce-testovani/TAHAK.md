# Tahák – Testování s pytestem

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## assert

```python
assert cena_vstupenky(65) == 120      # tvrdím, že…
```

Když podmínka platí, nestane se nic. Když neplatí, program spadne
s `AssertionError` a ukáže na řádek s tvrzením.

Výsledek, který čekáš, si spočítej sama. `assert f(3) == f(3)` platí
vždycky, a proto nic neověří.

## Tvary, se kterými si vystačíš

```python
assert vysledek == 100              # rovná se (číslo, text, seznam)
assert je_sude(4)                   # má být True
assert not je_sude(7)               # má být False
assert vysledek is None             # funkce nic nevrátila
assert "Jana" in text               # obsahuje
assert len(seznam) == 2             # délka
```

## Test

```python
def cena_vstupenky(vek):
    ...


def test_seniorska_sleva_plati_od_65():     # jméno začíná test_
    assert cena_vstupenky(65) == 120        # žádné parametry, uvnitř assert
```

- Testy nevoláš. Pytest najde funkce `test_…` a zavolá je sám.
- Jméno říká, co test ověřuje.
- Jeden test ověřuje jednu věc.

## Instalace a spuštění

```text
python -m pip install pytest          jednou, na Macu python3
python -m pytest                      všechny soubory test_*.py
python -m pytest 01_prvni_testy.py    jen tenhle soubor
python -m pytest -v                   s jmény testů
```

Ve VS Code je panel **Testing** (ikona baňky vlevo): zelená fajfka
prošel, červený křížek neprošel.

## Když test neprojde

```text
    def test_dospela_plati_180():
>       assert cena_vstupenky(40) == 180
E       assert 150 == 180
E        +  where 150 = cena_vstupenky(40)
```

Řádek s `>` je tvrzení, které neplatí. Řádky s `E` říkají, co
doopravdy vyšlo: funkce vrátila 150 a test čekal 180.

U textů pytest ukáže rozdíl: `-` je, co test čekal, `+` co vyšlo.

Na posledním řádku je souhrn, třeba `2 failed, 2 passed`. Pytest
pustí všechny testy, i když některý neprojde.

| Ve výpisu | Co se většinou stalo |
|---|---|
| `assert None == 100` | funkce nic nevrací, chybí `return` |
| `ZeroDivisionError`, `IndexError`… místo `assert` | funkce spadla, ještě než se porovnávalo |
| `NameError: name 'cena' is not defined` | funkce chybí, nebo se jmenuje jinak |
| `AttributeError: module 'finance' has no attribute 'zustatek'` | totéž, když se funkce importuje z jiného souboru |
| `TypeError: … takes 1 positional argument but 2 were given` | test volá funkci s jiným počtem argumentů |

Chyba může být i v testu. Rozhoduje zadání: když funkce dělá, co
má, opravuje se test. Neupravuj ale test jen proto, aby prošel.

## Co testovat

- **obyčejný případ**, který si umíš spočítat z hlavy,
- **okraje**: hranice (přesně 65, přesně 90), nula, prázdný seznam
  nebo text, jediná položka,
- **špatný vstup**: záporné číslo, hodnota mimo rozsah.

Dobré znamení: když ve funkci schválně uděláš chybu (`>` místo
`>=`), aspoň jeden test zčervená.

## Testy v projektu

```text
finance.py          funkce, které vrací výsledky – bez input a print
app.py              menu, input a print
test_finance.py     testy
```

```python
import finance                          # jméno souboru bez .py


def test_zustatek_bez_transakci():
    assert finance.zustatek([]) == 0
```

1. Zkopíruj testy ze zadání do `test_….py`. Jsou červené.
2. Piš funkci, dokud nezezelenají.
3. Spusť všechny testy, ne jen ty nové. Starý červený test znamená,
   že změna rozbila něco, co fungovalo.
