# ---------------------------------------------
#  Knihovny z internetu: pip
# ---------------------------------------------
# Spusť soubor. Nejspíš spadne – a to je teď dobře.
#
# Standardní knihovna je jen začátek. Další tisíce modulů napsali lidé
# z celého světa a dali je zdarma k dispozici na webu PyPI:
#   https://pypi.org
#
# Takovým modulům se říká knihovny nebo balíčky. Python je s sebou
# nemá, musíš si je nejdřív nainstalovat. K tomu slouží program pip.
#
# Na ukázku si vezmeme knihovnu cowsay. Kráva v ní umí mluvit.

import cowsay

cowsay.cow("Bú! Knihovna funguje.")


# Pokud soubor spadl s hláškou
#
#   ModuleNotFoundError: No module named 'cowsay'
#
# Python modul cowsay nenašel. Ve standardní knihovně není, takže ho
# nainstaluj:
#
#   1. Ve VS Code otevři terminál: v horním menu Terminal → New Terminal.
#      Dole se otevře okno, kam se píšou příkazy.
#   2. Napiš do něj příkaz a potvrď Enterem:
#
#          pip install cowsay
#
#      Na Windows případně:   py -m pip install cowsay
#      Na macOS případně:     python3 -m pip install cowsay
#
#   3. Na konci výpisu by mělo být:  Successfully installed cowsay-…
#   4. Spusť tenhle soubor znovu. Kráva by měla promluvit.
#
# Pokud to nejde ani tak, zavolej kouče. Na každém počítači to může
# zlobit trochu jinak.


# Instaluje se jednou na počítač, ne do každého souboru. Import pak píšeš
# do každého souboru, kde knihovnu používáš – stejně jako u random.
