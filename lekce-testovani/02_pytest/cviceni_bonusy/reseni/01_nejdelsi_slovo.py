# Řešení bonusu 1 – pytest
# Opravená funkce. Pod ní je, který test chybu našel.

def nejdelsi_slovo(veta):
    nejdelsi = ""
    for slovo in veta.split():
        if len(slovo) > len(nejdelsi):
            nejdelsi = slovo
    return nejdelsi


def test_nejdelsi_slovo_ve_vete():
    assert nejdelsi_slovo("pes leží na zahradě") == "zahradě"


def test_nejdelsi_slovo_na_konci():
    assert nejdelsi_slovo("já mám ráda programování") == "programování"


def test_jedno_slovo():
    assert nejdelsi_slovo("ahoj") == "ahoj"


def test_prazdny_text():
    assert nejdelsi_slovo("") == ""


def test_dve_stejne_dlouha_slova_vrati_prvni():
    assert nejdelsi_slovo("pes kos") == "pes"


# Chybu našel jen poslední test. Funkce měla >=, takže stejně dlouhé
# slovo, které přišlo později, přepsalo to dřívější. Vrátila kos
# místo pes.
#
# Zbylé testy by prošly i s chybou. Každá věta zadání, která začíná
# „když“, je kandidát na vlastní test.
