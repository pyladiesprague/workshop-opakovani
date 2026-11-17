# Modul k bonusu 3. Je stejný jako spropitne.py, který sis psala
# v lekci o modulech (03_vlastni_moduly, cvičení 1).
# Jen funkce, žádný input() ani print().


def spropitne(castka, procenta):
    return round(castka * procenta / 100)


def celkem(castka, procenta):
    return castka + spropitne(castka, procenta)
