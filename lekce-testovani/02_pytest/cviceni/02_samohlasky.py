# Cvičení 2 – pytest
# Napiš testy k funkci podle zadání. Funkce je správně, takže
# všechny tvoje testy mají projít.

# Spouštěj v terminálu ve složce cviceni:
#
#   python -m pytest 02_samohlasky.py -v

# Funkce pocet_samohlasek vrátí, kolik je v textu samohlásek
# a, e, i, o, u, y. Počítá malá i velká písmena. Písmena s čárkou
# nebo kroužkem (á, ů…) nepočítá.

def pocet_samohlasek(text):
    pocet = 0
    for znak in text.lower():
        if znak in "aeiouy":
            pocet = pocet + 1
    return pocet


# Sem napiš testy. Mysli na tři otázky ze souboru 03_co_testovat.py:
# obyčejný případ, okraje a vstup, který je nějak zvláštní.
