# Wordle: pro kouče

Tenhle soubor a složky `reseni/` jsou jen na větvi `reseni`. Účastnice je
během workshopu nedostanou, odkaz jim pošleme až na konci.

## Úvod (5 minut, naživo)

1. Zahraj jednu hru z `cviceni/reseni/10_herni_obrazovka` a nech místnost
   hádat.
2. Ukaž `!`: program poradí slovo. Tohle na konci dne budou umět napsat.
3. Řekni cíl: do kroku 3 dojde každá, to už je hratelná hra. Řešič je krok 8.
4. Ukaž strukturu: `cviceni/`, `napovedy/`, tři soubory s kódem.

## Co v kterém kroku vzniká

| Krok | Nové funkce v `logika.py` | Testy | Kde se nejčastěji zasekne |
| --- | --- | --- | --- |
| 1 | `vyhodnot` | hotové | index a `range`; `elif ... in tajne` |
| 2 | `uprav_vstup`, `chyba_slova` | s mezerami | cyklus na vstup uvnitř cyklu na pokusy; řeší to funkce `nacti_slovo` |
| 3 | `chyba_slova` s druhým parametrem | s mezerami | předání seznamu do funkcí; staré testy spadnou schválně |
| 4 | žádné | žádné | seznam n-tic a rozbalení v cyklu |
| 5 | `aktualizuj_pismena` | s mezerami + vlastní | funkce mění slovník a nic nevrací |
| 6 | oprava `vyhodnot` | vlastní, z tabulky | nejtěžší krok dne; dá se přeskočit |
| 7 | `filtruj` | vlastní | snaha psát podmínky pro každou barvu; stačí zavolat `vyhodnot` |
| 8 | `spocitej_pismena`, `ohodnot`, `nejlepsi_slovo` | vlastní | písmeno ve slově počítat jen jednou |
| 9 | `spocitej_statistiky` | vlastní | slovník ve slovníku; dělení nulou bez her |
| 10 | žádné | žádné | přesun výpisů do proměnné `zprava` |

## Čísla pro kontrolu

- Řešič z kroku 8 doporučí jako první slovo `opera`.
- Bonus 1: průměr 3,20 pokusu, nejhorší slovo `šátek` (6 pokusů), šest pokusů
  nepřekročí nikdy.
- Bonus 2: první slovo `loket`, průměr 2,99 pokusu.

## Na co si dát pozor

- Krok 6 je skok v obtížnosti. Kdo se zasekne na déle, ať ho přeskočí.
  Nápověda (krok 7) i řešič (krok 8) fungují i s původní funkcí `vyhodnot`.
- Testy v krocích 2, 3 a 5 mají mezery `___`. Dokud je účastnice nedoplní,
  test spadne na `NameError: name '___' is not defined`.
- V kroku 3 se mění počet parametrů `chyba_slova`. Testy z kroku 2 spadnou na
  `TypeError`, to je záměr.
- Barvy a mazání obrazovky fungují v terminálu ve VS Code po spuštění
  tlačítkem Run. V panelu Output nebo Debug Console ne.
- Mazání obrazovky (krok 10) je potřeba vyzkoušet na Windows i macOS.
  `pomocnik.py` volá příkaz `cls`, respektive `clear`.

## Řešení

- Složky v `cviceni/reseni/` obsahují celý program po každém kroku. Jmenují se
  stejně jako zadání kroku.
- Složky se generují z předlohy v `cviceni/reseni/_predloha/`. Ručně je
  neupravuj. Uprav předlohu a spusť `python
  cviceni/reseni/_predloha/sestav.py`. Skript zároveň spustí testy všech
  kroků.
- Seznamy slov si řešení berou ze složky projektu, nekopírují se.
- `bonusy/reseni/` má řešení obou bonusů.
