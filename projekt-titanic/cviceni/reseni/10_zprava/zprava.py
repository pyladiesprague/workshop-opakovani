# Řešení kroku 10 – Titanic v číslech
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import analyza

pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))
analyza.pridej_jmena(pasazeri)

for radek in analyza.sestav_zpravu(pasazeri):
    print(radek)
