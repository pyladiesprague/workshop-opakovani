# Nápověda ke kroku 6 – Kdo přežil častěji?

## Funkce

Ve sloupci `Survived` je 1 nebo 0. Počet přeživších je tedy součet toho
sloupce: začni nulou a v cyklu přičítej. Tahák L9, *Záznamy a tabulky*.

Procento je část děleno celek krát sto. Celek je `len(pasazeri)`.

U prázdného seznamu je celek nula a dělit nulou nejde. Zeptej se na to
podmínkou hned na začátku funkce a vrať 0.

Ve funkci `mira_preziti` použij funkci `pocet_prezivsich`, nepočítej znovu.

## Program

Ženy si vyfiltruj do jedné proměnné a muže do druhé. Na každý seznam pak
zavolej `mira_preziti`.

Třídy projdeš cyklem přes `[1, 2, 3]`, stejně jako v kroku 4.
