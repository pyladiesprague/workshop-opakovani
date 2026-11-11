# Bonusy

## Bonus 1: Jak dobrý je řešič

Ve složce `moje_hra` založ soubor `bonus1.py`. Nech řešič odehrát hru s každým slovem ze souboru `hadana_slova.txt`.

Pro každé tajné slovo začni se všemi slovy a opakovaně hádej `nejlepsi_slovo` a filtruj, dokud se netrefíš. Vypiš průměrný počet pokusů, nejhorší slovo a kolikrát by řešič překročil šest pokusů.

## Bonus 2: Lepší řešič

Počítání písmen je jen odhad. Přesnější je zeptat se: kdybych hádala tohle slovo, kolik slov mi průměrně zbude?

Pro každé kandidátské slovo projdi všechna možná tajná slova a spočítej do slovníku, kolikrát padl který výsledek. Klíčem bude n-tice, seznam klíčem být nemůže:

```python
klic = tuple(vyhodnot(kandidat, tajne))
```

Když výsledek padl n-krát, zbude po něm n slov. Průměrný zbytek je součet `n * n` přes všechny výsledky, vydělený počtem možných slov. Vyber slovo s nejmenším průměrným zbytkem.

První slovo počítej jen jednou a ulož si ho. Porovnej výsledek s prvním bonusem. Je lepší? Které slovo je první?
