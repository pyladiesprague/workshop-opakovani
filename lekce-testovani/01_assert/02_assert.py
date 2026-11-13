# ---------------------------------------------
#  assert
# ---------------------------------------------
# assert znamená „tvrdím, že“. Za něj napíšeš podmínku, stejnou
# jako za if. Když platí, nestane se nic. Když neplatí, program
# spadne s chybou AssertionError.
#
# Spusť soubor.

def cena_vstupenky(vek):
    if vek < 15:
        return 100
    elif vek > 65:
        return 120
    else:
        return 180


assert cena_vstupenky(8) == 100
assert cena_vstupenky(40) == 180
assert cena_vstupenky(70) == 120
print("První tři kontroly prošly.")

assert cena_vstupenky(65) == 120
print("Čtvrtá kontrola prošla.")


# Program spadl a v terminálu je známá chybová hláška:
#
#   Traceback (most recent call last):
#     File "02_assert.py", line 24, in <module>
#       assert cena_vstupenky(65) == 120
#              ^^^^^^^^^^^^^^^^^^^^^^^^^
#   AssertionError
#
# Čte se stejně jako hlášky z lekce 7: poslední řádek říká, co se
# stalo, a nad ním je řádek, na kterém to Python poznal. Tvrzení,
# že šedesátipětiletá zaplatí 120, neplatí.
#
# První tři asserty prošly potichu. Nic nevypsaly, a proto je tam
# print, abys viděla, že na ně došlo. Čtvrtý print už se nevypsal:
# assert, který neplatí, program zastaví.


# ----- Co se změnilo proti printu -----
#
# Správný výsledek už nemáš v hlavě ani v komentáři. Je přímo
# v kódu, za ==, a porovná ho Python.
#
# Když je všechno v pořádku, je ticho. Když něco nesedí, program
# spadne a ukáže přesně na řádek s tvrzením, které neplatí.
#
# Kontroly napíšeš jednou a pustíš je, kdykoli funkci změníš.
# Takové kontroly se jmenují testy.


# ----- Oprav to -----
#
# Změň ve funkci vek > 65 na vek >= 65 a spusť soubor znovu.
# Teď se vypíšou oba printy a program doběhne bez chyby.
#
# Pak zkus schválně pokazit první podmínku: vek < 15 přepiš na
# vek < 51. Spusť soubor. Který assert si toho všimne?
