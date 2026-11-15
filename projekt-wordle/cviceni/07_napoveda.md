# Krok 7 – Nápověda

Na konci tohohle kroku hra umí napovědět. Když hráč místo slova napíše `?`,
program vypíše, kolik tajných slov ještě přichází v úvahu, a prvních deset z
nich:

```text
Tvůj pokus: ?
Zbývá slov: 14
bavit, chata, hlava, vlast, ...
Tvůj pokus:
```

Nápověda se nepočítá jako pokus.

## Funkce

Funkce píšeš do `logika.py`.

| Funkce | Co vrátí |
| --- | --- |
| `filtruj(mozna, hadane, vysledek)` | nový seznam jen s těmi slovy z `mozna`, která odpovídají tomu, co hráč zjistil |

```python
mozna = ["kočka", "mléko", "sonda", "panna"]
print(filtruj(mozna, "banka", vyhodnot("banka", "panna")))
# ['panna']
```

Než začneš psát podmínky pro každou barvu, zastav se: co by platilo, kdyby
tajné bylo právě tohle slovo? Máš na to už hotovou funkci.

## Testy

Napiš testy sama. Co vyzkoušet:

- příklad nahoře,
- tajné slovo v seznamu vždycky zůstane,
- funkce původní seznam nemění.

## Program

Program píšeš do `wordle.py`.

1. Ve funkci `zahraj` začni seznamem všech slov z `hadana_slova.txt` a po
   každém pokusu ho zmenši funkcí `filtruj`.
2. Otazník zpracuj ve funkci `nacti_slovo`: vypiš nápovědu a zeptej se znovu.
   Funkce k tomu potřebuje seznam `mozna` jako další parametr.

Prvních deset slov získáš výřezem `mozna[:10]`. Seznam řetězců spojíš do
jednoho textu takhle:

```python
", ".join(["kočka", "mléko"])    # kočka, mléko
```

Zasekla ses? Nápověda je v souboru [`napovedy/07_napoveda.md`](../napovedy/07_napoveda.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] `?` vypíše počet zbývajících slov a nejvýš deset z nich
- [ ] po každém pokusu zbývajících slov ubývá
- [ ] `?` se nepočítá jako pokus
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
