# Bonus 1 – Barvy v terminálu

Příjmy zeleně, výdaje červeně, upozornění žlutě. Program se hned líp čte.

Terminál text obarví, když před něj vypíšeš zvláštní kód. Kód je obyčejný
řetězec. Začíná `\033[`, což je jeden neviditelný znak zapsaný zpětným
lomítkem, podobně jako `\n`.

```python
print("\033[32m" + "Tohle je zeleně." + "\033[0m")
```

| Kód | Co dělá |
|---|---|
| `"\033[31m"` | červená |
| `"\033[32m"` | zelená |
| `"\033[33m"` | žlutá |
| `"\033[36m"` | tyrkysová |
| `"\033[1m"` | tučné písmo |
| `"\033[0m"` | konec: vrátí obyčejné písmo |

Bez kódu pro konec by zůstalo obarvené i všechno, co vypíšeš potom.

Kódy si nikdo nepamatuje. Ulož je do slovníku `BARVY`, kde klíč je jméno
barvy, a napiš do `finance.py` funkci `obarvi(text, barva)`. Ta vrátí text,
před kterým je kód barvy a za kterým je kód pro konec:

```python
print(obarvi("Zůstatek: 25540 Kč", "zelena"))
```

Kde se barvy hodí:

- částky ve výpisu: příjmy zeleně, výdaje červeně,
- zůstatek: záporný červeně,
- hlášky o špatném vstupu žlutě,
- překročený rozpočet červeně, rozpočet v pořádku zeleně,
- sloupce grafu.

Dvě věci, na které si dej pozor:

- **Zarovnání.** Kódy barev nejsou vidět, ale jsou to znaky a `f"{text:10}"`
  je počítá do šířky. Text proto nejdřív zarovnej a až potom obarvi.
- **Testy.** Do funkce `sloupec` barvu nedávej. Testy z kroku 5 čekají
  přesný text bez barev. Obarvi až to, co funkce vrátí.

Testy: obarvený text začíná kódem barvy, končí kódem pro konec a obsahuje
původní text. O kolik znaků je delší než původní?

Kdyby se ti místo barev vypisovaly znaky jako `←[32m`, tvůj terminál barvy
neumí. V terminálu ve VS Code fungují.
