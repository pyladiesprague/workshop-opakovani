# Titanic

Dneska budeš datová analytička. Máš skutečný seznam pasažérů Titaniku a jednu hlavní otázku:

**Traduje se, že na Titaniku platilo pravidlo „ženy a děti první“. Opravdu platilo? A platilo pro všechny stejně?**

Odpověď v zadání nenajdeš, zjistíš ji z dat. Každý výsledek otevře další otázku a na konci sepíšeš zprávu se svým závěrem. Nakonec si položíš vlastní otázku a ukážeš ostatním, co jsi našla.

Pracovat můžeš sama nebo ve dvojici. Jsou to skuteční lidé, kteří při neštěstí zemřeli, tak s tím tak zacházej.

## Jak přemýšlí analytička

Pořád dokola se opakuje pět kroků:

1. **Polož otázku.**
2. **Odhadni odpověď.**
3. **Spočítej ji.**
4. **Porovnej výsledek** s odhadem a s tím, co už víš.
5. **Zeptej se, co tě zajímá dál.**

A pět zvyků, které se ti budou hodit:

- **Nejdřív odhad.** Bez odhadu tě žádný výsledek nepřekvapí.
- **Porovnávej.** Samotné číslo moc neřekne. Vždycky se ptej: oproti čemu?
- **Dívej se, kolik lidí ve skupině je.** Procento z pěti lidí toho moc neříká.
- **Ptej se, co chybí.** Lidé bez údajů můžou být jiní než ostatní.
- **U „proč“ buď opatrná.** Když dvě věci vycházejí spolu, ještě to neznamená, že jedna způsobuje druhou.

## Jak začít

Ve VS Code otevři složku `projekt-titanic/moje_analyza` přes **File → Open Folder**. Tady budeš pracovat celý den.

| Soubor | Co v něm je |
| --- | --- |
| `analyza.py` | Funkce, které počítají. Tady se nic nevypisuje. |
| `zprava.py` | Program, který výsledky vypíše. Spouštíš ho tlačítkem Run. |
| `test_analyza.py` | Testy funkcí z `analyza.py`. |
| `Titanic-Dataset.csv` | Data. |
| `poznamky.md` | Tvoje poznámky: odhady, výsledky a další otázky. |

## Co je v datech

V souboru je 891 pasažérů. Nejsou to všichni lidé na palubě, takže výsledky popisují jen tenhle soubor. Sloupce mají anglické názvy, jak to u skutečných dat bývá.

| Sloupec | Význam |
| --- | --- |
| `PassengerId` | Pořadové číslo |
| `Survived` | 1 = přežil, 0 = nepřežil |
| `Pclass` | Třída: 1, 2 nebo 3 |
| `Name` | Jméno, ve tvaru `Příjmení, Titul. Jméno` |
| `Sex` | `female` nebo `male` |
| `Age` | Věk. U 177 pasažérů chybí. |
| `SibSp` | Kolik sourozenců a manželů měl pasažér na palubě |
| `Parch` | Kolik rodičů a dětí měl pasažér na palubě |
| `Ticket` | Číslo lístku |
| `Fare` | Cena lístku v librách |
| `Cabin` | Kajuta. U 687 pasažérů chybí. |
| `Embarked` | Přístav nástupu: `S` Southampton, `C` Cherbourg, `Q` Queenstown |

## Jak spouštět testy

Vlevo klikni na ikonu zkumavky **Testing** a nahoře na dvě šipky **Run All Tests**. Zelená znamená, že test prošel, červená, že ne.

Test vypadá takhle:

```python
class TestMira(unittest.TestCase):
    def test_pocet_prezivsich(self):
        self.assertEqual(pocet_prezivsich(PASAZERI), 3)
```

Do `assertEqual` patří to, co funkce vrátila, a to, co vrátit měla. Slova `class` a `self` si zatím jen opiš. Co přesně znamenají, se naučíme v lekci o třídách.

Na testy nebudeme používat celý soubor, 891 řádků z hlavy nespočítáš. V `test_analyza.py` je seznam `PASAZERI` s pěti vymyšlenými pasažéry, u kterých výsledek snadno ověříš.

## Jak pracovat

Zadání je ve složce `kroky`, jeden soubor na jeden krok. Každý krok začíná otázkou.

1. Přečti si zadání a zapiš si do `poznamky.md` odhad.
2. Doplň funkce do `analyza.py` a testy do `test_analyza.py`.
3. Vypiš odpověď v `zprava.py`.
4. Doplň do `poznamky.md`, co vyšlo, co tě překvapilo a na co se chceš zeptat dál.
5. Ulož práci na GitHub: **Commit** a pak **Sync Changes**.

Když se zasekneš, zeptej se kouče.

## Kroky

| Krok | Otázka |
| --- | --- |
| [1](cviceni/01_nacteni.md) | Co v souboru vlastně je? |
| [2](cviceni/02_uklid.md) | Co v datech chybí? |
| [3](cviceni/03_pocitani.md) | Kolik lidí přežilo? |
| [4](cviceni/04_filtrovani.md) | Přežívaly ženy častěji? |
| [5](cviceni/05_skupiny.md) | Záleželo i na penězích? |
| [6](cviceni/06_dva_sloupce.md) | Co rozhodovalo víc, pohlaví, nebo třída? |
| [7](cviceni/07_deti.md) | A děti první? |
| [8](cviceni/08_zprava.md) | Co z toho plyne? |
| [9](cviceni/09_moje_otazka.md) | Co zajímá tebe? |

Kdo stihne všech devět kroků, pokračuje [bonusy](bonusy/).
