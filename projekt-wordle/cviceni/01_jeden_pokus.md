# Krok 1 – Jeden pokus

Na konci tohohle kroku program vyhodnotí jedno hádané slovo:

```text
Tvůj pokus: kabát
k a b á t
+ ? - - -
```

Tajné slovo je tady `kočka`. Značka `+` znamená, že písmeno sedí, `?` že ve
slově je, ale jinde, a `-` že ve slově není.

## Funkce

Funkce píšeš do `logika.py`.

| Funkce | Co vrátí |
| --- | --- |
| `vyhodnot(hadane, tajne)` | seznam pěti řetězců, jeden pro každé písmeno hádaného slova |

V seznamu můžou být tři hodnoty:

| Hodnota | Význam |
| --- | --- |
| `"spravne"` | Písmeno je ve slově a stojí na správném místě. |
| `"jinde"` | Písmeno ve slově je, ale na jiném místě. |
| `"neni"` | Písmeno ve slově není. |

```python
vyhodnot("kabát", "kočka")
# ["spravne", "jinde", "neni", "neni", "neni"]
```

Nahoře v `logika.py` jsou dvě konstanty, `DELKA_SLOVA` a `POCET_POKUSU`.
Konstanta je obyčejná proměnná, kterou program nikde nemění. Velká písmena v
názvu to dávají najevo. Používej je místo čísel 5 a 6.

## Testy

Otevři `test_logika.py` a tyhle testy zkopíruj na jeho konec:

```python
def test_uhodnute_slovo():
    assert logika.vyhodnot("panna", "panna") == [S, S, S, S, S]


def test_zadna_shoda():
    assert logika.vyhodnot("mléko", "sušit") == [N, N, N, N, N]


def test_pismeno_na_jinem_miste():
    assert logika.vyhodnot("kabát", "kočka") == [S, J, N, N, N]


def test_diakritika_je_jine_pismeno():
    assert logika.vyhodnot("město", "mesto") == [S, N, S, S, S]
```

`S`, `J` a `N` jsou zkratky pro `"spravne"`, `"jinde"` a `"neni"`. Najdeš je
nahoře v souboru s testy.

Spusť testy v panelu **Testing**. Budou červené a v hlášce uvidíš
`AttributeError: module 'logika' has no attribute 'vyhodnot'`. To je v
pořádku: testy popisují funkci, která ještě neexistuje. Napiš ji tak, aby
zezelenaly.

Slova se stejným písmenem dvakrát teď neřeš, přijdou na řadu v kroku 6.

## Program

Program píšeš do `wordle.py`.

1. Napiš funkci `vypis_pokus(hadane, vysledek)`, která vypíše slovo a pod něj
   značky `+`, `?` a `-` jako v ukázce nahoře.
2. Tajné slovo si zatím napiš přímo do kódu. Zeptej se hráče na slovo,
   vyhodnoť ho a vypiš.

Na začátku `wordle.py` už je `import logika`. Funkce a konstanty
z `logika.py` proto voláš s tečkou, stejně jako v testech:

```python
vysledek = logika.vyhodnot(hadane, "kočka")
```

Import už nikdy měnit nemusíš. Každá funkce, kterou do `logika.py` přidáš,
je ve `wordle.py` hned k dispozici jako `logika.jmeno_funkce`, konstanty
jako `logika.DELKA_SLOVA`.

Zasekla ses? Nápověda je v souboru [`napovedy/01_jeden_pokus.md`](../napovedy/01_jeden_pokus.md).

## Hotovo, když

- [ ] všech pět testů je zelených
- [ ] pro slovo `kabát` program vypíše `+ ? - - -`
- [ ] pro slovo `kočka` vypíše pět plusů
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
