# Řešení cvičení 2 – assert
# Opravená funkce. Pod ní je, jak se na chybu přišlo.

def je_plnoleta(vek):
    return vek >= 18


assert not je_plnoleta(10)
assert not je_plnoleta(17)
assert je_plnoleta(18)
assert je_plnoleta(30)

print("Hotovo, všechny asserty platí.")


# S původní funkcí spadne třetí assert:
#
#   assert je_plnoleta(18)
#   AssertionError
#
# Osmnáctiletá je podle zadání plnoletá, ale 18 > 18 neplatí.
# Patří tam >=.
#
# Věky 10 a 30 by chybu nenašly. Našla ji až osmnáctka, protože
# leží přesně na hranici. Hranice testuj vždycky.
