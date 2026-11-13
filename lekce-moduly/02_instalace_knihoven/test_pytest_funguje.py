# Nejjednodušší možný test. Kontroluje jen to, že pytest je
# nainstalovaný a umí najít a spustit testy.
#
# Funkce začíná na test_, takže ji pytest najde sám.
# assert znamená „tvrdím, že“: když tvrzení platí, test projde.


def test_pytest_funguje():
    assert 1 + 1 == 2
