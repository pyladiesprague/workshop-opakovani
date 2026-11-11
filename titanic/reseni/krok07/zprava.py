# Zpráva o pasažérech Titaniku. Spusť tlačítkem Run.

from analyza import (
    SOUBOR,
    filtruj,
    nacti_pasazery,
    prezivani_podle,
    pridej_skupiny,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_skupiny(pasazeri)

print("Podle věku:")
miry = prezivani_podle(pasazeri, "Skupina")
for skupina in miry:
    print(f"{skupina}: {miry[skupina]:.1f} %")

print("Dospělí podle pohlaví:")
dospeli = filtruj(pasazeri, "Skupina", "dospělý")
miry = prezivani_podle(dospeli, "Sex")
for pohlavi in miry:
    print(f"{pohlavi}: {miry[pohlavi]:.1f} %")

print("Děti podle třídy:")
deti = filtruj(pasazeri, "Skupina", "dítě")
miry = prezivani_podle(deti, "Pclass")
for trida in miry:
    print(f"{trida}: {miry[trida]:.1f} %  ({len(filtruj(deti, 'Pclass', trida))})")
