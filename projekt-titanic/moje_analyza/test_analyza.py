# Testy funkcí z analyza.py. Spouštěj je v panelu Testing ve VS Code (ikona zkumavky).

import unittest

from analyza import SOUBOR, nacti_pasazery


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
