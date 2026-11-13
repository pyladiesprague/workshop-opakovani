# ---------------------------------------------
#  Proč vlastní moduly
# ---------------------------------------------
# Spusť soubor a pak otevři prevody.py, který leží vedle něj.
#
# Funkce sis začala psát, aby se kód neopakoval a dal se pojmenovat.
# Dlouhý program se tak rozpadl na menší kousky, z nichž každý dělá
# jednu věc.
#
# Moduly jsou o patro výš. Když je funkcí hodně, soubor se prodlužuje
# a hledá se v něm čím dál hůř. Funkce, které k sobě patří, proto
# přesuneš do vlastního souboru – modulu – a pojmenuješ ho:
#
#   funkce  = pojmenovaný kus kódu      (def na_celsia ...)
#   modul   = pojmenovaný soubor funkcí (prevody.py)
#
# Žádné nové kouzlo to není. Modul random, který používáš od začátku,
# je taky jen soubor random.py s funkcemi. Leží někde v instalaci
# Pythonu, zatímco ten tvůj leží ve stejné složce jako tvůj program.

import prevody

print("Venku je 30 °C, to je", prevody.na_fahrenheity(30), "°F.")
print("Maraton má 26,2 mil, to je", prevody.mile_na_km(26.2), "km.")


# Řádek import prevody udělá to samé co import random:
# najde soubor prevody.py a zpřístupní jeho funkce přes tečku.
#
# K čemu je to dobré:
#   - Program je kratší a čte se líp. Kdo chce vědět, jak se převádí,
#     podívá se do prevody.py. Kdo chce vědět, co program dělá, čte tenhle.
#   - Stejné funkce můžeš použít ve víc programech, nemusíš je kopírovat.
#   - Funkce v modulu jde otestovat. Test si ji naimportuje stejně jako
#     tenhle soubor. To uvidíš na konci téhle části.
