# ---------------------------------------------
#  Kontrola printem
# ---------------------------------------------
# Kino dává slevy podle věku. Děti do 15 let platí 100 Kč, senioři
# od 65 let 120 Kč a ostatní 180 Kč.
#
# Spusť soubor a podívej se, jestli funkce počítá dobře.

def cena_vstupenky(vek):
    if vek < 15:
        return 100
    elif vek > 65:
        return 120
    else:
        return 180


print(cena_vstupenky(8))        # má být 100
print(cena_vstupenky(40))       # má být 180
print(cena_vstupenky(70))       # má být 120


# Všechna tři čísla sedí. Je tedy funkce v pořádku?
#
# Zkus ještě tohle:

print(cena_vstupenky(65))       # má být 120


# Vyšlo 180. Senioři mají slevu od 65 let, ale funkce se ptá na
# vek > 65, takže šedesátipětiletá zaplatí plnou cenu. Patří tam >=.
#
# Na tomhle příkladu jsou vidět dvě věci.
#
# První už znáš z debuggeru v lekci 7: program, který dá dobrý
# výsledek pro jeden vstup, tím ještě není ověřený. Chyby se rády
# schovávají na hranicích – tady přesně na 65.
#
# Druhá: kontrola printem stojí na tobě. Python vypíše číslo a ty
# musíš pokaždé porovnat, jestli je správně. U čtyř řádků to jde.
# Jenže když funkci za týden změníš, musíš znovu projít všechny
# výsledky a vzpomenout si, co mělo vyjít.
#
# Lepší by bylo napsat to, co má vyjít, rovnou do kódu – a nechat
# porovnávání na Pythonu. Přesně to umí assert v dalším souboru.
