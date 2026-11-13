# Řešení – Správce osobních financí

Řešení je jedno z mnoha možných. Když ti program funguje a testy jsou
zelené, tvoje řešení je stejně dobré, i když vypadá jinak.

## Řešení po krocích

Složka `krokN/` obsahuje celý projekt ve stavu po dokončení kroku N:
`finance.py`, `app.py`, `test_finance.py` s testy všech dosavadních kroků
a `ukazkova_data.py`. Složka `krok6/` má navíc `finance.json`.

| Složka | Stav |
|---|---|
| `krok1/` | výpis a zůstatek |
| `krok2/` | + přidání a odebrání transakce, kontrola vstupu |
| `krok3/` | + přehled měsíce, výdaje podle kategorií |
| `krok4/` | + rozpočty |
| `krok5/` | + graf výdajů |
| `krok6/` | + ukládání do souboru |

### Jako startovní bod

Zasekla ses v kroku 3 a chceš pokračovat krokem 4? Zkopíruj si soubory
`finance.py`, `app.py` a `test_finance.py` ze složky `krok3/` do složky
projektu místo svých a pokračuj zadáním kroku 4. Svoje původní soubory si
předtím někam schovej, ať se k nim můžeš vrátit.

## Bonusy

Ve složce `bonusy/` jsou řešení prvních čtyř bonusů. Ostatní bonusy
řešení nemají, jsou to otevřené úlohy.

- `bonus1_barvy/` je celý projekt po kroku 6 s barevným výstupem. Hodí se
  i na ukázku na začátku dne, co se bude stavět.
- `bonus2_html_report.py`, `bonus3_hledani.py` a `bonus4_razeni.py` jsou
  samostatné soubory, každý jde spustit zvlášť.

## Pro kouče

- Složky `krok1/` až `krok6/` a `bonusy/bonus1_barvy/` se generují z předlohy v `_predloha/`.
  Ručně je neupravuj. Uprav `_predloha/finance.py` nebo `_predloha/app.py`
  a spusť `python _predloha/sestav.py`. Jak fungují značky `#@`, je
  popsané na začátku skriptu.
- Předloha sama jde spustit (`python _predloha/app.py`) a chová se jako
  nejúplnější verze, tedy krok 6 s barvami. Změnu si tak vyzkoušíš dřív,
  než z ní necháš sestavit kroky.
- `_predloha/vzorovy_report.html` je ukázka výstupu bonusu HTML report nad
  ukázkovými daty. Otevři ji v prohlížeči. Vyrábí ji `sestav.py` spuštěním
  `bonusy/bonus2_html_report.py`, ručně ji neupravuj.
- Testy v `krokN/test_finance.py` skript bere přímo ze zadání
  (`zadani/krokN_*.md`). Když změníš testy v zadání, spusť ho taky.
- Ověření všech kroků: v každé složce `krokN/` spusť `python -m pytest`.
- Hledání testů z kořene repozitáře složky `reseni` přeskakuje (nastavení
  v `pytest.ini`), aby se řešení nepletla s prací účastnic.
