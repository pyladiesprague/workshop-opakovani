# Řešení bonusu 2 – Grafy s knihovnou
# Tvoje řešení může vypadat jinak, a to je v pořádku.
# Nejdřív je potřeba knihovnu nainstalovat, postup je v zadání bonusu.

import plotext as plt

import analyza

pasazeri = analyza.uprav_pasazery(analyza.nacti_pasazery(analyza.SOUBOR))

miry = analyza.prezivani_podle(pasazeri, "Pclass")
nazvy = []
hodnoty = []
for trida in analyza.TRIDY:
    nazvy.append(analyza.TRIDY[trida])
    hodnoty.append(miry[trida])

plt.simple_bar(nazvy, hodnoty, width=50, title="Přežití podle třídy (%)")
plt.show()
plt.clear_figure()

miry = analyza.miry_skupin(analyza.rozdel_podle_dvou(pasazeri, "Pclass", "Sex"))
zeny = []
muzi = []
for trida in analyza.TRIDY:
    zeny.append(miry[(trida, "female")])
    muzi.append(miry[(trida, "male")])

plt.simple_multiple_bar(
    nazvy,
    [zeny, muzi],
    width=50,
    labels=[analyza.POHLAVI["female"], analyza.POHLAVI["male"]],
    title="Přežití podle třídy a pohlaví (%)",
)
plt.show()
