# Bonus 3 – Rodiny

Podle příjmení najdi největší rodiny v souboru. Přežili všichni společně, nebo
se rodiny rozdělily?

Na konci tohohle bonusu program vypíše něco takového:

```text
?????: ? lidí, přežilo ?
?????: ? lidí, přežilo ?
```

- Jméno je ve tvaru `Příjmení, Titul. Jméno`. Příjmení je všechno před první
  čárkou. Text rozdělíš metodou `split`.
- Příjmení přidej pasažérům jako nový sloupec. Pak ti stačí funkce
  `rozdel_podle`, kterou už máš.
- Vypiš jen rodiny, které mají aspoň šest lidí.

Pozor na závěr: jsou všichni lidé se stejným příjmením opravdu jedna
rodina? Jak bys to z dat ověřila?
