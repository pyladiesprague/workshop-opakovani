# Řešení bonusu 4 – Děti a dospělí
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import analyza

SKUPINY = {
    "dítě": "děti do 16 let",
    "dospělý": "dospělí",
    "neznámý": "věk neznámý",
}


def vekova_skupina(vek):
    if vek is None:
        return "neznámý"
    if vek < 16:
        return "dítě"
    return "dospělý"


def pridej_skupiny(pasazeri):
    """Přidá každému pasažérovi sloupec Skupina."""
    for pasazer in pasazeri:
        pasazer["Skupina"] = vekova_skupina(pasazer["Age"])


pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))
pridej_skupiny(pasazeri)
deti = analyza.filtruj(pasazeri, "Skupina", "dítě")

for radek in analyza.tabulka("Podle věku", analyza.rozdel_podle(pasazeri, "Skupina"), SKUPINY):
    print(radek)
for radek in analyza.tabulka("Děti podle třídy", analyza.rozdel_podle(deti, "Pclass"), analyza.TRIDY):
    print(radek)
