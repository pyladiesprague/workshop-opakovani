# Bonus 1: zpráva v souboru

from analyza import (
    SLOZKA,
    SOUBOR,
    nacti_pasazery,
    pridej_skupiny,
    sestav_zpravu,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_skupiny(pasazeri)

with open(SLOZKA / "zprava.txt", "w", encoding="utf-8") as f:
    for radek in sestav_zpravu(pasazeri):
        f.write(f"{radek}\n")

print("Zpráva je v souboru zprava.txt.")
