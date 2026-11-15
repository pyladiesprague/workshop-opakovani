# Krok 6 – Uložení do souboru

Zatím program všechno zapomene, jakmile ho ukončíš. Přidaná transakce je
při dalším spuštění pryč, protože data žijí jen v paměti. Teď je uložíš
do souboru.

Tenhle krok používá dvě věci, které jsme na lekcích neprobírali: práci se
soubory a formát JSON. Obojí najdeš vysvětlené v `TAHAK.md` v části
*Soubory a JSON*. Přečti si ji, než začneš.

Ve složce projektu je připravený soubor `finance.json`. Otevři si ho.
Jsou v něm stejné transakce jako v `ukazkova_data.py` a vypadají skoro
stejně jako v Pythonu. JSON je způsob, jak seznamy a slovníky zapsat
jako text.

## Funkce

Funkce píšeš do `finance.py`.

| Funkce | Co dělá |
|---|---|
| `uloz(transakce, cesta)` | zapíše seznam transakcí do souboru jako JSON |
| `nacti(cesta)` | přečte soubor a vrátí seznam transakcí |

Na začátek `finance.py` patří `import json`.

## Testy

Zkopíruj na konec `test_finance.py`:

```python
def test_uloz_a_nacti(tmp_path):
    cesta = tmp_path / "pokus.json"
    finance.uloz(ukazka(), cesta)
    assert finance.nacti(cesta) == ukazka()


def test_ulozeni_zachova_hacky_a_carky(tmp_path):
    cesta = tmp_path / "pokus.json"
    transakce = [
        {"datum": "2026-11-21", "typ": "vydaj", "castka": 90, "kategorie": "jidlo", "popis": "žluťoučký koláč"},
    ]
    finance.uloz(transakce, cesta)
    assert finance.nacti(cesta)[0]["popis"] == "žluťoučký koláč"
```

Parametr `tmp_path` je dočasná složka, kterou testu půjčí pytest a potom
ji sám uklidí. Testy tak nesahají na tvůj opravdový `finance.json`.
Lomítkem se k cestě složky připojí jméno souboru. Ber to jako hotový recept.

**Vlastní test:** ulož prázdný seznam a zkontroluj, že se načte zase
prázdný seznam.

## Program

Uprav `app.py`.

- Transakce už neber z `ukazkova_data.py`. Na začátku programu je načti
  ze souboru `finance.json`.
- Po každém přidání a odebrání transakce seznam ulož.

Samotné jméno `"finance.json"` Python hledá ve složce, ze které program
spouštíš, a to nemusí být složka projektu. Pak program hlásí
`FileNotFoundError`, nebo si uloží nový soubor jinam. Proto cestu slož od
složky, ve které leží `app.py`. Patří na začátek `app.py`:

```python
from pathlib import Path

SOUBOR = Path(__file__).parent / "finance.json"
```

`__file__` je cesta k souboru `app.py`, `.parent` je složka, ve které leží,
a lomítko k ní připojí jméno souboru, stejně jako u `tmp_path` v testech.
Ber to jako hotový recept. Wordle a Titanic to dělají stejně.

Vyzkoušej to: přidej transakci, ukonči program, spusť ho znovu a nech si
vypsat transakce. Ta nová tam musí být.

Když si data pokazíš, původní `finance.json` si znovu stáhni z GitHubu,
nebo si ho nech vyrobit: v Pythonu zavolej `uloz` se seznamem
z `ukazkova_data.py`.

Zasekla ses? Nápověda je v souboru [`napovedy/06_soubory.md`](../napovedy/06_soubory.md).

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] přidaná transakce přežije ukončení a nové spuštění programu
- [ ] `finance.json` je po uložení pořád čitelný a jsou v něm háčky a čárky
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
