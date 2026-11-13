# Cvičení 1 – Rozděl program
# Uprav kód podle zadání a soubor spusť (Run).

# Program níž počítá spropitné. Funguje, ale logika a program jsou
#    v jednom souboru. Rozděl je:
#
#    1. Ve složce cviceni vytvoř nový soubor spropitne.py
#       (pravým tlačítkem na složku → New File).
#    2. Přesuň do něj obě funkce.
#    3. Tady nahoře je naimportuj a zkontroluj, že program dělá
#       totéž co předtím.


def spropitne(castka, procenta):
    return round(castka * procenta / 100)


def celkem(castka, procenta):
    return castka + spropitne(castka, procenta)


castka = int(input("Kolik stál oběd? "))
procenta = int(input("Kolik procent spropitného? "))

print(f"Spropitné: {spropitne(castka, procenta)} Kč")
print(f"Celkem zaplatíš: {celkem(castka, procenta)} Kč")
