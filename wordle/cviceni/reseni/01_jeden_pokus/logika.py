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
