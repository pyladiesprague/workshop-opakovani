# ---------------------------------------------
#  Import spustí celý soubor
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše jako první.

print("Začátek programu")

from upovidany import pozdrav

print(pozdrav("Petra"))


# Vypsalo se i něco, co v tomhle souboru vůbec není. Otevři upovidany.py.
#
# Při importu Python soubor modulu celý spustí, řádek po řádku:
#   def ...         funkci si jen zapamatuje, nic se nevypíše
#   print(...)      mimo funkci se opravdu provede
#
# Kdyby v modulu byl input(), program by se při importu nečekaně zeptal
# na odpověď. Testy by se na něm zasekly a čekaly by navždy.
#
# Proto pravidlo, které platí i v projektech:
#
#   V modulu jsou jen funkce. Všechno, co se má opravdu provést
#   (input, print, volání funkcí), patří do programu, který spouštíš.
