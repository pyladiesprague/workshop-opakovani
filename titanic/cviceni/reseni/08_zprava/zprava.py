# Zpráva o pasažérech Titaniku. Spusť tlačítkem Run.

from analyza import (
    SOUBOR,
    nacti_pasazery,
    pridej_skupiny,
    sestav_zpravu,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_skupiny(pasazeri)

for radek in sestav_zpravu(pasazeri):
    print(radek)
