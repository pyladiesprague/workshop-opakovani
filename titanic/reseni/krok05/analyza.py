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
