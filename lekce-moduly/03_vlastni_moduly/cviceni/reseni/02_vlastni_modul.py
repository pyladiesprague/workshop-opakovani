# Řešení cvičení 2 – Vlastní modul od nuly
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# 1. Ve složce cviceni vytvoř soubor texty.py se dvěma funkcemi:
#
#    ramecek(text)   vrátí text v rámečku z hvězdiček, tři řádky:
#
#                    ************
#                    * Ahoj Evo *
#                    ************
#
#                    (řádky spoj znakem nového řádku "\n")
#
#    kricet(text)    vrátí text velkými písmeny a s vykřičníkem na konci:
#                    kricet("ahoj") vrátí "AHOJ!"
#
#    Funkce text vrací (return), nevypisují ho.
#
# 2. Tady se zeptej na jméno a vypiš pozdrav v rámečku a pak ho
#    vypiš ještě jednou nakřičený. Funkce si vezmi z texty.py.

# Funkce jsou v souboru texty.py vedle tohohle.

import texty

jmeno = input("Jak se jmenuješ? ")
pozdrav = f"Ahoj {jmeno}"

print(texty.ramecek(pozdrav))
print(texty.kricet(pozdrav))
