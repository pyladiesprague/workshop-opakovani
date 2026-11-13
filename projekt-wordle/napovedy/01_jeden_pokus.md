# Nápověda ke kroku 1 – Jeden pokus

## Funkce

Projdi pozice jednu po druhé. U každé se nejdřív zeptej, jestli je v tajném slově na stejném místě stejné písmeno. Když ne, zeptej se operátorem `in`, jestli je písmeno v tajném slově aspoň někde.

```python
vysledek = []
for i in range(DELKA_SLOVA):
    if hadane[i] == tajne[i]:
        vysledek.append("spravne")
    ...
return vysledek
```

## Program

Poskládej si dva řetězce, jeden s písmeny a druhý se značkami, a pak je vypiš. Který výsledek má jakou značku, si můžeš uložit do slovníku:

```python
ZNACKY = {"spravne": "+", "jinde": "?", "neni": "-"}
```
