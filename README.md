# Workshop – opakování

Opakovací workshop kurzu PyLadies Praha (běh **podzim 2026**), sobota
21. 11. 2026. Zopakujeme si to hlavní z dosavadních lekcí, přidáme moduly
a testy a pak celý den stavíš vlastní program.

Výukové materiály k jednotlivým lekcím najdeš v repozitáři
[materialy](https://github.com/pyladiesprague/materialy).

## Než přijdeš

Připrav si počítač podle návodu [Před workshopem](PRED-WORKSHOPEM.md):
fork, clone a instalace knihoven. Zabere asi dvacet minut a ráno pak
můžeme hned začít.

## Jak den probíhá

1. **Ráno** si zkontrolujeme, že všem fungují testy, a projdeme dvě krátké
   lekce: moduly a testování s pytestem.
2. **Pak si vybereš jeden projekt** a pracuješ na něm zbytek dne, nejlépe ve
   dvojici. Projekt je rozdělený na kroky. Každý krok má zadání, testy a
   nápovědu a končí seznamem „Hotovo, když“.
3. **Po každém kroku** svou práci uložíš na GitHub: **Commit** a pak
   **Sync Changes**.
4. **Na konci dne** ukážeš ostatním, co jsi postavila. Nemusí to být hotové,
   stačí ukázat, co program umí, a říct, co ti dalo nejvíc práce.

Nikdo nemusí stihnout všechny kroky. Důležité je, aby to, co máš, fungovalo
a dávalo ti smysl.

## Jak si materiály stáhnout

Na workshopu pracuješ ve vlastním forku, stejně jako s `materialy`:

1. Nahoře klikni na **Fork** a pak na **Create fork**.
2. Fork si naklonuj v GitHub Desktop (**File → Clone repository**).
3. Ve VS Code otevři celou složku `workshop-opakovani`
   (**File → Open Folder**), ne jen jeden projekt nebo soubor.

Podrobně je to v návodu [Před workshopem](PRED-WORKSHOPEM.md).

Když clone nejde: nahoře klikni na zelené tlačítko **Code → Download ZIP**.
Stažený archiv rozbal a složku otevři ve VS Code (**File → Open Folder**).
Programovat se dá i tak, jen svou práci nebudeš ukládat na GitHub.

## Testy

Projekty stojí na testech. Ve VS Code je spouštíš v panelu **Testing**
(ikona baňky vlevo). Panel ukazuje testy všech projektů a lekcí. Jen svoje
spustíš šipkou u složky svého projektu, třeba `projekt-finance`.

V terminálu jde totéž:

```text
python -m pytest projekt-finance
```

Na Macu místo `python` piš `python3`.

## Lekce

| Složka | Téma |
|---|---|
| [`lekce-moduly/`](lekce-moduly/TAHAK.md) | vestavěné moduly, instalace knihoven přes pip a vlastní moduly |
| [`lekce-testovani/`](lekce-testovani/TAHAK.md) | `assert`, první testy s pytestem a jak číst test, který neprošel |

Začni moduly, testy na ně navazují. Soubory s výkladem procházej popořadě podle čísla, spouštěj je tlačítkem
**Run** a čti komentáře. Pak se pusť do složky `cviceni/`.

## Projekty

Vyber si jeden. Všechny tři procvičují totéž: funkce, seznamy, slovníky a
testy. Liší se tím, co na konci máš.

| Složka | Projekt |
|---|---|
| [`projekt-finance/`](projekt-finance/README.md) | Správce osobních financí: příjmy, výdaje, rozpočty a grafy v terminálu |
| [`projekt-wordle/`](projekt-wordle/README.md) | Wordle s řešičem: česká hra Wordle a program, který ji umí hrát sám |
| [`projekt-titanic/`](projekt-titanic/README.md) | Titanic: z dat o skutečných pasažérech zjistíš, kdo byl na palubě a jak dopadl |

Každý projekt začíná souborem `README.md`: co postavíš, jak začít a co dělat,
když se zasekneš.

## Když se zasekneš

1. Přečti si chybovou hlášku odspodu.
2. Otevři nápovědu ke kroku. Odkaz na ni je v zadání nad „Hotovo, když“.
3. Zeptej se kolegyně ve dvojici nebo u stolu.
4. Zavolej kouče.

---

Obsah sem přidávají koučové. Pokud chceš navrhnout úpravu, pošli pull request.
