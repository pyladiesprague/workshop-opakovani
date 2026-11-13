# Řešení – krok 6: Správce osobních financí – menu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from finance import zustatek
from finance import pridej_transakci, odeber_transakci
from finance import je_platna_castka, je_platne_datum
from finance import soucet_prijmu, soucet_vydaju
from finance import vydaje_podle_kategorie, transakce_za_mesic, nejvetsi_vydaj
from finance import zbyva_v_rozpoctu, prekrocene_rozpocty
from finance import sloupec
from finance import uloz, nacti
from ukazkova_data import KATEGORIE, rozpocty

SOUBOR = "finance.json"


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


def pridej(transakce, rozpocty):
    datum = zeptej_se_na_datum()
    typ = vyber_z_moznosti("Typ (prijem/vydaj): ", ["prijem", "vydaj"])
    castka = zeptej_se_na_castku()
    kategorie = vyber_z_moznosti(f"Kategorie ({', '.join(KATEGORIE)}): ", KATEGORIE)
    popis = zeptej_se_na_popis()
    pridej_transakci(transakce, datum, typ, castka, kategorie, popis)
    print("Přidáno.")

    if typ == "vydaj" and kategorie in rozpocty:
        mesic = datum[:7]
        v_mesici = transakce_za_mesic(transakce, mesic)
        zbyva = zbyva_v_rozpoctu(v_mesici, rozpocty, kategorie)
        if zbyva < 0:
            print(f"Pozor, rozpočet na {kategorie} za {mesic} je překročený o {-zbyva} Kč.")


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


def zeptej_se_na_mesic():
    while True:
        text = input("Měsíc (RRRR-MM): ").strip()
        # Měsíc je platný, když je platné datum jeho prvního dne.
        if je_platne_datum(text + "-01"):
            return text
        print("Měsíc napiš jako RRRR-MM, třeba 2026-11.")


def prehled_mesice(transakce):
    mesic = zeptej_se_na_mesic()
    v_mesici = transakce_za_mesic(transakce, mesic)
    if len(v_mesici) == 0:
        print("V tomhle měsíci nejsou žádné transakce.")
    else:
        print(f"Příjmy: {soucet_prijmu(v_mesici):7} Kč")
        print(f"Výdaje: {soucet_vydaju(v_mesici):7} Kč")
        print(f"Rozdíl: {zustatek(v_mesici):7} Kč")

        print()
        print("Výdaje podle kategorií:")
        for kategorie, castka in vydaje_podle_kategorie(v_mesici).items():
            print(f"  {kategorie:10} {castka:6} Kč")

        nejvetsi = nejvetsi_vydaj(v_mesici)
        if nejvetsi is None:
            print("V tomhle měsíci nebyl žádný výdaj.")
        else:
            print()
            print(f"Největší výdaj: {nejvetsi['popis']} ({nejvetsi['castka']} Kč)")


def ukaz_rozpocty(transakce, rozpocty):
    mesic = zeptej_se_na_mesic()
    v_mesici = transakce_za_mesic(transakce, mesic)
    for kategorie, limit in rozpocty.items():
        zbyva = zbyva_v_rozpoctu(v_mesici, rozpocty, kategorie)
        utraceno = limit - zbyva
        if zbyva < 0:
            stav = f"překročeno o {-zbyva} Kč"
        else:
            stav = f"zbývá {zbyva} Kč"
        print(f"  {kategorie:10} {utraceno:6} / {limit:6} Kč   {stav}")

    prekrocene = prekrocene_rozpocty(v_mesici, rozpocty)
    if len(prekrocene) > 0:
        print(f"Překročené rozpočty: {', '.join(prekrocene)}")


def nastav_rozpocet(rozpocty):
    kategorie = vyber_z_moznosti(f"Kategorie ({', '.join(KATEGORIE)}): ", KATEGORIE)
    castka = zeptej_se_na_castku()
    rozpocty[kategorie] = castka
    print(f"Rozpočet na {kategorie} je teď {castka} Kč na měsíc.")


def graf(transakce):
    soucty = vydaje_podle_kategorie(transakce)
    if len(soucty) == 0:
        print("Zatím tu nejsou žádné výdaje.")
    else:
        nejvyssi = max(soucty.values())
        for kategorie, castka in soucty.items():
            cara = sloupec(castka, nejvyssi, 30)
            print(f"{kategorie:10} {cara:30} {castka:7} Kč")


transakce = nacti(SOUBOR)
print("Správce osobních financí")

while True:
    print()
    print("1 – výpis transakcí")
    print("2 – zůstatek")
    print("3 – přidat transakci")
    print("4 – odebrat transakci")
    print("5 – přehled měsíce")
    print("6 – rozpočty")
    print("7 – nastavit rozpočet")
    print("8 – graf výdajů")
    print("0 – konec")
    volba = input("Co chceš udělat? ").strip()

    if volba == "1":
        vypis(transakce)
    elif volba == "2":
        print(f"Zůstatek: {zustatek(transakce)} Kč")
    elif volba == "3":
        pridej(transakce, rozpocty)
        uloz(transakce, SOUBOR)
    elif volba == "4":
        odeber(transakce)
        uloz(transakce, SOUBOR)
    elif volba == "5":
        prehled_mesice(transakce)
    elif volba == "6":
        ukaz_rozpocty(transakce, rozpocty)
    elif volba == "7":
        nastav_rozpocet(rozpocty)
    elif volba == "8":
        graf(transakce)
    elif volba == "0":
        print("Ahoj!")
        break
    else:
        print("Tuhle volbu neznám.")
