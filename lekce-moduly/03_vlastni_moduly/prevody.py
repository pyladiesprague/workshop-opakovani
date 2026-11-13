# Modul s převody jednotek.
#
# Tenhle soubor se nespouští, je to modul. Jiné soubory si z něj berou
# funkce pomocí import. Proto jsou tu jen funkce a žádný input() ani
# print() mimo ně.


def na_fahrenheity(celsia):
    """Převede teplotu ze stupňů Celsia na stupně Fahrenheita."""
    return celsia * 9 / 5 + 32


def na_celsia(fahrenheity):
    """Převede teplotu ze stupňů Fahrenheita na stupně Celsia."""
    return (fahrenheity - 32) * 5 / 9


def mile_na_km(mile):
    """Převede míle na kilometry, zaokrouhlí na jedno desetinné místo."""
    return round(mile * 1.609, 1)
