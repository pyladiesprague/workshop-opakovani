# Wordle: hraj tlačítkem Run.

from logika import POCET_POKUSU, chyba_slova, uprav_vstup, vyhodnot

ZNACKY = {"spravne": "+", "jinde": "?", "neni": "-"}


def vypis_pokus(hadane, vysledek):
    pismena = ""
    znacky = ""
    for i in range(len(hadane)):
        pismena = pismena + hadane[i] + " "
        znacky = znacky + ZNACKY[vysledek[i]] + " "
    print(pismena)
    print(znacky)


def nacti_slovo():
    while True:
        slovo = uprav_vstup(input("Tvůj pokus: "))
        chyba = chyba_slova(slovo)
        if chyba == "":
            return slovo
        print(chyba)


def zahraj(tajne):
    for pokus in range(1, POCET_POKUSU + 1):
        hadane = nacti_slovo()
        vypis_pokus(hadane, vyhodnot(hadane, tajne))
        if hadane == tajne:
            print(f"Uhodla jsi to na {pokus}. pokus!")
            return
    print(f"Došly pokusy. Tajné slovo bylo {tajne}.")


zahraj("kočka")
