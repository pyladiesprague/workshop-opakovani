# Řešení kroku 1 – Jeden pokus
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from logika import vyhodnot

ZNACKY = {"spravne": "+", "jinde": "?", "neni": "-"}


def vypis_pokus(hadane, vysledek):
    pismena = ""
    znacky = ""
    for i in range(len(hadane)):
        pismena = pismena + hadane[i] + " "
        znacky = znacky + ZNACKY[vysledek[i]] + " "
    print(pismena)
    print(znacky)


tajne = "kočka"
hadane = input("Tvůj pokus: ")
vypis_pokus(hadane, vyhodnot(hadane, tajne))
