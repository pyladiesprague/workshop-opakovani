# Řešení cvičení 2 – pytest

def pocet_samohlasek(text):
    pocet = 0
    for znak in text.lower():
        if znak in "aeiouy":
            pocet = pocet + 1
    return pocet


def test_jedno_slovo():
    assert pocet_samohlasek("pes") == 1


def test_vic_slov():
    assert pocet_samohlasek("ahoj svete") == 4


def test_velka_pismena_se_pocitaji():
    assert pocet_samohlasek("AHOJ") == 2


def test_y_je_samohlaska():
    assert pocet_samohlasek("byt") == 1


def test_prazdny_text_ma_nula_samohlasek():
    assert pocet_samohlasek("") == 0


def test_slovo_bez_samohlasek():
    assert pocet_samohlasek("brrr") == 0


def test_pismena_s_carkou_se_nepocitaji():
    assert pocet_samohlasek("líný") == 0


# Tvoje testy můžou vypadat jinak, hlavně ať pokrývají zadání.
#
# Každá věta zadání si zaslouží aspoň jeden test: velká písmena,
# y mezi samohláskami, písmena s čárkou. Zbytek jsou okraje: prázdný
# text a text, ve kterém samohláska není.
