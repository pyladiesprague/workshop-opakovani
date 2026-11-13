# Krok 2 – Přidání a odebrání transakce

Program zatím jen čte. Teď ho naučíš transakce přidávat a odebírat.
A hlavně: nesmí spadnout, ať uživatelka napíše cokoliv.

```text
Co chceš udělat? 3
Datum (RRRR-MM-DD): 21.11.2026
Datum napiš jako RRRR-MM-DD, třeba 2026-11-21.
Datum (RRRR-MM-DD): 2026-11-21
Typ (prijem/vydaj): vydaj
Částka v Kč: stovka
Částka musí být celé kladné číslo.
Částka v Kč: 100
Kategorie (vyplata, bydleni, jidlo, doprava, zabava, ostatni): jidlo
Popis: káva a dort
Přidáno.
```

## Funkce

Funkce píšeš do `finance.py`.

| Funkce | Co dělá |
|---|---|
| `pridej_transakci(transakce, datum, typ, castka, kategorie, popis)` | poskládá z údajů slovník, přidá ho na konec seznamu a vrátí ho |
| `odeber_transakci(transakce, cislo)` | odebere transakci s daným pořadovým číslem a vrátí ji; když taková není, vrátí `None` a seznam nechá být |
| `je_platna_castka(text)` | vrátí `True`, když je text celé kladné číslo |
| `je_platne_datum(text)` | vrátí `True`, když má text tvar `RRRR-MM-DD`, měsíc je 1 až 12 a den 1 až 31 |

Pořadové číslo je to z výpisu, takže první transakce má číslo 1, ne 0.

Poslední dvě funkce dostanou text z `input()` a jen řeknou, jestli je
v pořádku. Na nic se neptají a nic nevypisují, takže se dají otestovat.

## Testy

Zkopíruj na konec `test_finance.py`:

```python
def test_pridej_transakci():
    transakce = ukazka()
    finance.pridej_transakci(transakce, "2026-11-10", "vydaj", 80, "jidlo", "káva")
    assert len(transakce) == 6
    assert transakce[5]["popis"] == "káva"
    assert transakce[5]["castka"] == 80


def test_pridany_prijem_zvedne_zustatek():
    transakce = ukazka()
    finance.pridej_transakci(transakce, "2026-11-10", "prijem", 500, "ostatni", "dárek")
    assert finance.zustatek(transakce) == 600


def test_odeber_transakci():
    transakce = ukazka()
    odebrana = finance.odeber_transakci(transakce, 1)
    assert odebrana["popis"] == "pizza"
    assert len(transakce) == 4


def test_odeber_transakci_ktera_neexistuje():
    transakce = ukazka()
    assert finance.odeber_transakci(transakce, 99) is None
    assert finance.odeber_transakci(transakce, 0) is None
    assert len(transakce) == 5


def test_je_platna_castka():
    assert finance.je_platna_castka("250")
    assert not finance.je_platna_castka("0")
    assert not finance.je_platna_castka("-50")
    assert not finance.je_platna_castka("12.5")
    assert not finance.je_platna_castka("stovka")
    assert not finance.je_platna_castka("")


def test_je_platne_datum():
    assert finance.je_platne_datum("2026-11-21")
    assert not finance.je_platne_datum("21.11.2026")
    assert not finance.je_platne_datum("2026-11-2")
    assert not finance.je_platne_datum("2026-13-01")
    assert not finance.je_platne_datum("2026-11-32")
    assert not finance.je_platne_datum("rok-11-21")
    assert not finance.je_platne_datum("")
```

`assert` bez `==` říká „tohle má být pravda“, `assert not` říká „tohle má být
nepravda“.

Všimni si testu s číslem `0`. Zkus si v hlavě, co by udělalo
`transakce.pop(0 - 1)`. Přesně na takové chyby testy jsou.

**Vlastní test:** přidej a hned odeber stejnou transakci. Co má platit
o délce seznamu a o zůstatku?

## Program

Menu je v `app.py`.

Přidej do menu volby `3 – přidat transakci` a `4 – odebrat transakci`.

Při přidávání se ptej tak dlouho, dokud nedostaneš platnou odpověď:

- datum zkontroluj funkcí `je_platne_datum`,
- typ musí být `prijem`, nebo `vydaj`,
- částku zkontroluj funkcí `je_platna_castka` a převeď na číslo,
- kategorie musí být jedna z `KATEGORIE` z `ukazkova_data.py`,
- popis nesmí být prázdný.

Ptaní se v cyklu budeš potřebovat několikrát. Udělej si na něj funkce,
třeba `zeptej_se_na_castku()`, která vrátí až platné číslo.

Při odebírání nejdřív vypiš transakce, ať je vidět jejich čísla, a pak se
zeptej na číslo. Když transakce s tím číslem není, nebo to vůbec není
číslo, řekni to a nic neodebírej.

Zasekla ses? Nápověda je v souboru [`napovedy/02_pridani_a_odebrani.md`](../napovedy/02_pridani_a_odebrani.md).

## Hotovo, když

- [ ] všechny testy jsou zelené, včetně těch z kroku 1
- [ ] přidaná transakce je vidět ve výpisu a změní zůstatek
- [ ] program nespadne na vstupech `abc`, prázdný Enter, `-5`, `99`
- [ ] odebrání neexistujícího čísla nic nesmaže
