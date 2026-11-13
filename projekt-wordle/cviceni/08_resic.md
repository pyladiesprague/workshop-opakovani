# Krok 8 – Řešič

Když hráč napíše `!`, program mu poradí slovo. Ze všech slov, která přicházejí v úvahu, vybere to, které prozradí nejvíc.

## Funkce

Do `logika.py` přidej tři funkce:

1. `spocitej_pismena(slova)` vrátí slovník, ve kolika slovech je které písmeno. Slovo se dvěma a se počítá jen jednou.
2. `ohodnot(slovo, cetnosti)` sečte body za různá písmena ve slově. Slovo `panna` tedy dostane body za p, a, n.
3. `nejlepsi_slovo(mozna)` vrátí slovo s nejvíc body. Když je jich víc se stejnými body, je jedno, které vybereš.

```python
cetnosti = spocitej_pismena(["panna", "pivo"])
# {"p": 2, "a": 1, "n": 1, "i": 1, "v": 1, "o": 1}
ohodnot("panna", cetnosti)
# 4
```

Zasekla ses? Nápověda je v souboru [`napovedy/08_resic.md`](../napovedy/08_resic.md).

## Testy

Napiš testy sama, ke každé funkci aspoň jeden. Vymysli si malý seznam slov, u kterého výsledek spočítáš z hlavy.

## Program

Vykřičník přidej do funkce `nacti_slovo`, stejně jako otazník v minulém kroku.

Než to spustíš, odhadni, jaké první slovo program doporučí. Pak ho nech poradit a hraj podle něj. Na kolik pokusů to zvládne?
