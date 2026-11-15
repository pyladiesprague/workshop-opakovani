# Testy funkcí z analyza.py.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest

import analyza


def test_soubor_s_daty_existuje():
    # Tenhle test projde hned. Když je zelený, testy ti fungují.
    assert analyza.SOUBOR.exists()


def test_pocet_pasazeru():
    pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)
    assert len(pasazeri) == 891


def test_kazdy_pasazer_ma_dvanact_sloupcu():
    pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)
    assert len(pasazeri[0]) == 12


def test_jmeno_prvniho_pasazera():
    pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)
    assert pasazeri[0]["Name"] == "Braund, Mr. Owen Harris"


def test_cislo():
    assert analyza.cislo_nebo_nic("22") == 22.0


def test_prazdny_text():
    assert analyza.cislo_nebo_nic("") is None


def test_uprav_pasazera():
    radek = {"Survived": "1", "Pclass": "3", "SibSp": "1", "Parch": "0", "Fare": "7.25", "Age": ""}
    pasazer = analyza.uprav_pasazera(radek)
    assert pasazer["Survived"] == 1
    assert pasazer["Fare"] == 7.25
    assert pasazer["Age"] is None
