# Řešení bonusu 3 – Řazení podle částky
# Tvoje řešení může vypadat jinak, a to je v pořádku.
#
# Soubor jde spustit samostatně. Ve svém projektu dej funkci
# serazene_podle_castky do finance.py a výpis do app.py.

from ukazkova_data import transakce


def serazene_podle_castky(transakce):
    # Seznam slovníků metodou sort neseřadíme, seznam n-tic ano.
    # N-tice se porovnávají podle první položky, při shodě podle druhé.
    dvojice = []
    for index, t in enumerate(transakce):
        dvojice.append((t["castka"], index))

    dvojice.sort(reverse=True)

    serazene = []
    for castka, index in dvojice:
        serazene.append(transakce[index])
    return serazene


# Proč je ve dvojici index, a ne rovnou slovník: když mají dvě transakce
# stejnou částku, Python porovná druhé položky. Dva indexy porovnat umí,
# dva slovníky ne, a skončilo by to chybou TypeError.


# Testy, které patří do test_finance.py:
#
# def test_serazene_podle_castky():
#     serazene = finance.serazene_podle_castky(ukazka())
#     assert serazene[0]["popis"] == "brigáda"
#     assert serazene[4]["popis"] == "jízdenky"
#
# def test_serazeni_nemeni_puvodni_seznam():
#     transakce = ukazka()
#     finance.serazene_podle_castky(transakce)
#     assert transakce[0]["popis"] == "pizza"
#
# def test_serazeni_se_stejnymi_castkami():
#     transakce = ukazka()
#     finance.pridej_transakci(transakce, "2026-11-10", "vydaj", 300, "jidlo", "sushi")
#     assert len(finance.serazene_podle_castky(transakce)) == 6


for t in serazene_podle_castky(transakce):
    print(f"{t['castka']:6} Kč  {t['datum']}  {t['popis']}")
