# Krok 6 – Kdo přežil častěji?

Víš, kdo na palubě byl. Teď se podíváš, jak dopadli. Na konci tohohle kroku
budeš znát základní číslo a první rozdíly mezi skupinami:

```text
Přežilo: ??? z ???
To je ??.? %
Ženy: ??.? %
Muži: ??.? %
1. třída: ??.? %
2. třída: ??.? %
3. třída: ??.? %
```

Než začneš, zapiš si odhady: jaké procento pasažérů v souboru přežilo? A bude
rozdíl mezi ženami a muži? Mezi třídami?

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `pocet_prezivsich(pasazeri)` | počet přeživších |
| `mira_preziti(pasazeri)` | procento přeživších; pro prázdný seznam vrátí 0 |

Skupiny si vybereš funkcí `filtruj` z kroku 4.

## Testy

Zkopíruj na konec `test_analyza.py` a místo `___` doplň, co má vyjít:

```python
def test_pocet_prezivsich():
    assert analyza.pocet_prezivsich(ukazka()) == ___


def test_mira_preziti():
    assert analyza.mira_preziti(ukazka()) == ___


def test_mira_preziti_prazdneho_seznamu():
    assert analyza.mira_preziti(___) == 0
```

**Vlastní test:** jaká je míra přežití mužů z `ukazka()`? Vyjde 100 / 3, tedy
číslo s nekonečně mnoha desetinnými místy. Desetinná čísla se v počítači
ukládají nepřesně, proto je porovnávej přes `pytest.approx`. Nahoře v souboru
k tomu přidej `import pytest`:

```python
assert vysledek == pytest.approx(100 / 3)
```

## Program

Výpisy píšeš do `zprava.py`.

Vypiš, kolik lidí přežilo a kolik je to procent. Potom procento přeživších
žen, mužů a lidí z každé třídy.

Doplň poznámky. Rozdíly jsou velké. Napadá tě, proč tomu tak mohlo být?

Zasekla ses? Nápověda je v souboru [`napovedy/06_kdo_prezil.md`](../napovedy/06_kdo_prezil.md).

## Hotovo, když

- [ ] všechny testy včetně tvého vlastního jsou zelené
- [ ] program vypíše celkové přežití a přežití žen, mužů a tří tříd
- [ ] v `poznamky.md` máš odhady, výsledky a domněnku proč
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
