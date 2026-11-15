# Řešení – krok 2: Titanic – zpráva
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from analyza import SOUBOR, nacti_pasazery, uprav_pasazery

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

bez_veku = 0
for pasazer in pasazeri:
    if pasazer["Age"] is None:
        bez_veku = bez_veku + 1

print(f"Pasažérů: {len(pasazeri)}")
print(f"Bez věku: {bez_veku}")
