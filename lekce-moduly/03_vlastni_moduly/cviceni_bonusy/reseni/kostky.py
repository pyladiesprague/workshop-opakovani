# Modul k bonusu 1 – Modul, který importuje modul.

from random import randrange


def hod():
    return randrange(1, 7)


def hod_vice(pocet):
    hody = []
    for poradi in range(pocet):
        hody.append(hod())
    return hody
