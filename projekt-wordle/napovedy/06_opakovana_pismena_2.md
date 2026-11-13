# Nápověda 2 ke kroku 6 – Opakovaná písmena

V prvním průchodu zapiš na místa bez přesné shody zatím `"neni"`. Ve druhém průchodu pak některá `"neni"` přepíšeš na `"jinde"`:

```python
if vysledek[i] != "spravne" and hadane[i] in zbyla:
    vysledek[i] = "jinde"
    zbyla.remove(hadane[i])
```

`remove` odebere ze seznamu první výskyt hodnoty.
