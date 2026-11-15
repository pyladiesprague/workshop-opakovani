# Krok 9 – Statistiky

Na konci tohohle kroku si program pamatuje odehrané hry i po vypnutí a po
každé hře vypíše přehled:

```text
Her: 4   Úspěšnost: 75 %
Pokusy:  1: 0  2: 0  3: 2  4: 0  5: 0  6: 1
```

Do importu ve `wordle.py` přidej `pridej_radek`:

```python
pridej_radek("statistiky.txt", 4)
```

Tohle přidá do souboru řádek `4`. Když soubor neexistuje, založí ho. Funkce
`nacti_radky` pak vrátí seznam řetězců, takže čísla bude potřeba převést.

## Funkce

Funkce píšeš do `logika.py`.

| Funkce | Co vrátí |
| --- | --- |
| `spocitej_statistiky(radky)` | slovník s přehledem; `radky` je seznam řetězců, každý je počet pokusů, nebo `"0"` za prohru |

```python
spocitej_statistiky(["3", "0", "3", "6"])
# {"her": 4, "vyher": 3, "uspesnost": 75.0,
#  "pokusy": {1: 0, 2: 0, 3: 2, 4: 0, 5: 0, 6: 1}}
```

Úspěšnost je podíl výher v procentech. Když ještě nikdo nehrál, je úspěšnost
0.

## Testy

Napiš testy sama. Co vyzkoušet:

- příklad nahoře,
- situaci, kdy ještě nikdo nehrál.

## Program

Program píšeš do `wordle.py`.

1. Ať `zahraj` vrací počet pokusů, nebo 0, když hráč prohrál.
2. Po každé hře výsledek ulož a vypiš statistiky jako v ukázce nahoře.

Úspěšnost zaokrouhlíš funkcí `round`: `round(75.0)` je `75`.

Zasekla ses? Nápověda je v souboru [`napovedy/09_statistiky.md`](../napovedy/09_statistiky.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] po každé hře se vypíšou statistiky
- [ ] když program ukončíš a spustíš znovu, odehrané hry v nich zůstanou
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
