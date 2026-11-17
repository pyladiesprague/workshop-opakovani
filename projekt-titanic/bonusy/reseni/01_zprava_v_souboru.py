# Řešení bonusu 1 – Zpráva v souboru
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import analyza

pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))
analyza.pridej_jmena(pasazeri)
analyza.pridej_rodiny(pasazeri)

with open(analyza.SLOZKA / "zprava.txt", "w", encoding="utf-8") as f:
    for radek in analyza.sestav_zpravu(pasazeri):
        f.write(f"{radek}\n")

print("Zpráva je v souboru zprava.txt.")
