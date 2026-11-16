# Řešení bonusu 5 – Čistá obrazovka
# Tvoje řešení může vypadat jinak, a to je v pořádku.
#
# Soubor jde spustit samostatně, menu má jen tři volby. Ve svém projektu dej
# funkce vycisti_obrazovku a pockej do app.py a hlavní cyklus uprav stejně
# jako tady: smazat, vypsat zůstatek a menu, provést volbu, počkat na Enter.

import os

from ukazkova_data import transakce


def vycisti_obrazovku():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pockej():
    # Bez tohohle by výsledek volby hned zmizel: cyklus by obrazovku smazal.
    input("\nPokračuj klávesou Enter...")


def zustatek(transakce):
    # V projektu je tahle funkce ve finance.py.
    soucet = 0
    for t in transakce:
        if t["typ"] == "prijem":
            soucet += t["castka"]
        else:
            soucet -= t["castka"]
    return soucet


def vypis(transakce):
    for cislo, t in enumerate(transakce, start=1):
        print(f"{cislo:3}. {t['datum']}  {t['castka']:6} Kč  {t['popis']}")


while True:
    vycisti_obrazovku()
    print("Správce osobních financí")
    print(f"Zůstatek: {zustatek(transakce)} Kč")
    print()
    print("1 – výpis transakcí")
    print("2 – počet transakcí")
    print("0 – konec")
    volba = input("Co chceš udělat? ").strip()

    if volba == "0":
        print("Ahoj!")
        break

    if volba == "1":
        vypis(transakce)
    elif volba == "2":
        print(f"Transakcí je {len(transakce)}.")
    else:
        print("Tuhle volbu neznám.")
    pockej()
