# Nápověda ke kroku 1 – Co v souboru vlastně je?

## Funkce

Recept ze zadání stačí zabalit do funkce. Místo `SOUBOR` použij parametr
`soubor` a seznam nepiš do proměnné navíc, ale vrať ho.

```python
def nacti_pasazery(soubor):
    with open(soubor, encoding="utf-8") as f:
        ...
```

Pozor na odsazení: `return` patří dovnitř bloku `with`, nebo hned za něj.
Čtení ze souboru musí být uvnitř.

Recept na čtení CSV je i v taháku projektu, část *CSV*.

## Program

Počet položek seznamu je `len`. První položka má index 0. Tahák L8, *Seznam*.

Proměnnou do textu vložíš f-stringem. Tahák L6, *f-string*.
