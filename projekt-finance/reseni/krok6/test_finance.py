# Testy ke správci financí.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest
#
# Ke každému kroku najdeš v zadání připravené testy. Zkopíruj je na konec
# tohohle souboru a piš kód ve finance.py, dokud nebudou zelené.
# Vlastní testy piš taky sem.

import finance


def ukazka():
    # Malá sada transakcí na testování. Každý test si zavolá ukazka()
    # a dostane vlastní čerstvý seznam, takže si testy navzájem nic nezmění.
    return [
        {"datum": "2026-10-28", "typ": "vydaj", "castka": 300, "kategorie": "jidlo", "popis": "pizza"},
        {"datum": "2026-11-01", "typ": "prijem", "castka": 1000, "kategorie": "vyplata", "popis": "brigáda"},
        {"datum": "2026-11-03", "typ": "vydaj", "castka": 200, "kategorie": "jidlo", "popis": "oběd"},
        {"datum": "2026-11-05", "typ": "vydaj", "castka": 150, "kategorie": "doprava", "popis": "jízdenky"},
        {"datum": "2026-11-09", "typ": "vydaj", "castka": 250, "kategorie": "jidlo", "popis": "nákup"},
    ]


def test_ukazka_ma_pet_transakci():
    # Tenhle test projde hned. Když je zelený, testy ti fungují.
    assert len(ukazka()) == 5


def test_soucet_prijmu():
    assert finance.soucet_prijmu(ukazka()) == 1000


def test_soucet_vydaju():
    assert finance.soucet_vydaju(ukazka()) == 900


def test_zustatek():
    assert finance.zustatek(ukazka()) == 100


def test_zustatek_bez_transakci():
    assert finance.zustatek([]) == 0


def test_pridej_transakci():
    transakce = ukazka()
    finance.pridej_transakci(transakce, "2026-11-10", "vydaj", 80, "jidlo", "káva")
    assert len(transakce) == 6
    assert transakce[5]["popis"] == "káva"
    assert transakce[5]["castka"] == 80


def test_pridany_prijem_zvedne_zustatek():
    transakce = ukazka()
    finance.pridej_transakci(transakce, "2026-11-10", "prijem", 500, "ostatni", "dárek")
    assert finance.zustatek(transakce) == 600


def test_odeber_transakci():
    transakce = ukazka()
    odebrana = finance.odeber_transakci(transakce, 1)
    assert odebrana["popis"] == "pizza"
    assert len(transakce) == 4


def test_odeber_transakci_ktera_neexistuje():
    transakce = ukazka()
    assert finance.odeber_transakci(transakce, 99) is None
    assert finance.odeber_transakci(transakce, 0) is None
    assert len(transakce) == 5


def test_je_platna_castka():
    assert finance.je_platna_castka("250")
    assert not finance.je_platna_castka("0")
    assert not finance.je_platna_castka("-50")
    assert not finance.je_platna_castka("12.5")
    assert not finance.je_platna_castka("stovka")
    assert not finance.je_platna_castka("")


def test_je_platne_datum():
    assert finance.je_platne_datum("2026-11-21")
    assert not finance.je_platne_datum("21.11.2026")
    assert not finance.je_platne_datum("2026-11-2")
    assert not finance.je_platne_datum("2026-13-01")
    assert not finance.je_platne_datum("2026-11-32")
    assert not finance.je_platne_datum("rok-11-21")
    assert not finance.je_platne_datum("")


def test_vydaje_podle_kategorie():
    assert finance.vydaje_podle_kategorie(ukazka()) == {"jidlo": 750, "doprava": 150}


def test_vydaje_podle_kategorie_bez_transakci():
    assert finance.vydaje_podle_kategorie([]) == {}


def test_transakce_za_mesic():
    listopad = finance.transakce_za_mesic(ukazka(), "2026-11")
    assert len(listopad) == 4
    assert finance.soucet_vydaju(listopad) == 600


def test_transakce_za_mesic_nemeni_puvodni_seznam():
    transakce = ukazka()
    finance.transakce_za_mesic(transakce, "2026-11")
    assert len(transakce) == 5


def test_transakce_za_mesic_bez_transakci():
    assert finance.transakce_za_mesic(ukazka(), "2025-01") == []


def test_nejvetsi_vydaj():
    assert finance.nejvetsi_vydaj(ukazka())["popis"] == "pizza"


def test_nejvetsi_vydaj_bez_vydaju():
    assert finance.nejvetsi_vydaj([]) is None


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


def test_uloz_a_nacti(tmp_path):
    cesta = tmp_path / "pokus.json"
    finance.uloz(ukazka(), cesta)
    assert finance.nacti(cesta) == ukazka()


def test_ulozeni_zachova_hacky_a_carky(tmp_path):
    cesta = tmp_path / "pokus.json"
    transakce = [
        {"datum": "2026-11-21", "typ": "vydaj", "castka": 90, "kategorie": "jidlo", "popis": "žluťoučký koláč"},
    ]
    finance.uloz(transakce, cesta)
    assert finance.nacti(cesta)[0]["popis"] == "žluťoučký koláč"
