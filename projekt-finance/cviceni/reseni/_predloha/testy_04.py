# Vlastní testy kroku 4, napsané podle tabulky v zadání kroku 4.


def test_zbyva_v_rozpoctu():
    rozpocty = {"jidlo": 1000, "doprava": 100}
    assert finance.zbyva_v_rozpoctu(ukazka(), rozpocty, "jidlo") == 250


def test_zbyva_v_rozpoctu_po_prekroceni():
    rozpocty = {"jidlo": 1000, "doprava": 100}
    assert finance.zbyva_v_rozpoctu(ukazka(), rozpocty, "doprava") == -50


def test_zbyva_v_rozpoctu_kdyz_se_neutracelo():
    rozpocty = {"zabava": 500}
    assert finance.zbyva_v_rozpoctu(ukazka(), rozpocty, "zabava") == 500


def test_zbyva_v_rozpoctu_bez_rozpoctu():
    rozpocty = {"jidlo": 1000}
    assert finance.zbyva_v_rozpoctu(ukazka(), rozpocty, "doprava") is None


def test_prekrocene_rozpocty():
    rozpocty = {"jidlo": 1000, "doprava": 100}
    assert finance.prekrocene_rozpocty(ukazka(), rozpocty) == ["doprava"]


def test_rozpocet_presne_na_korunu_neni_prekroceny():
    rozpocty = {"jidlo": 750}
    assert finance.prekrocene_rozpocty(ukazka(), rozpocty) == []


def test_prekrocene_rozpocty_bez_rozpoctu():
    assert finance.prekrocene_rozpocty(ukazka(), {}) == []
