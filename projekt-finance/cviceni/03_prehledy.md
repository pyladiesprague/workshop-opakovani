# Krok 3 – Přehledy

Data už umíš zapisovat. Teď z nich program začne něco říkat: kolik jsi
utratila za jídlo, jak dopadl listopad, co tě stálo nejvíc.

```text
Co chceš udělat? 5
Měsíc (RRRR-MM): 2026-11
Příjmy:   33500 Kč
Výdaje:   20840 Kč
Rozdíl:   12660 Kč

Výdaje podle kategorií:
  bydleni     14000 Kč
  jidlo        4110 Kč
  doprava       550 Kč
  zabava        890 Kč
  ostatni      1290 Kč

Největší výdaj: nájem (14000 Kč)
```

## 1. Testy

Zkopíruj na konec `test_finance.py`:

```python
def test_vydaje_podle_kategorie():
    assert finance.vydaje_podle_kategorie(ukazka()) == {"jidlo": 750, "doprava": 150}


def test_vydaje_podle_kategorie_bez_transakci():
    assert finance.vydaje_podle_kategorie([]) == {}


def test_transakce_za_mesic():
    listopad = finance.transakce_za_mesic(ukazka(), "2026-11")
    assert len(listopad) == 4
    assert finance.soucet_vydaju(listopad) == 600


def test_transakce_za_mesic_nemeni_puvodni_seznam():
    transakce = ukazka()
    finance.transakce_za_mesic(transakce, "2026-11")
    assert len(transakce) == 5


def test_transakce_za_mesic_bez_transakci():
    assert finance.transakce_za_mesic(ukazka(), "2025-01") == []


def test_nejvetsi_vydaj():
    assert finance.nejvetsi_vydaj(ukazka())["popis"] == "pizza"


def test_nejvetsi_vydaj_bez_vydaju():
    assert finance.nejvetsi_vydaj([]) is None
```

## 2. Funkce do `finance.py`

| Funkce | Co vrátí |
|---|---|
| `vydaje_podle_kategorie(transakce)` | slovník, kde klíč je kategorie a hodnota součet výdajů v ní; příjmy se nepočítají |
| `transakce_za_mesic(transakce, mesic)` | nový seznam jen s transakcemi z daného měsíce; měsíc je text jako `"2026-11"` |
| `nejvetsi_vydaj(transakce)` | transakci s nejvyšší částkou mezi výdaji; když žádný výdaj není, vrátí `None` |

Podívej se na test `test_nejvetsi_vydaj`. Největší částku v ukázce má
brigáda za 1000, a přesto má vyjít pizza. Proč?

Funkce se dají skládat. Výdaje za listopad nepotřebují novou funkci:

```python
listopad = transakce_za_mesic(transakce, "2026-11")
print(soucet_vydaju(listopad))
```

**Vlastní test:** zkontroluj, že `vydaje_podle_kategorie` z listopadových
transakcí ukázky vrátí správný slovník. Nejdřív si ho spočítej ručně.

## 3. Menu do `app.py`

Přidej volbu `5 – přehled měsíce`. Zeptá se na měsíc a vypíše:

- příjmy, výdaje a rozdíl za ten měsíc,
- výdaje podle kategorií,
- největší výdaj.

Když v měsíci žádné transakce nejsou, vypiš jen zprávu o tom.

Měsíc od uživatelky zkontroluj. Šikovný trik: měsíc `2026-11` je platný
právě tehdy, když je platné datum `2026-11-01`, a na to už funkci máš.

## Nápověda

- Sčítání podle klíče je počítadlo, jen místo jedničky přičítáš částku. Tahák L9, *Počítadlo*.
- Nový seznam z těch položek, které projdou podmínkou. Tahák L8, *Stavění seznamu v cyklu*.
- Začíná text něčím? `startswith`. Tahák L6.
- Hledání největšího: pamatuj si zatím nejlepšího a začni s `None`. Tahák L9, *Kdo vyhrál*.
- Procházení slovníku po dvojicích: `for klic, hodnota in slovnik.items()`. Tahák L9.

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] přehled za `2026-11` z ukázkových dat sedí s ukázkou nahoře
- [ ] měsíc bez transakcí ani nesmyslný měsíc program neshodí

## Když zbyde čas

- Vypiš kategorie v přehledu od nejdražší po nejlevnější.
- Přidej funkci `prijmy_podle_kategorie`. Všimni si, kolik kódu se opakuje.
  Šla by z obou udělat jedna funkce s parametrem navíc?
- Přidej volbu, která vypíše přehled za všechny měsíce, které v datech jsou.
