# Krok 4: Barvy

Značky `+ ? -` nahraď barevnými poli jako ve skutečném Wordle. Do importu přidej `obarvi`:

```python
from pomocnik import nacti_radky, obarvi
```

`obarvi(" K ", "zelena")` vrátí text, který se vypíše s barevným pozadím. Barvy jsou `"zelena"`, `"zluta"` a `"seda"`.

## Program

1. Ve funkci `zahraj` si pokusy ukládej do seznamu n-tic `(hadane, vysledek)`.
2. Místo `vypis_pokus` napiš funkci `vypis_pokusy(pokusy)`. Po každém pokusu vypíše všechny dosavadní pokusy pod sebe, každé písmeno ve svém barevném poli. Písmena piš velká, řetězec na to má metodu `upper()`.

Správné písmeno je zelené, písmeno na jiném místě žluté a písmeno, které ve slově není, šedé.

Tahle změna se týká jen výpisu, takže se `logika.py` ani testy nemění.

Zasekla ses? Nápověda je v souboru [`napovedy/04_barvy.md`](../napovedy/04_barvy.md).
