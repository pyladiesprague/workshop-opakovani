# Krok 10: Herní obrazovka

Výpis v terminálu pořád ujíždí nahoru. Uděláme z něj obrazovku, která zůstává na místě. Do importu přidej `vycisti_obrazovku`. Tahle funkce smaže všechno, co je v terminálu vypsané.

```
             O   P   E   R   A
             ·   ·   ·   ·   ·
             ·   ·   ·   ·   ·
             ·   ·   ·   ·   ·
             ·   ·   ·   ·   ·
             ·   ·   ·   ·   ·

         Ě   Š   Č   Ř   Ž   Ý   Á   Í   É
 Q   W   E   R   T   Z   U   I   O   P   Ú
   A   S   D   F   G   H   J   K   L   Ů
 Y   X   C   V   B   N   M   Ď   Ť   Ň   Ó

  Takové slovo neznám.

  Tvůj pokus:
```

## Program

1. Napiš funkci `vykresli(pokusy, pismena, zprava)`, která smaže obrazovku a vypíše hrací plochu, klávesnici a zprávu.
2. Plocha má vždycky šest řádků. Prázdné pokusy vyplň tečkami.
3. Před každým pokusem zavolej `vykresli`.

Zarovnání na střed jako na obrázku je navíc. Výpis od levého kraje úplně stačí.

Teď narazíš na problém: když `print` vypíše chybu a hned potom se obrazovka smaže, hráč ji nestihne přečíst. Proto se chyba nevypisuje hned. Ulož ji do proměnné `zprava` a `vykresli` ji vypíše při dalším překreslení. Stejně naložíš s nápovědou, s radou řešiče i s výsledkem hry.

Tahle změna se týká jen výpisu, takže se `logika.py` ani testy nemění. Když po úpravách testy pořád procházejí, víš, že pravidla hry zůstala stejná.

Zasekla ses? Nápověda je v souboru [`napovedy/10_herni_obrazovka.md`](../napovedy/10_herni_obrazovka.md).
