# Bonusy

## Bonus 1: Zpráva v souboru

Ulož zprávu do souboru `zprava.txt`, abys ji mohla někomu poslat nebo vytisknout.

```python
with open(SLOZKA / "zprava.txt", "w", encoding="utf-8") as f:
    f.write("Jeden řádek\n")
```

`"w"` znamená zápis a `\n` je konec řádku. `SLOZKA` si naimportuj z `analyza.py`. Soubor se díky ní uloží vedle tvého programu.

## Bonus 2: Graf v textu

Vypiš přežití podle třídy jako sloupcový graf z textu. Každý znak `█` ať znamená dvě procenta.

## Bonus 3: Grafy s knihovnou

Graf z bonusu 2 sis napsala sama. Hotové knihovny tuhle práci udělají za tebe, tak si jednu vyzkoušíme. Je to jediná věc na workshopu, kterou je potřeba instalovat.

Ve VS Code otevři **Terminal → New Terminal** a napiš:

```
python -m pip install plotext==5.3.2
```

Když to nepůjde, zavolej kouče. Verzi piš přesně takhle, novější verze se ovládá jinak.

Graf pak nakreslíš takhle:

```python
import plotext as plt

plt.simple_bar(["1. třída", "2. třída"], [63.0, 47.3], width=50, title="Přežití (%)")
plt.show()
```

1. Nakresli přežití podle třídy z výsledků funkce `prezivani_podle`.
2. Před dalším grafem zavolej `plt.clear_figure()`.
3. Nakresli vedle sebe ženy a muže v každé třídě. Použij `plt.simple_multiple_bar(nazvy, [zeny, muzi], width=50, labels=["ženy", "muži"])`.

Sloupce se přizpůsobují šířce grafu, proto se dívej i na čísla vedle nich.

## Bonus 4: Rodiny

Podle příjmení najdi největší rodiny v souboru. Přežili všichni společně, nebo se rodiny rozdělily?

## Bonus 5: Podivné ceny

Někteří pasažéři mají cenu lístku 0 a tři mají přes 512 liber. Kdo to je? Mají něco společného?
