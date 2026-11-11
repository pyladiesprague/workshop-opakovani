# Logika hry Wordle.
# Funkce tady nic nevypisují a na nic se neptají, takže jdou snadno testovat.

DELKA_SLOVA = 5
POCET_POKUSU = 6


def vyhodnot(hadane, tajne):
    """Vrátí pro každé písmeno "spravne", "jinde" nebo "neni"."""
    vysledek = []
    for i in range(DELKA_SLOVA):
        if hadane[i] == tajne[i]:
            vysledek.append("spravne")
        elif hadane[i] in tajne:
            vysledek.append("jinde")
        else:
            vysledek.append("neni")
    return vysledek


def uprav_vstup(text):
    """Odstraní mezery kolem textu a převede ho na malá písmena."""
    return text.strip().lower()


def chyba_slova(slovo, povolena):
    """Vrátí text chyby. Když je slovo v pořádku, vrátí prázdný řetězec."""
    if len(slovo) != DELKA_SLOVA:
        return f"Slovo musí mít {DELKA_SLOVA} písmen."
    if slovo not in povolena:
        return "Takové slovo neznám."
    return ""
