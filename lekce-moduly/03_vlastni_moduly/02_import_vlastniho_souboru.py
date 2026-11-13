# ---------------------------------------------
#  Jak importovat vlastní soubor
# ---------------------------------------------
# Spusť soubor.
#
# U vlastního modulu fungují oba zápisy, které znáš z random:

from prevody import na_celsia

print("100 °F je", round(na_celsia(100), 1), "°C.")


import prevody

print("0 °C je", prevody.na_fahrenheity(0), "°F.")


# Kdy import vlastního souboru funguje:
#
#   - Soubor leží ve stejné složce jako program, který ho importuje.
#   - V importu píšeš jméno bez .py:   import prevody   (ne prevody.py)
#   - Jméno souboru je platné jméno v Pythonu: malá písmena, číslice
#     a podtržítka, nezačíná číslicí, žádné mezery, pomlčky ani háčky.
#       prevody.py, moje_funkce.py   ✓
#       01_prevody.py                ✗ začíná číslicí
#       moje-funkce.py               ✗ pomlčka
#
# Proto se soubory s výkladem jmenují 01_…, 02_… (ty jen spouštíš)
# a modul se jmenuje prevody.py (ten se importuje).


# Pozor na jméno, které už má jiný modul! Kdybys svůj soubor
# pojmenovala random.py, Python by při import random našel ten tvůj
# a skutečný random by se schoval. Program pak spadne s hláškou jako:
#
#   AttributeError: module 'random' has no attribute 'randrange'
#
# Stejně tak nikdy nepojmenuj soubor pytest.py nebo cowsay.py.
