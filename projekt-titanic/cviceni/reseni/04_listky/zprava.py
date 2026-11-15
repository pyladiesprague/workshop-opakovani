# Řešení – krok 4: Titanic – zpráva
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from analyza import (
    SOUBOR,
    filtruj,
    nacti_pasazery,
    nejdrazsi_listek,
    nejmladsi,
    nejstarsi,
    prumerna_cena,
    prumerny_vek,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

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
