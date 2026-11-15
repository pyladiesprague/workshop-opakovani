# Krok 4 – Kolik stál lístek?

Víš, jak staří lidé na palubě byli. Necestovali ale všichni stejně: loď měla
tři třídy a lístek do každé stál jinak. Na konci tohohle kroku budeš umět
vybrat z pasažérů jen některé a budeš vědět, kolik se za cestu platilo:

```text
1. třída: průměrně ??.? liber
2. třída: průměrně ??.? liber
3. třída: průměrně ??.? liber
Nejdražší lístek: ???.? liber
  ?????, lístek ?????
Zadarmo: ?? lidí
```

Než začneš, zapiš si odhad: kolikrát dražší byl lístek do 1. třídy než do 3.?

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `filtruj(pasazeri, sloupec, hodnota)` | nový seznam pasažérů, kteří mají v daném sloupci danou hodnotu |
| `prumerna_cena(pasazeri)` | průměrnou cenu lístku; pro prázdný seznam vrátí 0, jinak by program spadl na dělení nulou |
| `nejdrazsi_listek(pasazeri)` | nejvyšší cenu lístku; pro prázdný seznam vrátí 0 |

Jedna funkce `filtruj` poslouží pro všechny sloupce:

```python
zeny = filtruj(pasazeri, "Sex", "female")
prvni_trida = filtruj(pasazeri, "Pclass", 1)
```

Funkce se dají skládat. Průměrná cena v 1. třídě nepotřebuje novou funkci:

```python
prumerna_cena(filtruj(pasazeri, "Pclass", 1))
```

## Testy

První dva testy jsou hotové. U dalších doplň, co má vyjít.

```python
def test_filtruj_podle_textu():
    assert len(analyza.filtruj(ukazka(), "Sex", "female")) == 2


def test_prumerna_cena_prazdneho_seznamu():
    assert analyza.prumerna_cena([]) == 0


def test_filtruj_podle_cisla():
    assert len(analyza.filtruj(ukazka(), "Pclass", 3)) == ___


def test_prumerna_cena():
    assert analyza.prumerna_cena(ukazka()) == ___


def test_nejdrazsi_listek():
    assert analyza.nejdrazsi_listek(ukazka()) == ___
```

**Vlastní test:** co má `filtruj` vrátit, když nikdo nevyhovuje? Napiš na to
test.

## Program

Výpisy píšeš do `zprava.py`.

1. Vypiš průměrnou cenu lístku v každé třídě.
2. Vypiš nejvyšší cenu a jména všech, kdo ji zaplatili. Pomůže ti `filtruj`
   podle sloupce `Fare`. U každého vypiš i číslo lístku ze sloupce `Ticket`.
3. Vypiš, kolik lidí má cenu lístku 0.

Doplň poznámky. Čeho sis všimla u lidí s nejdražším lístkem? Co to říká o
sloupci `Fare`?

Zasekla ses? Nápověda je v souboru [`napovedy/04_listky.md`](../napovedy/04_listky.md).

## Hotovo, když

- [ ] všechny testy včetně tvého vlastního jsou zelené
- [ ] program vypíše průměrnou cenu ve třech třídách
- [ ] program vypíše, kdo měl nejdražší lístek a kolik lidí jelo zadarmo
- [ ] v `poznamky.md` máš odhad, výsledek a to, co tě překvapilo
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
