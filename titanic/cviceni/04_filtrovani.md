# Krok 4: Přežívaly ženy častěji?

Už znáš celkový výsledek. První část pravidla je „ženy první“, tak ji ověříme. Zapiš si odhad: jaké procento žen a jaké procento mužů přežilo?

## Logika

Do `analyza.py` přidej funkci `filtruj(pasazeri, sloupec, hodnota)`. Vrátí seznam pasažérů, kteří mají v daném sloupci danou hodnotu. Jedna funkce tak poslouží pro všechny sloupce:

```python
zeny = filtruj(pasazeri, "Sex", "female")
prvni_trida = filtruj(pasazeri, "Pclass", 1)
```

## Testy

První test je hotový. Druhý doplň a třetí vymysli sama. Co má funkce vrátit, když nikdo nevyhovuje?

```python
class TestFiltruj(unittest.TestCase):
    def test_podle_textu(self):
        self.assertEqual(len(filtruj(PASAZERI, "Sex", "female")), 2)

    def test_podle_cisla(self):
        self.assertEqual(len(filtruj(PASAZERI, "Pclass", 3)), ___)
```

## Zpráva

Vypiš procento přeživších žen a mužů. Doplň poznámky. Rozdíl je velký, ale znamená to, že na ničem jiném nezáleželo?
