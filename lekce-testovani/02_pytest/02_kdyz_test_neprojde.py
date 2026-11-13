# ---------------------------------------------
#  Když test neprojde
# ---------------------------------------------
# Ve funkci jsou dvě chyby. Spusť testy v terminálu ve složce
# 02_pytest:
#
#   python -m pytest 02_kdyz_test_neprojde.py

def cena_vstupenky(vek):
    if vek < 15:
        return 100
    elif vek > 65:
        return 120
    else:
        return 150


def test_dite_plati_100():
    assert cena_vstupenky(8) == 100


def test_dospela_plati_180():
    assert cena_vstupenky(40) == 180


def test_seniorka_plati_120():
    assert cena_vstupenky(70) == 120


def test_seniorska_sleva_plati_od_65():
    assert cena_vstupenky(65) == 120


# Výpis je tentokrát delší. Začni odspodu, jako u chybových hlášek.
#
#
# ----- Poslední řádek: kolik prošlo -----
#
#   ======================== 2 failed, 2 passed in 0.03s ========================
#
# Dva testy prošly (passed), dva ne (failed). Řádek je červený.
#
# Pytest pustil všechny čtyři testy, i když se to po cestě
# pokazilo. Holé asserty v minulé složce by se zastavily na první
# chybě a o té druhé by ses nedozvěděla.
#
#
# ----- Nad ním: které neprošly -----
#
#   FAILED 02_kdyz_test_neprojde.py::test_dospela_plati_180 - assert 150 == 180
#   FAILED 02_kdyz_test_neprojde.py::test_seniorska_sleva_plati_od_65 - assert 150 == 120
#
# Za dvojtečkami je jméno testu, za pomlčkou tvrzení, které neplatí.
#
#
# ----- Ještě výš: podrobnosti ke každému testu -----
#
#   ___________________________ test_dospela_plati_180 ____________________________
#
#       def test_dospela_plati_180():
#   >       assert cena_vstupenky(40) == 180
#   E       assert 150 == 180
#   E        +  where 150 = cena_vstupenky(40)
#
# Řádek se šipkou > je tvrzení, které neplatí.
#
# Řádky s E říkají proč. Pytest za tebe dosadil, co funkce doopravdy
# vrátila: cena_vstupenky(40) vrátila 150 a test čekal 180.
#
# Tohle je velký rozdíl proti obyčejnému assertu. Ten by řekl jen
# AssertionError a co vyšlo, bys musela zjišťovat printem nebo
# debuggerem.
#
#
# ----- Oprav to -----
#
# V obou testech vyšlo 150, a to vrací větev else. Dospělí mají
# platit 180. Oprav to a spusť testy znovu.
#
# Zbude jeden červený test: šedesátipětiletá pořád platí plnou
# cenu. Druhou chybu už znáš. Oprav i tu.
#
# Hotovo je, když poslední řádek říká 4 passed.


# ----- Kdo má pravdu -----
#
# Když test neprojde, chyba nemusí být ve funkci. Může být i v testu:
# třeba sis špatně spočítala, co má vyjít.
#
# Než něco opravíš, podívej se do zadání. Když funkce dělá, co má, a
# test čeká něco jiného, opravuje se test. Nikdy ale neupravuj test
# jen proto, aby prošel – pak už nic neověřuje.
