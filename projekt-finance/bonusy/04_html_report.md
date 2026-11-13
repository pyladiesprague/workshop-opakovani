# Bonus 4 – HTML report

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
