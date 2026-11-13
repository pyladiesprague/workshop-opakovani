# Cvičení 1 – pytest
# Přepiš asserty dole na testy pro pytest: každý do vlastní funkce
# s popisným jménem. Pak testy spusť.

# Testy spouštěj v terminálu, který stojí ve složce cviceni (pravým
# tlačítkem na složku → Open in Integrated Terminal):
#
#   python -m pytest 01_prepis_na_pytest.py -v

def je_sude(cislo):
    return cislo % 2 == 0


assert je_sude(4)
assert not je_sude(7)
assert je_sude(0)
assert not je_sude(-3)
