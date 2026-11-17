# Řešení kroku 9 – Statistiky
# Tvoje řešení může vypadat jinak, a to je v pořádku.
# Místo slova můžeš napsat ? (která slova zbývají) nebo ! (rada řešiče).

from random import randrange

import logika
from pomocnik import nacti_radky, obarvi, pridej_radek

BARVY_POLI = {"spravne": "zelena", "jinde": "zluta", "neni": "seda"}
BARVY_KLAVES = {"spravne": "zelena", "jinde": "zluta", "neni": "tlumena"}
KLAVESNICE = ["ěščřžýáíé", "qwertzuiopú", "asdfghjklů", "yxcvbnmďťňó"]
SOUBOR_STATISTIK = "statistiky.txt"


def vypis_pokusy(pokusy):
    print()
    for hadane, vysledek in pokusy:
        radek = ""
        for i in range(logika.DELKA_SLOVA):
            pole = f" {hadane[i].upper()} "
            radek = radek + obarvi(pole, BARVY_POLI[vysledek[i]]) + " "
        print(radek)
    print()


def vypis_klavesnici(pismena):
    for radek_klaves in KLAVESNICE:
        radek = ""
        for pismeno in radek_klaves:
            klavesa = f" {pismeno.upper()} "
            if pismeno in pismena:
                klavesa = obarvi(klavesa, BARVY_KLAVES[pismena[pismeno]])
            radek = radek + klavesa + " "
        print(radek)
    print()


def text_napovedy(mozna):
    return f"Zbývá slov: {len(mozna)}\n{', '.join(mozna[:10])}"


def nacti_slovo(povolena, mozna):
    while True:
        slovo = logika.uprav_vstup(input("Tvůj pokus: "))
        if slovo == "?":
            print(text_napovedy(mozna))
        elif slovo == "!":
            print(f"Zkus: {logika.nejlepsi_slovo(mozna).upper()}")
        else:
            chyba = logika.chyba_slova(slovo, povolena)
            if chyba == "":
                return slovo
            print(chyba)


def vypis_statistiky():
    statistiky = logika.spocitej_statistiky(nacti_radky(SOUBOR_STATISTIK))
    print(f"Her: {statistiky['her']}   Úspěšnost: {round(statistiky['uspesnost'])} %")

    radek = "Pokusy:"
    for pokus in statistiky["pokusy"]:
        radek = radek + f"  {pokus}: {statistiky['pokusy'][pokus]}"
    print(radek)
    print()


def zahraj(tajne, povolena, hadana):
    pismena = {}
    pokusy = []
    mozna = hadana

    for pokus in range(1, logika.POCET_POKUSU + 1):
        vypis_klavesnici(pismena)
        hadane = nacti_slovo(povolena, mozna)
        vysledek = logika.vyhodnot(hadane, tajne)
        pokusy.append((hadane, vysledek))
        logika.aktualizuj_pismena(pismena, hadane, vysledek)
        mozna = logika.filtruj(mozna, hadane, vysledek)
        vypis_pokusy(pokusy)

        if hadane == tajne:
            print(f"Uhodla jsi to na {pokus}. pokus!")
            return pokus
    print(f"Došly pokusy. Tajné slovo bylo {tajne}.")
    return 0


hadana = nacti_radky("hadana_slova.txt")
povolena = nacti_radky("povolena_slova.txt")

while True:
    tajne = hadana[randrange(len(hadana))]
    pokusu = zahraj(tajne, povolena, hadana)
    pridej_radek(SOUBOR_STATISTIK, pokusu)
    vypis_statistiky()
    if logika.uprav_vstup(input("Hrát znovu? (ano/ne) ")) != "ano":
        break
