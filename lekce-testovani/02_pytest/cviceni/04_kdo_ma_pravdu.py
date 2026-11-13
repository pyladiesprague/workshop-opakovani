# Cvičení 4 – pytest
# Spusť testy. Dva neprojdou: jednou je chyba ve funkci, jednou
# v testu. Podle zadání rozhodni, co je co, a oprav to.

# Spouštěj v terminálu ve složce cviceni:
#
#   python -m pytest 04_kdo_ma_pravdu.py

# Funkce delka_filmu dostane délku filmu v minutách a vrátí ji jako
# text v hodinách a minutách. Film kratší než hodina má jen minuty.
#
#   delka_filmu(90)   →  "1 h 30 min"
#   delka_filmu(45)   →  "45 min"

def delka_filmu(minuty):
    hodiny = minuty // 60
    zbytek = minuty % 60
    return f"{hodiny} h {zbytek} min"


def test_hodina_a_pul():
    assert delka_filmu(90) == "1 h 30 min"


def test_kratky_film_ma_jen_minuty():
    assert delka_filmu(45) == "45 min"


def test_dve_hodiny_a_kousek():
    assert delka_filmu(125) == "2 h 15 min"


def test_presne_dve_hodiny():
    assert delka_filmu(120) == "2 h 0 min"
