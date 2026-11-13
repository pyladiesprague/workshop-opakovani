# Řešení cvičení 5 – pytest

def inicialy(cele_jmeno):
    casti = cele_jmeno.split()
    jmeno = casti[0]
    prijmeni = casti[1]
    return f"{jmeno[0].upper()}. {prijmeni[0].upper()}."


def test_jmeno_a_prijmeni():
    assert inicialy("Jana Nováková") == "J. N."


def test_mala_pismena_se_zvetsi():
    assert inicialy("eva malá") == "E. M."


def test_mezery_navic_nevadi():
    assert inicialy("  Petra   Svobodová ") == "P. S."


# split() bez argumentu rozdělí text podle mezer a mezery navíc
# zahodí, i ty na začátku a na konci. Proto třetí test projde bez
# strip.
#
# Kdybys rozdělovala split(" "), třetí test neprojde: mezi dvěma
# mezerami vznikne prázdný kus "" a casti[0] by bylo právě ono.
# Přesně kvůli takovým věcem má test s mezerami navíc smysl.
#
# Na začátku funkce obsahovala jen pass a nic nevracela. Testy proto
# hlásily assert None == 'J. N.' – funkce bez return vrací None.
