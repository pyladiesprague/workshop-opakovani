# Řešení cvičení 1 – Rozděl program
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Program níž počítá spropitné. Funguje, ale logika a program jsou
#    v jednom souboru. Rozděl je:
#
#    1. Ve složce cviceni vytvoř nový soubor spropitne.py
#       (pravým tlačítkem na složku → New File).
#    2. Přesuň do něj obě funkce.
#    3. Tady nahoře je naimportuj a zkontroluj, že program dělá
#       totéž co předtím.

# Funkce jsou teď v souboru spropitne.py vedle tohohle.

from spropitne import celkem, spropitne

castka = int(input("Kolik stál oběd? "))
procenta = int(input("Kolik procent spropitného? "))

print(f"Spropitné: {spropitne(castka, procenta)} Kč")
print(f"Celkem zaplatíš: {celkem(castka, procenta)} Kč")
