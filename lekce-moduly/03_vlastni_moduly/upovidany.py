# Ukázkový modul, který se chová špatně.
# Importuje ho 03_import_spusti_cely_soubor.py.


def pozdrav(jmeno):
    return f"Ahoj, {jmeno}!"


# Tenhle řádek není ve funkci. Spustí se při každém importu.
print("Tohle vypsal modul upovidany, i když o to nikdo nežádal.")
