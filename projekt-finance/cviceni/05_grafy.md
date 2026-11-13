# Krok 5 – Grafy v terminálu

Čísla jsou přesná, ale obrázek je rychlejší. Graf nakreslíš ze znaků,
žádnou knihovnu nepotřebuješ.

```text
Co chceš udělat? 8
bydleni    ██████████████████████████████   28000 Kč
jidlo      ████████                          8260 Kč
doprava    █                                 1100 Kč
zabava     █                                 1310 Kč
ostatni    █                                 1290 Kč
```

Nejdelší sloupec patří nejvyšší částce a má pevnou šířku, tady 30 znaků.
Ostatní jsou kratší ve stejném poměru.

Znak `█` si zkopíruj odsud. Kdyby se ti v terminálu nezobrazil správně,
použij `#`.

## Funkce

Funkce píšeš do `finance.py`.

| Funkce | Co vrátí |
|---|---|
| `sloupec(hodnota, nejvyssi, sirka)` | text ze znaků `█`, dlouhý podle toho, jak velká je `hodnota` proti `nejvyssi`; nejvyšší hodnota dostane `sirka` znaků |

Dvě věci, na které testy myslí:

- Malá částka by po zaokrouhlení vyšla na nula znaků a z grafu by zmizela.
  Každá částka větší než nula má mít aspoň jeden znak.
- Když je `nejvyssi` nula, nesmí funkce spadnout na dělení nulou.

## Testy

Zkopíruj na konec `test_finance.py`:

```python
def test_sloupec_nejvyssi_hodnoty_ma_plnou_sirku():
    assert finance.sloupec(100, 100, 10) == "█" * 10


def test_sloupec_polovicni_hodnoty_je_polovicni():
    assert finance.sloupec(50, 100, 10) == "█" * 5


def test_sloupec_nuly_je_prazdny():
    assert finance.sloupec(0, 100, 10) == ""


def test_sloupec_male_hodnoty_je_videt():
    assert finance.sloupec(1, 1000, 10) == "█"


def test_sloupec_kdyz_je_nejvyssi_nula():
    assert finance.sloupec(0, 0, 10) == ""
```

**Vlastní test:** jak dlouhý má být sloupec pro hodnotu 75 ze 100 při
šířce 20? Napiš na to test.

## Program

Menu je v `app.py`.

Přidej volbu `8 – graf výdajů`. Pro každou kategorii vypíše její název,
sloupec a částku. Nejvyšší částku, podle které se sloupce měří, zjisti
z hodnot slovníku, který ti vrátí `vydaje_podle_kategorie`.

Když žádné výdaje nejsou, vypiš o tom zprávu.

Aby částky za sloupci stály pod sebou, zarovnej i sloupec na pevnou šířku.

Zasekla ses? Nápověda je v souboru [`napovedy/05_grafy.md`](../napovedy/05_grafy.md).

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] graf z ukázkových dat vypadá jako ukázka nahoře
- [ ] částky za sloupci stojí pod sebou
