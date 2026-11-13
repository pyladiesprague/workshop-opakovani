# Bonusy

Máš hotové kroky a zbývá čas? Vyber si, co tě láká. Bonusy na sebe
nenavazují a pořadí je na tobě.

U každého platí totéž co u kroků: logiku piš jako funkci do `finance.py`,
napiš k ní aspoň jeden test a teprve potom ji přidej do menu.

## Bonus 1 – Barvy v terminálu

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

## Bonus 2 – Hledání

Funkce `najdi(transakce, text)` vrátí seznam transakcí, které mají hledaný
text v popisu. Na velikosti písmen nezáleží: `"NÁKUP"` najde `"velký nákup"`.

Testy: hledání najde víc transakcí, nenajde nic, nezáleží na velikosti písmen.

## Bonus 3 – Řazení podle částky

Funkce `serazene_podle_castky(transakce)` vrátí nový seznam transakcí
seřazený od nejvyšší částky. Původní seznam nechá být.

Seznam slovníků metodou `sort` přímo neseřadíš. Seznam n-tic ano: n-tice se
porovnávají podle první položky, a když se shodují, podle druhé. Postav
tedy seznam dvojic `(castka, index)`, seřaď ho a podle indexů poskládej
výsledek.

Vyzkoušej, co se stane, když místo indexu dáš do dvojice rovnou slovník
a dvě transakce mají stejnou částku.

## Bonus 4 – HTML report

Grafické rozhraní bez jediné knihovny: program vyrobí webovou stránku
s přehledem a ty si ji otevřeš v prohlížeči.

Napiš funkci `html_report(transakce)`, která vrátí text stránky v jazyce
HTML. Stránka ukáže zůstatek, tabulku transakcí a sloupcový graf výdajů
podle kategorií. V menu pak text zapiš do souboru `report.html` a otevři ho.

Kostra stránky, od které se můžeš odrazit:

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="utf-8">
  <title>Moje finance</title>
</head>
<body>
  <h1>Moje finance</h1>
  <p>Zůstatek: 25540 Kč</p>
  <table>
    <tr><th>Datum</th><th>Popis</th><th>Částka</th></tr>
    <tr><td>2026-11-02</td><td>nájem</td><td>-14000 Kč</td></tr>
  </table>
  <div style="background: teal; height: 20px; width: 300px"></div>
</body>
</html>
```

- Řádky tabulky postav v cyklu do seznamu a spoj je přes `"\n".join(...)`.
- Sloupec grafu je `<div>`, kterému nastavíš šířku v pixelech. Šířku
  spočítej stejně jako délku sloupce v kroku 5.
- Zápis textu do souboru: `soubor.write(text)` uvnitř `with open(...)`.
  Viz `TAHAK.md`, *Soubory a JSON*.
- Otevření v prohlížeči: `import webbrowser` a `webbrowser.open("report.html")`.
- Pozor na složené závorky. Když do f-stringu vložíš styly CSS, které je
  používají, Python je bude brát jako místo pro hodnotu. Styly proto nech
  v obyčejném řetězci a s f-stringem je spoj přes `+`.

Test: text, který funkce vrátí, obsahuje `<table>` a popis některé transakce.

## Bonus 5 – Cíl spoření

Funkce `mesicu_do_cile(usetreno, cil, mesicni_uspora)` vrátí, za kolik
měsíců naspoříš cílovou částku. Když je měsíční úspora nula nebo záporná,
vrátí `None`, protože cíle nikdy nedosáhneš.

V menu se zeptej na cíl. Jako to, co už máš, vezmi zůstatek. Měsíční úsporu
spočítej jako průměrný rozdíl příjmů a výdajů za měsíce, které jsou v datech.

## Bonus 6 – Opakující se platby

Nájem a lítačku platíš každý měsíc. Udělej si seznam pravidelných plateb
a volbu „založit nový měsíc“, která je pro zadaný měsíc přidá všechny
najednou. Hlídej, ať stejný měsíc nejde založit dvakrát.

## Bonus 7 – Export do CSV

Funkce `radek_csv(t)` vrátí transakci jako jeden řádek textu s údaji
oddělenými středníkem: `2026-11-02;vydaj;14000;bydleni;nájem`.
Všechny řádky zapiš do souboru `finance.csv` a otevři ho v Excelu.

Se soubory CSV budeme pracovat ve 13. lekci. Tohle je ochutnávka.

## Bonus 8 – Krok zpět

Volba „vrátit poslední změnu“ vrátí seznam transakcí do stavu před
posledním přidáním nebo odebráním. Před každou změnou si schovej kopii
seznamu. Tahák L8, *Dvě jména, jeden seznam*.

## Bonus 9 – Náhodná data

Funkce `nahodne_transakce(pocet)` vyrobí seznam náhodných transakcí:
náhodný den, kategorii a částku. Hodí se na zkoušení přehledů a grafů
s větším množstvím dat. `randrange` a `choice` znáš z `random`.

Jak otestuješ funkci, která pokaždé vrátí něco jiného? Zkontroluj to, co
platit musí vždycky: počet, povolené kategorie, kladné částky.

## Bonus 10 – Kategorie podle popisu

Slovník klíčových slov, třeba `{"lidl": "jidlo", "lítačka": "doprava"}`,
a funkce `odhadni_kategorii(popis, klicova_slova)`, která podle popisu
navrhne kategorii. Když žádné slovo nenajde, vrátí `"ostatni"`. Při
přidávání transakce pak kategorii nabídni a nech ji potvrdit Enterem.

## Bonus 11 – Porovnání měsíců

Funkce `zmena_v_procentech(minule, ted)` vrátí, o kolik procent se výdaje
změnily proti minulému měsíci. Co má vrátit, když se minulý měsíc
neutratilo nic? Rozhodni se a napiš na to test.
