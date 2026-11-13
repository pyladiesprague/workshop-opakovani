# ---------------------------------------------
#  Pytest: knihovna na testování
# ---------------------------------------------
# Tenhle soubor se nespouští. Čti ho a dělej, co se v něm píše.
#
# V projektech dnes budeš psát testy – kousky kódu, které samy zkontrolují,
# že tvoje funkce počítají správně. Spouští je knihovna pytest.
# Ta ve standardní knihovně není, takže ji nainstaluj stejně jako cowsay.
#
#   1. V terminálu (Terminal → New Terminal) napiš:
#
#          pip install pytest
#
#      Na Windows případně:   py -m pip install pytest
#      Na macOS případně:     python3 -m pip install pytest
#
#   2. Ověř, že se nainstaloval. V terminálu napiš:
#
#          python -m pytest --version
#
#      (na macOS python3 místo python). Vypíše se třeba:  pytest 8.4.2
#
#
# Pytest je jiný než random nebo cowsay. Funkce z něj do svých programů
# skoro nikdy nevoláš. Pytest sám projde soubory, jejichž jméno začíná
# na test_, najde v nich funkce začínající na test_ a spustí je.
#
# Vedle tohohle souboru je jeden takový: test_pytest_funguje.py.
# Podívej se do něj a pak ho spusť:
#
#   3. Vlevo v liště klikni na ikonu baňky (Testing).
#      Pokud tam nic není, klikni na Configure Python Tests a vyber pytest.
#   4. Najdi test_pytest_funguje a klikni na šipku vedle něj.
#      Když svítí zeleně, pytest funguje a můžeš se pustit do testů.
#
# Bez VS Code jde totéž spustit v terminálu:
#
#          python -m pytest
#
# Na konci výpisu uvidíš, kolik testů prošlo (passed).
#
# Jak testy psát, si ukážeme v další části. Teď stačí, že pytest běží.
