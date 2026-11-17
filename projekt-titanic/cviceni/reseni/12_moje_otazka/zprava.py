# Řešení kroku 12 – Co zajímá tebe?
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import analyza

pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))
analyza.pridej_jmena(pasazeri)
analyza.pridej_rodiny(pasazeri)

for radek in analyza.sestav_zpravu(pasazeri):
    print(radek)

print()
print("Průzkumník: napiš název sloupce, třeba Sex nebo Titul.")
print("Prázdný řádek program ukončí.")
sloupce = list(pasazeri[0])

while True:
    text = input("Sloupec: ")
    if text.strip() == "":
        break
    nazev = analyza.najdi_sloupec(text, sloupce)
    if nazev is None:
        print(f"Takový sloupec neznám. Vyber si z těchhle: {', '.join(sloupce)}")
    else:
        radky = analyza.prehled_podle(pasazeri, nazev)
        if len(radky) > 20:
            print(f"Sloupec {nazev} má {len(radky)} různých hodnot, to je na přehled moc.")
        else:
            for radek in radky:
                print(radek)
