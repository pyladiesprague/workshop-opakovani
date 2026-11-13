# Řešení bonusu 2 – Jiné písmo
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# pyfiglet.figlet_format umí i jiná písma, jejich jména vrátí
#     pyfiglet.FigletFont.getFonts(). Zeptej se na text a vypiš ho
#     třemi náhodně vybranými písmy. Nad každý nápis napiš jméno
#     písma, ať víš, které se ti líbí.
#
#     Písmo se vybírá takhle:  pyfiglet.figlet_format(text, font="slant")

from random import choice

import pyfiglet

text = input("Text: ")
pisma = pyfiglet.FigletFont.getFonts()

for poradi in range(3):
    pismo = choice(pisma)
    print(f"--- {pismo} ---")
    print(pyfiglet.figlet_format(text, font=pismo))
