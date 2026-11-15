# Řešení kroku 3 – Kdo byl na palubě?
# Tvoje řešení může vypadat jinak, a to je v pořádku.
# Funkce tady nic nevypisují, takže jdou snadno testovat.

import csv
from pathlib import Path

# Data leží ve složce projektu.
SLOZKA = Path(__file__).parent.parent.parent.parent
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


def prumerny_vek(pasazeri):
    """Vrátí průměrný věk těch, u kterých věk známe. Když není u nikoho, vrátí None."""
    soucet = 0
    pocet = 0
    for pasazer in pasazeri:
        if pasazer["Age"] is not None:
            soucet = soucet + pasazer["Age"]
            pocet = pocet + 1
    if pocet == 0:
        return None
    return soucet / pocet


def nejstarsi(pasazeri):
    """Vrátí pasažéra s nejvyšším známým věkem. Když věk nemá nikdo, vrátí None."""
    vitez = None
    for pasazer in pasazeri:
        if pasazer["Age"] is not None:
            if vitez is None or pasazer["Age"] > vitez["Age"]:
                vitez = pasazer
    return vitez


def nejmladsi(pasazeri):
    """Vrátí pasažéra s nejnižším známým věkem. Když věk nemá nikdo, vrátí None."""
    vitez = None
    for pasazer in pasazeri:
        if pasazer["Age"] is not None:
            if vitez is None or pasazer["Age"] < vitez["Age"]:
                vitez = pasazer
    return vitez
