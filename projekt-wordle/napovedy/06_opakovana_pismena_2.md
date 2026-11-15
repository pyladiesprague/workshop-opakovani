# Nápověda 2 ke kroku 6 – Opakovaná písmena

V prvním průchodu zapiš na místa bez přesné shody zatím `"neni"`. Ve druhém
průchodu pak některá `"neni"` přepíšeš na `"jinde"`.

Prvek seznamu přepíšeš přes index: `vysledek[i] = "jinde"`.

Jedno písmeno ze seznamu odebereš metodou `remove`. Odebere první výskyt
hodnoty. Tahák L8, *Metody, které seznam mění*.

```python
zbyla = ["s", "o", "d"]
zbyla.remove("o")
# ["s", "d"]
```
