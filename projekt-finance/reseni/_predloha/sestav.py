"""Sestaví řešení po krocích z jedné předlohy. Nástroj pro kouče.

Spuštění:  python sestav.py

Předloha (finance.py a app.py v této složce) obsahuje kód všech kroků.
Značky říkají, do kterých kroků řádek patří:

    #@ 3+        samostatný řádek: všechno pod ním patří do kroku 3 a dalších
    #@ 2-4       samostatný řádek: všechno pod ním patří do kroků 2 až 4
    #@ vse       samostatný řádek: všechno pod ním patří do všech kroků
    kód  #@6     značka na konci řádku platí jen pro ten jeden řádek

Testy se berou ze zadání: do test_finance.py kroku N se za startovní soubor
přidají bloky s testy ze zadani/krok1_*.md až zadani/krokN_*.md. Řešení se
tak vždycky ověřuje proti testům, které účastnice opravdu dostanou.

Výsledek se zapíše do ../krok1 až ../krok6. Ty složky ručně neupravuj,
uprav předlohu a spusť skript znovu.
"""

import re
import shutil
from pathlib import Path

PREDLOHA = Path(__file__).resolve().parent
RESENI = PREDLOHA.parent
PROJEKT = RESENI.parent
POCET_KROKU = 6


def plati(rozsah, krok):
    if rozsah.endswith("+"):
        return krok >= int(rozsah[:-1])
    if "-" in rozsah:
        od, do = rozsah.split("-")
        return int(od) <= krok <= int(do)
    return krok == int(rozsah)


def vyber_krok(text, krok):
    radky = []
    blok = None
    for radek in text.splitlines():
        znacka = re.fullmatch(r"\s*#@ (\S+)", radek)
        if znacka:
            blok = None if znacka.group(1) == "vse" else znacka.group(1)
            continue

        rozsah = blok
        znacka = re.search(r"\s+#@(\S+)$", radek)
        if znacka:
            rozsah = znacka.group(1)
            radek = radek[: znacka.start()]

        if rozsah is None or plati(rozsah, krok):
            radky.append(radek)

    vysledek = "\n".join(radky) + "\n"
    vysledek = re.sub(r"\n{4,}", "\n\n\n", vysledek)
    return vysledek.replace("{KROK}", str(krok))


def testy_do_kroku(krok):
    text = (PROJEKT / "test_finance.py").read_text(encoding="utf-8")
    for cislo in range(1, krok + 1):
        zadani = sorted((PROJEKT / "zadani").glob(f"krok{cislo}_*.md"))
        if len(zadani) != 1:
            raise SystemExit(f"Čekám právě jedno zadání kroku {cislo}, mám {len(zadani)}.")
        obsah = zadani[0].read_text(encoding="utf-8")
        for blok in re.findall(r"```python\n(.*?)```", obsah, flags=re.DOTALL):
            if "def test_" in blok:
                text = text.rstrip("\n") + "\n\n\n" + blok.strip("\n") + "\n"
    return text


def zapis(cesta, text):
    cesta.write_text(text, encoding="utf-8", newline="\n")


def main():
    for krok in range(1, POCET_KROKU + 1):
        slozka = RESENI / f"krok{krok}"
        slozka.mkdir(exist_ok=True)
        for jmeno in ["finance.py", "app.py"]:
            predloha = (PREDLOHA / jmeno).read_text(encoding="utf-8")
            zapis(slozka / jmeno, vyber_krok(predloha, krok))
        zapis(slozka / "test_finance.py", testy_do_kroku(krok))
        # Aby šla složka použít samostatně jako startovní bod dalšího kroku.
        shutil.copyfile(PROJEKT / "ukazkova_data.py", slozka / "ukazkova_data.py")
        if krok == POCET_KROKU:
            shutil.copyfile(PROJEKT / "finance.json", slozka / "finance.json")
        print(f"krok{krok}: hotovo")

    # Řešení bonusů se píšou ručně, jen potřebují mít data vedle sebe.
    shutil.copyfile(PROJEKT / "ukazkova_data.py", RESENI / "bonusy" / "ukazkova_data.py")


main()
