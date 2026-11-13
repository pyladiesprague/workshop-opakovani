# Pro kouče – Správce osobních financí

Řešení je jedno z mnoha možných. Když účastnici program funguje a testy jsou
zelené, její řešení je stejně dobré, i když vypadá jinak.

Řešení jsou jen na větvi `reseni`. Během dne slouží koučům, aby mohli rychle
pomoct. Nikdo nedostává hotový krok, aby mohl pokračovat dalším (D5). Na konci
workshopu dostanou účastnice odkaz na větev a můžou si svou práci porovnat.

## Řešení po krocích

Složka `cviceni/reseni/NN_nazev/` se jmenuje stejně jako zadání kroku
`cviceni/NN_nazev.md`. Obsahuje celý projekt ve stavu po dokončení kroku:
`finance.py`, `app.py`, `test_finance.py` s testy všech dosavadních kroků
a `ukazkova_data.py`. Složka `06_soubory/` má navíc `finance.json`.

| Složka | Stav |
|---|---|
| `01_zaklad/` | výpis a zůstatek |
| `02_pridani_a_odebrani/` | + přidání a odebrání transakce, kontrola vstupu |
| `03_prehledy/` | + přehled měsíce, výdaje podle kategorií |
| `04_rozpocty/` | + rozpočty |
| `05_grafy/` | + graf výdajů |
| `06_soubory/` | + ukládání do souboru |

## Bonusy

Ve složce `bonusy/reseni/` jsou řešení všech čtyř bonusů. Nápady
v `napady.md` (dřív bonusy 5 až 11 a „Když zbyde čas“) řešení nemají, jsou
to otevřené úlohy.

- `01_barvy/` je celý projekt po kroku 6 s barevným výstupem. Hodí se
  i na ukázku na začátku dne, co se bude stavět.
- `02_hledani.py`, `03_razeni.py` a `04_html_report.py` jsou samostatné
  soubory, každý jde spustit zvlášť.

## Generátor řešení

- Složky `cviceni/reseni/NN_nazev/` a `bonusy/reseni/01_barvy/` se generují
  z předlohy v `cviceni/reseni/_predloha/`. Ručně je neupravuj. Uprav
  `_predloha/finance.py` nebo `_predloha/app.py` a spusť
  `python cviceni/reseni/_predloha/sestav.py`. Jak fungují značky `#@`, je
  popsané na začátku skriptu.
- Předloha sama jde spustit (`python cviceni/reseni/_predloha/app.py`) a chová
  se jako nejúplnější verze, tedy krok 6 s barvami. Změnu si tak vyzkoušíš
  dřív, než z ní necháš sestavit kroky.
- `_predloha/vzorovy_report.html` je ukázka výstupu bonusu HTML report nad
  ukázkovými daty. Otevři ji v prohlížeči. Vyrábí ji `sestav.py` spuštěním
  `bonusy/reseni/04_html_report.py`, ručně ji neupravuj.
- Testy v `test_finance.py` jednotlivých kroků bere skript přímo ze zadání
  (`cviceni/NN_*.md`). Když změníš testy v zadání, spusť ho taky.
- Ověření všech kroků: v každé složce `cviceni/reseni/NN_nazev/` spusť
  `python -m pytest`.
- Hledání testů z kořene repozitáře složky `reseni` přeskakuje (nastavení
  v `pytest.ini`), aby se řešení nepletla s prací účastnic.
