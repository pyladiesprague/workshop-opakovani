# Krok 4 – Rozpočty

Rozpočet je částka, kterou chceš za měsíc v jedné kategorii nejvýš utratit.
Program ti řekne, kolik ti z něj zbývá, a ozve se, když ho překročíš.

```text
Co chceš udělat? 6
Měsíc (RRRR-MM): 2026-11
  jidlo        4110 /   4000 Kč   překročeno o 110 Kč
  doprava       550 /   1000 Kč   zbývá 450 Kč
  zabava        890 /   1500 Kč   zbývá 610 Kč
Překročené rozpočty: jidlo
```

Rozpočty jsou slovník `rozpocty` v souboru `ukazkova_data.py`: klíč je
kategorie, hodnota je měsíční limit v korunách. Ne každá kategorie rozpočet má.

## Funkce

Funkce píšeš do `finance.py`.

| Funkce | Co vrátí |
|---|---|
| `zbyva_v_rozpoctu(transakce, rozpocty, kategorie)` | limit kategorie mínus výdaje v ní; po překročení vyjde záporné číslo; když kategorie rozpočet nemá, vrátí `None` |
| `prekrocene_rozpocty(transakce, rozpocty)` | seznam kategorií, ve kterých se utratilo víc, než je limit |

Funkce počítají se všemi transakcemi, které dostanou. Rozpočet je ale
měsíční, takže jim budeš posílat jen transakce jednoho měsíce. Funkci,
která je vybere, už máš z kroku 3.

Součet výdajů v kategorii taky nemusíš psát znovu.

## Testy

Od tohohle kroku píšeš testy sama. Stavba je stejná jako u testů, které už
máš: data z `ukazka()`, zavolání funkce a `assert`. Rozpočty si v každém
testu připrav jako malý slovník, třeba:

```python
rozpocty = {"jidlo": 1000, "doprava": 100}
```

V `ukazka()` se za jídlo utratilo 750 Kč a za dopravu 150 Kč. Na každý
řádek tabulky napiš jeden test:

| Co vyzkoušet | Rozpočty | Volání | Má vrátit |
|---|---|---|---|
| kolik zbývá | `{"jidlo": 1000, "doprava": 100}` | `zbyva_v_rozpoctu(ukazka(), rozpocty, "jidlo")` | `250` |
| překročený rozpočet | `{"jidlo": 1000, "doprava": 100}` | `zbyva_v_rozpoctu(ukazka(), rozpocty, "doprava")` | `-50` |
| kategorie bez výdajů | `{"zabava": 500}` | `zbyva_v_rozpoctu(ukazka(), rozpocty, "zabava")` | `500` |
| kategorie bez rozpočtu | `{"jidlo": 1000}` | `zbyva_v_rozpoctu(ukazka(), rozpocty, "doprava")` | `None` |
| překročené rozpočty | `{"jidlo": 1000, "doprava": 100}` | `prekrocene_rozpocty(ukazka(), rozpocty)` | `["doprava"]` |
| utraceno přesně na korunu | `{"jidlo": 750}` | `prekrocene_rozpocty(ukazka(), rozpocty)` | `[]` |
| žádné rozpočty | `{}` | `prekrocene_rozpocty(ukazka(), rozpocty)` | rozmysli sama |

Na `None` se v testu ptej přes `is None`, viz
[tahák k testování](../../lekce-testovani/TAHAK.md), *Tvary, se kterými si
vystačíš*.

## Program

Menu je v `app.py`.

Přidej dvě volby:

- `6 – rozpočty` se zeptá na měsíc a ke každé kategorii s rozpočtem vypíše,
  kolik se utratilo, jaký je limit a kolik zbývá, nebo o kolik je překročený.
- `7 – nastavit rozpočet` se zeptá na kategorii a částku a rozpočet uloží do
  slovníku. Když kategorie rozpočet už má, přepíše ho.

A ještě jedna věc: když po přidání výdaje bude rozpočet jeho kategorie v tom
měsíci překročený, program na to hned upozorní.

```text
Přidáno.
Pozor, rozpočet na jidlo za 2026-11 je překročený o 210 Kč.
```

Měsíc transakce tvoří prvních sedm znaků jejího data.

Slovník `rozpocty` si do `app.py` naimportuj z `ukazkova_data` a funkcím,
které ho potřebují, ho pošli jako argument.

Zasekla ses? Nápověda je v souboru [`napovedy/04_rozpocty.md`](../napovedy/04_rozpocty.md).

## Hotovo, když

- [ ] máš test na každý řádek tabulky a všechny jsou zelené
- [ ] rozpočty za `2026-11` z ukázkových dat sedí s ukázkou nahoře
- [ ] nově nastavený rozpočet se hned projeví ve volbě 6
- [ ] výdaj, který rozpočet překročí, vyvolá upozornění
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
