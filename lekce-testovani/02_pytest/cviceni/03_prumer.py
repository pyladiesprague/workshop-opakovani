# Cvičení 3 – pytest
# Napiš testy podle zadání. Jeden z nich neprojde. Přečti si výpis
# a oprav funkci.

# Spouštěj v terminálu ve složce cviceni:
#
#   python -m pytest 03_prumer.py
#
# Ověř aspoň tohle:
#   - průměr ze tří čísel,
#   - průměr z jediného čísla,
#   - prázdný seznam.

# Funkce prumer vrátí průměr čísel v seznamu. Pro prázdný seznam
# vrátí 0.

def prumer(cisla):
    return sum(cisla) / len(cisla)


# Sem napiš testy:
