# Modul ke cvičení 2 – Vlastní modul od nuly.


def ramecek(text):
    okraj = "*" * (len(text) + 4)
    return okraj + "\n* " + text + " *\n" + okraj


def kricet(text):
    return text.upper() + "!"
