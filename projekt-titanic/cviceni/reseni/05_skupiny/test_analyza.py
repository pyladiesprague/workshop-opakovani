# Testy funkcí z analyza.py. Spouštěj je v panelu Testing ve VS Code (ikona zkumavky).

import unittest

from analyza import (
    SOUBOR,
    cislo_nebo_nic,
    filtruj,
    mira_preziti,
    miry_skupin,
    nacti_pasazery,
    pocet_prezivsich,
    prezivani_podle,
    rozdel_podle,
    uprav_pasazera,
)

# Pět vymyšlených pasažérů. U tak malého seznamu spočítáš výsledek z hlavy.
PASAZERI = [
    {"Name": "Nováková, Mrs. Anna", "Sex": "female", "Pclass": 1, "Age": 30.0, "Survived": 1, "SibSp": 1, "Parch": 0, "Embarked": "S"},
    {"Name": "Novák, Mr. Jan", "Sex": "male", "Pclass": 1, "Age": 35.0, "Survived": 0, "SibSp": 1, "Parch": 0, "Embarked": "S"},
    {"Name": "Svoboda, Master. Petr", "Sex": "male", "Pclass": 3, "Age": 8.0, "Survived": 1, "SibSp": 0, "Parch": 1, "Embarked": "C"},
    {"Name": "Dvořák, Mr. Karel", "Sex": "male", "Pclass": 3, "Age": None, "Survived": 0, "SibSp": 0, "Parch": 0, "Embarked": "Q"},
    {"Name": "Černá, Miss. Eva", "Sex": "female", "Pclass": 3, "Age": 70.0, "Survived": 1, "SibSp": 0, "Parch": 0, "Embarked": "C"},
]


class TestNacteni(unittest.TestCase):
    def test_pocet_pasazeru(self):
        pasazeri = nacti_pasazery(SOUBOR)
        self.assertEqual(len(pasazeri), 891)

    def test_kazdy_pasazer_ma_dvanact_sloupcu(self):
        pasazeri = nacti_pasazery(SOUBOR)
        self.assertEqual(len(pasazeri[0]), 12)

    def test_jmeno_prvniho_pasazera(self):
        pasazeri = nacti_pasazery(SOUBOR)
        self.assertEqual(pasazeri[0]["Name"], "Braund, Mr. Owen Harris")


class TestUprava(unittest.TestCase):
    def test_cislo(self):
        self.assertEqual(cislo_nebo_nic("22"), 22.0)

    def test_prazdny_text(self):
        self.assertIsNone(cislo_nebo_nic(""))

    def test_uprav_pasazera(self):
        radek = {"Survived": "1", "Pclass": "3", "SibSp": "1", "Parch": "0", "Fare": "7.25", "Age": ""}
        pasazer = uprav_pasazera(radek)
        self.assertEqual(pasazer["Survived"], 1)
        self.assertEqual(pasazer["Fare"], 7.25)
        self.assertIsNone(pasazer["Age"])


class TestMira(unittest.TestCase):
    def test_pocet_prezivsich(self):
        self.assertEqual(pocet_prezivsich(PASAZERI), 3)

    def test_mira_preziti(self):
        self.assertEqual(mira_preziti(PASAZERI), 60)

    def test_prazdny_seznam(self):
        self.assertEqual(mira_preziti([]), 0)


class TestFiltruj(unittest.TestCase):
    def test_podle_textu(self):
        self.assertEqual(len(filtruj(PASAZERI, "Sex", "female")), 2)

    def test_podle_cisla(self):
        self.assertEqual(len(filtruj(PASAZERI, "Pclass", 3)), 3)

    def test_nikdo_nevyhovuje(self):
        self.assertEqual(filtruj(PASAZERI, "Sex", "jiné"), [])


class TestSkupiny(unittest.TestCase):
    def test_rozdel_podle(self):
        skupiny = rozdel_podle(PASAZERI, "Pclass")
        self.assertEqual(len(skupiny[1]), 2)
        self.assertEqual(len(skupiny[3]), 3)

    def test_prezivani_podle(self):
        miry = prezivani_podle(PASAZERI, "Sex")
        self.assertEqual(miry["female"], 100)
        self.assertAlmostEqual(miry["male"], 100 / 3)
