# Bonus 1 – Zpráva v souboru

Na konci tohohle bonusu bude zpráva uložená v souboru `zprava.txt`, takže ji
můžeš někomu poslat nebo vytisknout.

Do souboru se zapisuje takhle:

```python
with open(analyza.SLOZKA / "zprava.txt", "w", encoding="utf-8") as f:
    f.write("Jeden řádek\n")
```

- `"w"` znamená zápis. Když soubor neexistuje, vytvoří se. Když existuje,
  přepíše se.
- `\n` je konec řádku. Na rozdíl od `print` ho `write` sám nepřidá.
- `analyza.SLOZKA` je složka, ve které leží `analyza.py`. Soubor se díky ní
  uloží vedle tvého programu.

Zprávu máš jako seznam řádků ze `sestav_zpravu`, takže stačí cyklus.

Hotovo, když soubor `zprava.txt` otevřeš ve VS Code a je v něm totéž, co
program vypisuje, včetně háčků a čárek.
