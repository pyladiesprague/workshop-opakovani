# Nápověda ke kroku 12 – Co zajímá tebe?

Většinu otázek zodpovíš funkcemi, které už máš: `filtruj`, `rozdel_podle`,
`mira_preziti`, `tabulka`.

Když potřebuješ skupinu, která v datech není, třeba velikost rodiny nebo věk
po desetiletích, přidej pasažérům nový sloupec. Udělej to stejně jako
`pridej_jmena` v kroku 5: jedna funkce spočítá hodnotu pro jednoho pasažéra,
druhá ji v cyklu zapíše všem.

Funkce `moje_otazka` má stejnou stavbu jako `sestav_zpravu`: začni seznamem s
prázdným řádkem a nadpisem a přičítej k němu řádky. Tabulku ti udělá funkce
`tabulka`, potřebuje jen skupiny a popisky.

Popisky jsou slovník, který určuje názvy a pořadí řádků, třeba:

```python
RODINY = {"sám": "cestoval sám", "malá": "s 1 až 3 příbuznými", "velká": "se 4 a více příbuznými"}
```
