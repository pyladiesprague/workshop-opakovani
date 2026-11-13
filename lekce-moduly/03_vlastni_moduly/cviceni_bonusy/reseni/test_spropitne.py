# Řešení bonusu 2 – Otestuj svůj modul
# Tvoje řešení může vypadat jinak, a to je v pořádku.
#
# Soubor patří do složky cviceni, vedle spropitne.py.

import spropitne


def test_deset_procent():
    assert spropitne.spropitne(500, 10) == 50


def test_nulova_castka():
    assert spropitne.spropitne(0, 10) == 0


def test_celkem():
    assert spropitne.celkem(500, 10) == 550
