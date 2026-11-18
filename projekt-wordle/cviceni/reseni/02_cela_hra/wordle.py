# Řešení kroku 2 – Celá hra
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import logika


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
        slovo = logika.uprav_vstup(input("Tvůj pokus: "))
        chyba = logika.chyba_slova(slovo)
        if chyba == "":
            return slovo
        print(chyba)


def zahraj(tajne):
    for pokus in range(1, logika.POCET_POKUSU + 1):
        hadane = nacti_slovo()
        vypis_pokus(hadane, logika.vyhodnot(hadane, tajne))
        if hadane == tajne:
            print(f"Uhodla jsi to na {pokus}. pokus!")
            return
    print(f"Došly pokusy. Tajné slovo bylo {tajne}.")


zahraj("kočka")
