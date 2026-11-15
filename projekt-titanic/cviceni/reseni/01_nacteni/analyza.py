# Řešení – krok 1: Titanic – analýza
# Tvoje řešení může vypadat jinak, a to je v pořádku.
# Funkce tady nic nevypisují, takže jdou snadno testovat.

import csv
from pathlib import Path

# Data leží ve složce projektu.
SLOZKA = Path(__file__).parent.parent.parent.parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"


def nacti_pasazery(soubor):
    """Vrátí seznam slovníků, jeden slovník na každý řádek souboru."""
    with open(soubor, encoding="utf-8") as f:
        return list(csv.DictReader(f))
