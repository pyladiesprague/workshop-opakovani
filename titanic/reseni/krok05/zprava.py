# Zpráva o pasažérech Titaniku. Spusť tlačítkem Run.

from analyza import SOUBOR, nacti_pasazery, prezivani_podle, uprav_pasazery

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

print("Podle třídy:")
miry = prezivani_podle(pasazeri, "Pclass")
for trida in miry:
    print(f"{trida}: {miry[trida]:.1f} %")

print("Podle pohlaví:")
miry = prezivani_podle(pasazeri, "Sex")
for pohlavi in miry:
    print(f"{pohlavi}: {miry[pohlavi]:.1f} %")
