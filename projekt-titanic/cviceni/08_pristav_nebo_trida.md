# Krok 8 – Přístav, nebo třída?

V minulém kroku to vypadalo, že lidé z jednoho přístavu měli větší štěstí.
Jenže z toho přístavu jela 1. třídou taky největší část lidí. Co z toho
tedy rozhodovalo?

Zjistíš to tak, že porovnáš lidi ze stejné třídy. Na konci tohohle kroku budeš
umět dělit pasažéry podle dvou sloupců najednou:

```text
1. třída, C: ??.? %  (??)
1. třída, S: ??.? %  (???)
1. třída, Q: ??.? %  (?)
...
3. třída, Q: ??.? %  (??)
```

Než začneš, zapiš si odhad: když porovnáš jen lidi z 1. třídy, bude mezi
přístavy pořád rozdíl?

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `rozdel_podle_dvou(pasazeri, sloupec1, sloupec2)` | slovník jako `rozdel_podle`, jen je klíčem n-tice dvou hodnot |
| `prezivani_podle_dvou(pasazeri, sloupec1, sloupec2)` | slovník s procenty přeživších; hotovou funkci `miry_skupin` použij znovu |

N-tice klíčem slovníku být může, seznam ne.

```python
miry = prezivani_podle_dvou(pasazeri, "Embarked", "Pclass")
print(miry[("C", 1)])
```

## Testy

Napiš testy sama na `ukazka()`. Co vyzkoušet:

- kolik mužů ze 3. třídy je v ukázce,
- přežití aspoň tří kombinací třídy a pohlaví.

## Program

Výpisy píšeš do `zprava.py`.

1. Vypiš přežití pro každou kombinaci třídy a přístavu. U každé vypiš i počet
   lidí.
2. Stejnou funkcí vypiš kombinace třídy a pohlaví.

Doplň poznámky:

- Zmenšil se rozdíl mezi přístavy, když porovnáváš stejnou třídu? Zmizel
  úplně?
- Podívej se na počty lidí. Kterým řádkům bys nevěřila, protože je za nimi jen
  pár lidí?
- Kdo měl větší šanci: žena ve 3. třídě, nebo muž v 1.?

Zasekla ses? Nápověda je v souboru [`napovedy/08_pristav_nebo_trida.md`](../napovedy/08_pristav_nebo_trida.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] program vypíše všechny kombinace třídy a přístavu i třídy a pohlaví
- [ ] v `poznamky.md` máš odpovědi na tři otázky
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
