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
