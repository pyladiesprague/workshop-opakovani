# Nápověda ke kroku 1 – Jeden pokus

## Funkce

Projdi pozice jednu po druhé. U každé se nejdřív zeptej, jestli je v tajném
slově na stejném místě stejné písmeno. Když ne, zeptej se operátorem `in`,
jestli je písmeno v tajném slově aspoň někde.

- Výsledky sbírej do seznamu. Tahák L8, *Stavění seznamu v cyklu*.
- Na pozice se dostaneš přes `range` a index: `hadane[i]`, `tajne[i]`.

```python
vysledek = []
for i in range(DELKA_SLOVA):
    if hadane[i] == tajne[i]:
        vysledek.append("spravne")
    ...
return vysledek
```

## Program

Poskládej si dva řetězce, jeden s písmeny a druhý se značkami, a pak je vypiš.

Který výsledek má jakou značku, si ulož do slovníku. Značku pak najdeš přes
klíč, bez podmínek:

```python
ZNACKY = {"spravne": "+", "jinde": "?", "neni": "-"}
```
