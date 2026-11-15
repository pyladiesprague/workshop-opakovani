# Řešení bonusu 5 – Čistá obrazovka
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import os

from analyza import (
    SOUBOR,
    nacti_pasazery,
    najdi_sloupec,
    prehled_podle,
    pridej_jmena,
    uprav_pasazery,
)


def vycisti_obrazovku():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_jmena(pasazeri)
sloupce = list(pasazeri[0])

# Co se má ukázat, se nevypisuje hned. Uloží se do seznamu a vypíše se
# až po smazání obrazovky. Jinak by zpráva hned zmizela.
radky = ["Průzkumník: napiš název sloupce, třeba Sex nebo Titul."]

while True:
    vycisti_obrazovku()
    for radek in radky:
        print(radek)
    print()

    text = input("Sloupec (prázdný řádek končí): ")
    if text.strip() == "":
        break

    nazev = najdi_sloupec(text, sloupce)
    if nazev is None:
        radky = [f"Takový sloupec neznám. Vyber si z těchhle: {', '.join(sloupce)}"]
    else:
        prehled = prehled_podle(pasazeri, nazev)
        if len(prehled) > 20:
            radky = [f"Sloupec {nazev} má {len(prehled)} různých hodnot, to je na přehled moc."]
        else:
            radky = [f"Přežití podle sloupce {nazev}"] + prehled
