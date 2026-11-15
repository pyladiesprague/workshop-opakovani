# Titanic – ANALÝZA
#
# Sem piš funkce, které něco spočítají a výsledek vrátí (return).
# Nepatří sem žádný input() ani print(), ty piš do zprava.py.
# Díky tomu půjdou funkce z tohohle souboru testovat.
#
# Začni krokem 1: cviceni/01_nacteni.md

import csv
from pathlib import Path

# Složka, ve které leží tenhle soubor, a cesta k datům v ní.
# Díky tomu program data najde, ať ho spouštíš odkudkoliv.
SLOZKA = Path(__file__).parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"
