# Krok 4 – Barvy

Na konci tohohle kroku hra místo značek `+ ? -` ukazuje barevná pole a po
každém pokusu vypíše všechny dosavadní pokusy pod sebe:

```text
 K   A   B   Á   T
 P   A   U   Z   A
```

Na obrazovce bude každé písmeno ve svém poli: zelené sedí, žluté je ve slově
jinde, šedé ve slově není.

Do importu přidej `obarvi`:

```python
from pomocnik import nacti_radky, obarvi
```

`obarvi(" K ", "zelena")` vrátí text, který se vypíše s barevným pozadím.
Barvy jsou `"zelena"`, `"zluta"` a `"seda"`.

Tahle změna se týká jen výpisu, takže se `logika.py` ani testy nemění. Až
budeš hotová, testy musí být pořád zelené.

## Program

Program píšeš do `wordle.py`.

1. Ve funkci `zahraj` si pokusy ukládej do seznamu n-tic `(hadane, vysledek)`.
2. Místo `vypis_pokus` napiš funkci `vypis_pokusy(pokusy)`. Po každém pokusu
   vypíše všechny dosavadní pokusy pod sebe, každé písmeno ve svém barevném
   poli. Písmena piš velká, řetězec na to má metodu `upper()`.

Zasekla ses? Nápověda je v souboru [`napovedy/04_barvy.md`](../napovedy/04_barvy.md).

## Hotovo, když

- [ ] testy jsou pořád zelené
- [ ] po každém pokusu vidíš všechny pokusy pod sebou
- [ ] barvy odpovídají tomu, co dřív ukazovaly značky
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
