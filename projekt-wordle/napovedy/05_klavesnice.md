# Nápověda ke kroku 5 – Klávesnice

## Funkce

Slovník, který funkce dostane jako parametr, je pořád ten samý slovník. Co do
něj funkce zapíše, uvidí i ten, kdo ji zavolal. Tahák L9, *Slovník ve funkci*.

Projdi hádané slovo po pozicích. U každého písmene stačí dvě otázky: je
výsledek `"spravne"`? A když ne, je už písmeno ve slovníku?

```python
for i in range(DELKA_SLOVA):
    pismeno = hadane[i]
    if vysledek[i] == "spravne":
        ...
    elif pismeno not in pismena:
        ...
```

## Program

Slovník `pismena` založ jednou na začátku hry, ne v cyklu. Jinak by si
klávesnice po každém pokusu všechno zapomněla.

Na výpis potřebuješ dva cykly v sobě: vnější přes řádky klávesnice, vnitřní přes
písmena v řádku.

Jestli o písmenu něco víš, zjistíš podmínkou `if pismeno in pismena:`. Tahák
L9, *Když klíč chybí*.

Barvy kláves si ulož do druhého slovníku, který se od barev polí liší jen u
`"neni"`.
