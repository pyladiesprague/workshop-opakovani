# Testy logiky hry Wordle.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest

import logika

S = "spravne"
J = "jinde"
N = "neni"


def test_slovo_ma_pet_pismen():
    # Tenhle test projde hned. Když je zelený, testy ti fungují.
    assert logika.DELKA_SLOVA == 5


def test_uhodnute_slovo():
    assert logika.vyhodnot("panna", "panna") == [S, S, S, S, S]


def test_zadna_shoda():
    assert logika.vyhodnot("mléko", "sušit") == [N, N, N, N, N]


def test_pismeno_na_jinem_miste():
    assert logika.vyhodnot("kabát", "kočka") == [S, J, N, N, N]


def test_diakritika_je_jine_pismeno():
    assert logika.vyhodnot("město", "mesto") == [S, N, S, S, S]


def test_uprav_vstup():
    assert logika.uprav_vstup("  KOČKA ") == "kočka"


def test_kratke_slovo():
    assert logika.chyba_slova("kočk", ["kočka"]) == "Slovo musí mít 5 písmen."


def test_nezname_slovo():
    assert logika.chyba_slova("xyzab", ["kočka"]) == "Takové slovo neznám."


def test_povolene_slovo():
    assert logika.chyba_slova("kočka", ["kočka"]) == ""


def test_zapise_vsechna_pismena():
    pismena = {}
    logika.aktualizuj_pismena(pismena, "kabát", [S, J, N, N, N])
    assert pismena == {"k": S, "a": J, "b": N, "á": N, "t": N}


def test_spravne_se_nikdy_nezhorsi():
    pismena = {"k": S}
    logika.aktualizuj_pismena(pismena, "okapy", [N, J, N, N, N])
    assert pismena["k"] == S


def test_jinde_se_nezhorsi_na_neni():
    pismena = {"a": J}
    logika.aktualizuj_pismena(pismena, "banka", [N, N, N, N, N])
    assert pismena["a"] == J


def test_stejne_pismeno_dvakrat_v_jednom_slove():
    pismena = {}
    logika.aktualizuj_pismena(pismena, "banka", [N, J, N, N, N])
    assert pismena["a"] == J


def test_presna_shoda_ma_prednost():
    assert logika.vyhodnot("banka", "sonda") == [N, N, S, N, S]


def test_pismeno_v_hadanem_dvakrat_v_tajnem_jednou():
    assert logika.vyhodnot("mamka", "mléko") == [S, N, N, S, N]


def test_pismeno_v_hadanem_dvakrat_bez_presne_shody():
    assert logika.vyhodnot("banka", "okapy") == [N, J, N, J, N]


def test_pismeno_v_hadanem_jednou_v_tajnem_dvakrat():
    assert logika.vyhodnot("kočka", "kabát") == [S, N, N, N, J]


def test_shoda_a_jinde_u_stejneho_pismena():
    assert logika.vyhodnot("nanuk", "panna") == [J, S, S, N, N]


def test_filtruj_necha_jen_odpovidajici_slova():
    mozna = ["kočka", "mléko", "sonda", "panna"]
    vysledek = logika.vyhodnot("banka", "panna")
    assert logika.filtruj(mozna, "banka", vysledek) == ["panna"]


def test_tajne_slovo_vzdy_zustane():
    mozna = ["kočka", "mléko", "sonda", "panna"]
    for tajne in mozna:
        vysledek = logika.vyhodnot("kabát", tajne)
        assert tajne in logika.filtruj(mozna, "kabát", vysledek)


def test_filtruj_nemeni_puvodni_seznam():
    mozna = ["kočka", "mléko"]
    logika.filtruj(mozna, "kočka", [S, S, S, S, S])
    assert mozna == ["kočka", "mléko"]


def test_pismeno_se_ve_slove_pocita_jednou():
    cetnosti = logika.spocitej_pismena(["panna", "pivo"])
    assert cetnosti["n"] == 1
    assert cetnosti["p"] == 2


def test_opakovane_pismeno_nedava_body_navic():
    cetnosti = {"p": 2, "a": 3, "n": 4}
    assert logika.ohodnot("panna", cetnosti) == 9


def test_vybere_slovo_s_nejvic_body():
    slova = ["aabbc", "abcde", "aaaaa"]
    assert logika.nejlepsi_slovo(slova) == "abcde"


def test_jedine_slovo():
    assert logika.nejlepsi_slovo(["kočka"]) == "kočka"


def test_statistiky_bez_her():
    statistiky = logika.spocitej_statistiky([])
    assert statistiky["her"] == 0
    assert statistiky["uspesnost"] == 0


def test_statistiky_vyhry_a_prohry():
    statistiky = logika.spocitej_statistiky(["3", "0", "3", "6"])
    assert statistiky["her"] == 4
    assert statistiky["vyher"] == 3
    assert statistiky["uspesnost"] == 75
    assert statistiky["pokusy"][3] == 2
    assert statistiky["pokusy"][6] == 1
