# Testy logiky hry. Spouštěj je v panelu Testing ve VS Code (ikona zkumavky).

import unittest

from logika import aktualizuj_pismena, chyba_slova, uprav_vstup, vyhodnot

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


class TestAktualizujPismena(unittest.TestCase):
    def test_zapise_vsechna_pismena(self):
        pismena = {}
        aktualizuj_pismena(pismena, "kabát", [S, J, N, N, N])
        self.assertEqual(pismena, {"k": S, "a": J, "b": N, "á": N, "t": N})

    def test_spravne_se_nikdy_nezhorsi(self):
        pismena = {"k": S}
        aktualizuj_pismena(pismena, "okapy", [N, J, N, N, N])
        self.assertEqual(pismena["k"], S)

    def test_jinde_se_nezhorsi_na_neni(self):
        pismena = {"a": J}
        aktualizuj_pismena(pismena, "banka", [N, N, N, N, N])
        self.assertEqual(pismena["a"], J)

    def test_stejne_pismeno_dvakrat_v_jednom_slove(self):
        pismena = {}
        aktualizuj_pismena(pismena, "banka", [N, J, N, N, N])
        self.assertEqual(pismena["a"], J)
