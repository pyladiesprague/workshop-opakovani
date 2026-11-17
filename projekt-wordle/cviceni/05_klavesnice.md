# Krok 5 – Klávesnice

Na konci tohohle kroku hra před každým pokusem ukáže klávesnici, na které je
vidět, co už hráč o kterém písmenu ví:

```text
 Ě   Š   Č   Ř   Ž   Ý   Á   Í   É
 Q   W   E   R   T   Z   U   I   O   P   Ú
 A   S   D   F   G   H   J   K   L   Ů
 Y   X   C   V   B   N   M   Ď   Ť   Ň   Ó

Tvůj pokus:
```

## Funkce

Funkce píšeš do `logika.py`.

| Funkce | Co dělá |
| --- | --- |
| `aktualizuj_pismena(pismena, hadane, vysledek)` | do slovníku `pismena` zapíše, co hráč o písmenech hádaného slova zjistil; nic nevrací |

Slovník `pismena` vypadá třeba takhle:

```python
{"k": "spravne", "a": "jinde", "t": "neni"}
```

Funkce mění slovník, který dostala:

- Písmeno, které ve slovníku ještě není, zapíše.
- `"spravne"` zapíše vždycky, a to už ve slovníku zůstane.
- `"jinde"` se nesmí zhoršit na `"neni"`.

Poslední pravidlo je potřeba, protože v hádaném slově může být stejné písmeno
dvakrát a pokaždé dopadnout jinak.

## Testy

První test je hotový. U dalších doplň, co má ve slovníku být.

```python
def test_zapise_vsechna_pismena():
    pismena = {}
    logika.aktualizuj_pismena(pismena, "kabát", [S, J, N, N, N])
    assert pismena == {"k": S, "a": J, "b": N, "á": N, "t": N}


def test_spravne_se_nikdy_nezhorsi():
    pismena = {"k": S}
    logika.aktualizuj_pismena(pismena, "okapy", [N, J, N, N, N])
    assert pismena["k"] == ___


def test_jinde_se_nezhorsi_na_neni():
    pismena = {"a": J}
    logika.aktualizuj_pismena(pismena, "banka", [N, N, N, N, N])
    assert pismena["a"] == ___
```

**Vlastní test:** stejné písmeno dvakrát v jednom slově. Ve slově `banka`
vyjde první `a` jako `"jinde"` a druhé jako `"neni"`. Ve slovníku má
zůstat `"jinde"`.

## Program

Program píšeš do `wordle.py`.

Před každým pokusem vypiš klávesnici:

```python
KLAVESNICE = ["ěščřžýáíé", "qwertzuiopú", "asdfghjklů", "yxcvbnmďťňó"]
```

- Písmena, která jsou `"spravne"` nebo `"jinde"`, obarvi zeleně a žlutě jako
  pole.
- Písmena, která ve slově nejsou, ztlum. Slouží k tomu barva `"tlumena"`.
- Písmena, o kterých hráč ještě nic neví, vypiš bez barvy.

Zasekla ses? Nápověda je v souboru [`napovedy/05_klavesnice.md`](../napovedy/05_klavesnice.md).

## Hotovo, když

- [ ] všechny testy včetně tvého vlastního jsou zelené
- [ ] klávesnice se vypíše před každým pokusem
- [ ] písmeno, které jednou zezelenalo, zůstane zelené až do konce hry
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
