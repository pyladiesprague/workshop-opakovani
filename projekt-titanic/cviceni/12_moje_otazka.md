# Krok 12 – Co zajímá tebe?

Teď si otázku vybereš sama. Na konci tohohle kroku bude tvoje odpověď součástí
zprávy a na konci dne ji ukážeš ostatním:

```text
Moje otázka: ...
Podle ...                 Přežilo  (lidí)
  ...                      ??.? %  (???)
  ...                      ??.? %  (???)
```

Nejdřív si otázku vyber. Hraj si s průzkumníkem z minulého kroku a projdi si,
co sis během dne zapsala do poznámek. Pokud nevíš, čím začít, můžeš zkusit
některou z těchhle otázek:

- Přežívali lidé s rodinou častěji než ti, kdo cestovali sami? Kolik měl
  pasažér na palubě příbuzných, je `SibSp + Parch`. Rodina i s ním je
  o jednoho větší.
- Jak dopadly děti? Kde bys udělala hranici mezi dítětem a dospělým?
- Jak dopadli lidé podle věku po desetiletích?
- Muži ve 2. třídě přežívali skoro stejně málo jako ve 3. Platí to i pro ženy?
- Přežili častěji lidé, u kterých známe kajutu? Čím se od ostatních liší?
- Lidé bez věku přežívali méně často než ti s věkem. Proč u nich věk asi
  chybí?
- Kteří lidé jeli zadarmo a jak dopadli?

Otázku a odhad odpovědi si zapiš do `poznamky.md`.

## Funkce

Funkce píšeš do `analyza.py`.

| Funkce | Co vrátí |
| --- | --- |
| `moje_otazka(pasazeri)` | seznam řádků s tvojí otázkou a odpovědí na ni, stejně jako `tabulka` |

Zkus nejdřív, jestli ti stačí funkce, které už máš: `filtruj`, `rozdel_podle`,
`tabulka`, `graf`. Když ne, napiš novou.

## Testy

Napiš testy sama. Co vyzkoušet:

- co má `moje_otazka` vrátit pro `ukazka()`: nadpis a aspoň jeden řádek, který
  si spočítáš z hlavy,
- každou novou funkci, kterou sis kvůli otázce napsala.

## Program

Výsledek funkce `moje_otazka` přidej do `sestav_zpravu`, před závěr. Ve
`zprava.py` se nic měnit nemusí, zprávu už vypisuje.

### Je to příčina, nebo jen náhoda?

1. Podívej se, kolik lidí ve skupině je. Procento z pěti lidí toho moc neříká.
2. Zeptej se, čím dalším se skupiny liší. Vzpomeň si na přístavy a třídy.
3. Zapiš si do `poznamky.md` výsledek a to, jestli mu věříš.

### Prezentace

Na konci dne ukážeš svůj nejzajímavější výsledek. Stačí tři věty: na co ses
ptala, co vyšlo a jestli tomu věříš.

Zasekla ses? Nápověda je v souboru [`napovedy/12_moje_otazka.md`](../napovedy/12_moje_otazka.md).

## Hotovo, když

- [ ] tvoje testy jsou zelené
- [ ] odpověď na tvoji otázku je ve zprávě a je u ní vidět počet lidí
- [ ] v `poznamky.md` máš otázku, odhad, výsledek a jestli mu věříš
- [ ] práce je uložená na GitHubu: **Commit** a pak **Sync Changes**
