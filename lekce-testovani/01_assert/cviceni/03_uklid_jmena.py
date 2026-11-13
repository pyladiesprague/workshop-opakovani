# Cvičení 3 – assert
# Napiš asserty podle zadání. Když některý neprojde, oprav funkci.

# Funkce uklid_jmena dostane jméno tak, jak ho někdo napsal do
# formuláře, a vrátí ho uklizené: bez mezer na začátku a na konci,
# první písmeno velké a ostatní malá.
#
#   "  jana "    →  "Jana"
#   "PETRA"      →  "Petra"
#   "eva"        →  "Eva"

def uklid_jmena(jmeno):
    return jmeno.capitalize().strip()


# Sem napiš asserty:


print("Hotovo, všechny asserty platí.")
