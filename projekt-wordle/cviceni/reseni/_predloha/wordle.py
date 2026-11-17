# Wordle: hraj tlačítkem Run.
#@ 7
# Místo slova můžeš napsat ? a program ukáže, která slova zbývají.
#@ 8+
# Místo slova můžeš napsat ? (která slova zbývají) nebo ! (rada řešiče).
#@ vse

#@ 3+
from random import randrange

#@ vse
import logika
#@ importy

#@ 1-3
ZNACKY = {"spravne": "+", "jinde": "?", "neni": "-"}
#@ 4+
BARVY_POLI = {"spravne": "zelena", "jinde": "zluta", "neni": "seda"}
#@ 5+
BARVY_KLAVES = {"spravne": "zelena", "jinde": "zluta", "neni": "tlumena"}
KLAVESNICE = ["ěščřžýáíé", "qwertzuiopú", "asdfghjklů", "yxcvbnmďťňó"]
#@ 9+
SOUBOR_STATISTIK = "statistiky.txt"
#@ vse


#@ 1-3
def vypis_pokus(hadane, vysledek):
    pismena = ""
    znacky = ""
    for i in range(len(hadane)):
        pismena = pismena + hadane[i] + " "
        znacky = znacky + ZNACKY[vysledek[i]] + " "
    print(pismena)
    print(znacky)


#@ 4-9
def vypis_pokusy(pokusy):
    print()
    for hadane, vysledek in pokusy:
        radek = ""
        for i in range(logika.DELKA_SLOVA):
            pole = f" {hadane[i].upper()} "
            radek = radek + obarvi(pole, BARVY_POLI[vysledek[i]]) + " "
        print(radek)
    print()


#@ 10+
def vypis_hraci_plochu(pokusy):
    for hadane, vysledek in pokusy:
        radek = ""
        for i in range(logika.DELKA_SLOVA):
            pole = f" {hadane[i].upper()} "
            radek = radek + obarvi(pole, BARVY_POLI[vysledek[i]]) + " "
        print(f"{' ' * 12}{radek}")

    for i in range(logika.POCET_POKUSU - len(pokusy)):
        print(f"{' ' * 12}{obarvi(' ·  ' * logika.DELKA_SLOVA, 'tlumena')}")


#@ 5-9
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


#@ 10+
def vypis_klavesnici(pismena):
    for radek_klaves in KLAVESNICE:
        radek = ""
        for pismeno in radek_klaves:
            klavesa = f" {pismeno.upper()} "
            if pismeno in pismena:
                klavesa = obarvi(klavesa, BARVY_KLAVES[pismena[pismeno]])
            radek = radek + klavesa + " "
        odsazeni = (44 - len(radek_klaves) * 4) // 2
        print(f"{' ' * odsazeni}{radek}")


def vykresli(pokusy, pismena, zprava):
    vycisti_obrazovku()
    vypis_hraci_plochu(pokusy)
    print()
    vypis_klavesnici(pismena)
    print()
    print(f"  {zprava}")
    print()


#@ 7-9
def text_napovedy(mozna):
    return f"Zbývá slov: {len(mozna)}\n{', '.join(mozna[:10])}"


#@ 10+
def text_napovedy(mozna):
    return f"Zbývá slov: {len(mozna)}\n  {', '.join(mozna[:10])}"


#@ 2
def nacti_slovo():
    while True:
        slovo = logika.uprav_vstup(input("Tvůj pokus: "))
        chyba = logika.chyba_slova(slovo)
        if chyba == "":
            return slovo
        print(chyba)


#@ 3-6
def nacti_slovo(povolena):
    while True:
        slovo = logika.uprav_vstup(input("Tvůj pokus: "))
        chyba = logika.chyba_slova(slovo, povolena)
        if chyba == "":
            return slovo
        print(chyba)


#@ 7
def nacti_slovo(povolena, mozna):
    while True:
        slovo = logika.uprav_vstup(input("Tvůj pokus: "))
        if slovo == "?":
            print(text_napovedy(mozna))
        else:
            chyba = logika.chyba_slova(slovo, povolena)
            if chyba == "":
                return slovo
            print(chyba)


#@ 8-9
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


#@ 10+
def nacti_slovo(pokusy, pismena, povolena, mozna):
    zprava = obarvi("? = nápověda   ! = rada", "tlumena")
    while True:
        vykresli(pokusy, pismena, zprava)
        slovo = logika.uprav_vstup(input("  Tvůj pokus: "))
        if slovo == "?":
            zprava = text_napovedy(mozna)
        elif slovo == "!":
            zprava = f"Zkus: {logika.nejlepsi_slovo(mozna).upper()}"
        else:
            zprava = logika.chyba_slova(slovo, povolena)
            if zprava == "":
                return slovo


