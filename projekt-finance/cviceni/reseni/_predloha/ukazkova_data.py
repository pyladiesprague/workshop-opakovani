# Ukázková data pro správce financí.
#
# Jedna transakce je slovník, všechny transakce jsou seznam slovníků.
# Částky jsou v celých korunách a vždycky kladné – jestli jde o příjem,
# nebo výdaj, říká klíč "typ". Datum je text ve tvaru RRRR-MM-DD.

transakce = [
    {"datum": "2026-10-01", "typ": "prijem", "castka": 32000, "kategorie": "vyplata", "popis": "výplata"},
    {"datum": "2026-10-02", "typ": "vydaj", "castka": 14000, "kategorie": "bydleni", "popis": "nájem"},
    {"datum": "2026-10-05", "typ": "vydaj", "castka": 1850, "kategorie": "jidlo", "popis": "velký nákup"},
    {"datum": "2026-10-12", "typ": "vydaj", "castka": 550, "kategorie": "doprava", "popis": "lítačka"},
    {"datum": "2026-10-17", "typ": "vydaj", "castka": 420, "kategorie": "zabava", "popis": "kino"},
    {"datum": "2026-10-24", "typ": "vydaj", "castka": 2300, "kategorie": "jidlo", "popis": "nákupy a obědy"},
    {"datum": "2026-11-01", "typ": "prijem", "castka": 32000, "kategorie": "vyplata", "popis": "výplata"},
    {"datum": "2026-11-02", "typ": "vydaj", "castka": 14000, "kategorie": "bydleni", "popis": "nájem"},
    {"datum": "2026-11-04", "typ": "vydaj", "castka": 1630, "kategorie": "jidlo", "popis": "velký nákup"},
    {"datum": "2026-11-07", "typ": "prijem", "castka": 1500, "kategorie": "ostatni", "popis": "prodej kola na bazaru"},
    {"datum": "2026-11-10", "typ": "vydaj", "castka": 550, "kategorie": "doprava", "popis": "lítačka"},
    {"datum": "2026-11-13", "typ": "vydaj", "castka": 890, "kategorie": "zabava", "popis": "koncert"},
    {"datum": "2026-11-15", "typ": "vydaj", "castka": 2480, "kategorie": "jidlo", "popis": "oslava narozenin"},
    {"datum": "2026-11-19", "typ": "vydaj", "castka": 1290, "kategorie": "ostatni", "popis": "dárek pro mámu"},
]

# Kategorie, které program zná. Jinou při zadávání nepřijme.
KATEGORIE = ["vyplata", "bydleni", "jidlo", "doprava", "zabava", "ostatni"]

# Měsíční rozpočty: kolik korun chceš za měsíc v kategorii nejvýš utratit.
# Budeš je potřebovat až v kroku 4.
rozpocty = {"jidlo": 4000, "doprava": 1000, "zabava": 1500}
