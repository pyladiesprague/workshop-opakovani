# Testy funkcí z analyza.py.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest

#@ 6+
import pytest

#@ vse
import analyza


#@ 3+
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


#@ vse
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


#@ 2+
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


#@ 3+
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


#@ 4+
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


#@ 5+
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


#@ 6+
def test_pocet_prezivsich():
    assert analyza.pocet_prezivsich(ukazka()) == 3


def test_mira_preziti():
    assert analyza.mira_preziti(ukazka()) == 60


def test_mira_preziti_prazdneho_seznamu():
    assert analyza.mira_preziti([]) == 0


def test_mira_preziti_muzu():
    muzi = analyza.filtruj(ukazka(), "Sex", "male")
    assert analyza.mira_preziti(muzi) == pytest.approx(100 / 3)


#@ 7+
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


#@ 8+
def test_rozdel_podle_dvou():
    skupiny = analyza.rozdel_podle_dvou(ukazka(), "Pclass", "Sex")
    assert len(skupiny[(3, "male")]) == 2


def test_prezivani_podle_dvou():
    miry = analyza.prezivani_podle_dvou(ukazka(), "Pclass", "Sex")
    assert miry[(1, "male")] == 0
    assert miry[(3, "female")] == 100
    assert miry[(3, "male")] == 50


#@ 9+
def test_sloupec_nejvyssi_hodnoty_ma_plnou_sirku():
    assert analyza.sloupec_grafu(100, 100, 10) == "█" * 10


def test_sloupec_polovicni_hodnoty_je_polovicni():
    assert analyza.sloupec_grafu(50, 100, 10) == "█" * 5


def test_sloupec_nuly_je_prazdny():
    assert analyza.sloupec_grafu(0, 100, 10) == ""


def test_sloupec_male_hodnoty_je_videt():
    assert analyza.sloupec_grafu(1, 1000, 10) == "█"


def test_sloupec_kdyz_je_nejvyssi_nula():
    assert analyza.sloupec_grafu(0, 0, 10) == ""


def test_graf_ma_nadpis_a_radky():
    skupiny = analyza.rozdel_podle(ukazka(), "Sex")
    radky = analyza.graf("Podle pohlaví", skupiny, {"female": "ženy", "male": "muži"})
    assert radky[1] == "Podle pohlaví"
    assert len(radky) == 4
    assert "100.0 %" in radky[2]


def test_graf_preskoci_chybejici_skupinu():
    radky = analyza.graf("Podle pohlaví", {}, {"female": "ženy"})
    assert len(radky) == 2


#@ 10+
def test_radek_tabulky():
    assert analyza.radek_tabulky("ženy", 74.2, 314) == "  ženy                     74.2 %  (314)"


def test_radek_tabulky_zaokrouhli():
    assert " 18.9 %" in analyza.radek_tabulky("muži", 18.8908, 577)


def test_tabulka_ma_nadpis_a_radky():
    radky = analyza.tabulka("Podle pohlaví", {"female": ukazka()}, {"female": "ženy"})
    assert len(radky) == 3
    assert "(5)" in radky[2]


def test_tabulka_preskoci_chybejici_skupinu():
    radky = analyza.tabulka("Podle pohlaví", {}, {"female": "ženy"})
    assert len(radky) == 2


#@ 10-11
def test_sestav_zpravu():
    pasazeri = ukazka()
    analyza.pridej_jmena(pasazeri)
    radky = analyza.sestav_zpravu(pasazeri)
    assert "  ženy                    100.0 %  (2)" in radky
    assert "Závěr" in radky


#@ 11+
def test_najdi_sloupec_bez_ohledu_na_velikost_pismen():
    assert analyza.najdi_sloupec("sex", ["Sex", "Pclass"]) == "Sex"
    assert analyza.najdi_sloupec("  PCLASS ", ["Sex", "Pclass"]) == "Pclass"


def test_najdi_sloupec_ktery_neexistuje():
    assert analyza.najdi_sloupec("barva", ["Sex", "Pclass"]) is None


def test_prehled_podle():
    radky = analyza.prehled_podle(ukazka(), "Embarked")
    assert len(radky) == 3
    assert "  C                       100.0 %  (2)" in radky


#@ 12+
def test_velikost_rodiny():
    assert analyza.velikost_rodiny({"SibSp": 0, "Parch": 0}) == "sám"
    assert analyza.velikost_rodiny({"SibSp": 1, "Parch": 2}) == "malá"
    assert analyza.velikost_rodiny({"SibSp": 3, "Parch": 1}) == "velká"


def test_moje_otazka():
    pasazeri = ukazka()
    analyza.pridej_rodiny(pasazeri)
    radky = analyza.moje_otazka(pasazeri)
    assert radky[1] == "Moje otázka: pomohlo cestovat s rodinou?"
    assert "  cestoval sám             50.0 %  (2)" in radky


def test_sestav_zpravu():
    pasazeri = ukazka()
    analyza.pridej_jmena(pasazeri)
    analyza.pridej_rodiny(pasazeri)
    radky = analyza.sestav_zpravu(pasazeri)
    assert "  ženy                    100.0 %  (2)" in radky
    assert "Závěr" in radky
