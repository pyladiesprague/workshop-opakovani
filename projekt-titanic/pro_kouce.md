# Titanic: pro kouče

Tenhle soubor a složky `reseni/` jsou jen na větvi `reseni`. Účastnice je
během workshopu nedostanou, odkaz jim pošleme až na konci.

## Úvod (5 až 10 minut, naživo)

1. Ukaž, o co jde: máme seznam pasažérů a hledáme v něm, kdo byl na palubě a
   jak dopadl.
2. Nech místnost hádat dvě čísla: kolik let bylo nejstaršímu pasažérovi a jaké
   procento lidí v souboru přežilo. Odpovědi neprozrazuj, zjistí je v krocích
   3 a 6.
3. Ukaž pětikrokovou smyčku: otázka, odhad, výpočet, porovnání, další otázka.
4. Projdi pět zvyků. Stejný text je v `README.md`.
5. Ukaž `poznamky.md` a první krok.

## Co v kterém kroku vyjde

| Krok | Otázka | Výsledek |
| --- | --- | --- |
| 1 | Co v souboru je? | 891 pasažérů, 12 sloupců |
| 2 | Co chybí? | Věk u 177 lidí |
| 3 | Kdo byl na palubě? | Průměrný věk 29,7. Nejstarší Barkworth, 80 let. Nejmladší Thomas, 0,42 roku, tedy 5 měsíců. |
| 4 | Kolik stál lístek? | Průměr 84,2 / 20,7 / 13,7 libry. Nejdražší 512,33 libry, tři lidé na jednom lístku PC 17755. Zadarmo 15 lidí. |
| 5 | Jména | 17 titulů: Mr 517, Miss 182, Mrs 125, Master 40, Dr 7, Rev 6 a další. Mužská jména: William 35, John 25, George 14, Charles 13, Thomas 13, Henry 12, James 11, Richard 10. |
| 6 | Kdo přežil? | 342 z 891, tedy 38,4 %. Ženy 74,2 %, muži 18,9 %. Třídy 63,0 / 47,3 / 24,2 %. |
| 7 | Přístavy | S 33,7 % (644 lidí, 20 % v 1. třídě). C 55,4 % (168, 51 %). Q 39,0 % (77, 3 %). Dva lidé přístav nemají. |
| 8 | Přístav, nebo třída? | 1. třída: C 69,4 %, S 58,3 %. 3. třída: C 37,9 %, S 19,0 %, Q 37,5 %. Žena ve 3. třídě 50,0 %, muž v 1. třídě 36,9 %. |
| 9 | Graf | Tři grafy: třída, pohlaví, přístav. Sloupec 30 znaků = 100 %. |
| 10 | Zpráva | Přehled, tabulky, graf a závěr: čemu věřím a čemu ne. |
| 11 | Průzkumník | Program se zeptá na sloupec a vypíše přežití ve skupinách. |
| 12 | Vlastní otázka | Odpověď přidaná do zprávy. |

## Příčina, nebo jen souvislost

Projekt má vedle Pythonu jednu myšlenku: když dvě věci vycházejí spolu,
neznamená to, že jedna způsobuje druhou. Odborně se tomu říká rozdíl mezi
korelací a kauzalitou. Účastnicím ten pojem neříkej, pokud se samy nezeptají.
Mají na to přijít na třech příkladech:

- **Krok 6, rozdíl s vysvětlením.** Ženy a 1. třída přežívaly mnohem častěji.
  Skupiny jsou velké a rozdíl obrovský.
- **Kroky 7 a 8, skrytá příčina.** Z Cherbourgu přežilo 55 %, ze Southamptonu
  34 %. Jenže z Cherbourgu jela polovina lidí 1. třídou. Když se porovná
  stejná třída, rozdíl se zmenší. Nezmizí ale úplně, a to je v pořádku:
  správná odpověď je „třída vysvětluje velkou část“, ne „přístav nehrál žádnou
  roli“.
