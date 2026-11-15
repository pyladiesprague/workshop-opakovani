# Krok 6 – Opakovaná písmena

Na konci tohohle kroku hra správně vyhodnotí i slova, ve kterých je stejné
písmeno dvakrát.

Funkce `vyhodnot` má totiž chybu, kterou zatím nebylo vidět. Pro hádané slovo
`banka` a tajné slovo `sonda` vrátí `- ? + - +`.

Tajné slovo `sonda` má jedno a, a to je na konci, kde ho hráč trefil. Funkce
přesto hlásí, že a na druhém místě je `"jinde"`. Hráč si pak myslí, že jsou ve
slově dvě.

Tenhle krok je nejtěžší z celého dne. Když ti nepůjde, přeskoč ho a vrať se k
němu později. Další kroky fungují i bez něj.

## Testy

Od tohohle kroku píšeš testy sama. A tentokrát jimi začni: nejdřív testy,
potom oprava. Některé budou červené, a to je správně.

Co má vyjít, je v tabulce. Výsledky jsou tu psané značkami `+ ? -`:

| Volání | Výsledek |
| --- | --- |
| `vyhodnot("banka", "sonda")` | `- - + - +` |
| `vyhodnot("mamka", "mléko")` | `+ - - + -` |
| `vyhodnot("banka", "okapy")` | `- ? - ? -` |
| `vyhodnot("kočka", "kabát")` | `+ - - - ?` |
| `vyhodnot("nanuk", "panna")` | `? + + - -` |

## Funkce

Funkci opravuješ v `logika.py`.

| Funkce | Co se mění |
| --- | --- |
| `vyhodnot(hadane, tajne)` | každé písmeno tajného slova jde použít jen jednou a přesné shody mají přednost |

Jeden průchod slovem stačit nebude, takže si to nejdřív rozmysli na papíře.
Zkus si ručně vyhodnotit `banka` proti `sonda`: co musíš vědět, než rozhodneš
o prvním a?

Program ve `wordle.py` se nemění.

Zasekla ses? Nápověda je v souboru [`napovedy/06_opakovana_pismena_1.md`](../napovedy/06_opakovana_pismena_1.md).

Když nestačí, druhá je v souboru [`napovedy/06_opakovana_pismena_2.md`](../napovedy/06_opakovana_pismena_2.md).

## Hotovo, když

- [ ] pět nových testů je zelených
- [ ] staré testy jsou pořád zelené
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
