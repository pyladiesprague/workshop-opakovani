# Bonus 2: lepší řešič

from logika import filtruj, vyhodnot
from pomocnik import nacti_radky


def prumerny_zbytek(kandidat, mozna):
    pocty = {}
    for tajne in mozna:
        klic = tuple(vyhodnot(kandidat, tajne))
        if klic in pocty:
            pocty[klic] = pocty[klic] + 1
        else:
            pocty[klic] = 1

    soucet = 0
    for klic in pocty:
        soucet = soucet + pocty[klic] * pocty[klic]
    return soucet / len(mozna)


def nejlepsi_slovo(mozna):
    nejlepsi = mozna[0]
    nejlepsi_zbytek = prumerny_zbytek(nejlepsi, mozna)
    for slovo in mozna:
        zbytek = prumerny_zbytek(slovo, mozna)
        if zbytek < nejlepsi_zbytek:
            nejlepsi = slovo
            nejlepsi_zbytek = zbytek
    return nejlepsi


def odehraj(tajne, hadana, prvni_slovo):
    mozna = hadana
    hadane = prvni_slovo
    pokus = 1
    while hadane != tajne:
        mozna = filtruj(mozna, hadane, vyhodnot(hadane, tajne))
        hadane = nejlepsi_slovo(mozna)
        pokus = pokus + 1
    return pokus


hadana = nacti_radky("hadana_slova.txt")
prvni_slovo = nejlepsi_slovo(hadana)
soucet = 0
nejhorsi = hadana[0]
nejvic = 0
prohry = 0

for tajne in hadana:
    pokusu = odehraj(tajne, hadana, prvni_slovo)
    soucet = soucet + pokusu
    if pokusu > nejvic:
        nejvic = pokusu
        nejhorsi = tajne
    if pokusu > 6:
        prohry = prohry + 1

print(f"První slovo: {prvni_slovo}")
print(f"Průměr: {soucet / len(hadana):.2f} pokusu")
print(f"Nejhorší slovo: {nejhorsi} ({nejvic} pokusů)")
print(f"Víc než šest pokusů: {prohry}")
