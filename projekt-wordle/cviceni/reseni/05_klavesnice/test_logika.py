# Testy logiky hry Wordle.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest

import logika

S = "spravne"
J = "jinde"
N = "neni"


def test_slovo_ma_pet_pismen():
    # Tenhle test projde hned. Když je zelený, testy ti fungují.
    assert logika.DELKA_SLOVA == 5


def test_uhodnute_slovo():
    assert logika.vyhodnot("panna", "panna") == [S, S, S, S, S]


def test_zadna_shoda():
    assert logika.vyhodnot("mléko", "sušit") == [N, N, N, N, N]


def test_pismeno_na_jinem_miste():
    assert logika.vyhodnot("kabát", "kočka") == [S, J, N, N, N]


def test_diakritika_je_jine_pismeno():
    assert logika.vyhodnot("město", "mesto") == [S, N, S, S, S]


def test_uprav_vstup():
    assert logika.uprav_vstup("  KOČKA ") == "kočka"


def test_kratke_slovo():
    assert logika.chyba_slova("kočk", ["kočka"]) == "Slovo musí mít 5 písmen."


def test_nezname_slovo():
    assert logika.chyba_slova("xyzab", ["kočka"]) == "Takové slovo neznám."


def test_povolene_slovo():
    assert logika.chyba_slova("kočka", ["kočka"]) == ""


def test_zapise_vsechna_pismena():
    pismena = {}
    logika.aktualizuj_pismena(pismena, "kabát", [S, J, N, N, N])
    assert pismena == {"k": S, "a": J, "b": N, "á": N, "t": N}


def test_spravne_se_nikdy_nezhorsi():
    pismena = {"k": S}
    logika.aktualizuj_pismena(pismena, "okapy", [N, J, N, N, N])
    assert pismena["k"] == S


def test_jinde_se_nezhorsi_na_neni():
    pismena = {"a": J}
    logika.aktualizuj_pismena(pismena, "banka", [N, N, N, N, N])
    assert pismena["a"] == J


def test_stejne_pismeno_dvakrat_v_jednom_slove():
    pismena = {}
    logika.aktualizuj_pismena(pismena, "banka", [N, J, N, N, N])
    assert pismena["a"] == J
