# Bonus 5 – Čistá obrazovka

Průzkumník z kroku 11 vypisuje jednu odpověď pod druhou a starší výsledky
ujíždějí nahoru. Na konci tohohle bonusu program před každým přehledem
obrazovku smaže, takže je vidět vždycky jen poslední odpověď.

Terminál smažeš takhle. Windows má na to příkaz `cls`, macOS a Linux příkaz
`clear`:

```python
import os


def vycisti_obrazovku():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
```

Funkci dej do `zprava.py`. Vypisuje, takže do `analyza.py` nepatří.

1. Před každým přehledem obrazovku smaž.
2. Nad přehled vypiš, podle kterého sloupce je.
3. Narazíš na problém: když program napíše „Takový sloupec neznám“ a hned
   potom obrazovku smaže, uživatelka si to nestihne přečíst. Vymysli, jak to
   vyřešit.
