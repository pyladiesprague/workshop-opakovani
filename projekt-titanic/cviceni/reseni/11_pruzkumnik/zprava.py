# Řešení – krok 11: Titanic – zpráva
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from analyza import (
    SOUBOR,
    nacti_pasazery,
    najdi_sloupec,
    prehled_podle,
    pridej_jmena,
    sestav_zpravu,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_jmena(pasazeri)

for radek in sestav_zpravu(pasazeri):
    print(radek)

print()
print("Průzkumník: napiš název sloupce, třeba Sex nebo Titul.")
print("Prázdný řádek program ukončí.")
sloupce = list(pasazeri[0])

while True:
    text = input("Sloupec: ")
    if text.strip() == "":
        break
    nazev = najdi_sloupec(text, sloupce)
    if nazev is None:
        print(f"Takový sloupec neznám. Vyber si z těchhle: {', '.join(sloupce)}")
    else:
        radky = prehled_podle(pasazeri, nazev)
        if len(radky) > 20:
            print(f"Sloupec {nazev} má {len(radky)} různých hodnot, to je na přehled moc.")
        else:
            for radek in radky:
                print(radek)
