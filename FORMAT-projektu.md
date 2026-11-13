# Formát workshopu pro převod na web

Návrh ze 13. 11. 2026, rozhodnutí C3 v `TODO-format.md`: projekty jdou na web
stejně jako `materialy`. Převodník v `public-pages` (`code/materials/`) dnes
čte jen `pyladiesprague/materialy`. Tenhle dokument popisuje, co má umět
přečíst z tohoto repa a jaká pravidla proto musí dodržet zdroj.

Platí stejné zásady jako u `materialy`:
- Převodník čte Git commit, ne pracovní kopii.
- Python nikdy nespouští.
- Při neznámém formátu skončí chybou s názvem souboru. Nic tiše nepřeskočí.

Až převodník formát umí, přesune se popis zdroje (část 2) do README repa jako
sekce „Pro autory“, stejně jako v `materialy`.

## 1. Co převodník najde

```text
README.md                 úvod workshopu (stránka workshopu)
lekce-<nazev>/            lekce ve formátu materialy
projekt-<nazev>/          projekt ve formátu níže
<cokoli jiného>           převodník ignoruje (TODO, pytest.ini, .vscode …)
```

Pořadí a české názvy lekcí a projektů jsou v `config.json` převodníku pro tohle
repo, stejně jako `lessons` u `materialy`. Lekce workshopu nemají číslo, pořadí
proto určuje jen konfigurace.

### Adresy na webu

Rozhodl Vojta 13. 11.: workshop je v sekci Materiály, stejně jako lekce kurzu.
Adresa je název repa a pod ním cesty jako v Gitu (u `materialy` je to stejné):

```text
/materialy/workshop-opakovani/                                    úvod workshopu (README.md)
/materialy/workshop-opakovani/lekce-testovani/…                   lekce, cesty jako v materialy
/materialy/workshop-opakovani/projekt-finance/                    README projektu
/materialy/workshop-opakovani/projekt-finance/cviceni/01_zaklad/  krok
/materialy/workshop-opakovani/projekt-finance/bonusy/             všechny bonusy na jedné stránce
/materialy/workshop-opakovani/projekt-finance/napady/             nápady na rozšíření
```

- Přehled `/materialy/` dostane pod „Hodiny“ sekci „Workshopy“ s odkazem na
  workshop.
- Závěrečný workshop (`workshop-zaverecny`) půjde stejnou cestou na
  `/materialy/workshop-zaverecny/`.
- Termín, místo a program zůstávají v `/organizace/`. Harmonogram na stránku
  workshopu jen odkáže.
- Převodník přesměrování nevytváří. Adresy se proto po rozeslání odkazů
  účastnicím už nemění, a tím pádem ani názvy složek (`projekt-wordle/`,
  `projekt-titanic/` přejmenovat dřív).

## 2. Formát zdroje

### Lekce (`lekce-<nazev>/`)

Stejný formát jako `materialy` (viz README převodníku, „Podporovaný formát
zdroje“). Jediný rozdíl je název složky bez čísla. Jedno rozšíření:

- **Pomocné soubory.** Lekce o modulech potřebuje `.py` soubory, které nejsou
  výklad ani úloha: importovaný modul (`prevody.py`), testy k ukázce
  (`test_prevody.py`), modul k řešení (`reseni/spropitne.py`).
  - Pravidlo: `.py` bez číselné předpony `NN_` je pomocný soubor.
  - Převodník ho nevykresluje jako stránku, jen na něj odkáže na GitHubu
    (u výkladu i u řešení).
  - Soubor s předponou `NN_` musí formát dodržet, jinak je to chyba.

### Projekt (`projekt-<nazev>/`)

```text
projekt-finance/
  README.md                  úvodní stránka projektu
  TAHAK.md                   odkaz na GitHub, nevykresluje se (jako v materialy)
  napady.md                  stránka „Nápady na rozšíření“ (volitelná)
  cviceni/
    01_zaklad.md             krok = jedna stránka
    02_pridani_a_odebrani.md
  napovedy/
    01_zaklad.md             nápověda ke kroku se stejným jménem
    06_opakovana_pismena_1.md   víc nápověd ke kroku: _1, _2 …
    06_opakovana_pismena_2.md
  bonusy/
    01_barvy.md              jeden bonus = jeden soubor, na webu jedna stránka se všemi bonusy
  *.py, *.json, *.txt, *.csv, podsložky s kódem
                             nevykreslují se; odkazy na ně vedou na GitHub
```

