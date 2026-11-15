# Krok 5 – Co prozradí jména?

Znáš věk pasažérů i to, kolik zaplatili. Zbývá poslední věc, kterou o nich
seznam prozradí hned: jak se jmenovali a kým byli. Jména v souboru mají pevný
tvar: `Příjmení, Titul. Křestní jména`. Dá se z nich vyčíst víc, než se zdá.
Na konci tohohle kroku budeš vědět, kdo všechno na palubě byl a jak se
pasažéři nejčastěji jmenovali:

```text
Tituly:
  Mr: ???
  Mrs: ???
  ...
Nejčastější mužská jména:
  ?????: ??
  ?????: ??
  ...
```

Než začneš, zapiš si odhad: jaké bylo nejčastější mužské jméno? A jaké tituly
kromě `Mr` a `Mrs` v datech čekáš?

Tenhle krok má víc funkcí než ostatní. Když ti nepůjde, přeskoč ho a vrať se k
němu později. Kroky 6 až 9 fungují i bez něj.

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co dělá |
| --- | --- |
| `titul(jmeno)` | vrátí titul, tedy text mezi čárkou a tečkou |
| `krestni_jmeno(jmeno)` | vrátí první slovo za tečkou, bez uvozovek a závorek; když za tečkou nic není, vrátí `""` |
| `pridej_jmena(pasazeri)` | každému pasažérovi přidá sloupce `Titul` a `Krestni`; nic nevrací |
| `pocty(pasazeri, sloupec)` | vrátí slovník, kde klíče jsou hodnoty ze sloupce a hodnoty říkají, kolik pasažérů je má |

Text rozdělíš metodou `split`. Mezery, uvozovky a závorky z krajů odstraní
`strip`:

```python
"Braund, Mr. Owen Harris".split(",")
# ["Braund", " Mr. Owen Harris"]

'"Louis'.strip('"()')
# "Louis"
```

Nové sloupce fungují jako ostatní, takže na ně hned můžeš použít `filtruj` a
`pocty`:

```python
pocty(pasazeri, "Sex")
# {"male": ???, "female": ???}
```

## Testy

Zkopíruj na konec `test_analyza.py` a místo `___` doplň, co má vyjít:

```python
def test_titul():
    assert analyza.titul("Braund, Mr. Owen Harris") == ___
    assert analyza.titul("Rothes, the Countess. of (Lucy Noel Martha Dyer-Edwards)") == "the Countess"


def test_krestni_jmeno():
    assert analyza.krestni_jmeno("Braund, Mr. Owen Harris") == ___
    assert analyza.krestni_jmeno('Navratil, Mr. Michel ("Louis M Hoffman")') == "Michel"


def test_krestni_jmeno_v_zavorce():
    assert analyza.krestni_jmeno("Duff Gordon, Lady. (Lucille Christiana Sutherland)") == ___


def test_pocty():
    assert analyza.pocty(ukazka(), "Sex") == ___
```

**Vlastní test:** zkontroluj, že `pridej_jmena` přidá pasažérům z `ukazka()`
oba sloupce. Jaký titul má první z nich?

## Program

Výpisy píšeš do `zprava.py`.

1. Vypiš všechny tituly a u každého, kolik lidí ho má.
2. Vyber jen muže. Vypiš křestní jména, která má aspoň deset mužů, a u každého
   počet.

U žen křestní jména nepočítej. Vdané ženy jsou v seznamu zapsané jménem
manžela, vlastní jméno mají až v závorce.

Doplň poznámky. Který titul tě překvapil? Trefila ses s nejčastějším jménem?

Zasekla ses? Nápověda je v souboru [`napovedy/05_jmena.md`](../napovedy/05_jmena.md).

## Hotovo, když

- [ ] všechny testy včetně tvého vlastního jsou zelené
- [ ] program vypíše tituly s počty
- [ ] program vypíše nejčastější mužská jména s počty
- [ ] v `poznamky.md` máš odhad, výsledek a to, co tě překvapilo
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
