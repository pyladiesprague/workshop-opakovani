# Řešení kroku 1 – Co v souboru vlastně je?
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import analyza

pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)

print(f"Pasažérů: {len(pasazeri)}")
print(f"Sloupce: {list(pasazeri[0])}")
print(pasazeri[0])
