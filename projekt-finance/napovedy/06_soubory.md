# Nápověda ke kroku 6 – Uložení do souboru

- Zápis a čtení souboru, `json.dump` a `json.load`. `TAHAK.md`, *Soubory a
  JSON*.
- Nezapomeň na `encoding="utf-8"` při otevírání a `ensure_ascii=False` při
  zápisu. Bez `encoding` se na Windows háčky a čárky pokazí, to hlídají
  `test_nacti_hacky_a_carky` a `test_ulozeny_soubor_je_citelny`. Bez
  `ensure_ascii=False` se uloží jako nečitelné `žluťoučký`,
  to hlídá `test_ulozeny_soubor_je_citelny`.
- `FileNotFoundError`, nebo se data ukládají jinam? Cestu skládej od složky
  programu: `Path(__file__).parent / "finance.json"`. `TAHAK.md`, *Soubory
  a JSON*.
