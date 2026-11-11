# Krok 7: A děti první?

Druhá část pravidla je „děti první“. Zapiš si dva odhady: jaké procento dětí do 16 let přežilo? A bude výsledek stejný ve všech třídách?

## Logika

Sloupec s věkovou skupinou v souboru není, musíme si ho dopočítat. Do `analyza.py` přidej dvě funkce:

- `vekova_skupina(vek)` vrátí `"dítě"` do 16 let, `"dospělý"` od 16 let a `"neznámý"`, když je věk `None`.
- `pridej_skupiny(pasazeri)` přidá každému pasažérovi sloupec `Skupina`.

Nový sloupec funguje jako ostatní, takže na něj hned můžeš použít `filtruj` a `prezivani_podle`.

## Testy

Napiš testy sama. Vyzkoušej i hranici: co vrátí `vekova_skupina` pro přesně 16 let?

## Zpráva

Vypiš postupně:

1. Přežití podle věkové skupiny.
2. Přežití dospělých podle pohlaví.
3. Přežití dětí podle třídy. U každé třídy vypiš i počet dětí.

Doplň poznámky a vrať se k hlavní otázce. Tvoje odpověď se teď možná změnila.

Podívej se ještě na řádek `neznámý`. Lidé bez věku přežívali méně často než ostatní. Kdybychom je z výpočtů prostě vyhodili, výsledek by se změnil. Co myslíš, proč u nich věk asi chybí?
