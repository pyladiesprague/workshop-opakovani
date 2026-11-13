# Zpráva o pasažérech Titaniku. Spusť tlačítkem Run.

from analyza import SOUBOR, nacti_pasazery, prezivani_podle_dvou, uprav_pasazery

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

miry = prezivani_podle_dvou(pasazeri, "Pclass", "Sex")
for klic in miry:
    print(f"{klic}: {miry[klic]:.1f} %")

print(f"Žena ve 3. třídě: {miry[(3, 'female')]:.1f} %")
print(f"Muž v 1. třídě: {miry[(1, 'male')]:.1f} %")
print(f"Žena v 1. třídě: {miry[(1, 'female')]:.1f} %")
