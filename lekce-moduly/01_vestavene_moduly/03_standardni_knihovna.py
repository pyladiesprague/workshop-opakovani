# ---------------------------------------------
#  Co všechno Python umí sám
# ---------------------------------------------
# Spusť soubor. Na konci chvilku počká – to je schválně.
#
# Modulům, které má Python s sebou, se říká standardní knihovna.
# Nic se neinstaluje, stačí je importovat. Pár užitečných na ukázku:

# statistics – průměr, medián a další výpočty nad seznamem čísel
from statistics import mean, median

body = [7, 9, 4, 10, 8]
print("Průměr:", mean(body))
print("Medián:", median(body))


# datetime – datum a čas
from datetime import date

dnes = date.today()
print("Dnes je", dnes)
print("Rok:", dnes.year)


# time – například sleep, které program na chvilku uspí
from time import sleep

for cislo in range(3, 0, -1):
    print(cislo)
    sleep(1)            # počkej jednu sekundu
print("Start!")


# Seznam všech modulů standardní knihovny je v dokumentaci:
#   https://docs.python.org/3/library/
#
# Nemusíš je znát nazpaměť. Když něco potřebuješ, vyplatí se
# nejdřív zkusit vyhledat „python jak …“ – často už to
# v nějakém modulu je.
