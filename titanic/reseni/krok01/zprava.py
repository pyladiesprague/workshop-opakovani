# Zpráva o pasažérech Titaniku. Spusť tlačítkem Run.

from analyza import SOUBOR, nacti_pasazery

pasazeri = nacti_pasazery(SOUBOR)

print(f"Pasažérů: {len(pasazeri)}")
print(f"Sloupce: {list(pasazeri[0])}")
print(pasazeri[0])
