# Testy funkcí z analyza.py.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest

import pytest

import analyza


def ukazka():
    # Pět vymyšlených pasažérů. U tak malého seznamu spočítáš výsledek z hlavy.
    # Každý test si zavolá ukazka() a dostane vlastní čerstvý seznam.
    return [
        {"Name": "Nováková, Mrs. Anna", "Sex": "female", "Pclass": 1, "Age": 30.0, "Survived": 1, "SibSp": 1, "Parch": 0, "Fare": 80.0, "Embarked": "S"},
        {"Name": "Novák, Mr. Jan", "Sex": "male", "Pclass": 1, "Age": 35.0, "Survived": 0, "SibSp": 1, "Parch": 0, "Fare": 80.0, "Embarked": "S"},
        {"Name": "Svoboda, Master. Petr", "Sex": "male", "Pclass": 3, "Age": 8.0, "Survived": 1, "SibSp": 0, "Parch": 1, "Fare": 10.0, "Embarked": "C"},
        {"Name": "Dvořák, Mr. Karel", "Sex": "male", "Pclass": 3, "Age": None, "Survived": 0, "SibSp": 0, "Parch": 0, "Fare": 0.0, "Embarked": "Q"},
        {"Name": "Černá, Miss. Eva", "Sex": "female", "Pclass": 3, "Age": 70.0, "Survived": 1, "SibSp": 0, "Parch": 0, "Fare": 10.0, "Embarked": "C"},
    ]


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


def test_prumerny_vek_pocita_jen_znamy_vek():
    assert analyza.prumerny_vek(ukazka()) == 35.75


def test_prumerny_vek_kdyz_vek_nikdo_nema():
    assert analyza.prumerny_vek([{"Age": None}]) is None


def test_nejstarsi():
    assert analyza.nejstarsi(ukazka())["Name"] == "Černá, Miss. Eva"


def test_nejmladsi():
    assert analyza.nejmladsi(ukazka())["Name"] == "Svoboda, Master. Petr"


def test_nejstarsi_z_prazdneho_seznamu():
    assert analyza.nejstarsi([]) is None


def test_filtruj_podle_textu():
    assert len(analyza.filtruj(ukazka(), "Sex", "female")) == 2


def test_filtruj_podle_cisla():
    assert len(analyza.filtruj(ukazka(), "Pclass", 3)) == 3


def test_filtruj_nikdo_nevyhovuje():
    assert analyza.filtruj(ukazka(), "Sex", "jiné") == []


def test_prumerna_cena():
    assert analyza.prumerna_cena(ukazka()) == 36.0


def test_prumerna_cena_prazdneho_seznamu():
    assert analyza.prumerna_cena([]) == 0


def test_nejdrazsi_listek():
    assert analyza.nejdrazsi_listek(ukazka()) == 80.0


def test_titul():
    assert analyza.titul("Braund, Mr. Owen Harris") == "Mr"
    assert analyza.titul("Rothes, the Countess. of (Lucy Noel Martha Dyer-Edwards)") == "the Countess"


def test_krestni_jmeno():
    assert analyza.krestni_jmeno("Braund, Mr. Owen Harris") == "Owen"
    assert analyza.krestni_jmeno('Navratil, Mr. Michel ("Louis M Hoffman")') == "Michel"


def test_krestni_jmeno_v_zavorce():
    assert analyza.krestni_jmeno("Duff Gordon, Lady. (Lucille Christiana Sutherland)") == "Lucille"


def test_pridej_jmena():
    pasazeri = ukazka()
    analyza.pridej_jmena(pasazeri)
    assert pasazeri[0]["Titul"] == "Mrs"
    assert pasazeri[2]["Krestni"] == "Petr"


def test_pocty():
    assert analyza.pocty(ukazka(), "Sex") == {"female": 2, "male": 3}


def test_pocty_prazdneho_seznamu():
    assert analyza.pocty([], "Sex") == {}


def test_pocet_prezivsich():
    assert analyza.pocet_prezivsich(ukazka()) == 3


def test_mira_preziti():
    assert analyza.mira_preziti(ukazka()) == 60


def test_mira_preziti_prazdneho_seznamu():
    assert analyza.mira_preziti([]) == 0


def test_mira_preziti_muzu():
    muzi = analyza.filtruj(ukazka(), "Sex", "male")
    assert analyza.mira_preziti(muzi) == pytest.approx(100 / 3)


def test_rozdel_podle():
    skupiny = analyza.rozdel_podle(ukazka(), "Embarked")
    assert len(skupiny["S"]) == 2
    assert len(skupiny["C"]) == 2
    assert len(skupiny["Q"]) == 1


def test_prezivani_podle():
    miry = analyza.prezivani_podle(ukazka(), "Embarked")
    assert miry["C"] == 100
    assert miry["S"] == 50
    assert miry["Q"] == 0


def test_rozdel_podle_dvou():
    skupiny = analyza.rozdel_podle_dvou(ukazka(), "Pclass", "Sex")
    assert len(skupiny[(3, "male")]) == 2


def test_prezivani_podle_dvou():
    miry = analyza.prezivani_podle_dvou(ukazka(), "Pclass", "Sex")
    assert miry[(1, "male")] == 0
    assert miry[(3, "female")] == 100
    assert miry[(3, "male")] == 50
