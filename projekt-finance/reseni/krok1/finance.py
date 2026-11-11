# Řešení – krok 1: Správce osobních financí – logika
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
