# Pomocné funkce pro projekt Wordle.
# Tenhle soubor nemusíš číst ani měnit, stačí ho mít ve stejné složce jako
# svůj program. Práci se soubory a barvami si vysvětlíme později.

import os
from pathlib import Path

# Složka, ve které leží tenhle soubor. Hledají se v ní seznamy slov a statistiky.
SLOZKA = Path(__file__).parent.parent.parent.parent

BARVY = {
    "zelena": "\033[30;42m",
    "zluta": "\033[30;43m",
    "seda": "\033[97;100m",
    "tlumena": "\033[90m",
}
KONEC_BARVY = "\033[0m"


def obarvi(text, barva):
    """Vrátí text s barevným pozadím: "zelena", "zluta", "seda" nebo "tlumena"."""
    return f"{BARVY[barva]}{text}{KONEC_BARVY}"


def vycisti_obrazovku():
    """Smaže všechno, co je v terminálu vypsané."""
    # Windows má na mazání příkaz cls, macOS a Linux příkaz clear.
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def nacti_radky(soubor):
    """Vrátí seznam řádků souboru. Když soubor neexistuje, vrátí prázdný seznam."""
    cesta = SLOZKA / soubor
    if not cesta.exists():
        return []
    return cesta.read_text(encoding="utf-8").splitlines()


def pridej_radek(soubor, text):
    """Přidá na konec souboru jeden řádek. Když soubor neexistuje, založí ho."""
    with open(SLOZKA / soubor, "a", encoding="utf-8") as f:
        f.write(f"{text}\n")
