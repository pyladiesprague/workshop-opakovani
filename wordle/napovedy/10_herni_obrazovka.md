# Nápověda ke kroku 10: Herní obrazovka

Překreslovat se musí i po špatně zadaném slově, takže `vykresli` patří dovnitř cyklu ve funkci `nacti_slovo`. Ta k tomu potřebuje `pokusy` a `pismena` jako další parametry:

```python
def nacti_slovo(pokusy, pismena, povolena, mozna):
    zprava = ""
    while True:
        vykresli(pokusy, pismena, zprava)
        slovo = uprav_vstup(input("  Tvůj pokus: "))
        ...
```

V cyklu už nic nevypisuj přes `print`. Nápovědu, radu i chybu jen ulož do `zprava`.
