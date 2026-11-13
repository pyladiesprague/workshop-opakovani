# Řešení bonusu 1 – Kolik dní do Vánoc
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vypiš, kolik dní zbývá do Štědrého dne.
#     Pomůže ti date z modulu datetime:
#       date(2026, 12, 24)     vytvoří datum 24. 12. 2026
#       date.today()           je dnešní datum
#     Dvě data jde od sebe odečíst. Výsledek má hodnotu .days,
#     ve které je počet dní.

from datetime import date

vanoce = date(2026, 12, 24)
zbyva = vanoce - date.today()

print(f"Do Štědrého dne zbývá {zbyva.days} dní.")
