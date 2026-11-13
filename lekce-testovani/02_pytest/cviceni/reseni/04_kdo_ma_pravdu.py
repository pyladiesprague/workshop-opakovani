# Řešení cvičení 4 – pytest
# Opravená funkce a opravený test. Pod nimi je, jak se to poznalo.

def delka_filmu(minuty):
    hodiny = minuty // 60
    zbytek = minuty % 60
    if hodiny == 0:
        return f"{zbytek} min"
    return f"{hodiny} h {zbytek} min"


def test_hodina_a_pul():
    assert delka_filmu(90) == "1 h 30 min"


def test_kratky_film_ma_jen_minuty():
    assert delka_filmu(45) == "45 min"


def test_dve_hodiny_a_kousek():
    assert delka_filmu(125) == "2 h 5 min"


def test_presne_dve_hodiny():
    assert delka_filmu(120) == "2 h 0 min"


# Chyba ve funkci – test_kratky_film_ma_jen_minuty
#
#   E       AssertionError: assert '0 h 45 min' == '45 min'
#
# Zadání říká, že film kratší než hodina má jen minuty. Test čeká
# přesně to, takže má pravdu a opravuje se funkce.
#
#
# Chyba v testu – test_dve_hodiny_a_kousek
#
#   E       AssertionError: assert '2 h 5 min' == '2 h 15 min'
#
# 125 minut jsou dvě hodiny (120) a pět minut. Funkce počítá dobře,
# ten, kdo psal test, se přepočítal. Opravuje se test.
#
#
# Výsledek, který test čeká, si vždycky spočítej ručně a pečlivě.
# Špatně spočítaný test tě pošle hledat chybu tam, kde žádná není.
