# Bonus 3 – Řazení podle částky

Funkce `serazene_podle_castky(transakce)` vrátí nový seznam transakcí
seřazený od nejvyšší částky. Původní seznam nechá být.

Seznam slovníků metodou `sort` přímo neseřadíš. Seznam n-tic ano: n-tice se
porovnávají podle první položky, a když se shodují, podle druhé. Postav
tedy seznam dvojic `(castka, index)`, seřaď ho a podle indexů poskládej
výsledek.

Vyzkoušej, co se stane, když místo indexu dáš do dvojice rovnou slovník
a dvě transakce mají stejnou částku.
