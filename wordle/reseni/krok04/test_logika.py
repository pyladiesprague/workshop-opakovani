# Testy logiky hry. Spouštěj je v panelu Testing ve VS Code (ikona zkumavky).

import unittest

from logika import chyba_slova, uprav_vstup, vyhodnot

S = "spravne"
J = "jinde"
N = "neni"


class TestVyhodnot(unittest.TestCase):
    def test_uhodnute_slovo(self):
        self.assertEqual(vyhodnot("panna", "panna"), [S, S, S, S, S])

    def test_zadna_shoda(self):
        self.assertEqual(vyhodnot("mléko", "sušit"), [N, N, N, N, N])

    def test_pismeno_na_jinem_miste(self):
        self.assertEqual(vyhodnot("kabát", "kočka"), [S, J, N, N, N])

    def test_diakritika_je_jine_pismeno(self):
        self.assertEqual(vyhodnot("město", "mesto"), [S, N, S, S, S])


class TestVstup(unittest.TestCase):
    def test_uprav_vstup(self):
        self.assertEqual(uprav_vstup("  KOČKA "), "kočka")

    def test_kratke_slovo(self):
        self.assertEqual(chyba_slova("kočk", ["kočka"]), "Slovo musí mít 5 písmen.")

    def test_nezname_slovo(self):
        self.assertEqual(chyba_slova("xyzab", ["kočka"]), "Takové slovo neznám.")

    def test_povolene_slovo(self):
        self.assertEqual(chyba_slova("kočka", ["kočka"]), "")
