# Řešení – krok 10: Titanic – analýza
# Tvoje řešení může vypadat jinak, a to je v pořádku.
# Funkce tady nic nevypisují, takže jdou snadno testovat.

import csv
from pathlib import Path

# Data leží ve složce projektu.
SLOZKA = Path(__file__).parent.parent.parent.parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"
SIRKA_GRAFU = 30

POHLAVI = {"female": "ženy", "male": "muži"}
TRIDY = {1: "1. třída", 2: "2. třída", 3: "3. třída"}
PRISTAVY = {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}
ZAVER = [
    "",
    "Závěr",
    "  Čemu věřím: ženy a lidé z 1. třídy přežívali mnohem častěji.",
    "  Skupiny jsou velké a rozdíl je obrovský.",
    "  Čemu nevěřím: že rozhodoval přístav. Z Cherbourgu jela polovina",
    "  lidí 1. třídou, a ta přežívala častěji ve všech přístavech.",
]


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


def sloupec_grafu(hodnota, nejvyssi, sirka):
    """Vrátí text ze znaků █. Nejvyšší hodnota dostane plnou šířku."""
    if hodnota <= 0 or nejvyssi <= 0:
        return ""
    delka = int(hodnota * sirka / nejvyssi)
    if delka == 0:
        # I malá hodnota má být v grafu vidět.
        delka = 1
    return "█" * delka


def popisky_trid_a_pohlavi():
    popisky = {}
    for trida in TRIDY:
        for pohlavi in POHLAVI:
            popisky[(trida, pohlavi)] = f"{TRIDY[trida]}, {POHLAVI[pohlavi]}"
    return popisky


def graf(nadpis, skupiny, popisky):
    """Vrátí řádky grafu. Pořadí a názvy řádků určuje slovník popisky."""
    radky = ["", nadpis]
    for klic in popisky:
        if klic in skupiny:
            procenta = mira_preziti(skupiny[klic])
            cara = sloupec_grafu(procenta, 100, SIRKA_GRAFU)
            radky.append(f"  {popisky[klic]:16}{cara:{SIRKA_GRAFU}} {procenta:5.1f} %")
    return radky


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


def sestav_zpravu(pasazeri):
    """Vrátí zprávu jako seznam řádků."""
    stary = nejstarsi(pasazeri)
    mlady = nejmladsi(pasazeri)
    muzi = filtruj(pasazeri, "Sex", "male")

    radky = [
        "TITANIC V ČÍSLECH",
        "=" * 44,
        "",
        f"{'Pasažérů v souboru:':26}{len(pasazeri):5}",
        f"{'Přežilo:':26}{pocet_prezivsich(pasazeri):5} ({mira_preziti(pasazeri):.1f} %)",
        f"{'Průměrný věk:':26}{prumerny_vek(pasazeri):5.1f} let",
        f"{'Nejstarší:':26}{stary['Name']} ({stary['Age']:g})",
        f"{'Nejmladší:':26}{mlady['Name']} ({mlady['Age']:g})",
        "",
        "Průměrná cena lístku",
    ]
    for trida in TRIDY:
        cena = prumerna_cena(filtruj(pasazeri, "Pclass", trida))
        radky.append(f"  {TRIDY[trida]:24}{cena:5.1f} liber")

    radky.append("")
    radky.append(f"{'Různých titulů:':26}{len(pocty(pasazeri, 'Titul')):5}")
    radky.append("Nejčastější mužská jména")
    jmena = pocty(muzi, "Krestni")
    for jmeno in jmena:
        if jmena[jmeno] >= 20:
            radky.append(f"  {jmeno:24}{jmena[jmeno]:5}")

    radky = radky + tabulka("Podle pohlaví", rozdel_podle(pasazeri, "Sex"), POHLAVI)
    radky = radky + tabulka("Podle třídy", rozdel_podle(pasazeri, "Pclass"), TRIDY)
    radky = radky + tabulka(
        "Podle přístavu", rozdel_podle(pasazeri, "Embarked"), PRISTAVY
    )
    radky = radky + graf(
        "Třída a pohlaví v grafu",
        rozdel_podle_dvou(pasazeri, "Pclass", "Sex"),
        popisky_trid_a_pohlavi(),
    )
    radky = radky + ZAVER
    return radky
