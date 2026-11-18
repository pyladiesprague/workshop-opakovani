# Nápověda ke kroku 3 – Kdo byl na palubě?

## Funkce

`prumerny_vek`: průměr je součet děleno počet. Potřebuješ dvě proměnné, obě
začínají nulou. V cyklu přičítej jen u těch, kdo věk mají. Na to se zeptáš
přes `is not None`. Tahák projektu, *None*.

Počet není `len(pasazeri)`. Lidi bez věku do průměru nepočítáš, takže jimi ani
nedělíš.

`nejstarsi` je vzor „kdo vyhrál“: pamatuj si zatím nejstaršího a začni s
`None`. Tahák L9, *Kdo vyhrál*.

```python
vitez = None
for pasazer in pasazeri:
    if pasazer["Age"] is not None:
        if vitez is None or ...:
            vitez = pasazer
return vitez
```

Funkce vrací celého pasažéra, ne jen jeho věk. Jméno si pak přečteš přes klíč.

`nejmladsi` je stejná funkce s obráceným porovnáním.

## Program

Výsledek `analyza.nejstarsi(pasazeri)` si ulož do proměnné, třeba `stary`.
Je to slovník, takže jméno je `stary["Name"]`.

V f-stringu, který je v uvozovkách, piš klíč do apostrofů:
`f"{stary['Name']}"`. Tahák L9, *Slovník*.

Jedno desetinné místo: `f"{cislo:.1f}"`. Tahák L6, *Za dvojtečkou se říká, jak
to má vypadat*.
