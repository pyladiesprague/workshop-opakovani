# ---------------------------------------------
#  Co všechno umí assert
# ---------------------------------------------
# Za assert můžeš napsat jakoukoli podmínku, kterou znáš z if.
# V testech se nejčastěji objeví těch pár tvarů níž.
#
# Spusť soubor. Všechny asserty platí, takže se vypíše jen
# poslední řádek.

def pozdrav(jmeno):
    return f"Ahoj, {jmeno}!"


def je_sude(cislo):
    return cislo % 2 == 0


def kladna(cisla):
    vysledek = []
    for cislo in cisla:
        if cislo > 0:
            vysledek.append(cislo)
    return vysledek


# Rovná se – nejčastější tvar. Porovnat jde číslo, text i seznam.

assert pozdrav("Jana") == "Ahoj, Jana!"
assert kladna([3, -1, 0, 5]) == [3, 5]
assert kladna([]) == []


# Funkce vrací True nebo False. Stačí napsat volání, porovnání
# s True není potřeba. Pro False dej před volání not.

assert je_sude(4)
assert not je_sude(7)


# Kus textu v delším textu, nebo položka v seznamu.

assert "Jana" in pozdrav("Jana")
assert 5 in kladna([3, -1, 0, 5])


# Délka.

assert len(kladna([3, -1, 0, 5])) == 2

print("Všechno platí.")


# ----- Pozor na == -----
#
# Za assert patří dvě rovnítka, protože se porovnává. Jedno
# rovnítko je přiřazení do proměnné a Python ho za assertem
# nepustí – nahlásí SyntaxError ještě před spuštěním.
#
# Text se porovnává přesně, i s velkými písmeny, mezerami
# a interpunkcí. "Ahoj, Jana" bez vykřičníku neprojde.


# ----- Kdy assert nestačí -----
#
# Asserty v jednom souboru mají jednu nevýhodu. První, který
# neplatí, program zastaví, a o ostatních se nic nedozvíš. Kdyby
# v souboru byly tři chyby, uvidíš vždycky jen první.
#
# Proto se testy píšou do zvláštních funkcí a spouští je nástroj
# pytest. Ten pustí všechny a na konci řekne, které prošly a které
# ne. O tom je další složka.
