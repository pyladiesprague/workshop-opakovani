# Krok 7 – Záleželo na tom, kde kdo nastoupil?

Titanic nabíral cestující ve třech přístavech: Southampton (`S`), Cherbourg
(`C`) a Queenstown (`Q`). Na konci tohohle kroku budeš umět rozdělit pasažéry
do skupin podle libovolného sloupce a uvidíš, jestli se přístavy lišily:

```text
S: přežilo ??.? %  (??? lidí, v 1. třídě ?? %)
C: přežilo ??.? %  (??? lidí, v 1. třídě ?? %)
Q: přežilo ??.? %  (?? lidí, v 1. třídě ?? %)
```

Než začneš, zapiš si odhad: bude se přežití mezi přístavy lišit? Proč by mělo?

Mohla bys zavolat `filtruj` třikrát, jednou pro každý přístav. Co ale u
sloupce, kde hodnoty neznáš? Napíšeš funkci, která skupiny najde sama.

Jestli máš hotový krok 5, podobnou věc už znáš. Funkce `pocty` si u každé
hodnoty pamatuje, kolik lidí ji má. Teď si místo počtu schováš rovnou ty lidi,
celý seznam. S ním pak můžeš počítat cokoliv, třeba přežití.

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `rozdel_podle(pasazeri, sloupec)` | slovník, kde klíče jsou hodnoty ze sloupce a hodnoty jsou seznamy pasažérů |
| `miry_skupin(skupiny)` | dostane takový slovník a vrátí slovník, kde hodnoty jsou procenta přeživších |
| `prezivani_podle(pasazeri, sloupec)` | spojí obě předchozí funkce |

```python
prezivani_podle(pasazeri, "Sex")
# {"male": ??.?, "female": ??.?}
```

## Testy

Od tohohle kroku píšeš testy sama. Vezmi `ukazka()` a spočítej z hlavy, co má
vyjít. Co vyzkoušet:

- kolik pasažérů z ukázky nastoupilo v kterém přístavu,
- přežití v každém přístavu z ukázky.

## Program

Výpisy píšeš do `zprava.py`.

Pro každý přístav vypiš procento přeživších, počet lidí a podíl těch, kdo jeli 1. třídou.

Jeden řádek tě možná překvapí. V datech jsou dva lidé, u kterých přístav
chybí.

Teď se zastav a doplň poznámky:

- V jednom přístavu přežilo výrazně víc lidí. Může za to ten přístav?
- Podívej se na podíl 1. třídy. Co už víš o 1. třídě z minulého kroku?

Zasekla ses? Nápověda je v souboru [`napovedy/07_pristavy.md`](../napovedy/07_pristavy.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] program vypíše přežití, počet lidí a podíl 1. třídy pro každý přístav
- [ ] v `poznamky.md` máš odpověď na obě otázky
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
