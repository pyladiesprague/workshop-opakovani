# Analýza pasažérů Titaniku.
# Funkce tady nic nevypisují, takže jdou snadno testovat.

import csv
from pathlib import Path

# Složka, ve které leží tenhle soubor, a cesta k datům v ní.
# Díky tomu program data najde, ať máš ve VS Code otevřenou jakoukoliv složku.
SLOZKA = Path(__file__).parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"


def nacti_pasazery(soubor):
    """Vrátí seznam slovníků, jeden slovník na každý řádek souboru."""
    with open(soubor, encoding="utf-8") as f:
        return list(csv.DictReader(f))
