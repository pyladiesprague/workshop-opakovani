# Testy funkcí z analyza.py.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest
#
# V prvních krocích najdeš v zadání připravené testy. Zkopíruj je na konec
# tohohle souboru a piš kód v analyza.py, dokud nebudou zelené.
# V dalších krocích sem píšeš testy vlastní.

import analyza


def test_soubor_s_daty_existuje():
    # Tenhle test projde hned. Když je zelený, testy ti fungují.
    assert analyza.SOUBOR.exists()
