# Cvičení 4 – assert
# Napiš asserty podle zadání. Mysli i na prázdný seznam.

# Funkce drahe dostane seznam cen a hranici. Vrátí nový seznam jen
# s cenami, které jsou vyšší než hranice. Pořadí zůstane stejné.
#
#   drahe([50, 300, 120, 80], 100)   →  [300, 120]

def drahe(ceny, hranice):
    vysledek = []
    for cena in ceny:
        if cena > hranice:
            vysledek.append(cena)
    return vysledek


# Sem napiš asserty. Ověř aspoň:
#   - příklad ze zadání,
#   - seznam, ve kterém není žádná drahá cena,
#   - prázdný seznam,
#   - cenu, která se hranici přesně rovná.


print("Hotovo, všechny asserty platí.")
