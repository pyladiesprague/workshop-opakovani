# ---------------------------------------------
#  Jak zjistit, co knihovna umí
# ---------------------------------------------
# Spusť soubor. Potřebuje nainstalovaný cowsay z minulého souboru.
#
# Každá knihovna má na PyPI stránku s popisem a ukázkami:
#   https://pypi.org/project/cowsay/
#
# Tam se dočteš, že kromě krávy umí mluvit i další postavičky.
# Jejich jména jsou v seznamu cowsay.char_names:

import cowsay

print(cowsay.char_names)


# Každá postavička má svoji funkci, která se jmenuje stejně:
cowsay.tux("Ahoj, já jsem tučňák Tux.")
cowsay.trex("A já dinosaurus.")


# Knihovna je tedy pořád jen modul s funkcemi. Od random se liší
# jen tím, že ji napsal někdo jiný než autoři Pythonu a musíš si ji
# nainstalovat.
#
# Postup s jakoukoli novou knihovnou:
#   1. najdi ji (vyhledávač, PyPI, doporučení kouče),
#   2. nainstaluj: pip install jmeno_knihovny,
#   3. přečti si ukázky na její stránce,
#   4. importuj a použij.
