# Nápady na rozšíření

Tady jsou nápady, co dalšího můžeš programu přidat, když máš hotové kroky
i bonusy, nebo až budeš chtít pokračovat doma. Řešení k nim nejsou. Platí
totéž co u kroků: logiku piš jako funkci do `finance.py`, napiš k ní aspoň
jeden test a teprve potom ji přidej do menu.

## Ke kroku 1 – Základ: výpis a zůstatek

- Vypiš pod výpisem i součet příjmů a součet výdajů.
- Částky ve výpisu oddělují tisíce mezerou: `32 000`. Zvládneš to
  s tím, co umíš z řetězců?

## Ke kroku 2 – Přidání a odebrání transakce

- `je_platne_datum` pustí i 31. únor. Dokážeš ji zpřísnit? Nejdřív na to napiš test.
- Při zadávání data nabídni zkratku: prázdný Enter použije datum poslední transakce.
- Před odebráním se zeptej „Opravdu odebrat? (ano/ne)“.

## Ke kroku 3 – Přehledy

- Vypiš kategorie v přehledu od nejdražší po nejlevnější.
- Přidej funkci `prijmy_podle_kategorie`. Všimni si, kolik kódu se opakuje.
  Šla by z obou udělat jedna funkce s parametrem navíc?
- Přidej volbu, která vypíše přehled za všechny měsíce, které v datech jsou.

## Ke kroku 4 – Rozpočty

- Upozorni už ve chvíli, kdy je vyčerpáno 80 % rozpočtu.
- Vypiš u každého rozpočtu, kolik procent je vyčerpáno.
- Přidej volbu, která rozpočet kategorie zruší.

## Ke kroku 5 – Grafy v terminálu

- Zeptej se na měsíc a nakresli graf jen za něj.
- Nakresli graf výdajů po měsících: jeden sloupec na každý měsíc v datech.
- Seřaď sloupce od nejdelšího.
- Do přehledu rozpočtů z kroku 4 přidej ukazatel čerpání:
  `[██████░░░░] 60 %`.

## Ke kroku 6 – Uložení do souboru

- Ukládej i rozpočty. Do souboru může jít slovník se dvěma klíči:
  `{"transakce": [...], "rozpocty": {...}}`. Tahák L9, *data v datech*.
- Přidej volbu „uložit zálohu“, která data zapíše do souboru, jehož jméno
  si uživatelka zvolí.

## Větší nápady

### Cíl spoření

Funkce `mesicu_do_cile(usetreno, cil, mesicni_uspora)` vrátí, za kolik
měsíců naspoříš cílovou částku. Když je měsíční úspora nula nebo záporná,
vrátí `None`, protože cíle nikdy nedosáhneš.

V menu se zeptej na cíl. Jako to, co už máš, vezmi zůstatek. Měsíční úsporu
spočítej jako průměrný rozdíl příjmů a výdajů za měsíce, které jsou v datech.

### Opakující se platby

Nájem a lítačku platíš každý měsíc. Udělej si seznam pravidelných plateb
a volbu „založit nový měsíc“, která je pro zadaný měsíc přidá všechny
najednou. Hlídej, ať stejný měsíc nejde založit dvakrát.

### Export do CSV

Funkce `radek_csv(t)` vrátí transakci jako jeden řádek textu s údaji
oddělenými středníkem: `2026-11-02;vydaj;14000;bydleni;nájem`.
Všechny řádky zapiš do souboru `finance.csv` a otevři ho v Excelu.

Se soubory CSV budeme pracovat ve 13. lekci. Tohle je ochutnávka.

### Krok zpět

Volba „vrátit poslední změnu“ vrátí seznam transakcí do stavu před
posledním přidáním nebo odebráním. Před každou změnou si schovej kopii
seznamu. Tahák L8, *Dvě jména, jeden seznam*.

### Náhodná data

Funkce `nahodne_transakce(pocet)` vyrobí seznam náhodných transakcí:
náhodný den, kategorii a částku. Hodí se na zkoušení přehledů a grafů
s větším množstvím dat. `randrange` a `choice` znáš z `random`.

Jak otestuješ funkci, která pokaždé vrátí něco jiného? Zkontroluj to, co
platit musí vždycky: počet, povolené kategorie, kladné částky.

### Kategorie podle popisu

Slovník klíčových slov, třeba `{"lidl": "jidlo", "lítačka": "doprava"}`,
a funkce `odhadni_kategorii(popis, klicova_slova)`, která podle popisu
navrhne kategorii. Když žádné slovo nenajde, vrátí `"ostatni"`. Při
přidávání transakce pak kategorii nabídni a nech ji potvrdit Enterem.

### Porovnání měsíců

Funkce `zmena_v_procentech(minule, ted)` vrátí, o kolik procent se výdaje
změnily proti minulému měsíci. Co má vrátit, když se minulý měsíc
neutratilo nic? Rozhodni se a napiš na to test.
