# Bonus 4 – Děti a dospělí

V datech je věk, ale ne věková skupina. Na konci tohohle bonusu budeš vědět,
jak dopadly děti, a to i v jednotlivých třídách:

```text
Podle věku                Přežilo  (lidí)
  děti do 16 let           ??.? %  (??)
  dospělí                  ??.? %  (???)
  věk neznámý              ??.? %  (???)
```

1. Napiš funkci `vekova_skupina(vek)`. Vrátí `"dítě"` do 16 let, `"dospělý"`
   od 16 let a `"neznámý"`, když je věk `None`. Otestuj i hranici: co vrátí
   pro přesně 16 let?
2. Napiš funkci, která každému pasažérovi přidá sloupec `Skupina`. Udělej to
   stejně jako `pridej_jmena` v kroku 5.
3. Vypiš tabulku přežití podle věkové skupiny.
4. Vypiš přežití dětí podle třídy, i s počtem dětí.

Podívej se na řádek `věk neznámý`. Lidé bez věku přežívali jinak často než
ostatní. Co myslíš, proč u nich věk asi chybí?

A ještě jedna věc k zamyšlení: hranici 16 let jsme si vymysleli. Jak se
výsledek změní, když ji posuneš na 12 nebo na 18?
