# Nápověda ke kroku 5 – Co prozradí jména?

## Funkce

`split` rozdělí text na seznam a z něj si vezmeš kousek přes index. Tahák L8,
*Text a seznam*.

`titul`: rozděl jméno podle čárky a vezmi druhý kousek. Ten rozděl podle tečky
a vezmi první kousek. Zbylé mezery odstraní `strip`. Tahák L6, *Metody
řetězců*.

`krestni_jmeno`: rozděl jméno podle tečky a vezmi druhý kousek. Ten rozděl na
slova, tedy `split()` bez parametru, a vezmi první slovo.

- Seznam slov může být prázdný. Zeptej se na to přes `len`, než sáhneš na
  index 0.
- Uvozovky a závorky kolem slova odstraní `strip('"()')`.

`pridej_jmena` nic nevrací. Mění slovníky, které v seznamu dostala: každému
přidá dva nové klíče. Tahák L9, *Slovník ve funkci*.

```python
for pasazer in pasazeri:
    pasazer["Titul"] = ...
```

`pocty` je počítadlo: když hodnota ve slovníku ještě není, začni jedničkou,
jinak přičti jedna. Tahák L9, *Počítadlo*.

## Program

Ve `zprava.py` zavolej `analyza.pridej_jmena(pasazeri)` hned po načtení dat.

Tituly: zavolej `pocty` na sloupec `Titul` a slovník projdi cyklem. Tahák L9,
*Procházení*.

Jména: nejdřív si vyfiltruj muže, potom na ně zavolej `pocty` se sloupcem
`Krestni`. V cyklu vypiš jen jména, která mají počet aspoň deset.