Na `main` nejsou složky `reseni/` (C1). Kdyby se tam objevily, je to chyba,
aby řešení projektu omylem neodešlo na web.

#### Krok (`cviceni/NN_nazev.md`)

1. **První řádek:** `# Krok N – Název`. N musí sedět s `NN` v názvu souboru
   (stejně jako `Cvičení N` u úloh). Pomlčka je en dash `–`.
2. **Výsledek:** hned pod titulkem, bez nadpisu. Ukázka výstupu v bloku
   `text`, nebo jedno volání funkce s výsledkem.
3. **Sekce `##`** (rozhodl Vojta 13. 11.). Pevná jména v tomhle pořadí.
   Převodník neznámý nadpis `##` nebo špatné pořadí odmítne. Chybějící sekce
   nevadí, třeba krok jen s `Program`.
   - `## Funkce` – co přibude do souboru s logikou, tabulka funkcí (D8).
     I tam, kde se soubor jmenuje jinak (`logika.py`, `analyza.py`).
   - `## Testy` – hotové testy ke zkopírování, nebo seznam případů (D9).
   - `## Program` – co přibude do spustitelného souboru. I pro Titanic, kde
     je to `zprava.py`.
   - `## Hotovo, když` – kontrolní seznam (`- …`), vždy poslední.
   - Podnadpisy `###` uvnitř sekcí jsou volné.
   - Výjimky:
     - **Krok postavený na testu napřed** smí mít `## Testy` před
       `## Funkce`. Například Wordle 6: nejdřív test, který odhalí chybu, pak
       oprava.
     - **Otevřený poslední krok bez kódu** (Titanic 9) má `## Postup` místo
       `Funkce`, `Testy` a `Program`.

   Jak na to převést dnešní kroky:

   | Dnes | Nově |
   | --- | --- |
   | Finance `## 1. Testy`, `## 2. Funkce do finance.py`, `## 3. Menu do app.py` | `## Funkce`, `## Testy`, `## Program` (Funkce před Testy, D8) |
   | Finance `## Nápověda` | soubor v `napovedy/` a řádek s odkazem |
   | Finance `## Když zbyde čas` | `napady.md` |
   | Wordle, Titanic `## Logika` | `## Funkce` |
   | Titanic `## Zpráva` | `## Program` |
   | Wordle 6 `## Testy jako první`, `## Oprava` | `## Testy`, `## Funkce` (výjimka test napřed) |
   | Titanic 8 `## Závěr` | `### Závěr` uvnitř `## Program` |
   | Titanic 9 `## Postup`, `## Prezentace` | `## Postup`, `### Prezentace` uvnitř |
4. **Odkaz na nápovědu** je jeden řádek v pevném tvaru, kdekoli v kroku:
   ```text
   Zasekla ses? Nápověda je v souboru [`napovedy/NN_nazev.md`](../napovedy/NN_nazev.md).
   Zasekla ses? Nápověda je v souboru [`napovedy/NN_nazev.md`](../napovedy/NN_nazev.md), část Funkce.
   ```
   - Na webu (rozhodl Vojta 13. 11.) převodník řádek nahradí tlačítkem
     **Zobrazit nápovědu**, stejně jako je u úloh tlačítko „Zobrazit
     řešení“. Je to blok `<details class="napoveda">` se shrnutím
     „Zobrazit nápovědu / Skrýt nápovědu“. Obsahuje celou nápovědu, případně
     jen její část `## Funkce`.
   - Víc nápověd: druhý řádek `Když nestačí, druhá je v souboru […](…_2.md).`
     Převodník blok další nápovědy vloží na konec předchozího, s tlačítkem
     **Zobrazit další nápovědu**.
     - Další tlačítko se tedy objeví až po otevření předchozí nápovědy.
     - Takhle to pokračuje, dokud jsou nápovědy k dispozici (`_1`, `_2`,
       `_3` …).
     - Stačí čisté HTML, žádný skript.
   - Pro tisk: přepínač, který dnes otevírá řešení (`tisk.js`), by měl umět
     otevřít i nápovědy.
   - Odkaz na neexistující nápovědu, nebo nápověda bez odkazu z kroku, je
     chyba.
