# Kopie modulu ze cvičení 1 – Rozděl program, aby šlo řešení bonusu 2 spustit.
# Jen funkce, žádný input() ani print().


def spropitne(castka, procenta):
    return round(castka * procenta / 100)


def celkem(castka, procenta):
    return castka + spropitne(castka, procenta)
