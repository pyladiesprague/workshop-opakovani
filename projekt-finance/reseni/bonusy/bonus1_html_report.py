# Řešení bonusu 1 – HTML report
# Tvoje řešení může vypadat jinak, a to je v pořádku.
#
# Soubor jde spustit samostatně. Ve svém projektu dej funkci html_report
# do finance.py a zápis do souboru s otevřením prohlížeče do app.py.

import webbrowser

from ukazkova_data import transakce

# Styly obsahují složené závorky, proto nejsou v f-stringu.
STYLY = """
<style>
  body { font-family: sans-serif; margin: 2em; color: #222; }
  table { border-collapse: collapse; }
  th, td { padding: 4px 12px; border-bottom: 1px solid #ddd; text-align: left; }
  td.castka { text-align: right; }
  .prijem { color: green; }
  .vydaj { color: crimson; }
  .sloupec { background: teal; height: 18px; }
</style>
"""


def zustatek(transakce):
    celkem = 0
    for t in transakce:
        if t["typ"] == "prijem":
            celkem = celkem + t["castka"]
        else:
            celkem = celkem - t["castka"]
    return celkem


def vydaje_podle_kategorie(transakce):
    soucty = {}
    for t in transakce:
        if t["typ"] == "vydaj":
            soucty[t["kategorie"]] = soucty.get(t["kategorie"], 0) + t["castka"]
    return soucty


def bezpecny_text(text):
    # Znaky < a & mají v HTML zvláštní význam. Popis "sleva <50 %" by
    # bez téhle úpravy stránku rozbil.
    return text.replace("&", "&amp;").replace("<", "&lt;")


def html_radek(t):
    if t["typ"] == "prijem":
        castka = f"+{t['castka']} Kč"
    else:
        castka = f"-{t['castka']} Kč"
    return (
        f"<tr><td>{t['datum']}</td><td>{bezpecny_text(t['popis'])}</td>"
        f"<td>{t['kategorie']}</td><td class=\"castka {t['typ']}\">{castka}</td></tr>"
    )


def html_graf(transakce):
    soucty = vydaje_podle_kategorie(transakce)
    if len(soucty) == 0:
        return "<p>Zatím žádné výdaje.</p>"

    nejvyssi = max(soucty.values())
    casti = []
    for kategorie, castka in soucty.items():
        sirka = castka * 400 // nejvyssi
        casti.append(f"<p>{kategorie}: {castka} Kč</p>")
        casti.append(f"<div class=\"sloupec\" style=\"width: {sirka}px\"></div>")
    return "\n".join(casti)


def html_report(transakce):
    radky = []
    for t in transakce:
        radky.append(html_radek(t))
    tabulka = "\n".join(radky)

    hlavicka = "<!DOCTYPE html>\n<html lang=\"cs\">\n<head>\n<meta charset=\"utf-8\">\n"
    hlavicka = hlavicka + "<title>Moje finance</title>" + STYLY + "</head>\n"

    telo = f"""<body>
<h1>Moje finance</h1>
<p>Zůstatek: <strong>{zustatek(transakce)} Kč</strong></p>

<h2>Výdaje podle kategorií</h2>
{html_graf(transakce)}

<h2>Transakce</h2>
<table>
<tr><th>Datum</th><th>Popis</th><th>Kategorie</th><th>Částka</th></tr>
{tabulka}
</table>
</body>
</html>
"""
    return hlavicka + telo


with open("report.html", "w", encoding="utf-8") as soubor:
    soubor.write(html_report(transakce))

print("Report je v souboru report.html, otevírám ho v prohlížeči.")
webbrowser.open("report.html")
