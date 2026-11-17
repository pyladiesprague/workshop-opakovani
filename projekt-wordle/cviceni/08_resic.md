# Krok 8 – Řešič

Na konci tohohle kroku program umí hrát sám. Když hráč napíše `!`, program mu
poradí slovo:

```text
Tvůj pokus: !
Zkus: ?????
Tvůj pokus:
```

Ze všech slov, která přicházejí v úvahu, vybere to, které prozradí nejvíc:
slovo složené z písmen, která se v možných slovech vyskytují nejčastěji.

## Funkce

Funkce píšeš do `logika.py`.

| Funkce | Co vrátí |
| --- | --- |
| `spocitej_pismena(slova)` | slovník: v kolika slovech je které písmeno; slovo se dvěma `a` se počítá jen jednou |
| `ohodnot(slovo, cetnosti)` | součet bodů za různá písmena ve slově; slovo `panna` dostane body za p, a, n |
| `nejlepsi_slovo(mozna)` | slovo s nejvíc body; když je jich víc se stejnými body, je jedno které |

```python
cetnosti = spocitej_pismena(["panna", "pivo"])
# {"p": 2, "a": 1, "n": 1, "i": 1, "v": 1, "o": 1}
ohodnot("panna", cetnosti)
# 4
```

## Testy

Napiš testy sama, ke každé funkci aspoň jeden. Vymysli si malý seznam slov, u
kterého výsledek spočítáš z hlavy. Co vyzkoušet:

- písmeno, které je ve slově dvakrát, se počítá jednou,
- `nejlepsi_slovo` ze seznamu s jediným slovem.

## Program

Program píšeš do `wordle.py`.

Vykřičník přidej do funkce `nacti_slovo`, stejně jako otazník v minulém kroku.

Než to spustíš, odhadni, jaké první slovo program doporučí. Pak ho nech
poradit a hraj podle něj. Na kolik pokusů to zvládne?

Zasekla ses? Nápověda je v souboru [`napovedy/08_resic.md`](../napovedy/08_resic.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] `!` poradí slovo a nepočítá se jako pokus
- [ ] když hraješ jen podle rad, program slovo uhodne
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
