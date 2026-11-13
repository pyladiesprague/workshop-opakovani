# Řešení bonusu 2 – Otestuj svůj modul
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš testy k modulu spropitne.py ze cvičení 1.
#
#     1. Ve složce cviceni (tam, kde leží spropitne.py) vytvoř soubor
#        test_spropitne.py. Jméno musí začínat na test_, jinak ho
#        pytest nenajde.
#     2. Nahoře naimportuj modul: import spropitne
#     3. Napiš aspoň tři testy, každý jako funkci začínající na test_:
#          - 10 % z 500 Kč je 50 Kč,
#          - spropitné z 0 Kč je 0 Kč,
#          - celkem za 500 Kč s 10 % je 550 Kč.
#     4. Spusť je v panelu Testing a dívej se, jestli svítí zeleně.
#
#     Jak test vypadá, se podívej do 03_vlastni_moduly/test_prevody.py.

# U tebe se tenhle soubor jmenuje test_spropitne.py a leží ve složce
# cviceni vedle spropitne.py. Tady má jméno podle zadání, a tak ho pytest
# sám nenajde. Spustíš ho jménem: python -m pytest 02_test_modulu.py
# Modul spropitne.py je kvůli tomu zkopírovaný i sem.

import spropitne


def test_deset_procent():
    assert spropitne.spropitne(500, 10) == 50


def test_nulova_castka():
    assert spropitne.spropitne(0, 10) == 0


def test_celkem():
    assert spropitne.celkem(500, 10) == 550
