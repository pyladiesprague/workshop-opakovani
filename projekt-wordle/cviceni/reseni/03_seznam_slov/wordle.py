# Wordle: hraj tlačítkem Run.

from random import randrange

from logika import POCET_POKUSU, chyba_slova, uprav_vstup, vyhodnot
from pomocnik import nacti_radky

ZNACKY = {"spravne": "+", "jinde": "?", "neni": "-"}


def vypis_pokus(hadane, vysledek):
    pismena = ""
    znacky = ""
    for i in range(len(hadane)):
        pismena = pismena + hadane[i] + " "
        znacky = znacky + ZNACKY[vysledek[i]] + " "
    print(pismena)
    print(znacky)


def nacti_slovo(povolena):
    while True:
        slovo = uprav_vstup(input("Tvůj pokus: "))
        chyba = chyba_slova(slovo, povolena)
        if chyba == "":
            return slovo
        print(chyba)


def zahraj(tajne, povolena):
    for pokus in range(1, POCET_POKUSU + 1):
        hadane = nacti_slovo(povolena)
        vypis_pokus(hadane, vyhodnot(hadane, tajne))
        if hadane == tajne:
            print(f"Uhodla jsi to na {pokus}. pokus!")
            return
    print(f"Došly pokusy. Tajné slovo bylo {tajne}.")


hadana = nacti_radky("hadana_slova.txt")
povolena = nacti_radky("povolena_slova.txt")

while True:
    tajne = hadana[randrange(len(hadana))]
    zahraj(tajne, povolena)
    if uprav_vstup(input("Hrát znovu? (ano/ne) ")) != "ano":
        break
