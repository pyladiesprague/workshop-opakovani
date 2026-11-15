# Krok 2 – Celá hra

Na konci tohohle kroku má hráč šest pokusů a hra pozná výhru i prohru:

```text
Tvůj pokus: pes
Slovo musí mít 5 písmen.
Tvůj pokus: Kabát
k a b á t
+ ? - - -
Tvůj pokus: kočka
k o č k a
+ + + + +
Uhodla jsi to na 2. pokus!
```

## Funkce

Funkce píšeš do `logika.py`.

| Funkce | Co vrátí |
| --- | --- |
| `uprav_vstup(text)` | text bez mezer na začátku a na konci, převedený na malá písmena |
| `chyba_slova(slovo)` | `"Slovo musí mít 5 písmen."`, když slovo nemá pět písmen; když je v pořádku, prázdný řetězec `""` |

## Testy

Zkopíruj na konec `test_logika.py` a místo `___` doplň, co má funkce vrátit:

```python
def test_uprav_vstup():
    assert logika.uprav_vstup("  KOČKA ") == ___


def test_kratke_slovo():
    assert logika.chyba_slova("kočk") == ___


def test_spravna_delka():
    assert logika.chyba_slova("kočka") == ___
```

## Program

Program píšeš do `wordle.py`.

Napiš dvě funkce.

`nacti_slovo()` se hráče ptá tak dlouho, dokud nezadá slovo, které projde
kontrolou. Když slovo neprojde, vypíše chybu a zeptá se znovu. Vrátí upravené
slovo.

`zahraj(tajne)` odehraje celou hru:

- Nejvýš šestkrát načte slovo, vyhodnotí ho a vypíše.
- Když hráč uhodne, vypíše, na kolikátý pokus se to povedlo, a hra skončí.
- Když nevyjde ani šestý pokus, prozradí tajné slovo.

Špatně zadané slovo se díky `nacti_slovo` nepočítá jako pokus.

Zasekla ses? Nápověda je v souboru [`napovedy/02_cela_hra.md`](../napovedy/02_cela_hra.md).

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] slovo `Kabát` s velkým písmenem a mezerami kolem hra přijme
- [ ] krátké slovo hra odmítne a pokus za něj nepočítá
- [ ] po šesti špatných pokusech hra prozradí tajné slovo
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
