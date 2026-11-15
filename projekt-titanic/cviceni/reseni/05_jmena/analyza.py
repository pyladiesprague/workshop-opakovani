# Řešení kroku 5 – Co prozradí jména?
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


def filtruj(pasazeri, sloupec, hodnota):
    """Vrátí pasažéry, kteří mají v daném sloupci danou hodnotu."""
    vybrani = []
    for pasazer in pasazeri:
        if pasazer[sloupec] == hodnota:
            vybrani.append(pasazer)
    return vybrani


def prumerna_cena(pasazeri):
    """Vrátí průměrnou cenu lístku. Pro prázdný seznam vrátí 0."""
    if len(pasazeri) == 0:
        return 0
    soucet = 0
    for pasazer in pasazeri:
        soucet = soucet + pasazer["Fare"]
    return soucet / len(pasazeri)


def nejdrazsi_listek(pasazeri):
    """Vrátí nejvyšší cenu lístku. Pro prázdný seznam vrátí 0."""
    nejvyssi = 0
    for pasazer in pasazeri:
        if pasazer["Fare"] > nejvyssi:
            nejvyssi = pasazer["Fare"]
    return nejvyssi


def titul(jmeno):
    """Z "Braund, Mr. Owen Harris" vrátí "Mr"."""
    za_carkou = jmeno.split(",")[1]
    return za_carkou.split(".")[0].strip()


def krestni_jmeno(jmeno):
    """Z "Braund, Mr. Owen Harris" vrátí "Owen". Když jméno chybí, vrátí ""."""
    slova = jmeno.split(".")[1].split()
    if len(slova) == 0:
        return ""
    return slova[0].strip('"()')


def pridej_jmena(pasazeri):
    """Přidá každému pasažérovi sloupce Titul a Krestni."""
    for pasazer in pasazeri:
        pasazer["Titul"] = titul(pasazer["Name"])
        pasazer["Krestni"] = krestni_jmeno(pasazer["Name"])


def pocty(pasazeri, sloupec):
    """Vrátí slovník: hodnota ve sloupci -> kolik pasažérů ji má."""
    vysledek = {}
    for pasazer in pasazeri:
        hodnota = pasazer[sloupec]
        if hodnota in vysledek:
            vysledek[hodnota] = vysledek[hodnota] + 1
        else:
            vysledek[hodnota] = 1
    return vysledek
