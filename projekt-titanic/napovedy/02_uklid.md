# Nápověda ke kroku 2 – Co v datech chybí?

## Funkce

`cislo_nebo_nic`: nejdřív se zeptej, jestli je text prázdný. Prázdný text je
`""`. Teprve potom převáděj funkcí `float`.

`uprav_pasazera`: udělej si kopii řádku a v kopii přepiš jednu hodnotu po
druhé. Hodnotu ve slovníku přepíšeš přes klíč. Tahák L9, *Měnění*.

```python
pasazer = radek.copy()
pasazer["Survived"] = int(radek["Survived"])
...
return pasazer
```

`uprav_pasazery`: nový seznam, do kterého přidáváš upravené pasažéry. Tahák
L8, *Stavění seznamu v cyklu*.

Proč kopie a `None`, najdeš v taháku projektu, části *None* a *Kopie
slovníku*.

## Program

Je to počítadlo: začni nulou a v cyklu přičti jedničku pokaždé, když má
pasažér věk `None`. Tahák L4, *Počítadlo*.
