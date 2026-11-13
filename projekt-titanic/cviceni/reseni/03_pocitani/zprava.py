# Zpráva o pasažérech Titaniku. Spusť tlačítkem Run.

from analyza import (
    SOUBOR,
    mira_preziti,
    nacti_pasazery,
    pocet_prezivsich,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

print(f"Pasažérů: {len(pasazeri)}")
print(f"Přežilo: {pocet_prezivsich(pasazeri)}")
print(f"To je {mira_preziti(pasazeri):.1f} %")
