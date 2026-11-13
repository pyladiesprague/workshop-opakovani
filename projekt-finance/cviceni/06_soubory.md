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

## 1. Testy

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

## 2. Funkce do `finance.py`

| Funkce | Co dělá |
|---|---|
| `uloz(transakce, cesta)` | zapíše seznam transakcí do souboru jako JSON |
| `nacti(cesta)` | přečte soubor a vrátí seznam transakcí |

Na začátek `finance.py` patří `import json`.

**Vlastní test:** ulož prázdný seznam a zkontroluj, že se načte zase
prázdný seznam.

## 3. Úprava `app.py`

- Transakce už neber z `ukazkova_data.py`. Na začátku programu je načti
  ze souboru `finance.json`.
- Po každém přidání a odebrání transakce seznam ulož.

Vyzkoušej to: přidej transakci, ukonči program, spusť ho znovu a nech si
vypsat transakce. Ta nová tam musí být.

Kdyby program hlásil `FileNotFoundError`, hledá soubor v jiné složce, než
ve které leží. Spouštěj `app.py` tlačítkem **Run** s otevřenou složkou
celého workshopu, případně si v terminálu přejdi do složky projektu.

Když si data pokazíš, původní `finance.json` si znovu stáhni z GitHubu,
nebo si ho nech vyrobit: v Pythonu zavolej `uloz` se seznamem
z `ukazkova_data.py`.

## Nápověda

- Zápis a čtení souboru, `json.dump` a `json.load`. `TAHAK.md`, *Soubory a JSON*.
- Nezapomeň na `encoding="utf-8"` při otevírání a `ensure_ascii=False` při
  zápisu. Bez nich se háčky a čárky pokazí, a hlídá to druhý test.

## Hotovo, když

- [ ] všechny testy jsou zelené
- [ ] přidaná transakce přežije ukončení a nové spuštění programu
- [ ] `finance.json` je po uložení pořád čitelný a jsou v něm háčky a čárky

## Když zbyde čas

- Ukládej i rozpočty. Do souboru může jít slovník se dvěma klíči:
  `{"transakce": [...], "rozpocty": {...}}`. Tahák L9, *data v datech*.
- Přidej volbu „uložit zálohu“, která data zapíše do souboru, jehož jméno
  si uživatelka zvolí.
