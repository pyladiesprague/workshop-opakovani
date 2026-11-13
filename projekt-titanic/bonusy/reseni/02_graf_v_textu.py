# Bonus 2: graf v textu

from analyza import SOUBOR, TRIDY, nacti_pasazery, prezivani_podle, uprav_pasazery

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
miry = prezivani_podle(pasazeri, "Pclass")

for trida in TRIDY:
    sloupec = "█" * round(miry[trida] / 2)
    print(f"{TRIDY[trida]:10}{sloupec} {miry[trida]:.1f} %")
