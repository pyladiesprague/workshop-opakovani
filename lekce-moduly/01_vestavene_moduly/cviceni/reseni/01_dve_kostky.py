# Řešení cvičení 1 – Dvě kostky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Hoď dvěma kostkami (každá má čísla 1 až 6) a vypiš obě čísla
#    i jejich součet. Použij randrange z modulu random.
#    Ukázka výstupu:
#
#    Padlo 3 a 5, dohromady 8.

from random import randrange

prvni = randrange(1, 7)
druha = randrange(1, 7)
print(f"Padlo {prvni} a {druha}, dohromady {prvni + druha}.")
