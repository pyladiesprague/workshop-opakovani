# Nápověda ke kroku 2 – Celá hra

- Mezery kolem textu a malá písmena: metody `strip` a `lower`. Tahák L6,
  *Metody řetězců*.
- Ptaní, dokud není odpověď v pořádku: `while True`. Tahák L4, *Nekonečný
  cyklus*.

Funkce `nacti_slovo` je nekonečný cyklus, ze kterého vyskočíš příkazem
`return`:

```python
def nacti_slovo():
    while True:
        slovo = uprav_vstup(input("Tvůj pokus: "))
        ...
```

Ve funkci `zahraj` počítej pokusy od jedničky: `for pokus in range(1,
POCET_POKUSU + 1)`.

Když hráč uhodne, ukonči funkci příkazem `return`. Co je napsané za cyklem, se
pak provede jen při prohře.
