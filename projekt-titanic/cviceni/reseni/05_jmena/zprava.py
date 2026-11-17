# Řešení kroku 5 – Co prozradí jména?
# Tvoje řešení může vypadat jinak, a to je v pořádku.

import analyza

pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))
analyza.pridej_jmena(pasazeri)

bez_veku = 0
for pasazer in pasazeri:
    if pasazer["Age"] is None:
        bez_veku = bez_veku + 1

print(f"Pasažérů: {len(pasazeri)}")
print(f"Bez věku: {bez_veku}")

stary = analyza.nejstarsi(pasazeri)
mlady = analyza.nejmladsi(pasazeri)

print(f"Průměrný věk: {analyza.prumerny_vek(pasazeri):.1f}")
print(f"Nejstarší: {stary['Name']}, věk {stary['Age']}")
print(f"Nejmladší: {mlady['Name']}, věk {mlady['Age']}")

for trida in [1, 2, 3]:
    cena = analyza.prumerna_cena(analyza.filtruj(pasazeri, "Pclass", trida))
    print(f"{trida}. třída: průměrně {cena:.1f} liber")

nejvyssi = analyza.nejdrazsi_listek(pasazeri)
print(f"Nejdražší lístek: {nejvyssi} liber")
for pasazer in analyza.filtruj(pasazeri, "Fare", nejvyssi):
    print(f"  {pasazer['Name']}, lístek {pasazer['Ticket']}")

print(f"Zadarmo: {len(analyza.filtruj(pasazeri, 'Fare', 0))} lidí")

print("Tituly:")
tituly = analyza.pocty(pasazeri, "Titul")
for nazev in tituly:
    print(f"  {nazev}: {tituly[nazev]}")

print("Nejčastější mužská jména:")
jmena = analyza.pocty(analyza.filtruj(pasazeri, "Sex", "male"), "Krestni")
for jmeno in jmena:
    if jmena[jmeno] >= 10:
        print(f"  {jmeno}: {jmena[jmeno]}")