5. **Bloky kódu** mají vždy uvedený jazyk: `python`, `text` nebo `html`. Kód
   převodník nemění.
6. **Odkazy** jsou relativní:
   - Na jiný `.md` v projektu se přepíšou na URL stránky.
   - Na jiný soubor (kód, data) vedou na GitHub ke stejnému commitu.
   - Odkaz mimo projekt je chyba, kromě odkazu na `../lekce-*/`.
7. **Odkazy na taháky lekcí** se píšou textem „Tahák L8, *Název sekce*“.
   Volitelně z nich převodník udělá odkaz na tahák v `materialy`.

#### Nápověda (`napovedy/NN_nazev[_K].md`)

- **První řádek:** `# Nápověda ke kroku N – Název`. Pro víc nápověd
  `# Nápověda K ke kroku N – Název`. N a K musí sedět s názvem souboru.
- Části `## Funkce`, `## Program` atd. jsou volitelné. Odkaz z kroku na ně
  míří slovy „část Funkce“.
- Na webu nemá vlastní stránku, je jen sbalená v kroku.

#### Bonus (`bonusy/NN_nazev.md`)

- **První řádek:** `# Bonus N – Název`. N musí sedět s názvem souboru.
- Na webu jsou všechny bonusy jedna stránka, každý bonus je sekce
  `## Bonus N – Název`, stejně jako `cviceni_bonusy` v materialy. Nadpisy uvnitř
  bonusu se proto posunou o úroveň níž.

#### README projektu

- **První řádek:** `# Název projektu` (rozhodl Vojta 13. 11.).
  - Jen krátký název bez „Projekt:“ a bez podtitulu: `# Správce osobních
    financí`, `# Wordle s řešičem`, `# Titanic`.
  - To, co projekt láká (třeba otázka u Titanicu), patří do prvního odstavce.
  - Převodník bere název stránky projektu z titulku. V `config.json` je jen
    pořadí projektů a krátký popis do přehledu workshopu (jako `description`
    u lekcí v materialy), protože úvody v README jsou na to moc dlouhé.
- Odkazy na kroky a bonusy (`cviceni/…`, `bonusy/`) se přepíšou na stránky.
- Sekce podle šablony README v `TODO-format.md`. Převodník je nekontroluje.

#### Řešení

Řešení projektů na webu nejsou, ani odkazem na větev `reseni` (rozhodl
Vojta 13. 11.). Převodník čte `main`, kde řešení projektů nejsou (C1).
Lekce mají řešení na `main` a web je ukazuje sbalené pod úlohou jako
v materialy.

## 3. Co je potřeba sjednotit v současných materiálech

Stav ke 13. 11. 2026 na `main`. ✅ = už vyhovuje.

### Celé repo
- [ ] Složky projektů: `wordle/` na `projekt-wordle/` a `titanic/` na
      `projekt-titanic/` (D7). Převodník hledá projekty podle předpony.
- ✅ `projekt-finance/`, struktura `cviceni/`, `napovedy/`, `bonusy/` (C2).
- ✅ Na `main` nejsou řešení projektů (C1).

### Lekce
- ✅ `lekce-testovani/`: všech 29 souborů výkladu, cvičení a řešení vyhovuje.
- [ ] `lekce-moduly/`: osm `.py` bez předpony, které převodník dnes odmítne.
      Po přidání pravidla „pomocné soubory“ budou v pořádku:
      `02_instalace_knihoven/test_pytest_funguje.py`,
      `03_vlastni_moduly/prevody.py`, `test_prevody.py`, `upovidany.py`,
      `cviceni/reseni/spropitne.py`, `texty.py`,
      `cviceni_bonusy/reseni/kostky.py`, `spropitne.py`.
