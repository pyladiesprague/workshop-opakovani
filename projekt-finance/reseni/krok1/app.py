# Řešení – krok 1: Správce osobních financí – menu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from finance import zustatek
from ukazkova_data import transakce


def vypis(transakce):
    if len(transakce) == 0:
        print("Zatím tu nejsou žádné transakce.")
    for cislo, t in enumerate(transakce, start=1):
        if t["typ"] == "prijem":
            znamenko = "+"
        else:
            znamenko = "-"
        zacatek = f"{cislo:3}. {t['datum']}  {znamenko}{t['castka']:6} Kč"
        print(f"{zacatek}  {t['kategorie']:8} {t['popis']}")


print("Správce osobních financí")

while True:
    print()
    print("1 – výpis transakcí")
    print("2 – zůstatek")
    print("0 – konec")
    volba = input("Co chceš udělat? ").strip()

    if volba == "1":
        vypis(transakce)
    elif volba == "2":
        print(f"Zůstatek: {zustatek(transakce)} Kč")
    elif volba == "0":
        print("Ahoj!")
        break
    else:
        print("Tuhle volbu neznám.")
