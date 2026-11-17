# Řešení kroku 4 – Barvy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import randrange

import logika
from pomocnik import nacti_radky, obarvi

BARVY_POLI = {"spravne": "zelena", "jinde": "zluta", "neni": "seda"}


def vypis_pokusy(pokusy):
    print()
    for hadane, vysledek in pokusy:
        radek = ""
        for i in range(logika.DELKA_SLOVA):
            pole = f" {hadane[i].upper()} "
            radek = radek + obarvi(pole, BARVY_POLI[vysledek[i]]) + " "
        print(radek)
    print()


def nacti_slovo(povolena):
    while True:
        slovo = logika.uprav_vstup(input("Tvůj pokus: "))
        chyba = logika.chyba_slova(slovo, povolena)
        if chyba == "":
            return slovo
        print(chyba)


def zahraj(tajne, povolena):
    pokusy = []

    for pokus in range(1, logika.POCET_POKUSU + 1):
        hadane = nacti_slovo(povolena)
        pokusy.append((hadane, logika.vyhodnot(hadane, tajne)))
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
    if logika.uprav_vstup(input("Hrát znovu? (ano/ne) ")) != "ano":
        break
