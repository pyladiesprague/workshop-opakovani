# Zpráva o pasažérech Titaniku. Spusť tlačítkem Run.

from analyza import SOUBOR, filtruj, mira_preziti, nacti_pasazery, uprav_pasazery

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

zeny = filtruj(pasazeri, "Sex", "female")
muzi = filtruj(pasazeri, "Sex", "male")

print(f"Ženy: {mira_preziti(zeny):.1f} %")
print(f"Muži: {mira_preziti(muzi):.1f} %")
