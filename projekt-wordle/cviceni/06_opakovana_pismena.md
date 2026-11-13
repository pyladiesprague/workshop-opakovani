# Krok 6 – Opakovaná písmena

Funkce `vyhodnot` má chybu, kterou zatím nebylo vidět. Pro hádané slovo `banka` a tajné slovo `sonda` vrátí `- ? + - +`.

Tajné slovo `sonda` má jedno a, a to je na konci, kde ho hráč trefil. Funkce přesto hlásí, že a na druhém místě je `"jinde"`. Hráč si pak myslí, že jsou ve slově dvě.

Tenhle krok je nejtěžší z celého dne. Když ti nepůjde, přeskoč ho a vrať se k němu později. Další kroky fungují i bez něj.

## Testy

Tentokrát začni testy. Napiš je celé sama a teprve potom oprav funkci. Některé budou červené, a to je správně.

Do `test_logika.py` přidej třídu `TestOpakovanaPismena`. Výsledky jsou tady psané značkami `+ ? -`:

| Volání | Výsledek |
| --- | --- |
| `vyhodnot("banka", "sonda")` | `- - + - +` |
| `vyhodnot("mamka", "mléko")` | `+ - - + -` |
| `vyhodnot("banka", "okapy")` | `- ? - ? -` |
| `vyhodnot("kočka", "kabát")` | `+ - - - ?` |
| `vyhodnot("nanuk", "panna")` | `? + + - -` |

## Funkce

Každé písmeno tajného slova jde použít jen jednou a přesné shody mají přednost. Jeden průchod slovem stačit nebude, takže si to nejdřív rozmysli na papíře. Zkus si ručně vyhodnotit `banka` proti `sonda`: co musíš vědět, než rozhodneš o prvním a?

Zasekla ses? Nápověda je v souboru [`napovedy/06_opakovana_pismena_1.md`](../napovedy/06_opakovana_pismena_1.md).

Když nestačí, druhá je v souboru [`napovedy/06_opakovana_pismena_2.md`](../napovedy/06_opakovana_pismena_2.md).
