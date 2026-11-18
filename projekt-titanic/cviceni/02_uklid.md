# Krok 2 – Co v datech chybí?

Na konci tohohle kroku budou čísla v datech opravdu čísla a budeš vědět, u
kolika lidí chybí věk:

```text
Pasažérů: ???
Bez věku: ???
```

V minulém kroku jsi viděla, že z CSV je všechno text. Taky sis možná všimla,
že u některých lidí něco chybí. Než začneme počítat, data si uklidíme.

Chybějící hodnotu budeme ukládat jako `None`. To je v Pythonu hodnota, která
znamená „nic“. Kdybychom místo ní napsali 0, vypadalo by to jako novorozeně a
průměrný věk by vyšel špatně. Jestli je hodnota `None`, zjistíš pomocí `is
None`:

```python
if vek is None:
    print("Věk neznáme")
```

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `cislo_nebo_nic(text)` | text převedený na desetinné číslo; z prázdného textu udělá `None` |
| `uprav_pasazera(radek)` | kopii slovníku, ve které jsou čísla opravdu čísla |
| `uprav_pasazery(radky)` | seznam upravených pasažérů |

Co má `uprav_pasazera` převést:

- `Survived`, `Pclass`, `SibSp` a `Parch` jsou celá čísla.
- `Fare` je desetinné číslo.
- `Age` převeď funkcí `cislo_nebo_nic`.

Kopii slovníku dostaneš takhle: `radek.copy()`. Původní řádek se pak nezmění.

## Testy

Zkopíruj na konec `test_analyza.py` a místo `___` doplň, co má vyjít:

```python
def test_cislo():
    assert analyza.cislo_nebo_nic("22") == ___


def test_prazdny_text():
    assert analyza.cislo_nebo_nic(___) is None


def test_uprav_pasazera():
    radek = {"Survived": "1", "Pclass": "3", "SibSp": "1", "Parch": "0", "Fare": "7.25", "Age": ""}
    pasazer = analyza.uprav_pasazera(radek)
    assert pasazer["Survived"] == ___
    assert pasazer["Fare"] == ___
    assert pasazer["Age"] is None
```

## Program

Výpisy píšeš do `zprava.py`.

Výpis sloupců a prvního pasažéra z kroku 1 už můžeš smazat, splnil svůj účel.
Místo něj vypiš počet pasažérů a to, u kolika z nich neznáme věk. Věk budeme
za chvíli potřebovat, takže si to zapiš do `poznamky.md`.

Zasekla ses? Nápověda je v souboru [`napovedy/02_uklid.md`](../napovedy/02_uklid.md).

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] program vypíše, kolik pasažérů nemá věk
- [ ] číslo máš zapsané v `poznamky.md`
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
