# Řešení – {TITULEK}: Správce osobních financí – menu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from finance import zustatek
#@ 2+
from finance import pridej_transakci, odeber_transakci
from finance import je_platna_castka, je_platne_datum
#@ 3+
from finance import soucet_prijmu, soucet_vydaju
from finance import vydaje_podle_kategorie, transakce_za_mesic, nejvetsi_vydaj
#@ 4+
from finance import zbyva_v_rozpoctu, prekrocene_rozpocty
#@ 5+
from finance import sloupec
#@ 6+
from finance import uloz, nacti
#@ 7
from finance import obarvi
#@ vse
from ukazkova_data import transakce  #@1
from ukazkova_data import transakce, KATEGORIE  #@2-3
from ukazkova_data import transakce, KATEGORIE, rozpocty  #@4-5
from ukazkova_data import KATEGORIE, rozpocty  #@6+
#@ 6+

SOUBOR = "finance.json"
#@ 7


def upozorni(text):
    # Hlášky o špatném vstupu jsou žluté, ať nezapadnou.
    print(obarvi(text, "zluta"))
#@ vse


def vypis(transakce):
    if len(transakce) == 0:
        print("Zatím tu nejsou žádné transakce.")
    for cislo, t in enumerate(transakce, start=1):
        if t["typ"] == "prijem":
            znamenko = "+"
            barva = "zelena"  #@7
        else:
            znamenko = "-"
            barva = "cervena"  #@7
        zacatek = f"{cislo:3}. {t['datum']}  {znamenko}{t['castka']:6} Kč"  #@1-6
        print(f"{zacatek}  {t['kategorie']:8} {t['popis']}")  #@1-6
        # Nejdřív zarovnat, potom obarvit. Kódy barev by se počítaly do šířky.  #@7
        castka = obarvi(f"{znamenko}{t['castka']:6} Kč", barva)  #@7
        print(f"{cislo:3}. {t['datum']}  {castka}  {t['kategorie']:8} {t['popis']}")  #@7
#@ 7


def vypis_zustatek(transakce):
    castka = zustatek(transakce)
    if castka < 0:
        print(obarvi(f"Zůstatek: {castka} Kč", "cervena"))
    else:
        print(obarvi(f"Zůstatek: {castka} Kč", "zelena"))
#@ 2+


def zeptej_se_na_datum():
    while True:
        text = input("Datum (RRRR-MM-DD): ").strip()
        if je_platne_datum(text):
            return text
        print("Datum napiš jako RRRR-MM-DD, třeba 2026-11-21.")  #@2-6
        upozorni("Datum napiš jako RRRR-MM-DD, třeba 2026-11-21.")  #@7


def zeptej_se_na_castku():
    while True:
        text = input("Částka v Kč: ").strip()
        if je_platna_castka(text):
            return int(text)
        print("Částka musí být celé kladné číslo.")  #@2-6
        upozorni("Částka musí být celé kladné číslo.")  #@7


def zeptej_se_na_popis():
    while True:
        text = input("Popis: ").strip()
        if text != "":
            return text
        print("Popis nesmí být prázdný.")  #@2-6
        upozorni("Popis nesmí být prázdný.")  #@7


def vyber_z_moznosti(otazka, moznosti):
    while True:
        text = input(otazka).strip().lower()
        if text in moznosti:
            return text
        print(f"Vyber jednu z možností: {', '.join(moznosti)}.")  #@2-6
        upozorni(f"Vyber jednu z možností: {', '.join(moznosti)}.")  #@7


def pridej(transakce):  #@2-3
def pridej(transakce, rozpocty):  #@4+
    datum = zeptej_se_na_datum()
    typ = vyber_z_moznosti("Typ (prijem/vydaj): ", ["prijem", "vydaj"])
    castka = zeptej_se_na_castku()
    kategorie = vyber_z_moznosti(f"Kategorie ({', '.join(KATEGORIE)}): ", KATEGORIE)
    popis = zeptej_se_na_popis()
    pridej_transakci(transakce, datum, typ, castka, kategorie, popis)
    print("Přidáno.")  #@2-6
    print(obarvi("Přidáno.", "zelena"))  #@7
    #@ 4+

    if typ == "vydaj" and kategorie in rozpocty:
        mesic = datum[:7]
        v_mesici = transakce_za_mesic(transakce, mesic)
        zbyva = zbyva_v_rozpoctu(v_mesici, rozpocty, kategorie)
        if zbyva < 0:
            print(f"Pozor, rozpočet na {kategorie} za {mesic} je překročený o {-zbyva} Kč.")  #@4-6
            text = f"Pozor, rozpočet na {kategorie} za {mesic} je překročený o {-zbyva} Kč."  #@7
            print(obarvi(text, "cervena"))  #@7
    #@ 2+


def odeber(transakce):
    vypis(transakce)
    text = input("Číslo transakce, kterou chceš odebrat: ").strip()
    if text.isdigit():
        odebrana = odeber_transakci(transakce, int(text))
        if odebrana is None:
            print("Transakce s tímhle číslem neexistuje.")  #@2-6
            upozorni("Transakce s tímhle číslem neexistuje.")  #@7
        else:
            print(f"Odebráno: {odebrana['popis']} ({odebrana['castka']} Kč)")
    else:
        print("To není číslo.")  #@2-6
        upozorni("To není číslo.")  #@7
#@ 3+


