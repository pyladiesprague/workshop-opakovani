# Řešení bonusu 4 – Děti a dospělí
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from analyza import (
    SOUBOR,
    TRIDY,
    filtruj,
    nacti_pasazery,
    rozdel_podle,
    tabulka,
    uprav_pasazery,
)

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


pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_skupiny(pasazeri)
deti = filtruj(pasazeri, "Skupina", "dítě")

for radek in tabulka("Podle věku", rozdel_podle(pasazeri, "Skupina"), SKUPINY):
    print(radek)
for radek in tabulka("Děti podle třídy", rozdel_podle(deti, "Pclass"), TRIDY):
    print(radek)
