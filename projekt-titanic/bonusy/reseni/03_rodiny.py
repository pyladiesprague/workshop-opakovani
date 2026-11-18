# Řešení bonusu 3 – Rodiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import analyza

pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))

for pasazer in pasazeri:
    pasazer["Prijmeni"] = pasazer["Name"].split(",")[0]

rodiny = analyza.rozdel_podle(pasazeri, "Prijmeni")

for prijmeni in rodiny:
    if len(rodiny[prijmeni]) >= 6:
        prezili = analyza.pocet_prezivsich(rodiny[prijmeni])
        print(f"{prijmeni}: {len(rodiny[prijmeni])} lidí, přežilo {prezili}")
