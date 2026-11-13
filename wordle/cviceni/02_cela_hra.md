# Krok 2: Celá hra

Udělej z jednoho pokusu celou hru. Hráč má šest pokusů.

## Logika

Do `logika.py` přidej dvě funkce:

- `uprav_vstup(text)` odstraní mezery kolem textu a převede ho na malá písmena.
- `chyba_slova(slovo)` vrátí `"Slovo musí mít 5 písmen."`, když slovo nemá pět písmen. Když je v pořádku, vrátí prázdný řetězec `""`.

## Testy

Na konec `test_logika.py` zkopíruj tuhle třídu a místo `___` doplň, co má funkce vrátit. Nahoře v souboru přidej nové funkce do importu.

```python
class TestVstup(unittest.TestCase):
    def test_uprav_vstup(self):
        self.assertEqual(uprav_vstup("  KOČKA "), ___)

    def test_kratke_slovo(self):
        self.assertEqual(chyba_slova("kočk"), ___)

    def test_spravna_delka(self):
        self.assertEqual(chyba_slova("kočka"), ___)
```

## Program

Ve `wordle.py` napiš dvě funkce.

`nacti_slovo()` se hráče ptá tak dlouho, dokud nezadá slovo, které projde kontrolou. Když slovo neprojde, vypíše chybu a zeptá se znovu. Vrátí upravené slovo.

`zahraj(tajne)` odehraje celou hru:

- Nejvýš šestkrát načte slovo, vyhodnotí ho a vypíše.
- Když hráč uhodne, vypíše, na kolikátý pokus se to povedlo, a hra skončí.
- Když nevyjde ani šestý pokus, prozradí tajné slovo.

Špatně zadané slovo se díky `nacti_slovo` nepočítá jako pokus.

Zasekla ses? Nápověda je v souboru [`napovedy/02_cela_hra.md`](../napovedy/02_cela_hra.md).
