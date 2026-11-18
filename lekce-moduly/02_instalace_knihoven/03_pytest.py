# ---------------------------------------------
#  Pytest: knihovna na testování
# ---------------------------------------------
# Tenhle soubor se nespouští. Čti ho a dělej, co se v něm píše.
#
# V projektech dnes budeš psát testy – kousky kódu, které samy zkontrolují,
# že tvoje funkce počítají správně. Spouští je knihovna pytest. Je to
# knihovna z PyPI, stejně jako cowsay, a nainstalovala sis ji doma podle
# návodu Před workshopem. Kdyby chyběla, nainstaluj ji stejně jako cowsay:
#
#          pip install pytest
#
#
# Pytest je jiný než random nebo cowsay. Funkce z něj do svých programů
# skoro nikdy nevoláš. Pytest sám projde soubory, jejichž jméno začíná
# na test_, najde v nich funkce začínající na test_ a spustí je.
#
# Vedle tohohle souboru je jeden takový: test_pytest_funguje.py.
# Podívej se do něj a pak ho spusť:
#
#   1. Vlevo v liště klikni na ikonu baňky (Testing).
#      Pokud tam nic není, klikni na Configure Python Tests a vyber pytest.
#   2. Najdi test_pytest_funguje a klikni na šipku vedle něj.
#      Když svítí zeleně, pytest funguje a můžeš se pustit do testů.
#
# Bez VS Code jde totéž spustit v terminálu:
#
#          python -m pytest
#
# Na konci výpisu uvidíš, kolik testů prošlo (passed).
#
# Jak testy psát, se naučíš v lekci o testování, která následuje po
# modulech. Teď stačí, že pytest běží.
