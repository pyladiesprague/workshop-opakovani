# Cvičení 5 – pytest
# Testy už jsou hotové, chybí funkce. Napiš ji tak, aby všechny
# testy prošly.

# Spouštěj v terminálu ve složce cviceni:
#
#   python -m pytest 05_nejdriv_testy.py
#
# Na začátku jsou všechny testy červené. Nevadí to – piš funkci
# a spouštěj testy znovu, dokud nezezelenají. Takhle budeš pracovat
# i v projektu na workshopu.

# Funkce inicialy dostane celé jméno a vrátí iniciály: první
# písmeno jména a příjmení, každé s tečkou, mezi nimi mezera.

def inicialy(cele_jmeno):
    pass        # pass nic nedělá, jen drží místo. Nahraď ho svým kódem.


def test_jmeno_a_prijmeni():
    assert inicialy("Jana Nováková") == "J. N."


def test_mala_pismena_se_zvetsi():
    assert inicialy("eva malá") == "E. M."


def test_mezery_navic_nevadi():
    assert inicialy("  Petra   Svobodová ") == "P. S."
