# Řešení cvičení 2 – Kdo myje nádobí
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Máš seznam lidí z bytu. Vylosuj, kdo dnes myje nádobí,
#    a vypiš to. Pomůže ti funkce choice z modulu random.

from random import choice

lide = ["Anna", "Petra", "Jana", "Eva"]

print(f"Nádobí dnes myje {choice(lide)}.")
