# Krok 6: Co rozhodovalo víc, pohlaví, nebo třída?

Ženy přežívaly častěji a 1. třída taky. Který z těch dvou vlivů byl silnější? Zapiš si odhad: kdo měl větší šanci, žena ve 3. třídě, nebo muž v 1.?

## Logika

Do `analyza.py` přidej dvě funkce:

- `rozdel_podle_dvou(pasazeri, sloupec1, sloupec2)` funguje jako `rozdel_podle`, jen je klíčem n-tice dvou hodnot. N-tice klíčem být může, seznam ne.
- `prezivani_podle_dvou(pasazeri, sloupec1, sloupec2)` vrátí procenta přeživších. Hotovou funkci `miry_skupin` použij znovu.

```python
miry = prezivani_podle_dvou(pasazeri, "Pclass", "Sex")
print(miry[(3, "female")])
```

## Testy

Napiš testy sama na seznamu `PASAZERI`.

## Zpráva

Vypiš všechny kombinace třídy a pohlaví a odpověz na otázku z nadpisu.

Pak porovnej ženy v 1. a ve 3. třídě. Platilo „ženy první“ pro všechny ženy stejně? Doplň poznámky.
