# Řešení cvičení 3 – pytest
# Opravená funkce. Pod ní je, jak se na chybu přišlo.

def prumer(cisla):
    if len(cisla) == 0:
        return 0
    return sum(cisla) / len(cisla)


def test_prumer_tri_cisel():
    assert prumer([2, 4, 9]) == 5


def test_prumer_jednoho_cisla():
    assert prumer([7]) == 7


def test_prumer_prazdneho_seznamu_je_nula():
    assert prumer([]) == 0


# S původní funkcí neprojde test prázdného seznamu, ale jinak, než
# jsi zvyklá. Výpis má dvě patra, jako chybové hlášky z lekce 7:
#
#       def test_prumer_prazdneho_seznamu_je_nula():
#   >       assert prumer([]) == 0
#
#   cisla = []
#
#       def prumer(cisla):
#   >       return sum(cisla) / len(cisla)
#   E       ZeroDivisionError: division by zero
#
# Horní patro je test, odkud se funkce zavolala. Spodní je místo,
# kde to spadlo – uvnitř funkce prumer. Nad ním pytest vypsal, s čím
# byla funkce zavolaná: cisla = [].
#
# Test tedy nespadl na tom, že by tvrzení neplatilo. Spadl dřív,
# když funkce počítala. Poznáš to podle posledního řádku s E: místo
# assert … je tam jméno chyby, tady ZeroDivisionError.
#
# Prázdný seznam má délku nula a dělit nulou nejde. Funkce se na něj
# musí zeptat dřív, než dělí.
