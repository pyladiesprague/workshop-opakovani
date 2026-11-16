# Vlastní testy kroku 5, napsané podle seznamu v zadání kroku 5.


def test_sloupec_nejvyssi_hodnoty_ma_plnou_sirku():
    assert finance.sloupec(100, 100, 10) == "█" * 10


def test_sloupec_polovicni_hodnoty_je_polovicni():
    assert finance.sloupec(50, 100, 10) == "█" * 5


def test_sloupec_nuly_je_prazdny():
    assert finance.sloupec(0, 100, 10) == ""


def test_sloupec_male_hodnoty_je_videt():
    assert finance.sloupec(1, 1000, 10) == "█"


def test_sloupec_kdyz_je_nejvyssi_nula():
    assert finance.sloupec(0, 0, 10) == ""


def test_sloupec_tri_ctvrtiny():
    assert finance.sloupec(75, 100, 20) == "█" * 15
