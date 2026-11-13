# Bonus 1 – Zpráva v souboru

Ulož zprávu do souboru `zprava.txt`, abys ji mohla někomu poslat nebo vytisknout.

```python
with open(SLOZKA / "zprava.txt", "w", encoding="utf-8") as f:
    f.write("Jeden řádek\n")
```

`"w"` znamená zápis a `\n` je konec řádku. `SLOZKA` si naimportuj z `analyza.py`. Soubor se díky ní uloží vedle tvého programu.
