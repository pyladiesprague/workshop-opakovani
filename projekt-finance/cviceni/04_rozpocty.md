# Krok 4 – Rozpočty

Rozpočet je částka, kterou chceš za měsíc v jedné kategorii nejvýš utratit.
Program ti řekne, kolik ti z něj zbývá, a ozve se, když ho překročíš.

```text
Co chceš udělat? 6
Měsíc (RRRR-MM): 2026-11
  jidlo        4110 /   4000 Kč   překročeno o 110 Kč
  doprava       550 /   1000 Kč   zbývá 450 Kč
  zabava        890 /   1500 Kč   zbývá 610 Kč
Překročené rozpočty: jidlo
```

Rozpočty jsou slovník `rozpocty` v souboru `ukazkova_data.py`: klíč je
kategorie, hodnota je měsíční limit v korunách. Ne každá kategorie rozpočet má.

## 1. Testy

Zkopíruj na konec `test_finance.py`:

```python
def test_zbyva_v_rozpoctu():
    rozpocty = {"jidlo": 1000, "doprava": 100}
    assert finance.zbyva_v_rozpoctu(ukazka(), rozpocty, "jidlo") == 250


def test_zbyva_v_rozpoctu_po_prekroceni():
    rozpocty = {"jidlo": 1000, "doprava": 100}
    assert finance.zbyva_v_rozpoctu(ukazka(), rozpocty, "doprava") == -50


def test_zbyva_v_rozpoctu_kdyz_se_neutracelo():
    rozpocty = {"zabava": 500}
    assert finance.zbyva_v_rozpoctu(ukazka(), rozpocty, "zabava") == 500


def test_zbyva_v_rozpoctu_bez_rozpoctu():
    rozpocty = {"jidlo": 1000}
    assert finance.zbyva_v_rozpoctu(ukazka(), rozpocty, "doprava") is None


def test_prekrocene_rozpocty():
    rozpocty = {"jidlo": 1000, "doprava": 100}
    assert finance.prekrocene_rozpocty(ukazka(), rozpocty) == ["doprava"]


def test_rozpocet_presne_na_korunu_neni_prekroceny():
    rozpocty = {"jidlo": 750}
    assert finance.prekrocene_rozpocty(ukazka(), rozpocty) == []
```

## 2. Funkce do `finance.py`

| Funkce | Co vrátí |
|---|---|
| `zbyva_v_rozpoctu(transakce, rozpocty, kategorie)` | limit kategorie mínus výdaje v ní; po překročení vyjde záporné číslo; když kategorie rozpočet nemá, vrátí `None` |
| `prekrocene_rozpocty(transakce, rozpocty)` | seznam kategorií, ve kterých se utratilo víc, než je limit |

Funkce počítají se všemi transakcemi, které dostanou. Rozpočet je ale
měsíční, takže jim budeš posílat jen transakce jednoho měsíce. Funkci,
která je vybere, už máš z kroku 3.

Součet výdajů v kategorii taky nemusíš psát znovu.

**Vlastní test:** co má `prekrocene_rozpocty` vrátit, když je slovník
rozpočtů prázdný? Napiš na to test a zjisti, jestli to tvoje funkce splní.

## 3. Menu do `app.py`

Přidej dvě volby:

- `6 – rozpočty` se zeptá na měsíc a ke každé kategorii s rozpočtem vypíše,
  kolik se utratilo, jaký je limit a kolik zbývá, nebo o kolik je překročený.
- `7 – nastavit rozpočet` se zeptá na kategorii a částku a rozpočet uloží do
  slovníku. Když kategorie rozpočet už má, přepíše ho.

A ještě jedna věc: když po přidání výdaje bude rozpočet jeho kategorie v tom
měsíci překročený, program na to hned upozorní.

```text
Přidáno.
Pozor, rozpočet na jidlo za 2026-11 je překročený o 210 Kč.
```

Měsíc transakce jsou první znaky jejího data.

Slovník `rozpocty` si do `app.py` naimportuj z `ukazkova_data` a funkcím,
které ho potřebují, ho pošli jako argument.

## Nápověda

- Je klíč ve slovníku? `in`. Čtení, které nespadne, když klíč chybí: `get` s výchozí hodnotou. Tahák L9, *Když klíč chybí*.
- Přidání i přepsání hodnoty je stejný zápis: `slovnik[klic] = hodnota`. Tahák L9, *Měnění*.
- Limit i kategorie najednou: `for kategorie, limit in rozpocty.items()`. Tahák L9.
- Prvních sedm znaků textu: `text[:7]`. Tahák L6.

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] rozpočty za `2026-11` z ukázkových dat sedí s ukázkou nahoře
- [ ] nově nastavený rozpočet se hned projeví ve volbě 6
- [ ] výdaj, který rozpočet překročí, vyvolá upozornění

## Když zbyde čas

- Upozorni už ve chvíli, kdy je vyčerpáno 80 % rozpočtu.
- Vypiš u každého rozpočtu, kolik procent je vyčerpáno.
- Přidej volbu, která rozpočet kategorie zruší.
