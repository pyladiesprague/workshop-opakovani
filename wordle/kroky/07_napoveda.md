# Krok 7: Nápověda

Když hráč místo slova napíše `?`, program vypíše, kolik tajných slov ještě přichází v úvahu, a prvních deset z nich. Nápověda se nepočítá jako pokus.

## Logika

Do `logika.py` přidej funkci `filtruj(mozna, hadane, vysledek)`. Ze seznamu `mozna` nechá jen slova, která odpovídají tomu, co hráč zatím zjistil:

```python
mozna = ["kočka", "mléko", "sonda", "panna"]
print(filtruj(mozna, "banka", vyhodnot("banka", "panna")))
# ['panna']
```

Než začneš psát podmínky pro každou barvu, zastav se: co by platilo, kdyby tajné bylo právě tohle slovo? Máš na to už hotovou funkci.

Zasekla ses? Nápověda je v souboru [`napovedy/07_napoveda.md`](../napovedy/07_napoveda.md).

## Testy

Napiš testy sama. Jeden z nich ať ověří, že tajné slovo v seznamu vždycky zůstane.

## Program

1. Ve funkci `zahraj` začni seznamem všech slov z `hadana_slova.txt` a po každém pokusu ho zmenši funkcí `filtruj`.
2. Otazník zpracuj ve funkci `nacti_slovo`: vypiš nápovědu a zeptej se znovu. Funkce k tomu potřebuje seznam `mozna` jako další parametr.

Prvních deset slov získáš výřezem `mozna[:10]`. Seznam řetězců spojíš do jednoho textu takhle:

```python
", ".join(["kočka", "mléko"])    # kočka, mléko
```
