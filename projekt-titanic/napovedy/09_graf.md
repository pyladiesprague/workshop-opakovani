# Nápověda ke kroku 9 – Jak to ukázat na první pohled?

## Funkce

`sloupec_grafu`: délka sloupce je trojčlenka. Hodnota `nejvyssi` má `sirka`
znaků, kolik jich má `hodnota`?

- Počet znaků musí být celé číslo. Desetinné číslo převedeš funkcí `int`, ta
  desetinnou část zahodí.
- Opakování textu: `"█" * 5`.
- Dvě výjimky ošetři podmínkami: nulu nebo nulové `nejvyssi` na začátku
  funkce, příliš malou hodnotu po výpočtu délky.

`graf`: začni seznamem s prázdným řádkem a nadpisem. Potom projdi slovník
`popisky`. Tím je dané pořadí řádků.

```python
radky = ["", nadpis]
for klic in popisky:
    if klic in skupiny:
        ...
return radky
```

Aby procenta stála pod sebou, zarovnej název i sloupec na pevnou šířku. Tahák
L6, *Za dvojtečkou se říká, jak to má vypadat*.

## Program

`graf` vrací seznam řádků. Vypíšeš je cyklem, jeden `print` na řádek.
