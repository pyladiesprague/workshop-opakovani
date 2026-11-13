# Řešení cvičení 3 – assert
# Opravená funkce. Pod ní je, jak se na chybu přišlo.

def uklid_jmena(jmeno):
    return jmeno.strip().capitalize()


assert uklid_jmena("  jana ") == "Jana"
assert uklid_jmena("PETRA") == "Petra"
assert uklid_jmena("eva") == "Eva"

print("Hotovo, všechny asserty platí.")


# S původní funkcí spadne hned první assert. Když chceš vidět, co
# funkce doopravdy vrátila, vypiš si to:
#
#   print(uklid_jmena("  jana "))     # jana
#
# Mezery zmizely, ale první písmeno zůstalo malé. capitalize dá
# velké písmeno prvnímu znaku – a prvním znakem byla mezera. Mezery
# se musí uklidit dřív, než se zvětšuje: nejdřív strip, pak
# capitalize.
#
# Další dva asserty by prošly i s chybou. Chybu našel jen ten vstup,
# který měl mezery na začátku. Zkoušej vstupy, které se od sebe liší.
