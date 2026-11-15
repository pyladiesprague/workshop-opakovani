# Testy logiky hry Wordle.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest
#
# V prvních krocích najdeš v zadání připravené testy. Zkopíruj je na konec
# tohohle souboru a piš kód v logika.py, dokud nebudou zelené.
# V dalších krocích sem píšeš testy vlastní.

import logika

# Zkratky pro výsledky jednotlivých písmen, ať se testy dobře čtou.
S = "spravne"
J = "jinde"
N = "neni"


def test_slovo_ma_pet_pismen():
    # Tenhle test projde hned. Když je zelený, testy ti fungují.
    assert logika.DELKA_SLOVA == 5