- ✅ Řešení bonusu 2 v `lekce-moduly` (rozhodl Vojta 13. 11.): dřív
      `reseni/test_spropitne.py`, které převodník nespároval s úlohou
      `02_test_modulu.py` a které nešlo spustit. Teď je to
      `reseni/02_test_modulu.py` ve formátu řešení a vedle něj kopie
      `spropitne.py` jako pomocný soubor. Spouští se jménem:
      `python -m pytest 02_test_modulu.py` (3 testy projdou).

### Kroky

| | Finance (6) | Wordle (10) | Titanic (9) |
| --- | --- | --- | --- |
| Titulek `# Krok N – …` | ✅ | ❌ `Krok N:` | ❌ `Krok N:` |
| Výsledek pod titulkem | ✅ | ❌ chybí, kroky začínají zadáním | ❌ chybí (pozor, výsledek je odpověď; ukázat tvar s vymyšlenými čísly) |
| Sekce `##` (převod viz část 2, Krok, bod 3) | ❌ `1. Testy`, `2. Funkce do …`, `3. Menu do …`: přejmenovat a přehodit Funkce před Testy (D8) | ❌ `Logika` na `Funkce`; krok 6 na `Testy`, `Funkce` | ❌ `Logika` na `Funkce`, `Zpráva` na `Program`; krok 8 `### Závěr`; krok 9 `### Prezentace` |
| `## Hotovo, když` | ✅ | ❌ chybí všude | ❌ chybí všude |
| Odkaz na nápovědu | ❌ nápověda je přímo v kroku (`## Nápověda`), přesunout do `napovedy/` | ✅ 13 řádků v pevném tvaru | ❌ nápovědy nejsou |
| Navíc | ❌ `## Když zbyde čas`: přesunout do `napady.md` | | |
| Bloky kódu bez jazyka | ✅ | ❌ kroky 1, 9, 10 | ❌ krok 8 |

### Nápovědy
- [ ] Wordle: titulky `# Nápověda ke kroku N: …` na `# Nápověda ke kroku N – …`
      (11 souborů). Krok 6 má `Nápověda 1` a `Nápověda 2` ✅.
- [ ] Finance: vytvořit `napovedy/` ze sekcí `## Nápověda` (6 kroků).
- [ ] Titanic: napsat nápovědy (TODO), rovnou v tomhle formátu.

### Bonusy
- ✅ Všech 18 souborů začíná `# Bonus N – Název` a číslo sedí s názvem.
- [ ] Titanic `bonusy/03_grafy_s_knihovnou.md`: blok kódu bez jazyka.

### README a ostatní
- ✅ Titulky README: `# Správce osobních financí`, `# Wordle s řešičem`,
      `# Titanic` (sjednoceno 13. 11.).
- [ ] `napady.md` zatím nemá žádný projekt (TODO).
- [ ] Wordle a Titanic nemají `TAHAK.md` (Titanic ho potřebuje kvůli CSV).

### Převodník (`public-pages`)
- [ ] Zdroj `pyladiesprague/workshop-opakovani`, vlastní `config.json`
      (pořadí a názvy lekcí a projektů), výstup do
      `content/materialy/workshop-opakovani/` (adresy viz část 1).
- [ ] Sekce „Workshopy“ v šabloně přehledu `code/materials/overview.md`.
- [ ] Lekce bez čísla (`lekce-<nazev>/`) a pomocné soubory bez `NN_`.
- [ ] Projekty: stránky kroků, bonusů a nápadů, nápovědy za tlačítkem
      „Zobrazit nápovědu“ (další vnořené za „Zobrazit další nápovědu“),
      přepis odkazů, kontrola titulků, sekcí, odkazů a bloků kódu.
- [ ] Styl `details.napoveda` podle `details.reseni` a otevírání nápověd
      v `tisk.js`.
- [ ] Workflow `web.yml` v tomhle repu podle `materialy` (secret
      `PUBLIC_PAGES_TOKEN`, přeskočit ve forcích).
