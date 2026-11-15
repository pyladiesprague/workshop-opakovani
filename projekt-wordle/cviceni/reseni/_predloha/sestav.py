"""Sestaví řešení po krocích z jedné předlohy. Nástroj pro kouče, větev reseni.

Spuštění:  python sestav.py

Předloha jsou soubory v této složce (viz SABLONY níž). Každý obsahuje kód
všech kroků a značky říkají, do kterých kroků která část patří:

    #@ 3+        všechno pod značkou patří do kroku 3 a dalších
    #@ 2-4       všechno pod značkou patří do kroků 2 až 4
    #@ 5         všechno pod značkou patří jen do kroku 5
    #@ vse       všechno pod značkou patří do všech kroků
    #@ importy   na tohle místo skript doplní importy z modulů v MODULY
                 podle toho, která jména se v programu opravdu používají

Značka je vždy na samostatném řádku a platí až do další značky. Funkce,
která se mezi kroky mění, je v předloze víckrát pod sebou, pokaždé s jiným
rozsahem kroků. Předloha proto sama spustit nejde, spouští se až výsledek.

Kroky skript najde podle zadání v ../../NN_nazev.md. Výsledek zapíše do
../NN_nazev/, tedy do složky se stejným jménem, jako má zadání kroku. Ty
složky ručně neupravuj, uprav předlohu a spusť skript znovu.

Do ../../../bonusy/reseni zkopíruje moduly z posledního kroku, aby šla
spustit řešení bonusů.

Datové soubory se nekopírují. Řešení si je berou ze složky projektu.

Nakonec skript v každé složce kroku spustí testy (python -m pytest).
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

PREDLOHA = Path(__file__).resolve().parent
RESENI = PREDLOHA.parent
CVICENI = RESENI.parent
PROJEKT = CVICENI.parent
BONUSY = PROJEKT / "bonusy" / "reseni"

# --- nastavení projektu ----------------------------------------------------
SABLONY = ["logika.py", "wordle.py", "test_logika.py"]
PROGRAM = "wordle.py"     # soubor, do kterého se doplňují importy
MODULY = ["logika", "pomocnik"]       # moduly, ze kterých program importuje
Z_PROJEKTU = ["pomocnik.py"]    # soubory, které se berou ze složky projektu
DO_BONUSU = ["logika.py", "pomocnik.py"]
HLAVICKY = ["logika.py", "wordle.py"]  # soubory, které dostanou hlavičku řešení
# ---------------------------------------------------------------------------

ZNACKA = re.compile(r"^\s*#@ (\S+)\s*$")
# Soubory v projektu hledají data vedle sebe. Řešení leží hlouběji.
SLOZKA_V_PROJEKTU = "SLOZKA = Path(__file__).parent\n"
SLOZKA_V_KROKU = "SLOZKA = Path(__file__).parent.parent.parent.parent\n"
SLOZKA_V_BONUSECH = "SLOZKA = Path(__file__).parent.parent.parent\n"


def kroky():
    """Vrátí jména kroků podle souborů se zadáním, třeba '01_jeden_pokus'."""
    jmena = []
    for soubor in sorted(CVICENI.glob("[0-9][0-9]_*.md")):
        jmena.append(soubor.stem)
    return jmena


def plati(rozsah, krok):
    if rozsah == "vse":
        return True
    if rozsah.endswith("+"):
        return krok >= int(rozsah[:-1])
    if "-" in rozsah:
        od, do = rozsah.split("-")
        return int(od) <= krok <= int(do)
    return krok == int(rozsah)


def vyber(text, krok):
    """Vrátí řádky předlohy, které patří do daného kroku."""
    radky = []
    rozsah = "vse"
    for radek in text.splitlines():
        znacka = ZNACKA.match(radek)
        if znacka is None:
            if plati(rozsah, krok):
                radky.append(radek)
        elif znacka.group(1) == "importy":
            if plati(rozsah, krok):
                radky.append(radek)
        else:
            rozsah = znacka.group(1)
    return "\n".join(radky)


def uklid(text):
    """Nejvýš dva prázdné řádky za sebou, žádné na začátku a na konci."""
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip("\n") + "\n"


def verejna_jmena(text):
    """Jména funkcí a konstant, která modul nabízí."""
    return re.findall(r"^def (\w+)", text, re.M) + re.findall(
        r"^([A-Z][A-Z_]*) =", text, re.M
    )


def radek_importu(modul, jmena):
    jmena = sorted(jmena)
    radek = f"from {modul} import {', '.join(jmena)}"
    if len(radek) <= 88:
        return radek
    return f"from {modul} import (\n" + "".join(f"    {j},\n" for j in jmena) + ")"


def dopln_importy(program, moduly):
    """Nahradí řádek '#@ importy' importy jmen, která program používá."""
    importy = []
    for modul in MODULY:
        pouzita = []
        for jmeno in verejna_jmena(moduly[modul]):
            if re.search(rf"\b{jmeno}\b", program):
                pouzita.append(jmeno)
        if pouzita:
            importy.append(radek_importu(modul, pouzita))
    return program.replace("#@ importy", "\n".join(importy))


def nazev_kroku(jmeno_kroku):
    """Název z titulku zadání: „# Krok 3 – Seznam slov“ → „Seznam slov“."""
    zadani = PROJEKT / "cviceni" / f"{jmeno_kroku}.md"
    prvni = zadani.read_text(encoding="utf-8").split("\n", 1)[0]
    shoda = re.fullmatch(r"# Krok \d+ – (.+)", prvni)
    if not shoda:
        raise SystemExit(f"{zadani.name} nezačíná titulkem „# Krok N – Název“.")
    return shoda[1]


