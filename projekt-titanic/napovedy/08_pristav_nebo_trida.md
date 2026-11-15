# Nápověda ke kroku 8 – Přístav, nebo třída?

## Funkce

`rozdel_podle_dvou` je skoro stejná jako `rozdel_podle`. Liší se jen klíč:
místo jedné hodnoty je to n-tice dvou hodnot. Tahák L9, *Skupiny*. O n-tici
jako klíči je i tahák projektu.

```python
klic = (pasazer[sloupec1], pasazer[sloupec2])
```

`prezivani_podle_dvou` je zase jeden řádek. Funkci `miry_skupin` je jedno,
jestli jsou klíče čísla, texty, nebo n-tice.

## Program

Hodnotu pod n-ticí čteš stejně jako pod jiným klíčem, jen jsou v hranatých
závorkách ještě kulaté: `miry[("C", 1)]`.

Aby řádky šly po třídách, použij dva cykly v sobě: vnější přes třídy `[1, 2,
3]`, vnitřní přes přístavy `["C", "S", "Q"]`. Klíč si z nich poskládáš sama.

Počet lidí ve skupině ti dá `rozdel_podle_dvou`, procento
`prezivani_podle_dvou`. Zavolej obě.
