# Nápověda ke kroku 5 – Klávesnice

## Funkce

Projdi hádané slovo po pozicích. U každého písmene stačí dvě otázky:

```python
for i in range(DELKA_SLOVA):
    pismeno = hadane[i]
    if vysledek[i] == "spravne":
        ...
    elif pismeno not in pismena:
        ...
```

## Program

Potřebuješ dva cykly v sobě: vnější přes řádky klávesnice, vnitřní přes písmena v řádku. Jestli o písmenu něco víš, zjistíš podmínkou `if pismeno in pismena:`.

Barvy kláves si ulož do druhého slovníku, který se od barev polí liší jen u `"neni"`.
