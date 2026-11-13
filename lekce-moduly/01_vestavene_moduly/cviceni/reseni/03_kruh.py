# Řešení cvičení 3 – Kruh
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na poloměr kruhu a vypiš jeho obvod (2 · pí · r)
#    a obsah (pí · r · r), oba zaokrouhlené na dvě desetinná místa.
#    Tentokrát použij zápis import math a pí z modulu math.

import math

polomer = float(input("Poloměr kruhu: "))

obvod = 2 * math.pi * polomer
obsah = math.pi * polomer ** 2

print("Obvod:", round(obvod, 2))
print("Obsah:", round(obsah, 2))
