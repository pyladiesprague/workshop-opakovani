# Krok 3: Kolik lidí přežilo?

Tenhle výsledek je základ. Všechny další skupiny budeme porovnávat právě s ním.

Zapiš si do `poznamky.md` odhad: jaké procento pasažérů v souboru přežilo?

## Logika

Do `analyza.py` přidej dvě funkce:

- `pocet_prezivsich(pasazeri)` vrátí počet přeživších.
- `mira_preziti(pasazeri)` vrátí procento přeživších. Pro prázdný seznam vrátí 0, jinak by program spadl na dělení nulou.

## Testy

Testovat budeme na pěti vymyšlených pasažérech. Do `test_analyza.py` pod import zkopíruj seznam `PASAZERI`:

```python
PASAZERI = [
    {"Name": "Nováková, Mrs. Anna", "Sex": "female", "Pclass": 1, "Age": 30.0, "Survived": 1, "SibSp": 1, "Parch": 0, "Embarked": "S"},
    {"Name": "Novák, Mr. Jan", "Sex": "male", "Pclass": 1, "Age": 35.0, "Survived": 0, "SibSp": 1, "Parch": 0, "Embarked": "S"},
    {"Name": "Svoboda, Master. Petr", "Sex": "male", "Pclass": 3, "Age": 8.0, "Survived": 1, "SibSp": 0, "Parch": 1, "Embarked": "C"},
    {"Name": "Dvořák, Mr. Karel", "Sex": "male", "Pclass": 3, "Age": None, "Survived": 0, "SibSp": 0, "Parch": 0, "Embarked": "Q"},
    {"Name": "Černá, Miss. Eva", "Sex": "female", "Pclass": 3, "Age": 70.0, "Survived": 1, "SibSp": 0, "Parch": 0, "Embarked": "C"},
]
```

Pak přidej tuhle třídu a spočítej z hlavy, co má vyjít:

```python
class TestMira(unittest.TestCase):
    def test_pocet_prezivsich(self):
        self.assertEqual(pocet_prezivsich(PASAZERI), ___)

    def test_mira_preziti(self):
        self.assertEqual(mira_preziti(PASAZERI), ___)

    def test_prazdny_seznam(self):
        self.assertEqual(mira_preziti(___), 0)
```

## Zpráva

Vypiš počet pasažérů, počet přeživších a procento na jedno desetinné místo. Doplň poznámky.
