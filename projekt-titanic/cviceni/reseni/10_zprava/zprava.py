# Řešení – krok 10: Titanic – zpráva
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from analyza import SOUBOR, nacti_pasazery, pridej_jmena, sestav_zpravu, uprav_pasazery

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_jmena(pasazeri)

for radek in sestav_zpravu(pasazeri):
    print(radek)
