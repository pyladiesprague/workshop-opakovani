# Řešení bonusu 2 – Grafy s knihovnou
# Tvoje řešení může vypadat jinak, a to je v pořádku.
# Nejdřív je potřeba knihovnu nainstalovat, postup je v zadání bonusu.

import plotext as plt

from analyza import (
    POHLAVI,
    SOUBOR,
    TRIDY,
    miry_skupin,
    nacti_pasazery,
    prezivani_podle,
    rozdel_podle_dvou,
    uprav_pasazery,
)

pasazeri = uprav_pasazery(nacti_pasazery(SOUBOR))

miry = prezivani_podle(pasazeri, "Pclass")
nazvy = []
hodnoty = []
for trida in TRIDY:
    nazvy.append(TRIDY[trida])
    hodnoty.append(miry[trida])

plt.simple_bar(nazvy, hodnoty, width=50, title="Přežití podle třídy (%)")
plt.show()
plt.clear_figure()

miry = miry_skupin(rozdel_podle_dvou(pasazeri, "Pclass", "Sex"))
zeny = []
muzi = []
for trida in TRIDY:
    zeny.append(miry[(trida, "female")])
    muzi.append(miry[(trida, "male")])

plt.simple_multiple_bar(
    nazvy,
    [zeny, muzi],
    width=50,
    labels=[POHLAVI["female"], POHLAVI["male"]],
    title="Přežití podle třídy a pohlaví (%)",
)
plt.show()
