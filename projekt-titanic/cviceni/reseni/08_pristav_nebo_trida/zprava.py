# Řešení kroku 8 – Přístav, nebo třída?
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
    print(f"{trida}. třída: průměrně {cena:.1f} libry")

nejvyssi = analyza.nejdrazsi_listek(pasazeri)
print(f"Nejdražší lístek: {nejvyssi:.1f} libry")
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

zeny = analyza.filtruj(pasazeri, "Sex", "female")
muzi = analyza.filtruj(pasazeri, "Sex", "male")

print(f"Přežilo: {analyza.pocet_prezivsich(pasazeri)} z {len(pasazeri)}")
print(f"To je {analyza.mira_preziti(pasazeri):.1f} %")
print(f"Ženy: {analyza.mira_preziti(zeny):.1f} %")
print(f"Muži: {analyza.mira_preziti(muzi):.1f} %")
for trida in [1, 2, 3]:
    ve_tride = analyza.filtruj(pasazeri, "Pclass", trida)
    print(f"{trida}. třída: {analyza.mira_preziti(ve_tride):.1f} %")

skupiny = analyza.rozdel_podle(pasazeri, "Embarked")
miry = analyza.miry_skupin(skupiny)
for pristav in skupiny:
    lidi = skupiny[pristav]
    prvni_trida = len(analyza.filtruj(lidi, "Pclass", 1)) / len(lidi) * 100
    print(f"{pristav}: přežilo {miry[pristav]:.1f} %  ({len(lidi)} lidí, v 1. třídě {prvni_trida:.0f} %)")

miry = analyza.prezivani_podle_dvou(pasazeri, "Embarked", "Pclass")
skupiny = analyza.rozdel_podle_dvou(pasazeri, "Embarked", "Pclass")
for trida in [1, 2, 3]:
    for pristav in ["C", "S", "Q"]:
        klic = (pristav, trida)
        print(f"{trida}. třída, {pristav}: {miry[klic]:.1f} %  ({len(skupiny[klic])})")

print()
miry = analyza.prezivani_podle_dvou(pasazeri, "Pclass", "Sex")
for klic in miry:
    print(f"{klic}: {miry[klic]:.1f} %")
