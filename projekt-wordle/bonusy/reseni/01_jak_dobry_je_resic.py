# Řešení bonusu 1 – Jak dobrý je řešič
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import logika
from pomocnik import nacti_radky


def odehraj(tajne, hadana):
    mozna = hadana
    pokus = 0
    while True:
        pokus = pokus + 1
        hadane = logika.nejlepsi_slovo(mozna)
        if hadane == tajne:
            return pokus
        mozna = logika.filtruj(mozna, hadane, logika.vyhodnot(hadane, tajne))


hadana = nacti_radky("hadana_slova.txt")
soucet = 0
nejhorsi = hadana[0]
nejvic = 0
prohry = 0

for tajne in hadana:
    pokusu = odehraj(tajne, hadana)
    soucet = soucet + pokusu
    if pokusu > nejvic:
        nejvic = pokusu
        nejhorsi = tajne
    if pokusu > 6:
        prohry = prohry + 1

print(f"První slovo: {logika.nejlepsi_slovo(hadana)}")
print(f"Průměr: {soucet / len(hadana):.2f} pokusu")
print(f"Nejhorší slovo: {nejhorsi} ({nejvic} pokusů)")
print(f"Víc než šest pokusů: {prohry}")
