# Testy ke správci financí.
#
# Spouštěj je v panelu Testing (ikona baňky vlevo) nebo v terminálu
# příkazem: python -m pytest
#
# Ke každému kroku najdeš v zadání připravené testy. Zkopíruj je na konec
# tohohle souboru a piš kód ve finance.py, dokud nebudou zelené.
# Vlastní testy piš taky sem.

import finance


def ukazka():
    # Malá sada transakcí na testování. Každý test si zavolá ukazka()
    # a dostane vlastní čerstvý seznam, takže si testy navzájem nic nezmění.
    return [
        {"datum": "2026-10-28", "typ": "vydaj", "castka": 300, "kategorie": "jidlo", "popis": "pizza"},
        {"datum": "2026-11-01", "typ": "prijem", "castka": 1000, "kategorie": "vyplata", "popis": "brigáda"},
        {"datum": "2026-11-03", "typ": "vydaj", "castka": 200, "kategorie": "jidlo", "popis": "oběd"},
        {"datum": "2026-11-05", "typ": "vydaj", "castka": 150, "kategorie": "doprava", "popis": "jízdenky"},
        {"datum": "2026-11-09", "typ": "vydaj", "castka": 250, "kategorie": "jidlo", "popis": "nákup"},
    ]


def test_ukazka_ma_pet_transakci():
    # Tenhle test projde hned. Když je zelený, testy ti fungují.
    assert len(ukazka()) == 5


def test_soucet_prijmu():
    assert finance.soucet_prijmu(ukazka()) == 1000


def test_soucet_vydaju():
    assert finance.soucet_vydaju(ukazka()) == 900


def test_zustatek():
    assert finance.zustatek(ukazka()) == 100


def test_zustatek_bez_transakci():
    assert finance.zustatek([]) == 0
