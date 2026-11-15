# Řešení bonusu 1 – Zpráva v souboru
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from analyza import (
    SLOZKA,
    SOUBOR,
    nacti_pasazery,
    pridej_jmena,
    pridej_rodiny,
    sestav_zpravu,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_jmena(pasazeri)
pridej_rodiny(pasazeri)

with open(SLOZKA / "zprava.txt", "w", encoding="utf-8") as f:
    for radek in sestav_zpravu(pasazeri):
        f.write(f"{radek}\n")

print("Zpráva je v souboru zprava.txt.")