def s_hlavickou(jmeno, text, krok, nazev):
    """První řádek souboru nahradí hlavičkou řešení, stejnou jako v materialy."""
    if jmeno not in HLAVICKY:
        return text
    zbytek = text.split("\n", 1)[1]
    return (
        f"# Řešení kroku {krok} – {nazev}\n"
        "# Tvoje řešení může vypadat jinak, a to je v pořádku.\n" + zbytek
    )


def sestav_krok(krok, jmeno_kroku):
    slozka = RESENI / jmeno_kroku
    if slozka.exists():
        shutil.rmtree(slozka)
    slozka.mkdir()

    soubory = {}
    for jmeno in Z_PROJEKTU:
        soubory[jmeno] = (PROJEKT / jmeno).read_text(encoding="utf-8")
    for jmeno in SABLONY:
        predloha = (PREDLOHA / jmeno).read_text(encoding="utf-8")
        soubory[jmeno] = uklid(vyber(predloha, krok))

    moduly = {}
    for modul in MODULY:
        moduly[modul] = soubory[f"{modul}.py"]
    soubory[PROGRAM] = uklid(dopln_importy(soubory[PROGRAM], moduly))

    nazev = nazev_kroku(jmeno_kroku)
    for jmeno in soubory:
        text = s_hlavickou(jmeno, soubory[jmeno], krok, nazev)
        text = text.replace(SLOZKA_V_PROJEKTU, SLOZKA_V_KROKU)
        (slozka / jmeno).write_text(text, encoding="utf-8", newline="\n")
    return slozka


def spust_testy(slozka):
    vysledek = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
        cwd=slozka,
        capture_output=True,
        text=True,
    )
    radky = vysledek.stdout.strip().splitlines()
    posledni = radky[-1] if radky else vysledek.stderr.strip()
    print(f"{slozka.name}: {posledni}")
    return vysledek.returncode == 0


def main():
    vse_v_poradku = True
    posledni = None
    for cislo, jmeno_kroku in enumerate(kroky(), start=1):
        posledni = sestav_krok(cislo, jmeno_kroku)
        if not spust_testy(posledni):
            vse_v_poradku = False

    BONUSY.mkdir(parents=True, exist_ok=True)
    for jmeno in DO_BONUSU:
        text = (posledni / jmeno).read_text(encoding="utf-8")
        text = text.replace(SLOZKA_V_KROKU, SLOZKA_V_BONUSECH)
        (BONUSY / jmeno).write_text(text, encoding="utf-8", newline="\n")

    for cache in PROJEKT.rglob("__pycache__"):
        shutil.rmtree(cache)

    if not vse_v_poradku:
        print("Některé testy neprošly.")
        sys.exit(1)
    print("Hotovo, všechny testy prošly.")


if __name__ == "__main__":
    main()
