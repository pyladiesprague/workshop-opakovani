# Řešení cvičení 1 – pytest

def je_sude(cislo):
    return cislo % 2 == 0


def test_ctyrka_je_suda():
    assert je_sude(4)


def test_sedmicka_neni_suda():
    assert not je_sude(7)


def test_nula_je_suda():
    assert je_sude(0)


def test_zaporne_liche_cislo_neni_sude():
    assert not je_sude(-3)


# Výpis s -v končí 4 passed.
#
# Asserty pod funkcemi už v souboru zůstat nemají. Pytest při
# načítání souboru provede všechno, co není uvnitř funkce, a kdyby
# některý z nich neplatil, spadlo by to ještě před prvním testem.
