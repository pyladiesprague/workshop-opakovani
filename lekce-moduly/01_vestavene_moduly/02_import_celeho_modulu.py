# ---------------------------------------------
#  Import celého modulu
# ---------------------------------------------
# Spusť soubor a porovnej oba zápisy.
#
# Import jde napsat i druhým způsobem. Místo jedné funkce si přineseš
# celý modul a funkce z něj voláš přes tečku:

import random

hod = random.randrange(1, 7)
print("Na kostce padlo:", hod)
print("Dnes bude:", random.choice(["dort", "palačinky", "zmrzlina"]))


# random.randrange čti jako „funkce randrange z modulu random“.
# Je to stejná funkce jako minule, jen napsaná i s adresou.
#
#   from random import randrange    →  randrange(1, 7)
#   import random                   →  random.randrange(1, 7)
#
# Oba zápisy dělají totéž. Kterým zápisem začít:
#   from ... import   když z modulu potřebuješ jednu dvě funkce
#   import ...        když jich potřebuješ víc, nebo chceš, aby
#                     bylo na první pohled vidět, odkud funkce je


# Modul nemusí mít jen funkce. Modul math má i hotové hodnoty:
import math

print("Odmocnina z 196 je", math.sqrt(196))
print("Pí je", math.pi)

polomer = 3
print("Pizza o poloměru 3 má plochu", round(math.pi * polomer ** 2, 1))


# Pozor na to, co je v jménu a co v tečce. Takhle to nefunguje:
#
#   import math
#   print(sqrt(16))         NameError: name 'sqrt' is not defined
#
# Při „import math“ zná Python jen jméno math. K funkci se dostaneš
# přes math.sqrt.
