# Bonus 2 – Grafy s knihovnou

Graf v kroku 9 sis napsala sama. Hotové knihovny tuhle práci udělají za tebe,
tak si jednu vyzkoušíme. Knihovnu je potřeba nainstalovat.

Ve VS Code otevři **Terminal → New Terminal** a napiš:

```text
python -m pip install plotext==5.3.2
```

Když to nepůjde, zavolej kouče. Verzi piš přesně takhle, novější verze se
ovládá jinak.

Graf pak nakreslíš takhle:

```python
import plotext as plt

plt.simple_bar(["1. třída", "2. třída"], [10.0, 20.0], width=50, title="Přežití (%)")
plt.show()
```

Program piš do nového souboru, třeba `grafy.py`.

1. Nakresli přežití podle třídy z výsledků funkce `prezivani_podle`.
2. Před dalším grafem zavolej `plt.clear_figure()`.
3. Nakresli vedle sebe ženy a muže v každé třídě. Použij
   `plt.simple_multiple_bar(nazvy, [zeny, muzi], width=50, labels=["ženy",
   "muži"])`. Skupiny podle třídy a pohlaví ti vrátí `rozdel_podle_dvou`,
   procenta z nich udělá `miry_skupin`.

Sloupce se přizpůsobují šířce grafu, proto se dívej i na čísla vedle nich.

Porovnej výsledek se svým grafem z kroku 9. Co umí knihovna navíc? A co bylo
na vlastním grafu lepší?
