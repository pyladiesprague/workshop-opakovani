# Zpráva o pasažérech Titaniku. Spusť tlačítkem Run.

import analyza

#@ 1
pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)

print(f"Pasažérů: {len(pasazeri)}")
print(f"Sloupce: {list(pasazeri[0])}")
print(pasazeri[0])
#@ 2+
pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))
#@ 5+
analyza.pridej_jmena(pasazeri)
#@ 12+
analyza.pridej_rodiny(pasazeri)
#@ 2-9

bez_veku = 0
for pasazer in pasazeri:
    if pasazer["Age"] is None:
        bez_veku = bez_veku + 1

print(f"Pasažérů: {len(pasazeri)}")
print(f"Bez věku: {bez_veku}")
#@ 3-9

stary = analyza.nejstarsi(pasazeri)
mlady = analyza.nejmladsi(pasazeri)

print(f"Průměrný věk: {analyza.prumerny_vek(pasazeri):.1f}")
print(f"Nejstarší: {stary['Name']}, věk {stary['Age']}")
print(f"Nejmladší: {mlady['Name']}, věk {mlady['Age']}")
#@ 4-9

for trida in [1, 2, 3]:
    cena = analyza.prumerna_cena(analyza.filtruj(pasazeri, "Pclass", trida))
    print(f"{trida}. třída: průměrně {cena:.1f} liber")

nejvyssi = analyza.nejdrazsi_listek(pasazeri)
print(f"Nejdražší lístek: {nejvyssi} liber")
for pasazer in analyza.filtruj(pasazeri, "Fare", nejvyssi):
    print(f"  {pasazer['Name']}, lístek {pasazer['Ticket']}")

print(f"Zadarmo: {len(analyza.filtruj(pasazeri, 'Fare', 0))} lidí")
#@ 5-9

print("Tituly:")
tituly = analyza.pocty(pasazeri, "Titul")
for nazev in tituly:
    print(f"  {nazev}: {tituly[nazev]}")

print("Nejčastější mužská jména:")
jmena = analyza.pocty(analyza.filtruj(pasazeri, "Sex", "male"), "Krestni")
for jmeno in jmena:
    if jmena[jmeno] >= 10:
        print(f"  {jmeno}: {jmena[jmeno]}")
#@ 6-9

zeny = analyza.filtruj(pasazeri, "Sex", "female")
muzi = analyza.filtruj(pasazeri, "Sex", "male")

print(f"Přežilo: {analyza.pocet_prezivsich(pasazeri)} z {len(pasazeri)}")
print(f"To je {analyza.mira_preziti(pasazeri):.1f} %")
print(f"Ženy: {analyza.mira_preziti(zeny):.1f} %")
print(f"Muži: {analyza.mira_preziti(muzi):.1f} %")
for trida in [1, 2, 3]:
    ve_tride = analyza.filtruj(pasazeri, "Pclass", trida)
    print(f"{trida}. třída: {analyza.mira_preziti(ve_tride):.1f} %")
#@ 7-9

skupiny = analyza.rozdel_podle(pasazeri, "Embarked")
miry = analyza.miry_skupin(skupiny)
for pristav in skupiny:
    lidi = skupiny[pristav]
    prvni_trida = len(analyza.filtruj(lidi, "Pclass", 1)) / len(lidi) * 100
    print(f"{pristav}: přežilo {miry[pristav]:.1f} %  ({len(lidi)} lidí, v 1. třídě {prvni_trida:.0f} %)")
#@ 8-9

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
#@ 9

for radek in analyza.graf("Přežití podle třídy", analyza.rozdel_podle(pasazeri, "Pclass"), analyza.TRIDY):
    print(radek)
for radek in analyza.graf("Přežití podle pohlaví", analyza.rozdel_podle(pasazeri, "Sex"), analyza.POHLAVI):
    print(radek)
for radek in analyza.graf("Přežití podle přístavu", analyza.rozdel_podle(pasazeri, "Embarked"), analyza.PRISTAVY):
    print(radek)
#@ 10+

for radek in analyza.sestav_zpravu(pasazeri):
    print(radek)
#@ 11+

print()
print("Průzkumník: napiš název sloupce, třeba Sex nebo Titul.")
print("Prázdný řádek program ukončí.")
sloupce = list(pasazeri[0])

while True:
    text = input("Sloupec: ")
    if text.strip() == "":
        break
    nazev = analyza.najdi_sloupec(text, sloupce)
    if nazev is None:
        print(f"Takový sloupec neznám. Vyber si z těchhle: {', '.join(sloupce)}")
    else:
        radky = analyza.prehled_podle(pasazeri, nazev)
        if len(radky) > 20:
            print(f"Sloupec {nazev} má {len(radky)} různých hodnot, to je na přehled moc.")
        else:
            for radek in radky:
                print(radek)
