# Bonus 2 – pytest
# Funkce vrací správný výsledek, a přesto má chybu. Napiš test,
# který ji odhalí, a pak funkci oprav.

# Spouštěj v terminálu ve složce cviceni_bonusy:
#
#   python -m pytest 02_puvodni_seznam.py
#
# Funkce tri_nejlevnejsi dostane seznam cen a vrátí nový seznam se
# třemi nejnižšími cenami od nejmenší. Původní seznam nechá tak, jak
# byl.

def tri_nejlevnejsi(ceny):
    ceny.sort()
    return ceny[:3]


def test_tri_nejlevnejsi():
    assert tri_nejlevnejsi([500, 120, 80, 300, 90]) == [80, 90, 120]


# Tenhle test projde. Napiš další, který ověří poslední větu zadání.
# Nápověda: seznam si ulož do proměnné, zavolej funkci a pak
# se podívej, co je v proměnné.
