# Řešení – krok 3: Správce osobních financí – logika
# Tvoje řešení může vypadat jinak, a to je v pořádku.


def soucet_prijmu(transakce):
    celkem = 0
    for t in transakce:
        if t["typ"] == "prijem":
            celkem = celkem + t["castka"]
    return celkem


def soucet_vydaju(transakce):
    celkem = 0
    for t in transakce:
        if t["typ"] == "vydaj":
            celkem = celkem + t["castka"]
    return celkem


def zustatek(transakce):
    return soucet_prijmu(transakce) - soucet_vydaju(transakce)


def pridej_transakci(transakce, datum, typ, castka, kategorie, popis):
    nova = {
        "datum": datum,
        "typ": typ,
        "castka": castka,
        "kategorie": kategorie,
        "popis": popis,
    }
    transakce.append(nova)
    return nova


def odeber_transakci(transakce, cislo):
    # Číslo je pořadí ve výpisu, tedy od jedničky. Index je o jedna menší.
    # Bez téhle kontroly by nula odebrala poslední transakci (index -1).
    if cislo < 1 or cislo > len(transakce):
        return None
    return transakce.pop(cislo - 1)


def je_platna_castka(text):
    # isdigit() neprojde pro prázdný text, mínus ani desetinnou čárku.
    return text.isdigit() and int(text) > 0


def je_platne_datum(text):
    if len(text) != 10:
        return False
    if text[4] != "-" or text[7] != "-":
        return False

    rok = text[:4]
    mesic = text[5:7]
    den = text[8:]
    if not rok.isdigit() or not mesic.isdigit() or not den.isdigit():
        return False

    if int(mesic) < 1 or int(mesic) > 12:
        return False
    if int(den) < 1 or int(den) > 31:
        return False
    return True


def vydaje_podle_kategorie(transakce):
    soucty = {}
    for t in transakce:
        if t["typ"] == "vydaj":
            kategorie = t["kategorie"]
            if kategorie in soucty:
                soucty[kategorie] = soucty[kategorie] + t["castka"]
            else:
                soucty[kategorie] = t["castka"]
    return soucty


def transakce_za_mesic(transakce, mesic):
    # Měsíc je text jako "2026-11". Datum "2026-11-21" jím začíná.
    vybrane = []
    for t in transakce:
        if t["datum"].startswith(mesic):
            vybrane.append(t)
    return vybrane


def nejvetsi_vydaj(transakce):
    nejvetsi = None
    for t in transakce:
        if t["typ"] == "vydaj":
            if nejvetsi is None or t["castka"] > nejvetsi["castka"]:
                nejvetsi = t
    return nejvetsi
