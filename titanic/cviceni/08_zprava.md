# Krok 8: Co z toho plyne?

Máš odpovědi, teď z nich uděláme zprávu, kterou si může přečíst někdo, kdo u toho nebyl. Zpráva má tabulky a na konci tvůj závěr: platilo pravidlo, a platilo pro všechny stejně?

```
TITANIC: PLATILO „ŽENY A DĚTI PRVNÍ“?
============================================

Pasažérů celkem:            891
Přežilo:                    342 (38.4 %)

Dospělí podle pohlaví     Přežilo  (lidí)
  ženy                     77.5 %  (218)
  muži                     17.4 %  (413)
```

Zarovnání umí f-string, znáš ho z lekce o řetězcích:

```python
f"{nazev:24}"       # text na 24 míst, zarovnaný doleva
f"{procenta:5.1f}"  # číslo na 5 míst, jedno desetinné
```

U každého řádku je počet lidí, aby čtenář viděl, jak velká skupina za procentem stojí.

## Logika

Do `analyza.py` přidej tři funkce. Pořád nic nevypisují, jen skládají text:

- `radek_tabulky(nazev, procenta, pocet)` vrátí jeden zformátovaný řádek.
- `tabulka(nadpis, skupiny, popisky)` vrátí seznam řádků. `skupiny` je slovník z `rozdel_podle`. Ve slovníku `popisky` jsou klíče a jejich české názvy, třeba `{"female": "ženy", "male": "muži"}`. Určuje pořadí řádků. Když nějaká skupina chybí, řádek vynech.
- `sestav_zpravu(pasazeri)` vrátí celou zprávu jako seznam řádků: dospělé podle pohlaví, třídy, kombinace třídy a pohlaví, věk a děti podle třídy.

Seznamy spojíš pomocí `+`:

```python
radky = radky + tabulka("Podle třídy", rozdel_podle(pasazeri, "Pclass"), TRIDY)
```

## Závěr

Na konec zprávy přidej dvě nebo tři věty vlastními slovy. Odpověz na hlavní otázku a opři se o čísla z tabulek. Pomůžou ti poznámky.

## Testy

Napiš testy sama. U `radek_tabulky` porovnej celý řádek a zkontroluj, že se číslo správně zaokrouhlí.

## Zpráva

V `zprava.py` už zůstane jen načtení dat a cyklus, který vypíše řádky ze `sestav_zpravu`.
