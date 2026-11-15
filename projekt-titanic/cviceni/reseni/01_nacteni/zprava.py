# Řešení – krok 1: Titanic – zpráva
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from analyza import SOUBOR, nacti_pasazery

pasazeri = nacti_pasazery(SOUBOR)

print(f"Pasažérů: {len(pasazeri)}")
print(f"Sloupce: {list(pasazeri[0])}")
print(pasazeri[0])
