"""Sestaví řešení po krocích z jedné předlohy. Nástroj pro kouče.

Spuštění:  python sestav.py

Předloha (finance.py a app.py v této složce) obsahuje kód všech kroků
a jako "krok 7" i obarvenou verzi z bonusu Barvy v terminálu.
Značky říkají, do kterých kroků řádek patří:

    #@ 3+        samostatný řádek: všechno pod ním patří do kroku 3 a dalších
    #@ 2-4       samostatný řádek: všechno pod ním patří do kroků 2 až 4
    #@ vse       samostatný řádek: všechno pod ním patří do všech kroků
    kód  #@6     značka na konci řádku platí jen pro ten jeden řádek

Testy se berou ze zadání: do test_finance.py kroku N se za startovní soubor
přidají bloky s testy ze zadani/krok1_*.md až zadani/krokN_*.md. Řešení se
tak vždycky ověřuje proti testům, které účastnice opravdu dostanou.
Obarvená verze má navíc testy z testy_barvy.py.

Výsledek se zapíše do ../krok1 až ../krok6 a ../bonusy/bonus1_barvy.
Ty složky ručně neupravuj, uprav předlohu a spusť skript znovu.
"""

import re
import shutil
from pathlib import Path

PREDLOHA = Path(__file__).resolve().parent
RESENI = PREDLOHA.parent
PROJEKT = RESENI.parent
POCET_KROKU = 6
KROK_BARVY = 7


def plati(rozsah, krok):
    if rozsah.endswith("+"):
        return krok >= int(rozsah[:-1])
    if "-" in rozsah:
        od, do = rozsah.split("-")
        return int(od) <= krok <= int(do)
    return krok == int(rozsah)


def vyber_krok(text, krok, titulek):
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
    return vysledek.replace("{TITULEK}", titulek)


def pridej_testy(text, testy):
    return text.rstrip("\n") + "\n\n\n" + testy.strip("\n") + "\n"


def testy_do_kroku(krok):
    text = (PROJEKT / "test_finance.py").read_text(encoding="utf-8")
    for cislo in range(1, krok + 1):
        zadani = sorted((PROJEKT / "zadani").glob(f"krok{cislo}_*.md"))
        if len(zadani) != 1:
            raise SystemExit(f"Čekám právě jedno zadání kroku {cislo}, mám {len(zadani)}.")
        obsah = zadani[0].read_text(encoding="utf-8")
        for blok in re.findall(r"```python\n(.*?)```", obsah, flags=re.DOTALL):
            if "def test_" in blok:
                text = pridej_testy(text, blok)
    return text


def zapis(cesta, text):
    cesta.write_text(text, encoding="utf-8", newline="\n")


def sestav(slozka, krok, titulek, testy):
    slozka.mkdir(parents=True, exist_ok=True)
    for jmeno in ["finance.py", "app.py"]:
        predloha = (PREDLOHA / jmeno).read_text(encoding="utf-8")
        zapis(slozka / jmeno, vyber_krok(predloha, krok, titulek))
    zapis(slozka / "test_finance.py", testy)
    # Aby šla složka použít samostatně, třeba jako startovní bod dalšího kroku.
    shutil.copyfile(PROJEKT / "ukazkova_data.py", slozka / "ukazkova_data.py")
    if krok >= POCET_KROKU:
        shutil.copyfile(PROJEKT / "finance.json", slozka / "finance.json")
    print(f"{slozka.relative_to(RESENI).as_posix()}: hotovo")


def main():
    for krok in range(1, POCET_KROKU + 1):
        sestav(RESENI / f"krok{krok}", krok, f"krok {krok}", testy_do_kroku(krok))

    testy_barvy = (PREDLOHA / "testy_barvy.py").read_text(encoding="utf-8")
    sestav(
        RESENI / "bonusy" / "bonus1_barvy",
        KROK_BARVY,
        "bonus 1, Barvy v terminálu",
        pridej_testy(testy_do_kroku(POCET_KROKU), testy_barvy),
    )

    # Ostatní řešení bonusů se píšou ručně, jen potřebují mít data vedle sebe.
    shutil.copyfile(PROJEKT / "ukazkova_data.py", RESENI / "bonusy" / "ukazkova_data.py")


main()
