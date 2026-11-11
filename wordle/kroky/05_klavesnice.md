# Krok 5: Klávesnice

Pod pokusy přidej přehled písmen, aby hráč viděl, co už o kterém písmenu ví.

## Logika

Do `logika.py` přidej funkci `aktualizuj_pismena(pismena, hadane, vysledek)`. Ve slovníku `pismena` si hra pamatuje, co hráč o každém písmenu zjistil:

```python
{"k": "spravne", "a": "jinde", "t": "neni"}
```

Funkce nic nevrací. Změní slovník, který dostala:

- Písmeno, které ve slovníku ještě není, zapíše.
- `"spravne"` zapíše vždycky, a to už ve slovníku zůstane.
- `"jinde"` se nesmí zhoršit na `"neni"`.

Poslední pravidlo je potřeba, protože v hádaném slově může být stejné písmeno dvakrát a pokaždé dopadnout jinak.

## Testy

První test je hotový. U dalších doplň, co má ve slovníku být.

```python
class TestAktualizujPismena(unittest.TestCase):
    def test_zapise_vsechna_pismena(self):
        pismena = {}
        aktualizuj_pismena(pismena, "kabát", [S, J, N, N, N])
        self.assertEqual(pismena, {"k": S, "a": J, "b": N, "á": N, "t": N})

    def test_spravne_se_nikdy_nezhorsi(self):
        pismena = {"k": S}
        aktualizuj_pismena(pismena, "okapy", [N, J, N, N, N])
        self.assertEqual(pismena["k"], ___)

    def test_jinde_se_nezhorsi_na_neni(self):
        pismena = {"a": J}
        aktualizuj_pismena(pismena, "banka", [N, N, N, N, N])
        self.assertEqual(pismena["a"], ___)
```

Ještě přidej vlastní test pro stejné písmeno dvakrát v jednom slově. Ve slově `banka` vyjde první a `"jinde"` a druhé `"neni"`. Ve slovníku má zůstat `"jinde"`.

Zasekla ses? Nápověda je v souboru [`napovedy/05_klavesnice.md`](../napovedy/05_klavesnice.md), část Funkce.

## Program

Před každým pokusem vypiš klávesnici:

```python
KLAVESNICE = ["ěščřžýáíé", "qwertzuiopú", "asdfghjklů", "yxcvbnmďťňó"]
```

- Písmena, která jsou `"spravne"` nebo `"jinde"`, obarvi zeleně a žlutě jako pole.
- Písmena, která ve slově nejsou, ztlum. Slouží k tomu barva `"tlumena"`.
- Písmena, o kterých hráč ještě nic neví, vypiš bez barvy.

Zasekla ses? Nápověda je v souboru [`napovedy/05_klavesnice.md`](../napovedy/05_klavesnice.md), část Program.
