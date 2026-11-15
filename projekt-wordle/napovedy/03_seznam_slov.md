# Nápověda ke kroku 3 – Seznam slov

- Jestli je slovo v seznamu, zjistíš operátorem `in`, případně `not in`.
- Oba soubory načti jen jednou, na začátku programu.
- Náhodné slovo je slovo na náhodném indexu, tedy na indexu od 0 do
  `len(slova) - 1`. Tahák L4, *Náhodné číslo*.

Hraní znovu je další cyklus `while True`, tentokrát kolem volání `zahraj`.
Ukončíš ho příkazem `break`. Tahák L4, *break*.

Odpověď hráče na otázku „Hrát znovu?“ uprav stejnou funkcí jako hádané slovo.
Projde pak i `ANO` nebo ` ano `.
