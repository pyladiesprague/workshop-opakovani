# ---------------------------------------------
#  První testy s pytestem
# ---------------------------------------------
# Tenhle soubor nespouštěj tlačítkem Run. Přečti si ho celý a podle
# návodu dole ho pusť přes pytest.

def cena_vstupenky(vek):
    if vek < 15:
        return 100
    elif vek >= 65:
        return 120
    else:
        return 180


def test_dite_plati_100():
    assert cena_vstupenky(8) == 100


def test_dospela_plati_180():
    assert cena_vstupenky(40) == 180


def test_seniorka_plati_120():
    assert cena_vstupenky(70) == 120


def test_seniorska_sleva_plati_od_65():
    assert cena_vstupenky(65) == 120


# Asserty z minulé složky jsou teď každý ve vlastní funkci. Takové
# funkci se říká test. Má tři pravidla:
#
#   - jméno začíná test_,
#   - nemá žádné parametry,
#   - uvnitř je assert.
#
# Za test_ napiš, co test ověřuje. Když test jednou neprojde, jméno
# ti řekne, co se rozbilo, dřív než otevřeš kód.
#
# Nikde v souboru se testy nevolají. To udělá pytest: najde všechny
# funkce, jejichž jméno začíná test_, a postupně je zavolá.


# ----- Instalace -----
#
# pytest není součástí Pythonu, musíš si ho nainstalovat. Stačí to
# jednou. V terminálu VS Code napiš:
#
#   python -m pip install pytest
#
# Na Macu místo python piš python3, tady i ve všech dalších
# příkazech.


# ----- Spuštění -----
#
# 1. V levém panelu Explorer klikni pravým tlačítkem na složku
#    02_pytest a vyber "Open in Integrated Terminal". Otevře se
#    terminál, který stojí v téhle složce.
#
# 2. Napiš do něj:
#
#      python -m pytest 01_prvni_testy.py
#
# Na konci výpisu uvidíš:
#
#   01_prvni_testy.py ....                                   [100%]
#
#   ============================ 4 passed in 0.01s ============================
#
# Každá tečka je jeden test, který prošel. Passed znamená prošel.
# Když je řádek zelený, je všechno v pořádku.


# ----- Podrobnější výpis -----
#
# Když chceš vidět jména testů, přidej na konec příkazu -v:
#
#   python -m pytest 01_prvni_testy.py -v
#
#   01_prvni_testy.py::test_dite_plati_100 PASSED                [ 25%]
#   01_prvni_testy.py::test_dospela_plati_180 PASSED             [ 50%]
#   01_prvni_testy.py::test_seniorka_plati_120 PASSED            [ 75%]
#   01_prvni_testy.py::test_seniorska_sleva_plati_od_65 PASSED   [100%]
#
# Teď je vidět, proč na jménech záleží. Výpis se čte jako seznam
# toho, co program umí.
