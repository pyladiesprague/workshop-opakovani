# Řešení bonusu 3 – Hledání
# Tvoje řešení může vypadat jinak, a to je v pořádku.
#
# Soubor jde spustit samostatně. Ve svém projektu dej funkci najdi
# do finance.py a ptaní se na hledaný text do app.py.

from ukazkova_data import transakce


def najdi(transakce, text):
    # Obě strany převedeme na malá písmena, aby na velikosti nezáleželo.
    hledany = text.lower()
    nalezene = []
    for t in transakce:
        if hledany in t["popis"].lower():
            nalezene.append(t)
    return nalezene


# Testy, které patří do test_finance.py:
#
# def test_najdi_vic_transakci():
#     transakce = ukazka()
#     finance.pridej_transakci(transakce, "2026-11-10", "vydaj", 90, "jidlo", "oběd v menze")
#     assert len(finance.najdi(transakce, "oběd")) == 2
#
# def test_najdi_nezalezi_na_velikosti_pismen():
#     assert finance.najdi(ukazka(), "PIZZA")[0]["popis"] == "pizza"
#
# def test_najdi_nic():
#     assert finance.najdi(ukazka(), "jachta") == []


hledany = input("Co hledáš? ").strip()
nalezene = najdi(transakce, hledany)
if len(nalezene) == 0:
    print("Nic jsem nenašla.")
for t in nalezene:
    print(f"{t['datum']}  {t['castka']:6} Kč  {t['popis']}")
