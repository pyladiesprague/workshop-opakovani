# Krok 9 – Statistiky

Program si bude pamatovat odehrané hry i po vypnutí. Do importu ve `wordle.py` přidej `pridej_radek`:

```python
pridej_radek("statistiky.txt", 4)
```

Tohle přidá do souboru řádek `4`. Když soubor neexistuje, založí ho. Funkce `nacti_radky` pak vrátí seznam řetězců, takže čísla bude potřeba převést.

## Funkce

Do `logika.py` přidej funkci `spocitej_statistiky(radky)`. Dostane seznam řádků, kde každý je počet pokusů, nebo `"0"` za prohru. Vrátí slovník:

```python
spocitej_statistiky(["3", "0", "3", "6"])
# {"her": 4, "vyher": 3, "uspesnost": 75.0,
#  "pokusy": {1: 0, 2: 0, 3: 2, 4: 0, 5: 0, 6: 1}}
```

Úspěšnost je podíl výher v procentech. Když ještě nikdo nehrál, je úspěšnost 0.

Zasekla ses? Nápověda je v souboru [`napovedy/09_statistiky.md`](../napovedy/09_statistiky.md).

## Testy

Napiš testy sama. Nezapomeň na situaci, kdy ještě nikdo nehrál.

## Program

1. Ať `zahraj` vrací počet pokusů, nebo 0, když hráč prohrál.
2. Po každé hře výsledek ulož a vypiš statistiky:

```text
Her: 4   Úspěšnost: 75 %
Pokusy:  1: 0  2: 0  3: 2  4: 0  5: 0  6: 1
```

Úspěšnost zaokrouhlíš funkcí `round`: `round(75.0)` je `75`.
