# Řešení kroku 7 – Záleželo na tom, kde kdo nastoupil?
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from analyza import (
    SOUBOR,
    filtruj,
    mira_preziti,
    miry_skupin,
    nacti_pasazery,
    nejdrazsi_listek,
    nejmladsi,
    nejstarsi,
    pocet_prezivsich,
    pocty,
    pridej_jmena,
    prumerna_cena,
    prumerny_vek,
    rozdel_podle,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))
pridej_jmena(pasazeri)

bez_veku = 0
for pasazer in pasazeri:
    if pasazer["Age"] is None:
        bez_veku = bez_veku + 1

print(f"Pasažérů: {len(pasazeri)}")
print(f"Bez věku: {bez_veku}")

stary = nejstarsi(pasazeri)
mlady = nejmladsi(pasazeri)

print(f"Průměrný věk: {prumerny_vek(pasazeri):.1f}")
print(f"Nejstarší: {stary['Name']}, věk {stary['Age']}")
print(f"Nejmladší: {mlady['Name']}, věk {mlady['Age']}")

for trida in [1, 2, 3]:
    cena = prumerna_cena(filtruj(pasazeri, "Pclass", trida))
    print(f"{trida}. třída: průměrně {cena:.1f} liber")

nejvyssi = nejdrazsi_listek(pasazeri)
print(f"Nejdražší lístek: {nejvyssi} liber")
for pasazer in filtruj(pasazeri, "Fare", nejvyssi):
    print(f"  {pasazer['Name']}, lístek {pasazer['Ticket']}")

print(f"Zadarmo: {len(filtruj(pasazeri, 'Fare', 0))} lidí")

print("Tituly:")
tituly = pocty(pasazeri, "Titul")
for nazev in tituly:
    print(f"  {nazev}: {tituly[nazev]}")

print("Nejčastější mužská jména:")
jmena = pocty(filtruj(pasazeri, "Sex", "male"), "Krestni")
for jmeno in jmena:
    if jmena[jmeno] >= 10:
        print(f"  {jmeno}: {jmena[jmeno]}")

zeny = filtruj(pasazeri, "Sex", "female")
muzi = filtruj(pasazeri, "Sex", "male")

print(f"Přežilo: {pocet_prezivsich(pasazeri)} z {len(pasazeri)}")
print(f"To je {mira_preziti(pasazeri):.1f} %")
print(f"Ženy: {mira_preziti(zeny):.1f} %")
print(f"Muži: {mira_preziti(muzi):.1f} %")
for trida in [1, 2, 3]:
    ve_tride = filtruj(pasazeri, "Pclass", trida)
    print(f"{trida}. třída: {mira_preziti(ve_tride):.1f} %")

skupiny = rozdel_podle(pasazeri, "Embarked")
miry = miry_skupin(skupiny)
for pristav in skupiny:
    lidi = skupiny[pristav]
    prvni_trida = len(filtruj(lidi, "Pclass", 1)) / len(lidi) * 100
    print(f"{pristav}: přežilo {miry[pristav]:.1f} %  ({len(lidi)} lidí, v 1. třídě {prvni_trida:.0f} %)")
