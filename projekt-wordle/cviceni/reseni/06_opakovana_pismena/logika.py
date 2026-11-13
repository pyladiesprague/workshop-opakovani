# Logika hry Wordle.
# Funkce tady nic nevypisují a na nic se neptají, takže jdou snadno testovat.

DELKA_SLOVA = 5
POCET_POKUSU = 6


def vyhodnot(hadane, tajne):
    """Vrátí pro každé písmeno "spravne", "jinde" nebo "neni"."""
    vysledek = []
    zbyla = []

    # První průchod: najdi přesné shody. Písmena tajného slova,
    # která hráč netrefil, si schovej do seznamu.
    for i in range(DELKA_SLOVA):
        if hadane[i] == tajne[i]:
            vysledek.append("spravne")
        else:
            vysledek.append("neni")
            zbyla.append(tajne[i])

    # Druhý průchod: "jinde" dostane písmeno, jen dokud nějaké zbývá.
    for i in range(DELKA_SLOVA):
        if vysledek[i] != "spravne" and hadane[i] in zbyla:
            vysledek[i] = "jinde"
            zbyla.remove(hadane[i])

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


def aktualizuj_pismena(pismena, hadane, vysledek):
    """Zapíše do slovníku, co hráč o každém písmenu zjistil."""
    for i in range(DELKA_SLOVA):
        pismeno = hadane[i]
        if vysledek[i] == "spravne":
            pismena[pismeno] = "spravne"
        elif pismeno not in pismena:
            pismena[pismeno] = vysledek[i]
