# Řešení bonusu 3 – pytest
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# U tebe se tenhle soubor jmenuje test_spropitne.py a leží ve složce
# cviceni_bonusy vedle spropitne.py. Tady má jméno podle zadání, a tak
# ho pytest sám nenajde. Spustíš ho jménem v terminálu ve složce reseni:
#
#   python -m pytest 03_test_modulu.py
#
# Modul spropitne.py je kvůli tomu zkopírovaný i sem.

import spropitne


def test_deset_procent():
    assert spropitne.spropitne(500, 10) == 50


def test_nulova_castka():
    assert spropitne.spropitne(0, 10) == 0


def test_celkem():
    assert spropitne.celkem(500, 10) == 550
