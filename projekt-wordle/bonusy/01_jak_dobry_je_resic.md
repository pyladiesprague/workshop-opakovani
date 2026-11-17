# Bonus 1 – Jak dobrý je řešič

Řešič umí poradit jedno slovo. Jak dobře by ale hrál celou hru? Na konci
tohohle bonusu to budeš vědět:

```text
První slovo: ?????
Průměr: ?.?? pokusu
Nejhorší slovo: ????? (? pokusů)
Víc než šest pokusů: ?
```

Ve složce projektu založ soubor `bonus1.py` a na jeho začátek napiš
`import logika`, stejně jako ve hře. Nech řešič odehrát hru s každým slovem
ze souboru `hadana_slova.txt`.

Pro každé tajné slovo začni se všemi slovy a opakovaně hádej `nejlepsi_slovo`
a filtruj, dokud se netrefíš. Vypiš průměrný počet pokusů, nejhorší slovo a
kolikrát by řešič překročil šest pokusů.

Tady žádný `input()` není, program hraje sám proti sobě. Hru jednoho slova si
napiš jako funkci, která vrátí počet pokusů.
