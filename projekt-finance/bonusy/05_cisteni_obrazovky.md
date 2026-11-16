# Bonus 5 – Čistá obrazovka

Menu v `app.py` se po každé volbě vypíše znovu pod předchozí výstup a starší
výpisy ujíždějí nahoru. Na konci tohohle bonusu program před každým menu
obrazovku smaže, takže je vidět jen menu a výsledek poslední volby.

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

Funkci dej do `app.py`. Vypisuje, takže do `finance.py` nepatří.

1. Na začátku každého průchodu hlavním cyklem obrazovku smaž.
2. Narazíš na problém: výpis transakcí nebo graf se ukáže a hned zmizí,
   protože cyklus obrazovku smaže a vypíše menu. Vymysli, jak to vyřešit.
3. Nad menu vypiš zůstatek, ať ho máš pořád na očích.
