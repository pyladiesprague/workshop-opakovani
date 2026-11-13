# Řešení cvičení 4 – Odpočet
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se, od kolika se má odpočítávat. Pak vypisuj čísla
#    dolů až k jedničce, mezi každými dvěma počkej sekundu,
#    a nakonec vypiš „Šťastný nový rok!“.
#    Na čekání použij sleep z modulu time.

from time import sleep

od = int(input("Od kolika odpočítávat? "))

for cislo in range(od, 0, -1):
    print(cislo)
    sleep(1)
print("Šťastný nový rok!")
