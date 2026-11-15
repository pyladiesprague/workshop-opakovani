# Nápověda ke kroku 4 – Kolik stál lístek?

## Funkce

`filtruj` je stavění nového seznamu: projdi pasažéry a do nového seznamu
přidej jen ty, kteří projdou podmínkou. Tahák L8, *Stavění seznamu v cyklu*.

Název sloupce přijde jako parametr, takže ho do hranatých závorek napiš bez
uvozovek:

```python
if pasazer[sloupec] == hodnota:
```

Když nikdo nevyhovuje, cyklus do seznamu nic nepřidá a funkce vrátí prázdný
seznam. Nic zvláštního pro to psát nemusíš.

`prumerna_cena`: součet cen děleno počet lidí. Cenu má každý, takže tentokrát
můžeš dělit `len(pasazeri)`. Na prázdný seznam se zeptej hned na začátku.

`nejdrazsi_listek`: pamatuj si zatím nejvyšší cenu a začni nulou.

## Program

Tři třídy projdeš cyklem přes seznam `[1, 2, 3]`.

Kdo zaplatil nejvíc, zjistíš ve dvou krocích: nejdřív nejvyšší cenu, potom
`filtruj` podle sloupce `Fare` a téhle ceny.

Počet lidí zadarmo je délka seznamu, který vrátí `filtruj(pasazeri, "Fare",
0)`.
