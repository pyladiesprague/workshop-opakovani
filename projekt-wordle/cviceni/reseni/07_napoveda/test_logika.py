# Testy logiky hry. Spouštěj je v panelu Testing ve VS Code (ikona zkumavky).

import unittest

from logika import aktualizuj_pismena, chyba_slova, filtruj, uprav_vstup, vyhodnot

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


class TestOpakovanaPismena(unittest.TestCase):
    def test_presna_shoda_ma_prednost(self):
        self.assertEqual(vyhodnot("banka", "sonda"), [N, N, S, N, S])

    def test_pismeno_v_hadanem_dvakrat_v_tajnem_jednou(self):
        self.assertEqual(vyhodnot("mamka", "mléko"), [S, N, N, S, N])

    def test_pismeno_v_hadanem_dvakrat_bez_presne_shody(self):
        self.assertEqual(vyhodnot("banka", "okapy"), [N, J, N, J, N])

    def test_pismeno_v_hadanem_jednou_v_tajnem_dvakrat(self):
        self.assertEqual(vyhodnot("kočka", "kabát"), [S, N, N, N, J])

    def test_shoda_a_jinde_u_stejneho_pismena(self):
        self.assertEqual(vyhodnot("nanuk", "panna"), [J, S, S, N, N])


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


class TestFiltruj(unittest.TestCase):
    def test_nechava_jen_odpovidajici_slova(self):
        mozna = ["kočka", "mléko", "sonda", "panna"]
        vysledek = vyhodnot("banka", "panna")
        self.assertEqual(filtruj(mozna, "banka", vysledek), ["panna"])

    def test_tajne_slovo_vzdy_zustane(self):
        mozna = ["kočka", "mléko", "sonda", "panna"]
        for tajne in mozna:
            vysledek = vyhodnot("kabát", tajne)
            self.assertIn(tajne, filtruj(mozna, "kabát", vysledek))

    def test_nemeni_puvodni_seznam(self):
        mozna = ["kočka", "mléko"]
        filtruj(mozna, "kočka", [S, S, S, S, S])
        self.assertEqual(mozna, ["kočka", "mléko"])
