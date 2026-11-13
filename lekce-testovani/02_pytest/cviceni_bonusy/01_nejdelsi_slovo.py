# Bonus 1 – pytest
# Napiš testy podle zadání. Ve funkci je chyba, která se ukáže jen
# na jednom z okrajů. Najdi ho a funkci oprav.

# Spouštěj v terminálu ve složce cviceni_bonusy:
#
#   python -m pytest 01_nejdelsi_slovo.py
#
# Funkce nejdelsi_slovo vrátí nejdelší slovo z věty. Když je
# nejdelších slov víc stejně dlouhých, vrátí to, které je ve větě
# první. Pro prázdný text vrátí prázdný text "".

def nejdelsi_slovo(veta):
    nejdelsi = ""
    for slovo in veta.split():
        if len(slovo) >= len(nejdelsi):
            nejdelsi = slovo
    return nejdelsi


# Sem napiš testy:
