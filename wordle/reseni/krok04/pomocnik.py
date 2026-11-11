# Pomocné funkce pro projekt Wordle.
# Tenhle soubor nemusíš číst ani měnit, stačí ho mít ve stejné složce jako
# svůj program. Práci se soubory a barvami si vysvětlíme později.

from pathlib import Path

SLOZKA = Path(__file__).parent

BARVY = {
    "zelena": "\033[30;42m",
    "zluta": "\033[30;43m",
    "seda": "\033[97;100m",
    "tlumena": "\033[90m",
}
KONEC_BARVY = "\033[0m"


def _cesta(soubor):
    # Vzorová řešení nemají vlastní seznamy slov, ty leží ve složce moje_hra.
    for slozka in (SLOZKA, SLOZKA.parent.parent / "moje_hra"):
        if (slozka / soubor).exists():
            return slozka / soubor
    return SLOZKA / soubor


def obarvi(text, barva):
    """Vrátí text s barevným pozadím: "zelena", "zluta", "seda" nebo "tlumena"."""
    return f"{BARVY[barva]}{text}{KONEC_BARVY}"


def vycisti_obrazovku():
    """Smaže všechno, co je v terminálu vypsané."""
    print("\033[2J\033[H", end="")


def nacti_radky(soubor):
    """Vrátí seznam řádků souboru. Když soubor neexistuje, vrátí prázdný seznam."""
    cesta = _cesta(soubor)
    if not cesta.exists():
        return []
    return cesta.read_text(encoding="utf-8").splitlines()


def pridej_radek(soubor, text):
    """Přidá na konec souboru jeden řádek. Když soubor neexistuje, založí ho."""
    with open(_cesta(soubor), "a", encoding="utf-8") as f:
        f.write(f"{text}\n")
