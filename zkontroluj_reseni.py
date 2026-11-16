"""Zkontroluje všechna řešení projektů. Nástroj pro kouče, větev reseni.

Spuštění z kořene repozitáře:  python zkontroluj_reseni.py

1. Ve složkách projekt-*/cviceni/reseni/NN_* a projekt-*/bonusy/reseni/NN_*
   spustí python -m pytest. Každá složka se testuje zvlášť, protože soubory
   se v nich jmenují stejně.
2. Skripty projekt-*/bonusy/reseni/NN_*.py nemají testy, a tak je jen spustí:
   musí doběhnout bez chyby. Skripty, které čekají na input(), přeskočí
   a vypíše je, ať je vidět, co zkontrolované není.

Potřebuje pytest a pro bonus Titanicu 2 knihovnu plotext:
    python -m pip install pytest plotext==5.3.2

Stejně to běží na GitHubu po každém pushi do reseni (.github/workflows/reseni.yml).
"""

import os
import subprocess
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent
LIMIT_SEKUND = 60

# Výpisy skriptů obsahují háčky a znaky jako █. Bez UTF-8 by na Windows
# spadly při zápisu do zachyceného výstupu, i když jsou v pořádku.
PROSTREDI = {**os.environ, "PYTHONIOENCODING": "utf-8"}


def spust(prikaz, slozka):
    """Spustí příkaz ve složce. Vrátí (prošlo, poslední řádek výpisu)."""
    try:
        vysledek = subprocess.run(
            prikaz,
            cwd=slozka,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdin=subprocess.DEVNULL,
            timeout=LIMIT_SEKUND,
            env=PROSTREDI,
        )
    except subprocess.TimeoutExpired:
        return False, f"nedoběhl do {LIMIT_SEKUND} s"
    vypis = vysledek.stdout if vysledek.returncode == 0 else vysledek.stderr or vysledek.stdout
    radky = vypis.strip().splitlines()
    return vysledek.returncode == 0, radky[-1] if radky else ""


def main():
    slozky = sorted(KOREN.glob("projekt-*/cviceni/reseni/[0-9][0-9]_*/")) + sorted(
        KOREN.glob("projekt-*/bonusy/reseni/[0-9][0-9]_*/")
    )
    skripty = sorted(KOREN.glob("projekt-*/bonusy/reseni/[0-9][0-9]_*.py"))
    if len(slozky) == 0:
        print("Žádná řešení tu nejsou. Jsi na větvi reseni?")
        sys.exit(1)

    chyby = 0
    for slozka in slozky:
        proslo, radek = spust([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"], slozka)
        print(f"{slozka.relative_to(KOREN).as_posix()}: {radek}")
        if not proslo:
            chyby = chyby + 1

    preskocene = []
    for skript in skripty:
        jmeno = skript.relative_to(KOREN).as_posix()
        if "input(" in skript.read_text(encoding="utf-8"):
            preskocene.append(jmeno)
            continue
        proslo, radek = spust([sys.executable, skript.name], skript.parent)
        print(f"{jmeno}: {'doběhl' if proslo else 'CHYBA ' + radek}")
        if not proslo:
            chyby = chyby + 1

    for jmeno in preskocene:
        print(f"{jmeno}: přeskočeno, čeká na input()")

    if chyby > 0:
        print(f"Řešení s chybou: {chyby}")
        sys.exit(1)
    print("Všechna řešení prošla.")


if __name__ == "__main__":
    main()
