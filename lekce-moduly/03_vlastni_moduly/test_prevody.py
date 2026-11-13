# Testy k modulu prevody.py.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest
#
# Testy si modul naimportují stejně jako jakýkoli jiný program.

import prevody


def test_bod_mrazu_na_fahrenheity():
    assert prevody.na_fahrenheity(0) == 32


def test_bod_varu_na_fahrenheity():
    assert prevody.na_fahrenheity(100) == 212


def test_bod_mrazu_na_celsia():
    assert prevody.na_celsia(32) == 0


def test_maraton_na_km():
    assert prevody.mile_na_km(26.2) == 42.2
