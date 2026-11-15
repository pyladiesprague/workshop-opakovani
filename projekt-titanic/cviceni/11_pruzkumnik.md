# Krok 11 – Co dalšího se dá z dat zjistit?

V datech je toho víc, než se vešlo do zprávy, a v posledním kroku si vybereš
otázku vlastní. Aby se ti dobře hledalo, postavíš si na to nástroj.

Na konci tohohle kroku bude mít program průzkumníka. Zeptá se na sloupec a
ukáže přežití ve skupinách podle něj:

```text
Průzkumník: napiš název sloupce, třeba Sex nebo Titul.
Prázdný řádek program ukončí.
Sloupec: embarked
  S                        ??.? %  (???)
  C                        ??.? %  (???)
  Q                        ??.? %  (??)
Sloupec: barva
Takový sloupec neznám. Vyber si z těchhle: PassengerId, Survived, ...
Sloupec:
```

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `najdi_sloupec(text, sloupce)` | název sloupce ze seznamu `sloupce`, který odpovídá tomu, co uživatelka napsala; když takový není, vrátí `None` |
| `prehled_podle(pasazeri, sloupec)` | seznam řádků, jeden pro každou hodnotu ve sloupci: hodnota, procento přeživších a počet lidí |

Lidé píšou různě. `najdi_sloupec` má najít sloupec `Sex`, ať uživatelka napíše
`sex`, `SEX` nebo ` Sex ` s mezerami.

V `prehled_podle` použij hotovou funkci `radek_tabulky`. Název řádku musí být
text, hodnotu převedeš funkcí `str`.

## Testy

Napiš testy sama. Co vyzkoušet:

- `najdi_sloupec` s malými písmeny, s velkými písmeny a s mezerami kolem,
- `najdi_sloupec` pro sloupec, který neexistuje,
- kolik řádků vrátí `prehled_podle` pro `ukazka()` a sloupec `Embarked`.

## Program

Průzkumníka píšeš do `zprava.py`, pod výpis zprávy.

Pod výpis zprávy přidej cyklus:

1. Zeptej se na sloupec. Prázdná odpověď program ukončí.
2. Když sloupec neexistuje, řekni to a vypiš, ze kterých si uživatelka může
   vybrat.
3. Když existuje, vypiš přehled. Sloupce jako `Name` mají stovky různých
   hodnot. Když má přehled víc než dvacet řádků, vypiš místo něj jen zprávu,
   že je hodnot moc.

Seznam všech sloupců získáš takhle: `list(pasazeri[0])`.

Teď si průzkumníka vyzkoušej na sloupci `Titul`. Ten vznikl v kroku 5. Pokud
jsi ho přeskočila, je teď dobrá chvíle se k němu vrátit. Potom doplň poznámky:

- Podle výpisu nepřežil žádný duchovní (`Rev`) a přežila každá hraběnka. Kolik
  jich ale bylo?
- Kterým řádkům bys věřila a kterým ne? Podle čeho to poznáš?

Zasekla ses? Nápověda je v souboru [`napovedy/11_pruzkumnik.md`](../napovedy/11_pruzkumnik.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] průzkumník najde sloupec bez ohledu na velká a malá písmena a mezery
      kolem
- [ ] neznámý sloupec ani prázdná odpověď program neshodí
- [ ] u sloupce s moc hodnotami program vypíše jen zprávu
- [ ] v `poznamky.md` máš, kterým řádkům u titulů věříš a kterým ne
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
