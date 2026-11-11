# Krok 5: Záleželo i na penězích?

Ženy přežívaly mnohem častěji. Jenže pasažéři se lišili i třídou, a tedy penězi. Měli lidé z 1. třídy větší šanci? Zapiš si odhad pro všechny tři třídy.

Mohla bys zavolat `filtruj` třikrát, jednou pro každou třídu. Co ale u sloupce, kde hodnot neznáš? Napíšeme funkci, která skupiny najde sama.

## Logika

Do `analyza.py` přidej dvě funkce:

- `rozdel_podle(pasazeri, sloupec)` vrátí slovník, kde klíče jsou hodnoty ze sloupce a hodnoty jsou seznamy pasažérů.
- `miry_skupin(skupiny)` dostane takový slovník a vrátí slovník, kde hodnoty jsou procenta přeživších.
- `prezivani_podle(pasazeri, sloupec)` spojí obě předchozí funkce.

```python
prezivani_podle(pasazeri, "Sex")
# {"male": 18.9..., "female": 74.2...}
```

## Testy

Od tohoto kroku píšeš testy sama. Vezmi seznam `PASAZERI` a spočítej z hlavy, co má vyjít.

Pozor na výsledky jako 100 / 3. Desetinná čísla se v počítači ukládají nepřesně, proto na ně používej `assertAlmostEqual`:

```python
self.assertAlmostEqual(miry["male"], 100 / 3)
```

## Zpráva

Vypiš přežití podle třídy. Pak stejnou funkcí zkus i jiný sloupec. Doplň poznámky.
