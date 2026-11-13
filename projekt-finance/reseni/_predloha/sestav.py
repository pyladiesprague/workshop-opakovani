"""Sestaví řešení po krocích z jedné předlohy. Nástroj pro kouče.

Spuštění:  python sestav.py

Předloha jsou soubory finance.py a app.py v této složce. Obsahují kód všech
kroků a jako "krok 7" i obarvenou verzi z bonusu Barvy v terminálu.

Předloha sama je platný Python a jde spustit (python app.py): chová se jako
nejúplnější verze, tedy krok 6 s barvami. Data si bere z ukazkova_data.py
a finance.json v této složce; obojí sem tento skript kopíruje z projektu.

Značky říkají, do kterých kroků řádek patří:

    #@ 3+            samostatný řádek: všechno pod ním patří do kroku 3 a dalších
    #@ 2-4           samostatný řádek: všechno pod ním patří do kroků 2 až 4
    #@ vse           samostatný řádek: všechno pod ním patří do všech kroků
    #@ 0             samostatný řádek: všechno pod ním je jen pro předlohu
    kód  #@6+        značka na konci řádku platí jen pro ten jeden řádek
    #@2-6| kód       řádek, který do nejúplnější verze nepatří; v předloze je
                     komentář, do kroků 2 až 6 se zapíše jako kód se stejným
                     odsazením, jaké má značka

Řádek, který se mezi kroky liší, je tedy v předloze dvakrát pod sebou:
starší podoba jako "#@1-6| ..." a nejnovější jako kód se značkou "#@7".

Testy se berou ze zadání: do test_finance.py kroku N se za startovní soubor
přidají bloky s testy ze zadani/krok1_*.md až zadani/krokN_*.md. Řešení se
tak vždycky ověřuje proti testům, které účastnice opravdu dostanou.
Obarvená verze má navíc testy z testy_barvy.py.

Výsledek se zapíše do ../krok1 až ../krok6 a ../bonusy/bonus1_barvy.
Ty složky ručně neupravuj, uprav předlohu a spusť skript znovu.

Nakonec skript spustí řešení bonusu HTML report (../bonusy/bonus2_html_report.py)
nad ukázkovými daty a stránku uloží sem jako vzorovy_report.html. Je to ukázka,
jak má výstup bonusu vypadat; stačí ji otevřít v prohlížeči.
"""

import contextlib
import io
import os
import re
import runpy
import shutil
import sys
import tempfile
import webbrowser
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
        # Samostatná značka přepíná rozsah pro další řádky.
        znacka = re.fullmatch(r"\s*#@ (\S+)", radek)
        if znacka:
            blok = None if znacka.group(1) == "vse" else znacka.group(1)
            continue

        rozsah = blok
        # Zakomentovaný řádek starší podoby: "    #@2-6| kód".
        stary = re.fullmatch(r"(\s*)#@(\S+)\| ?(.*)", radek)
        if stary:
            rozsah = stary.group(2)
            radek = stary.group(1) + stary.group(3)
        else:
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
    # Data pro předlohu samotnou, aby šla spustit. Přepíšou se čistou kopií.
    shutil.copyfile(PROJEKT / "ukazkova_data.py", PREDLOHA / "ukazkova_data.py")
    shutil.copyfile(PROJEKT / "finance.json", PREDLOHA / "finance.json")

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

    vzorovy_report()


def vzorovy_report():
    """Spustí řešení bonusu HTML report a jeho výstup uloží k předloze jako ukázku."""
    bonusy = RESENI / "bonusy"
    puvodni_slozka = Path.cwd()
    puvodni_otevreni = webbrowser.open
    # Skript zapisuje report.html do aktuální složky a otevírá prohlížeč.
    # Tady ho necháme psát do dočasné složky a prohlížeč neotvíráme.
    with tempfile.TemporaryDirectory() as docasna:
        os.chdir(docasna)
        sys.path.insert(0, str(bonusy))
        webbrowser.open = lambda *argumenty: None
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                runpy.run_path(str(bonusy / "bonus2_html_report.py"), run_name="__main__")
            html = Path("report.html").read_text(encoding="utf-8")
        finally:
            webbrowser.open = puvodni_otevreni
            sys.path.remove(str(bonusy))
            sys.modules.pop("ukazkova_data", None)
            os.chdir(puvodni_slozka)
    zapis(PREDLOHA / "vzorovy_report.html", html)
    print("_predloha/vzorovy_report.html: hotovo")


main()
