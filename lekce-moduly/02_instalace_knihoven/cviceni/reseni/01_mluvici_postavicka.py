# Řešení cvičení 1 – Mluvící postavička
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se uživatelky, co má postavička říct a která to má být
#    (třeba cow, tux nebo dragon). Pak ji nech promluvit.
#
#    cowsay.draw(text, cowsay.CHARS[jmeno]) nechá mluvit postavičku
#    podle jména. Seznam jmen je v cowsay.char_names. Když jméno
#    v seznamu není, vypiš, ze kterých jde vybírat.

import cowsay

text = input("Co má postavička říct? ")
jmeno = input("Která postavička? ").strip().lower()

if jmeno in cowsay.char_names:
    cowsay.draw(text, cowsay.CHARS[jmeno])
else:
    print("Takovou neznám. Vyber si z:", ", ".join(cowsay.char_names))
