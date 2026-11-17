# Krok 9 – Jak to ukázat na první pohled?

Výpis z minulého kroku měl patnáct řádků čísel. Kdo se v tom má vyznat? Čísla
jsou přesná, ale obrázek je rychlejší. Na konci tohohle kroku program nakreslí
graf ze znaků, žádnou knihovnu nepotřebuješ:

```text
Přežití podle třídy
  1. třída        ████████████████████████        ??.? %
  2. třída        ███████████████                 ??.? %
  3. třída        ███████                         ??.? %
```

Délky sloupců v ukázce jsou vymyšlené. Plná šířka grafu je 30 znaků a znamená
100 %.

Znak `█` si zkopíruj odsud. Kdyby se ti v terminálu nezobrazil správně, použij
`#`.

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `sloupec_grafu(hodnota, nejvyssi, sirka)` | text ze znaků `█`, dlouhý podle toho, jak velká je `hodnota` proti `nejvyssi`; nejvyšší hodnota dostane `sirka` znaků |
| `graf(nadpis, skupiny, popisky)` | seznam řádků grafu: prázdný řádek, nadpis a pak jeden řádek pro každou skupinu |

Dvě věci, na které si u `sloupec_grafu` dej pozor:

- Malá hodnota by po zaokrouhlení vyšla na nula znaků a z grafu by zmizela.
  Každá hodnota větší než nula má mít aspoň jeden znak.
- Když je `nejvyssi` nula, nesmí funkce spadnout na dělení nulou.

Funkce `graf` dostane `skupiny`, tedy slovník z `rozdel_podle`, a slovník
`popisky`. V něm jsou klíče skupin a jejich české názvy:

```python
TRIDY = {1: "1. třída", 2: "2. třída", 3: "3. třída"}
POHLAVI = {"female": "ženy", "male": "muži"}
PRISTAVY = {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}
```

Slovníky dej do `analyza.py` pod `SOUBOR`. Ve `zprava.py` je pak použiješ
jako `analyza.TRIDY` a tak dál.

Slovník `popisky` určuje i pořadí řádků. Když nějaká skupina v datech chybí,
řádek vynech. A naopak: skupina, která není v popiscích, se do grafu
nedostane. Tak z grafu zmizí dva lidé bez přístavu.

Každý řádek má název, sloupec a procento. Sloupec počítej proti 100 %, aby šly
grafy mezi sebou porovnávat.

Funkce pořád nic nevypisuje, jen vrací seznam řetězců.

## Testy

Napiš testy sama. U `sloupec_grafu` vyzkoušej těchhle pět případů:

| Volání | Výsledek |
| --- | --- |
| `sloupec_grafu(100, 100, 10)` | deset znaků `█` |
| `sloupec_grafu(50, 100, 10)` | pět znaků `█` |
| `sloupec_grafu(0, 100, 10)` | prázdný řetězec |
| `sloupec_grafu(1, 1000, 10)` | jeden znak `█` |
| `sloupec_grafu(0, 0, 10)` | prázdný řetězec |

Deset znaků zapíšeš jako `"█" * 10`.

U funkce `graf` vyzkoušej, kolik řádků vrátí pro `ukazka()` rozdělenou podle
pohlaví a že skupinu, která v datech chybí, přeskočí.

## Program

Výpisy píšeš do `zprava.py`.

Vypiš tři grafy: přežití podle třídy, podle pohlaví a podle přístavu.

Podívej se na ně a doplň poznámky. Co je z grafu vidět hned? A co z něj naopak
vidět není? Vzpomeň si, kolik lidí v jednotlivých přístavech nastoupilo.

Zasekla ses? Nápověda je v souboru [`napovedy/09_graf.md`](../napovedy/09_graf.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] program vypíše tři grafy
- [ ] procenta za sloupci stojí pod sebou
- [ ] v `poznamky.md` máš, co je z grafu vidět a co ne
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
