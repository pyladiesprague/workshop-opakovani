# Řešení cvičení 1 – assert

def obvod(a, b):
    return 2 * a + 2 * b


assert obvod(3, 5) == 16
assert obvod(4, 4) == 16        # čtverec
assert obvod(10, 1) == 22

print("Hotovo, všechny asserty platí.")


# Čísla můžou být jakákoli, hlavní je spočítat si výsledek sama.
# Kdybys napsala assert obvod(3, 5) == obvod(3, 5), platil by vždycky,
# i kdyby funkce počítala nesmysl. Test, který nemůže selhat, nic
# neověří.
