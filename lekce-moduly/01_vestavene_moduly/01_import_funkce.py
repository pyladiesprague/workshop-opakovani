# ---------------------------------------------
#  Import: půjčím si funkci odjinud
# ---------------------------------------------
# Spusť soubor víckrát – pokaždé padne něco jiného.
#
# Tenhle řádek znáš od lekce o cyklu while:

from random import randrange

# Čte se zprava doleva: „z modulu random si vezmi funkci randrange“.
#
# Modul je obyčejný soubor s Pythonem, ve kterém jsou připravené funkce.
# Modul random napsal někdo jiný a Python ho má s sebou. Ty si z něj jen
# řekneš o to, co potřebuješ.

hod = randrange(1, 7)
print("Na kostce padlo:", hod)


# Bez řádku s importem by Python randrange neznal a spadl by:
#
#   NameError: name 'randrange' is not defined
#
# Import proto patří na začátek souboru, ještě před první použití.


# Z jednoho modulu si můžeš vzít víc funkcí najednou, oddělíš je čárkou.
# Funkce choice vybere náhodnou položku ze seznamu:
from random import choice, shuffle

dezerty = ["dort", "palačinky", "zmrzlina", "jablko"]
print("Dnes bude:", choice(dezerty))

# shuffle seznam zamíchá – jako balíček karet:
shuffle(dezerty)
print("Pořadí ochutnávky:", dezerty)


# Všechny importy se podle zvyklostí píšou nahoru, každý na svůj řádek.
# Tady jsou rozházené jen proto, aby byly vedle ukázky.
