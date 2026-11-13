# Wordle: hraj tlačítkem Run.

from random import randrange

from logika import DELKA_SLOVA, POCET_POKUSU, chyba_slova, uprav_vstup, vyhodnot
from pomocnik import nacti_radky, obarvi

BARVY_POLI = {"spravne": "zelena", "jinde": "zluta", "neni": "seda"}


def vypis_pokusy(pokusy):
    print()
    for hadane, vysledek in pokusy:
        radek = ""
        for i in range(DELKA_SLOVA):
            pole = f" {hadane[i].upper()} "
            radek = radek + obarvi(pole, BARVY_POLI[vysledek[i]]) + " "
        print(radek)
    print()


def nacti_slovo(povolena):
    while True:
        slovo = uprav_vstup(input("Tvůj pokus: "))
        chyba = chyba_slova(slovo, povolena)
        if chyba == "":
            return slovo
        print(chyba)


def zahraj(tajne, povolena):
    pokusy = []

    for pokus in range(1, POCET_POKUSU + 1):
        hadane = nacti_slovo(povolena)
        pokusy.append((hadane, vyhodnot(hadane, tajne)))
        vypis_pokusy(pokusy)

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
