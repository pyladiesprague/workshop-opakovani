# Testy funkcí z analyza.py. Spouštěj je v panelu Testing ve VS Code (ikona zkumavky).

import unittest

from analyza import (
    SOUBOR,
    cislo_nebo_nic,
    filtruj,
    mira_preziti,
    miry_skupin,
    moje_otazka,
    nacti_pasazery,
    pocet_prezivsich,
    prezivani_podle,
    prezivani_podle_dvou,
    pridej_skupiny,
    radek_tabulky,
    rozdel_podle,
    rozdel_podle_dvou,
    sestav_zpravu,
    tabulka,
    uprav_pasazera,
    vekova_skupina,
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


class TestDvaSloupce(unittest.TestCase):
    def test_rozdel_podle_dvou(self):
        skupiny = rozdel_podle_dvou(PASAZERI, "Pclass", "Sex")
        self.assertEqual(len(skupiny[(3, "male")]), 2)

    def test_prezivani_podle_dvou(self):
        miry = prezivani_podle_dvou(PASAZERI, "Pclass", "Sex")
        self.assertEqual(miry[(1, "male")], 0)
        self.assertEqual(miry[(3, "female")], 100)
        self.assertEqual(miry[(3, "male")], 50)


class TestVekoveSkupiny(unittest.TestCase):
    def test_hranice_veku(self):
        self.assertEqual(vekova_skupina(15.9), "dítě")
        self.assertEqual(vekova_skupina(16.0), "dospělý")

    def test_neznamy_vek(self):
        self.assertEqual(vekova_skupina(None), "neznámý")

    def test_pridej_skupiny(self):
        pasazeri = [PASAZERI[2].copy(), PASAZERI[3].copy()]
        pridej_skupiny(pasazeri)
        self.assertEqual(pasazeri[0]["Skupina"], "dítě")
        self.assertEqual(pasazeri[1]["Skupina"], "neznámý")


class TestZprava(unittest.TestCase):
    def test_radek_tabulky(self):
        self.assertEqual(
            radek_tabulky("ženy", 74.2, 314), "  ženy                     74.2 %  (314)"
        )

    def test_zaokrouhleni(self):
        self.assertIn(" 18.9 %", radek_tabulky("muži", 18.8908, 577))

    def test_tabulka_ma_nadpis_a_radky(self):
        radky = tabulka("Podle pohlaví", {"female": PASAZERI}, {"female": "ženy"})
        self.assertEqual(len(radky), 3)
        self.assertIn("(5)", radky[2])

    def test_tabulka_preskoci_chybejici_skupinu(self):
        radky = tabulka("Podle pohlaví", {}, {"female": "ženy"})
        self.assertEqual(len(radky), 2)

    def test_sestav_zpravu(self):
        pasazeri = []
        for pasazer in PASAZERI:
            pasazeri.append(pasazer.copy())
        pridej_skupiny(pasazeri)
        radky = sestav_zpravu(pasazeri)
        self.assertIn("  ženy                    100.0 %  (2)", radky)
        self.assertIn("Závěr", radky)


class TestMojeOtazka(unittest.TestCase):
    def test_moje_otazka(self):
        radky = moje_otazka(PASAZERI)
        self.assertEqual(radky[1], "Moje otázka: záleželo na přístavu?")
        self.assertIn("  Cherbourg               100.0 %  (2)", radky)
