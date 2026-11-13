# Bonus 5: podivné ceny

from analyza import SOUBOR, nacti_pasazery, uprav_pasazery

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

print("Lístek zdarma:")
for pasazer in pasazeri:
    if pasazer["Fare"] == 0:
        print(f"  {pasazer['Name']}, třída {pasazer['Pclass']}, lístek {pasazer['Ticket']}")

print("Nejdražší lístky:")
for pasazer in pasazeri:
    if pasazer["Fare"] > 500:
        print(f"  {pasazer['Name']}, lístek {pasazer['Ticket']}, {pasazer['Fare']} liber")
