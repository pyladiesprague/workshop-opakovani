"""Spustí testy ve všech složkách s řešením. Nástroj pro kouče, větev reseni.

Spuštění z kořene repozitáře:  python zkontroluj_reseni.py

Projde složky projekt-*/cviceni/reseni/NN_* a v každé spustí python -m pytest.
Každá složka se testuje zvlášť, protože soubory se v nich jmenují stejně.
"""

import subprocess
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent


def main():
    slozky = sorted(KOREN.glob("projekt-*/cviceni/reseni/[0-9][0-9]_*"))
    if len(slozky) == 0:
        print("Žádná řešení tu nejsou. Jsi na větvi reseni?")
        sys.exit(1)

    chyby = 0
    for slozka in slozky:
        vysledek = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
            cwd=slozka,
            capture_output=True,
            text=True,
        )
        radky = vysledek.stdout.strip().splitlines()
        posledni = radky[-1] if radky else vysledek.stderr.strip()
        print(f"{slozka.relative_to(KOREN)}: {posledni}")
        if vysledek.returncode != 0:
            chyby = chyby + 1

    if chyby > 0:
        print(f"Složek s chybou: {chyby}")
        sys.exit(1)
    print("Všechna řešení prošla.")


if __name__ == "__main__":
    main()
