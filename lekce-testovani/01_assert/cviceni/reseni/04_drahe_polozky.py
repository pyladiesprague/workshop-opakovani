# Řešení cvičení 4 – assert
# Funkce je správně, všechny asserty projdou.

def drahe(ceny, hranice):
    vysledek = []
    for cena in ceny:
        if cena > hranice:
            vysledek.append(cena)
    return vysledek


assert drahe([50, 300, 120, 80], 100) == [300, 120]
assert drahe([10, 20, 30], 100) == []
assert drahe([], 100) == []
assert drahe([100, 101], 100) == [101]

print("Hotovo, všechny asserty platí.")


# Prázdný seznam a seznam bez drahých cen vypadají jako zbytečné
# případy. Funkce, které si s nimi neporadí, jsou přitom časté:
# třeba když počítají průměr a dělí délkou seznamu, prázdný seznam
# skončí dělením nulou.
#
# Poslední assert hlídá hranici. Zadání říká „vyšší než“, takže
# stovka do výsledku nepatří a 101 ano.
