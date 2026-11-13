# Řešení bonusu 1 – Modul, který importuje modul
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# 1. Ve složce cviceni_bonusy vytvoř soubor kostky.py s funkcemi:
#
#     hod()              vrátí náhodné číslo od 1 do 6
#     hod_vice(pocet)    vrátí seznam s tolika hody, kolik je pocet
#
#     Modul kostky.py si sám importuje randrange z modulu random.
#     Moduly můžou importovat další moduly, stejně jako programy.
#
# 2. Tady se zeptej, kolika kostkami hodit, hoď jimi a vypiš
#     všechny hody a jejich součet.

# Funkce jsou v souboru kostky.py vedle tohohle.

from kostky import hod_vice

pocet = int(input("Kolika kostkami hodit? "))
hody = hod_vice(pocet)

print("Padlo:", hody)
print("Součet:", sum(hody))
