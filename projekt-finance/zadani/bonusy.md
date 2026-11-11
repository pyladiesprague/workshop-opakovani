# Bonusy

Máš hotové kroky a zbývá čas? Vyber si, co tě láká. Bonusy na sebe
nenavazují a pořadí je na tobě.

U každého platí totéž co u kroků: logiku piš jako funkci do `finance.py`,
napiš k ní aspoň jeden test a teprve potom ji přidej do menu.

## Bonus 1 – HTML report

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

## Bonus 4 – Cíl spoření

Funkce `mesicu_do_cile(usetreno, cil, mesicni_uspora)` vrátí, za kolik
měsíců naspoříš cílovou částku. Když je měsíční úspora nula nebo záporná,
vrátí `None`, protože cíle nikdy nedosáhneš.

V menu se zeptej na cíl. Jako to, co už máš, vezmi zůstatek. Měsíční úsporu
spočítej jako průměrný rozdíl příjmů a výdajů za měsíce, které jsou v datech.

## Bonus 5 – Opakující se platby

Nájem a lítačku platíš každý měsíc. Udělej si seznam pravidelných plateb
a volbu „založit nový měsíc“, která je pro zadaný měsíc přidá všechny
najednou. Hlídej, ať stejný měsíc nejde založit dvakrát.

## Bonus 6 – Export do CSV

Funkce `radek_csv(t)` vrátí transakci jako jeden řádek textu s údaji
oddělenými středníkem: `2026-11-02;vydaj;14000;bydleni;nájem`.
Všechny řádky zapiš do souboru `finance.csv` a otevři ho v Excelu.

Se soubory CSV budeme pracovat ve 13. lekci. Tohle je ochutnávka.

## Bonus 7 – Krok zpět

Volba „vrátit poslední změnu“ vrátí seznam transakcí do stavu před
posledním přidáním nebo odebráním. Před každou změnou si schovej kopii
seznamu. Tahák L8, *Dvě jména, jeden seznam*.

## Bonus 8 – Náhodná data

Funkce `nahodne_transakce(pocet)` vyrobí seznam náhodných transakcí:
náhodný den, kategorii a částku. Hodí se na zkoušení přehledů a grafů
s větším množstvím dat. `randrange` a `choice` znáš z `random`.

Jak otestuješ funkci, která pokaždé vrátí něco jiného? Zkontroluj to, co
platit musí vždycky: počet, povolené kategorie, kladné částky.

## Bonus 9 – Kategorie podle popisu

Slovník klíčových slov, třeba `{"lidl": "jidlo", "lítačka": "doprava"}`,
a funkce `odhadni_kategorii(popis, klicova_slova)`, která podle popisu
navrhne kategorii. Když žádné slovo nenajde, vrátí `"ostatni"`. Při
přidávání transakce pak kategorii nabídni a nech ji potvrdit Enterem.

## Bonus 10 – Porovnání měsíců

Funkce `zmena_v_procentech(minule, ted)` vrátí, o kolik procent se výdaje
změnily proti minulému měsíci. Co má vrátit, když se minulý měsíc
neutratilo nic? Rozhodni se a napiš na to test.
