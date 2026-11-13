# Bonus 4: rodiny

from analyza import (
    SOUBOR,
    nacti_pasazery,
    pocet_prezivsich,
    rozdel_podle,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

for pasazer in pasazeri:
    pasazer["Prijmeni"] = pasazer["Name"].split(",")[0]

rodiny = rozdel_podle(pasazeri, "Prijmeni")

for prijmeni in rodiny:
    if len(rodiny[prijmeni]) >= 6:
        prezili = pocet_prezivsich(rodiny[prijmeni])
        print(f"{prijmeni}: {len(rodiny[prijmeni])} lidí, přežilo {prezili}")
