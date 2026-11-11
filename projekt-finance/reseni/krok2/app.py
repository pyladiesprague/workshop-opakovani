# Řešení – krok 2: Správce osobních financí – menu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from finance import zustatek
from finance import pridej_transakci, odeber_transakci
from finance import je_platna_castka, je_platne_datum
from ukazkova_data import transakce, KATEGORIE


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


def zeptej_se_na_datum():
    while True:
        text = input("Datum (RRRR-MM-DD): ").strip()
        if je_platne_datum(text):
            return text
        print("Datum napiš jako RRRR-MM-DD, třeba 2026-11-21.")


def zeptej_se_na_castku():
    while True:
        text = input("Částka v Kč: ").strip()
        if je_platna_castka(text):
            return int(text)
        print("Částka musí být celé kladné číslo.")


def zeptej_se_na_popis():
    while True:
        text = input("Popis: ").strip()
        if text != "":
            return text
        print("Popis nesmí být prázdný.")


def vyber_z_moznosti(otazka, moznosti):
    while True:
        text = input(otazka).strip().lower()
        if text in moznosti:
            return text
        print(f"Vyber jednu z možností: {', '.join(moznosti)}.")


def pridej(transakce):
    datum = zeptej_se_na_datum()
    typ = vyber_z_moznosti("Typ (prijem/vydaj): ", ["prijem", "vydaj"])
    castka = zeptej_se_na_castku()
    kategorie = vyber_z_moznosti(f"Kategorie ({', '.join(KATEGORIE)}): ", KATEGORIE)
    popis = zeptej_se_na_popis()
    pridej_transakci(transakce, datum, typ, castka, kategorie, popis)
    print("Přidáno.")


def odeber(transakce):
    vypis(transakce)
    text = input("Číslo transakce, kterou chceš odebrat: ").strip()
    if text.isdigit():
        odebrana = odeber_transakci(transakce, int(text))
        if odebrana is None:
            print("Transakce s tímhle číslem neexistuje.")
        else:
            print(f"Odebráno: {odebrana['popis']} ({odebrana['castka']} Kč)")
    else:
        print("To není číslo.")


print("Správce osobních financí")

while True:
    print()
    print("1 – výpis transakcí")
    print("2 – zůstatek")
    print("3 – přidat transakci")
    print("4 – odebrat transakci")
    print("0 – konec")
    volba = input("Co chceš udělat? ").strip()

    if volba == "1":
        vypis(transakce)
    elif volba == "2":
        print(f"Zůstatek: {zustatek(transakce)} Kč")
    elif volba == "3":
        pridej(transakce)
    elif volba == "4":
        odeber(transakce)
    elif volba == "0":
        print("Ahoj!")
        break
    else:
        print("Tuhle volbu neznám.")
