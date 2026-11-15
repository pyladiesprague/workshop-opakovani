# Nápověda ke kroku 10 – Titanic v číslech

## Funkce

`radek_tabulky`: jeden f-string. Název zarovnej na pevnou šířku, procento na
pět míst s jedním desetinným. Tahák L6, *Za dvojtečkou se říká, jak to má
vypadat*.

`tabulka` má stejnou stavbu jako `graf` z minulého kroku: seznam s nadpisem,
cyklus přes `popisky`, podmínka, jestli skupina existuje. Liší se jen řádek,
který do seznamu přidáváš. Počet lidí ve skupině je `len`.

`sestav_zpravu`: začni seznamem s nadpisem a celkovými čísly. Potom k němu
přičítej jednu část za druhou.

- Všechna čísla už umíš spočítat funkcemi z minulých kroků. Tady je jen
  skládáš do textu.
- Nejstaršího a nejmladšího si na začátku ulož do proměnných.
- Průměrné ceny podle tříd přidávej v cyklu přes `TRIDY` metodou `append`.

## Testy

Test na celý řádek: napiš si řádek nejdřív ručně a spočítej mezery. Nebo si ho
nech jednou vypsat, zkontroluj očima a teprve potom ho zkopíruj do testu.

Jestli je text někde uvnitř seznamu nebo řetězce, zjistíš přes `in`.

Než zavoláš `sestav_zpravu` na `ukazka()`, zavolej na ni `pridej_jmena`.
Zpráva sloupce se jmény potřebuje.

## Program

Ve `zprava.py` zůstanou tři věci: načtení dat, `pridej_jmena` a cyklus s
`print`.