#@ 9
def vypis_statistiky():
    statistiky = logika.spocitej_statistiky(nacti_radky(SOUBOR_STATISTIK))
    print(f"Her: {statistiky['her']}   Úspěšnost: {round(statistiky['uspesnost'])} %")

    radek = "Pokusy:"
    for pokus in statistiky["pokusy"]:
        radek = radek + f"  {pokus}: {statistiky['pokusy'][pokus]}"
    print(radek)
    print()


#@ 10+
def vypis_statistiky():
    statistiky = logika.spocitej_statistiky(nacti_radky(SOUBOR_STATISTIK))
    print(f"  Her: {statistiky['her']}   Úspěšnost: {round(statistiky['uspesnost'])} %")

    radek = "  Pokusy:"
    for pokus in statistiky["pokusy"]:
        radek = radek + f"  {pokus}: {statistiky['pokusy'][pokus]}"
    print(radek)
    print()


#@ 2
def zahraj(tajne):
    for pokus in range(1, logika.POCET_POKUSU + 1):
        hadane = nacti_slovo()
        vypis_pokus(hadane, logika.vyhodnot(hadane, tajne))
        if hadane == tajne:
            print(f"Uhodla jsi to na {pokus}. pokus!")
            return
    print(f"Došly pokusy. Tajné slovo bylo {tajne}.")


#@ 3
def zahraj(tajne, povolena):
    for pokus in range(1, logika.POCET_POKUSU + 1):
        hadane = nacti_slovo(povolena)
        vypis_pokus(hadane, logika.vyhodnot(hadane, tajne))
        if hadane == tajne:
            print(f"Uhodla jsi to na {pokus}. pokus!")
            return
    print(f"Došly pokusy. Tajné slovo bylo {tajne}.")


#@ 4
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


#@ 5-6
def zahraj(tajne, povolena):
    pismena = {}
    pokusy = []

    for pokus in range(1, logika.POCET_POKUSU + 1):
        vypis_klavesnici(pismena)
        hadane = nacti_slovo(povolena)
        vysledek = logika.vyhodnot(hadane, tajne)
        pokusy.append((hadane, vysledek))
        logika.aktualizuj_pismena(pismena, hadane, vysledek)
        vypis_pokusy(pokusy)

        if hadane == tajne:
            print(f"Uhodla jsi to na {pokus}. pokus!")
            return
    print(f"Došly pokusy. Tajné slovo bylo {tajne}.")


#@ 7-8
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
            return
    print(f"Došly pokusy. Tajné slovo bylo {tajne}.")


#@ 9
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


#@ 10+
def zahraj(tajne, povolena, hadana):
    pismena = {}
    pokusy = []
    mozna = hadana

    for pokus in range(1, logika.POCET_POKUSU + 1):
        hadane = nacti_slovo(pokusy, pismena, povolena, mozna)
        vysledek = logika.vyhodnot(hadane, tajne)
        pokusy.append((hadane, vysledek))
        logika.aktualizuj_pismena(pismena, hadane, vysledek)
        mozna = logika.filtruj(mozna, hadane, vysledek)

        if hadane == tajne:
            vykresli(pokusy, pismena, f"Uhodla jsi to na {pokus}. pokus!")
            return pokus

    vykresli(pokusy, pismena, f"Došly pokusy. Tajné slovo bylo {tajne.upper()}.")
    return 0


#@ 1
tajne = "kočka"
hadane = input("Tvůj pokus: ")
vypis_pokus(hadane, logika.vyhodnot(hadane, tajne))
#@ 2
zahraj("kočka")
#@ 3+
hadana = nacti_radky("hadana_slova.txt")
povolena = nacti_radky("povolena_slova.txt")

while True:
    tajne = hadana[randrange(len(hadana))]
#@ 3-6
    zahraj(tajne, povolena)
#@ 7-8
    zahraj(tajne, povolena, hadana)
#@ 9+
    pokusu = zahraj(tajne, povolena, hadana)
    pridej_radek(SOUBOR_STATISTIK, pokusu)
    vypis_statistiky()
#@ 3-9
    if logika.uprav_vstup(input("Hrát znovu? (ano/ne) ")) != "ano":
        break
#@ 10+
    if logika.uprav_vstup(input("  Hrát znovu? (ano/ne) ")) != "ano":
        break
