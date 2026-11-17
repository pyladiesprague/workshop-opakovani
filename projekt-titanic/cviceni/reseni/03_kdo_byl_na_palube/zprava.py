# Řešení kroku 3 – Kdo byl na palubě?
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import analyza

pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))

bez_veku = 0
for pasazer in pasazeri:
    if pasazer["Age"] is None:
        bez_veku = bez_veku + 1

print(f"Pasažérů: {len(pasazeri)}")
print(f"Bez věku: {bez_veku}")

stary = analyza.nejstarsi(pasazeri)
mlady = analyza.nejmladsi(pasazeri)

print(f"Průměrný věk: {analyza.prumerny_vek(pasazeri):.1f}")
print(f"Nejstarší: {stary['Name']}, věk {stary['Age']}")
print(f"Nejmladší: {mlady['Name']}, věk {mlady['Age']}")
