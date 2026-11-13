# Krok 2 – Co v datech chybí?

V minulém kroku jsi viděla, že z CSV je všechno text. Taky sis možná všimla, že u některých lidí něco chybí. Než začneme počítat, data si uklidíme a zjistíme, co v nich chybí.

Chybějící hodnotu budeme ukládat jako `None`. To je v Pythonu hodnota, která znamená „nic“. Kdybychom místo ní napsali 0, vypadalo by to jako novorozeně a průměrný věk by vyšel špatně. Jestli je hodnota `None`, zjistíš pomocí `is None`:

```python
if vek is None:
    print("Věk neznáme")
```

## Funkce

Do `analyza.py` přidej tři funkce:

- `cislo_nebo_nic(text)` převede text na desetinné číslo. Z prázdného textu udělá `None`.
- `uprav_pasazera(radek)` vrátí kopii slovníku, ve které jsou čísla opravdu čísla. Kopii dostaneš takhle: `radek.copy()`.
  - `Survived`, `Pclass`, `SibSp` a `Parch` jsou celá čísla.
  - `Fare` je desetinné číslo.
  - `Age` převeď funkcí `cislo_nebo_nic`.
- `uprav_pasazery(radky)` vrátí seznam upravených pasažérů.

## Testy

Do `test_analyza.py` přidej tuhle třídu a místo `___` doplň, co má vyjít. Nahoře přidej nové funkce do importu.

```python
class TestUprava(unittest.TestCase):
    def test_cislo(self):
        self.assertEqual(cislo_nebo_nic("22"), ___)

    def test_prazdny_text(self):
        self.assertIsNone(cislo_nebo_nic(___))

    def test_uprav_pasazera(self):
        radek = {"Survived": "1", "Pclass": "3", "SibSp": "1", "Parch": "0", "Fare": "7.25", "Age": ""}
        pasazer = uprav_pasazera(radek)
        self.assertEqual(pasazer["Survived"], ___)
        self.assertEqual(pasazer["Fare"], ___)
        self.assertIsNone(pasazer["Age"])
```

## Program

Vypiš, u kolika pasažérů neznáme věk. Věk budeme za chvíli potřebovat, takže si to zapiš do `poznamky.md`.
