# Krok 10 – Titanic v číslech

Tvůj `zprava.py` teď vypisuje dlouhou řadu čísel, ve které se vyznáš jen ty.
Uděláš z nich zprávu, kterou si může přečíst někdo, kdo u toho nebyl. Na konci
tohohle kroku program vypíše přehled, tabulky, graf a tvůj závěr:

```text
TITANIC V ČÍSLECH
============================================

Pasažérů v souboru:         ???
Přežilo:                    ??? (??.? %)
Průměrný věk:              ??.? let

Podle pohlaví             Přežilo  (lidí)
  ženy                     ??.? %  (???)
  muži                     ??.? %  (???)
```

Zarovnání umí f-string, znáš ho z lekce o řetězcích:

```python
f"{nazev:24}"       # text na 24 míst, zarovnaný doleva
f"{procenta:5.1f}"  # číslo na 5 míst, jedno desetinné
```

U každého řádku tabulky je počet lidí, aby čtenář viděl, jak velká skupina za
procentem stojí.

## Funkce

Funkce píšeš do `analyza.py`.

Pořád nic nevypisují, jen skládají text.

| Funkce | Co vrátí |
| --- | --- |
| `radek_tabulky(nazev, procenta, pocet)` | jeden zformátovaný řádek |
| `tabulka(nadpis, skupiny, popisky)` | seznam řádků tabulky; `skupiny` a `popisky` fungují stejně jako u funkce `graf` |
| `sestav_zpravu(pasazeri)` | celou zprávu jako seznam řádků |

Co má ve zprávě být:

- počet pasažérů, kolik jich přežilo, průměrný věk, nejstarší a nejmladší
  pasažér,
- průměrná cena lístku v každé třídě,
- něco o jménech, třeba počet různých titulů a nejčastější mužská jména (pokud
  jsi krok 5 přeskočila, tuhle část vynech),
- tabulky přežití podle pohlaví, třídy a přístavu,
- aspoň jeden graf z minulého kroku,
- cokoliv dalšího, co tě během dne zaujalo.

Seznamy spojíš pomocí `+`:

```python
radky = radky + tabulka("Podle třídy", rozdel_podle(pasazeri, "Pclass"), TRIDY)
```

## Testy

Napiš testy sama. Co vyzkoušet:

- `radek_tabulky`: porovnej celý řádek a zkontroluj, že se číslo správně
  zaokrouhlí,
- `tabulka`: počet řádků, a že skupinu, která chybí, přeskočí,
- `sestav_zpravu`: že ve zprávě z `ukazka()` je řádek, který si umíš spočítat
  z hlavy.

## Program

Výpisy píšeš do `zprava.py`.

Výpisy z kroků 2 až 9 teď ze `zprava.py` smaž, nahradí je zpráva. Zůstane jen
načtení dat, `pridej_jmena` a cyklus, který vypíše řádky ze `sestav_zpravu`.

Neboj se mazat. Všechno, co ty výpisy počítaly, máš ve funkcích v `analyza.py`
a staré verze souboru jsou na GitHubu.

### Závěr

Na konec zprávy přidej pár vět vlastními slovy:

- **Čemu věříš.** Jeden výsledek, o kterém si myslíš, že opravdu něco znamená.
  Proč?
- **Čemu nevěříš.** Jeden výsledek, který je podle tebe jen náhoda nebo má
  jinou příčinu, než se na první pohled zdá. Proč?

Pomůžou ti poznámky z kroků 6, 7 a 8.

Zasekla ses? Nápověda je v souboru [`napovedy/10_zprava.md`](../napovedy/10_zprava.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] program vypíše celou zprávu a sloupce v tabulkách stojí pod sebou
- [ ] u každého procenta je vidět počet lidí
- [ ] zpráva končí tvým závěrem: čemu věříš a čemu ne
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
