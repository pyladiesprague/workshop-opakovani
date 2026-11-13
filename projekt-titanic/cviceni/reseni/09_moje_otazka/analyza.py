# Analýza pasažérů Titaniku.
# Funkce tady nic nevypisují, takže jdou snadno testovat.

import csv
from pathlib import Path

# Složka, ve které leží tenhle soubor, a cesta k datům v ní.
# Díky tomu program data najde, ať máš ve VS Code otevřenou jakoukoliv složku.
SLOZKA = Path(__file__).parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"


def nacti_pasazery(soubor):
    """Vrátí seznam slovníků, jeden slovník na každý řádek souboru."""
    with open(soubor, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cislo_nebo_nic(text):
    """Převede text na číslo. Z prázdného textu udělá None."""
    if text == "":
        return None
    return float(text)


def uprav_pasazera(radek):
    """Vrátí kopii řádku, ve které jsou čísla opravdu čísla."""
    pasazer = radek.copy()
    pasazer["Survived"] = int(radek["Survived"])
    pasazer["Pclass"] = int(radek["Pclass"])
    pasazer["SibSp"] = int(radek["SibSp"])
    pasazer["Parch"] = int(radek["Parch"])
    pasazer["Fare"] = float(radek["Fare"])
    pasazer["Age"] = cislo_nebo_nic(radek["Age"])
    return pasazer


def uprav_pasazery(radky):
    pasazeri = []
    for radek in radky:
        pasazeri.append(uprav_pasazera(radek))
    return pasazeri


def pocet_prezivsich(pasazeri):
    pocet = 0
    for pasazer in pasazeri:
        pocet = pocet + pasazer["Survived"]
    return pocet


def mira_preziti(pasazeri):
    """Vrátí procento přeživších. Pro prázdný seznam vrátí 0."""
    if len(pasazeri) == 0:
        return 0
    return pocet_prezivsich(pasazeri) / len(pasazeri) * 100


def filtruj(pasazeri, sloupec, hodnota):
    """Vrátí pasažéry, kteří mají v daném sloupci danou hodnotu."""
    vybrani = []
    for pasazer in pasazeri:
        if pasazer[sloupec] == hodnota:
            vybrani.append(pasazer)
    return vybrani


def rozdel_podle(pasazeri, sloupec):
    """Vrátí slovník: hodnota ve sloupci -> seznam pasažérů s touto hodnotou."""
    skupiny = {}
    for pasazer in pasazeri:
        hodnota = pasazer[sloupec]
        if hodnota not in skupiny:
            skupiny[hodnota] = []
        skupiny[hodnota].append(pasazer)
    return skupiny


def miry_skupin(skupiny):
    """Ze slovníku skupin udělá slovník: klíč skupiny -> procento přeživších."""
    miry = {}
    for klic in skupiny:
        miry[klic] = mira_preziti(skupiny[klic])
    return miry


def prezivani_podle(pasazeri, sloupec):
    """Vrátí slovník: hodnota ve sloupci -> procento přeživších."""
    return miry_skupin(rozdel_podle(pasazeri, sloupec))


def rozdel_podle_dvou(pasazeri, sloupec1, sloupec2):
    """Vrátí slovník: n-tice dvou hodnot -> seznam pasažérů."""
    skupiny = {}
    for pasazer in pasazeri:
        klic = (pasazer[sloupec1], pasazer[sloupec2])
        if klic not in skupiny:
            skupiny[klic] = []
        skupiny[klic].append(pasazer)
    return skupiny


def prezivani_podle_dvou(pasazeri, sloupec1, sloupec2):
    """Vrátí slovník: n-tice dvou hodnot -> procento přeživších."""
    return miry_skupin(rozdel_podle_dvou(pasazeri, sloupec1, sloupec2))


def vekova_skupina(vek):
    if vek is None:
        return "neznámý"
    if vek < 16:
        return "dítě"
    return "dospělý"


def pridej_skupiny(pasazeri):
    """Přidá každému pasažérovi sloupec Skupina."""
    for pasazer in pasazeri:
        pasazer["Skupina"] = vekova_skupina(pasazer["Age"])


POHLAVI = {"female": "ženy", "male": "muži"}
TRIDY = {1: "1. třída", 2: "2. třída", 3: "3. třída"}
SKUPINY = {
    "dítě": "děti do 16 let",
    "dospělý": "dospělí",
    "neznámý": "věk neznámý",
}
PRISTAVY = {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}
ZAVER = [
    "",
    "Závěr",
    "  Pravidlo „ženy a děti první“ platilo jen zčásti.",
    "  Ženy přežívaly mnohem častěji než muži, ale ve 3. třídě",
    "  přežila jen polovina. Děti z 1. a 2. třídy přežily",
    "  téměř všechny, děti ze 3. třídy méně než z poloviny.",
]


def radek_tabulky(nazev, procenta, pocet):
    return f"  {nazev:24}{procenta:5.1f} %  ({pocet})"


def tabulka(nadpis, skupiny, popisky):
    """Vrátí řádky tabulky. Pořadí a názvy řádků určuje slovník popisky."""
    radky = ["", f"{nadpis:26}Přežilo  (lidí)"]
    for klic in popisky:
        if klic in skupiny:
            skupina = skupiny[klic]
            radky.append(
                radek_tabulky(popisky[klic], mira_preziti(skupina), len(skupina))
            )
    return radky


def popisky_trid_a_pohlavi():
    popisky = {}
    for trida in TRIDY:
        for pohlavi in POHLAVI:
            popisky[(trida, pohlavi)] = f"{TRIDY[trida]}, {POHLAVI[pohlavi]}"
    return popisky


def moje_otazka(pasazeri):
    """Záleželo na tom, kde pasažéři nastoupili, a proč?"""
    radky = ["", "Moje otázka: záleželo na přístavu?"]
    radky = radky + tabulka(
        "Podle přístavu", rozdel_podle(pasazeri, "Embarked"), PRISTAVY
    )
    z_cherbourgu = filtruj(pasazeri, "Embarked", "C")
    prvni_trida = filtruj(z_cherbourgu, "Pclass", 1)
    podil = len(prvni_trida) / len(z_cherbourgu) * 100
    radky.append("")
    radky.append(f"  Z pasažérů z Cherbourgu jelo 1. třídou {podil:.1f} %.")
    return radky


def sestav_zpravu(pasazeri):
    """Vrátí zprávu jako seznam řádků."""
    prezili = pocet_prezivsich(pasazeri)
    dospeli = filtruj(pasazeri, "Skupina", "dospělý")
    deti = filtruj(pasazeri, "Skupina", "dítě")

    radky = [
        "TITANIC: PLATILO „ŽENY A DĚTI PRVNÍ“?",
        "=" * 44,
        "",
        f"{'Pasažérů celkem:':26}{len(pasazeri):5}",
        f"{'Přežilo:':26}{prezili:5} ({mira_preziti(pasazeri):.1f} %)",
    ]
    radky = radky + tabulka(
        "Dospělí podle pohlaví", rozdel_podle(dospeli, "Sex"), POHLAVI
    )
    radky = radky + tabulka(
        "Všichni podle třídy", rozdel_podle(pasazeri, "Pclass"), TRIDY
    )
    radky = radky + tabulka(
        "Třída a pohlaví",
        rozdel_podle_dvou(pasazeri, "Pclass", "Sex"),
        popisky_trid_a_pohlavi(),
    )
    radky = radky + tabulka(
        "Podle věku", rozdel_podle(pasazeri, "Skupina"), SKUPINY
    )
    radky = radky + tabulka(
        "Děti podle třídy", rozdel_podle(deti, "Pclass"), TRIDY
    )
    radky = radky + moje_otazka(pasazeri)
    radky = radky + ZAVER
    return radky