def zeptej_se_na_mesic():
    while True:
        text = input("Měsíc (RRRR-MM): ").strip()
        # Měsíc je platný, když je platné datum jeho prvního dne.
        if je_platne_datum(text + "-01"):
            return text
        print("Měsíc napiš jako RRRR-MM, třeba 2026-11.")  #@3-6
        upozorni("Měsíc napiš jako RRRR-MM, třeba 2026-11.")  #@7


def prehled_mesice(transakce):
    mesic = zeptej_se_na_mesic()
    v_mesici = transakce_za_mesic(transakce, mesic)
    if len(v_mesici) == 0:
        print("V tomhle měsíci nejsou žádné transakce.")
    else:
        print(f"Příjmy: {soucet_prijmu(v_mesici):7} Kč")  #@3-6
        print(f"Výdaje: {soucet_vydaju(v_mesici):7} Kč")  #@3-6
        print(obarvi(f"Příjmy: {soucet_prijmu(v_mesici):7} Kč", "zelena"))  #@7
        print(obarvi(f"Výdaje: {soucet_vydaju(v_mesici):7} Kč", "cervena"))  #@7
        print(f"Rozdíl: {zustatek(v_mesici):7} Kč")

        print()
        print("Výdaje podle kategorií:")  #@3-6
        print(obarvi("Výdaje podle kategorií:", "tucne"))  #@7
        for kategorie, castka in vydaje_podle_kategorie(v_mesici).items():
            print(f"  {kategorie:10} {castka:6} Kč")

        nejvetsi = nejvetsi_vydaj(v_mesici)
        if nejvetsi is None:
            print("V tomhle měsíci nebyl žádný výdaj.")
        else:
            print()
            print(f"Největší výdaj: {nejvetsi['popis']} ({nejvetsi['castka']} Kč)")
#@ 4+


def ukaz_rozpocty(transakce, rozpocty):
    mesic = zeptej_se_na_mesic()
    v_mesici = transakce_za_mesic(transakce, mesic)
    for kategorie, limit in rozpocty.items():
        zbyva = zbyva_v_rozpoctu(v_mesici, rozpocty, kategorie)
        utraceno = limit - zbyva
        if zbyva < 0:
            stav = f"překročeno o {-zbyva} Kč"  #@4-6
            stav = obarvi(f"překročeno o {-zbyva} Kč", "cervena")  #@7
        else:
            stav = f"zbývá {zbyva} Kč"  #@4-6
            stav = obarvi(f"zbývá {zbyva} Kč", "zelena")  #@7
        print(f"  {kategorie:10} {utraceno:6} / {limit:6} Kč   {stav}")

    prekrocene = prekrocene_rozpocty(v_mesici, rozpocty)
    if len(prekrocene) > 0:
        print(f"Překročené rozpočty: {', '.join(prekrocene)}")  #@4-6
        print(obarvi(f"Překročené rozpočty: {', '.join(prekrocene)}", "cervena"))  #@7


def nastav_rozpocet(rozpocty):
    kategorie = vyber_z_moznosti(f"Kategorie ({', '.join(KATEGORIE)}): ", KATEGORIE)
    castka = zeptej_se_na_castku()
    rozpocty[kategorie] = castka
    print(f"Rozpočet na {kategorie} je teď {castka} Kč na měsíc.")
#@ 5+


def graf(transakce):
    soucty = vydaje_podle_kategorie(transakce)
    if len(soucty) == 0:
        print("Zatím tu nejsou žádné výdaje.")
    else:
        nejvyssi = max(soucty.values())
        for kategorie, castka in soucty.items():
            cara = sloupec(castka, nejvyssi, 30)
            print(f"{kategorie:10} {cara:30} {castka:7} Kč")  #@5-6
            # Sloupec se musí zarovnat na 30 znaků dřív, než se obarví.  #@7
            cara = obarvi(f"{cara:30}", "tyrkysova")  #@7
            print(f"{kategorie:10} {cara} {castka:7} Kč")  #@7
#@ vse


#@ 6+
transakce = nacti(SOUBOR)
#@ vse
print("Správce osobních financí")  #@1-6
print(obarvi("Správce osobních financí", "tucne"))  #@7

while True:
    print()
    print("1 – výpis transakcí")
    print("2 – zůstatek")
    print("3 – přidat transakci")  #@2+
    print("4 – odebrat transakci")  #@2+
    print("5 – přehled měsíce")  #@3+
    print("6 – rozpočty")  #@4+
    print("7 – nastavit rozpočet")  #@4+
    print("8 – graf výdajů")  #@5+
    print("0 – konec")
    volba = input("Co chceš udělat? ").strip()

    if volba == "1":
        vypis(transakce)
    elif volba == "2":
        print(f"Zůstatek: {zustatek(transakce)} Kč")  #@1-6
        vypis_zustatek(transakce)  #@7
    #@ 2-3
    elif volba == "3":
        pridej(transakce)
    #@ 4+
    elif volba == "3":
        pridej(transakce, rozpocty)
    #@ 6+
        uloz(transakce, SOUBOR)
    #@ 2+
    elif volba == "4":
        odeber(transakce)
    #@ 6+
        uloz(transakce, SOUBOR)
    #@ 3+
    elif volba == "5":
        prehled_mesice(transakce)
    #@ 4+
    elif volba == "6":
        ukaz_rozpocty(transakce, rozpocty)
    elif volba == "7":
        nastav_rozpocet(rozpocty)
    #@ 5+
    elif volba == "8":
        graf(transakce)
    #@ vse
    elif volba == "0":
        print("Ahoj!")
        break
    else:
        print("Tuhle volbu neznám.")  #@1-6
        upozorni("Tuhle volbu neznám.")  #@7
