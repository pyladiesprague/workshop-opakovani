# Testy funkcí z analyza.py. Spouštěj je v panelu Testing ve VS Code (ikona zkumavky).

import unittest

from analyza import SOUBOR, cislo_nebo_nic, nacti_pasazery, uprav_pasazera


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