- **Krok 11, náhoda.** Průzkumník podle titulu ukáže, že nepřežil žádný
  duchovní a přežila každá hraběnka. Duchovních je šest a hraběnka jedna. Z
  tak malých skupin se nedá nic vyvodit. Kdo chce, může si stejně vyzkoušet
  křestní jména: Johnů přežilo 12 %, Williamů 23 %, a jméno za to nemůže.

Nevysvětluj to předem a nedělej z toho přednášku. Nech je výsledek vidět a
zeptej se: „Může za to ten přístav? Čím dalším se ti lidé lišili?“ Stačí jedna
dvě věty do poznámek, není to test. Kdo má plnou hlavu Pythonu, odpoví jednou
větou a jde dál.

## Na co si dát pozor

- Pasažéři v souboru nejsou všichni lidé na palubě. Výsledky popisují jen
  tento soubor.
- V krocích 2 až 9 se výpisy v `zprava.py` sčítají, nic se nemaže. V kroku 10
  je účastnice smažou a nahradí zprávou. Řešení jsou udělaná stejně.
- Krok 5 má nejvíc funkcí z první poloviny. Kdo se na něm zasekne, může ho
  přeskočit, kroky 6 až 9 ho nepotřebují.
- Krok 3: lidé bez věku. Kdo dělí `len(pasazeri)`, dostane špatný průměr a
  test to chytí.
- Krok 4: tři lidé s nejdražším lístkem mají stejné číslo lístku. `Fare` je
  cena za lístek, ne za osobu.
- Krok 5: vdané ženy jsou zapsané jménem manžela, vlastní jméno mají v
  závorce. Proto se křestní jména počítají jen u mužů.
- Krok 7: v datech jsou dva lidé bez přístavu, ve výpisu mají prázdný klíč. Je
  to dobrá chvíle připomenout zvyk „ptej se, co chybí“.
- Krok 8: v Queenstownu jeli 1. třídou jen 2 lidé a 2. třídou 3. Procenta z
  těch řádků nic neříkají. Nech účastnice, ať si toho všimnou samy.
- Testy v krocích 2 až 6 mají mezery `___`. Dokud je účastnice nedoplní, test
  spadne na `NameError: name '___' is not defined`.
- V kroku 6 se poprvé objeví `pytest.approx`. Kdo zapomene `import pytest`,
  dostane `NameError`.
- Několik pasažérů je známých i mimo data, třeba Margaret „Molly“ Brown nebo
  hraběnka z Rothes. Dá se to použít jako zpestření, v zadání to není.

## Kde se testy mění

| Kroky | Testy |
| --- | --- |
| 1 | hotové, zkopírují se |
| 2 až 6 | s mezerami, kroky 4, 5 a 6 mají i jeden vlastní |
| 7 až 12 | vlastní, zadání říká, co vyzkoušet |

## Řešení

- Složky v `cviceni/reseni/` obsahují celý program po každém kroku. Jmenují se
  stejně jako zadání kroku.
- Složky se generují z předlohy v `cviceni/reseni/_predloha/`. Ručně je
  neupravuj. Uprav předlohu a spusť `python
  cviceni/reseni/_predloha/sestav.py`. Skript zároveň spustí testy všech
  kroků.
- Data si řešení berou ze složky projektu, soubor CSV se nekopíruje.
- `bonusy/reseni/` má řešení všech pěti bonusů. Bonus 2 potřebuje
  nainstalovanou knihovnu plotext.
- Krok 12 má v řešení jako vlastní otázku velikost rodiny: sám 30,4 % (537),
  rodina do 3 lidí 57,9 % (292), 4 a víc 16,1 % (62). Je to jen příklad, každá
  účastnice bude mít jinou.
- Bonus 4 se vrací k otázce „ženy a děti první“: děti do 16 let 59,0 % (83),
  dospělí 38,2 % (631).
