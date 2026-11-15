# Nápověda ke kroku 11 – Co dalšího se dá z dat zjistit?

## Funkce

`najdi_sloupec`: to, co uživatelka napsala, nejdřív uprav: mezery pryč a malá
písmena. Tahák L6, *Metody řetězců*.

Názvy sloupců mají velká písmena (`Sex`, `Pclass`), takže je při porovnání
převeď na malá taky. Vrátit ale musíš původní název, ne ten zmenšený.

Když cyklus doběhne a nic nenašel, vrať `None`.

`prehled_podle`: rozděl pasažéry funkcí `rozdel_podle`, projdi skupiny a pro
každou přidej jeden `radek_tabulky`.

## Program

Je to cyklus `while True` s `break`. Tahák L4, *Nekonečný cyklus*.

Na `None` se ptej přes `is None`.

Seznam řetězců spojíš do jednoho textu metodou `join`. Tahák L8, *Text a
seznam*.
