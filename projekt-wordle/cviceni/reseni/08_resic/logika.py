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


def filtruj(mozna, hadane, vysledek):
    """Vrátí slova, která by pro tohle hádané slovo dala stejný výsledek."""
    zbyla = []
    for slovo in mozna:
        if vyhodnot(hadane, slovo) == vysledek:
            zbyla.append(slovo)
    return zbyla


def spocitej_pismena(slova):
    """Vrátí slovník: ve kolika slovech se které písmeno vyskytuje."""
    cetnosti = {}
    for slovo in slova:
        videna = ""
        for pismeno in slovo:
            if pismeno not in videna:
                videna = videna + pismeno
                if pismeno in cetnosti:
                    cetnosti[pismeno] = cetnosti[pismeno] + 1
                else:
                    cetnosti[pismeno] = 1
    return cetnosti


def ohodnot(slovo, cetnosti):
    """Sečte body za různá písmena ve slově."""
    body = 0
    videna = ""
    for pismeno in slovo:
        if pismeno not in videna:
            videna = videna + pismeno
            body = body + cetnosti[pismeno]
    return body


def nejlepsi_slovo(mozna):
    """Vrátí slovo s nejvíc body. Při shodě bodů vyhrává dřívější slovo."""
    cetnosti = spocitej_pismena(mozna)
    nejlepsi = mozna[0]
    for slovo in mozna:
        if ohodnot(slovo, cetnosti) > ohodnot(nejlepsi, cetnosti):
            nejlepsi = slovo
    return nejlepsi
