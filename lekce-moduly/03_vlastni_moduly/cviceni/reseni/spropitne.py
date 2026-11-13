# Modul ke cvičení 1 – Rozděl program.
# Jen funkce, žádný input() ani print().


def spropitne(castka, procenta):
    return round(castka * procenta / 100)


def celkem(castka, procenta):
    return castka + spropitne(castka, procenta)
