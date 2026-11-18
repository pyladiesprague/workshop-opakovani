# Krok 3 – Kdo byl na palubě?

Na konci tohohle kroku budeš vědět, jak staří lidé na Titaniku cestovali a kdo
z nich byl nejstarší a nejmladší:

```text
Průměrný věk: ??.?
Nejstarší: ?????, věk ??.?
Nejmladší: ?????, věk ?.??
```

Než začneš, zapiš si do `poznamky.md` odhad: jaký byl průměrný věk pasažérů? A
kolik let bylo nejstaršímu?

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `prumerny_vek(pasazeri)` | průměrný věk těch pasažérů, u kterých věk známe; když ho neznáme u nikoho, vrátí `None` |
| `nejstarsi(pasazeri)` | celého pasažéra (slovník) s nejvyšším věkem; když věk nemá nikdo, vrátí `None` |
| `nejmladsi(pasazeri)` | celého pasažéra s nejnižším věkem; když věk nemá nikdo, vrátí `None` |

Pozor na lidi bez věku. Mají v `Age` hodnotu `None`, se kterou se nedá počítat
ani ji porovnávat. Funkce je musí přeskočit.

## Testy

Na testy nebudeme používat celý soubor, stovky řádků z hlavy nespočítáš.
Testovat budeme na pěti vymyšlených pasažérech. Do `test_analyza.py` pod řádek
`import analyza` zkopíruj funkci `ukazka`:

```python
def ukazka():
    # Pět vymyšlených pasažérů. U tak malého seznamu spočítáš výsledek z hlavy.
    # Každý test si zavolá ukazka() a dostane vlastní čerstvý seznam.
    return [
        {"Name": "Nováková, Mrs. Anna", "Sex": "female", "Pclass": 1, "Age": 30.0, "Survived": 1, "SibSp": 1, "Parch": 0, "Fare": 80.0, "Embarked": "S"},
        {"Name": "Novák, Mr. Jan", "Sex": "male", "Pclass": 1, "Age": 35.0, "Survived": 0, "SibSp": 1, "Parch": 0, "Fare": 80.0, "Embarked": "S"},
        {"Name": "Svoboda, Master. Petr", "Sex": "male", "Pclass": 3, "Age": 8.0, "Survived": 1, "SibSp": 0, "Parch": 1, "Fare": 10.0, "Embarked": "C"},
        {"Name": "Dvořák, Mr. Karel", "Sex": "male", "Pclass": 3, "Age": None, "Survived": 0, "SibSp": 0, "Parch": 0, "Fare": 0.0, "Embarked": "Q"},
        {"Name": "Černá, Miss. Eva", "Sex": "female", "Pclass": 3, "Age": 70.0, "Survived": 1, "SibSp": 0, "Parch": 0, "Fare": 10.0, "Embarked": "C"},
    ]
```

Pak na konec souboru přidej tyhle testy a místo `___` doplň, co má vyjít.
Spočítej to z hlavy nebo na papíře:

```python
def test_prumerny_vek_pocita_jen_znamy_vek():
    assert analyza.prumerny_vek(ukazka()) == ___


def test_prumerny_vek_kdyz_vek_nikdo_nema():
    assert analyza.prumerny_vek([{"Age": None}]) is None


def test_nejstarsi():
    assert analyza.nejstarsi(ukazka())["Name"] == ___


def test_nejmladsi():
    assert analyza.nejmladsi(ukazka())["Name"] == ___
```

## Program

Výpisy píšeš do `zprava.py`.

Výpis z minulého kroku nech, jak je, a nové řádky přidej pod něj. Tak to dělej
i v dalších krocích: `zprava.py` ti bude postupně růst.

Vypiš průměrný věk na jedno desetinné místo a jméno a věk nejstaršího a
nejmladšího pasažéra.

Podívej se na věk nejmladšího. Co to číslo asi znamená? Doplň poznámky.

Zasekla ses? Nápověda je v souboru [`napovedy/03_kdo_byl_na_palube.md`](../napovedy/03_kdo_byl_na_palube.md).

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] program vypíše průměrný věk a nejstaršího a nejmladšího pasažéra, pod
      výpisem z kroku 2
- [ ] v `poznamky.md` máš odhad i výsledek
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
