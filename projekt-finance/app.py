# Správce osobních financí – MENU
#
# Tenhle soubor spouštíš (Run). Ptá se uživatelky, co chce udělat,
# volá funkce z finance.py a vypisuje výsledky.
# Patří sem všechno s input() a print().
#
# Začni krokem 1: zadani/krok1_zaklad.md

from ukazkova_data import transakce

print("Správce osobních financí")
print(f"Načteno transakcí: {len(transakce)}")
