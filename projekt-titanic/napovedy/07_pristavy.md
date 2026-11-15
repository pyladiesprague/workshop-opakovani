# Nápověda ke kroku 7 – Záleželo na tom, kde kdo nastoupil?

## Funkce

`rozdel_podle` je vzor „skupiny“: slovník, kde hodnotou je seznam. Když klíč
ve slovníku ještě není, založ pod ním prázdný seznam. Potom do seznamu přidej
pasažéra. Tahák L9, *Skupiny*.

```python
skupiny = {}
for pasazer in pasazeri:
    hodnota = pasazer[sloupec]
    ...
return skupiny
```

`miry_skupin`: nový slovník se stejnými klíči. Projdi klíče a ke každému ulož
`mira_preziti` jeho seznamu. Tahák L9, *Stavění slovníku v cyklu*.

`prezivani_podle` je jeden řádek: výsledek první funkce pošli do druhé.

## Program

Rozděl pasažéry podle sloupce `Embarked` a slovník projdi cyklem přes klíče.
Tahák L9, *Procházení*.

Pod každým klíčem je seznam lidí z jednoho přístavu. Počet lidí je `len`.
Kolik z nich jelo 1. třídou, zjistíš tak, že na ten seznam zavoláš `filtruj`.

Podíl v procentech je zase část děleno celek krát sto.
