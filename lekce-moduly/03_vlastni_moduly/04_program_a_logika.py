# ---------------------------------------------
#  Program, logika a testy
# ---------------------------------------------
# Spusť soubor a zkus převést pár teplot.
#
# Tohle je ten soubor, který spouštíš. Je v něm všechno, co mluví
# s uživatelkou: input a print. Počítání si půjčuje z prevody.py.

from prevody import na_celsia, na_fahrenheity

print("Převodník teplot")
smer = input("Převést na C, nebo na F? ").strip().upper()
hodnota = float(input("Teplota: "))

if smer == "F":
    print(f"{hodnota} °C je {round(na_fahrenheity(hodnota), 1)} °F.")
elif smer == "C":
    print(f"{hodnota} °F je {round(na_celsia(hodnota), 1)} °C.")
else:
    print("Napiš C, nebo F.")


# Ve složce teď leží tři druhy souborů:
#
#   prevody.py              logika     funkce, které počítají a vrací výsledek
#   04_program_a_logika.py  program    input, print, spouští se tlačítkem Run
#   test_prevody.py         testy      kontrolují funkce z prevody.py
#
# Otevři test_prevody.py. Testy si modul importují úplně stejně jako
# tenhle program – import prevody. Program s input() otestovat nejde,
# test by čekal na odpověď. Funkci, která jen vrátí číslo, ano.
#
# Stejně jsou rozdělené i projekty, na kterých dnes budeš pracovat.
# Ve financích je to finance.py (logika), app.py (program)
# a test_finance.py (testy).
