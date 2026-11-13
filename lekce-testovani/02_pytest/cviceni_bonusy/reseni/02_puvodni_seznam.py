# Řešení bonusu 2 – pytest
# Opravená funkce. Pod ní je, co bylo špatně.

def tri_nejlevnejsi(ceny):
    serazene = sorted(ceny)
    return serazene[:3]


def test_tri_nejlevnejsi():
    assert tri_nejlevnejsi([500, 120, 80, 300, 90]) == [80, 90, 120]


def test_puvodni_seznam_zustane_stejny():
    ceny = [500, 120, 80, 300, 90]
    tri_nejlevnejsi(ceny)
    assert ceny == [500, 120, 80, 300, 90]


# S původní funkcí druhý test neprojde:
#
#   E       assert [80, 90, 120, 300, 500] == [500, 120, 80, 300, 90]
#
# sort mění seznam, na kterém ho zavoláš – to znáš z lekce 8. Funkce
# tak seřadila i seznam, který jí někdo poslal. Kdo by ho po zavolání
# dál používal, měl by v něm najednou jiné pořadí.
#
# sorted(ceny) je vestavěná funkce, která vrátí nový seřazený seznam
# a původní nechá být. Jde to i bez ní: ceny[:] udělá kopii seznamu
# a teprve na té se zavolá sort.
#
#   kopie = ceny[:]
#   kopie.sort()
#   return kopie[:3]
#
# Proto v projektu na workshopu volá každý test ukazka() a dostane
# vlastní čerstvý seznam. Kdyby testy sdílely jeden, funkce, která
# ho změní, by rozbila testy po ní.
