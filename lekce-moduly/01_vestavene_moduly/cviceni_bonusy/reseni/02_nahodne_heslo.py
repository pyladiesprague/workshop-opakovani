# Řešení bonusu 2 – Náhodné heslo
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vyrob náhodné heslo o 12 znacích z písmen a číslic
#     v řetězci znaky. V cyklu přidávej po jednom znaku,
#     který vybereš funkcí choice – ta umí vybírat i z řetězce.

from random import choice

znaky = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"

heslo = ""
for poradi in range(12):
    heslo = heslo + choice(znaky)

print("Tvoje nové heslo:", heslo)
