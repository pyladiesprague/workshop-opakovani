# ---------------------------------------------
#  Testy v projektu
# ---------------------------------------------
# Tenhle soubor se nespouští, je to jen čtení. Ukazuje, jak jsou
# testy uspořádané v projektech na workshopu.
#
# Zatím byla funkce i testy v jednom souboru. V opravdovém projektu
# se to rozdělí na tři soubory. Na workshopu je takhle uspořádaný
# každý projekt, třeba projekt-finance:
#
#   finance.py          logika: funkce, které počítají a vrací výsledky
#   app.py              program: menu, input a print, volá funkce z finance.py
#   test_finance.py     testy funkcí z finance.py


# ----- Test si funkci půjčí -----
#
# Testy jsou v jiném souboru než funkce, takže si je musí naimportovat.
# Funguje to stejně jako u random, jen místo random je jméno tvého
# souboru bez .py:
#
#   import finance
#
#
#   def test_zustatek_bez_transakci():
#       assert finance.zustatek([]) == 0
#
# Soubor s testy musí být ve stejné složce jako soubor s funkcemi.


# ----- Proč logika zvlášť -----
#
# Testovat jde funkci, která něco vrací. Funkce, která se ptá přes
# input, by při testu čekala, až někdo něco napíše. Funkce, která
# jen vypíše print, nevrací nic, s čím by assert mohl porovnat.
#
# Proto je logika ve finance.py bez inputu a printu. Všechno, co se
# ptá a vypisuje, je v app.py.
#
# Pozor: při importu se celý soubor provede. Kdyby ve finance.py byl
# input mimo funkci, testy by se zasekly a čekaly na odpověď.


# ----- Jména souborů -----
#
# Soubor s testy se jmenuje test_ a za tím jméno souboru, který
# testuje: test_finance.py testuje finance.py.
#
# Díky začátku test_ ho pytest najde sám. Nemusíš mu říkat, který
# soubor má spustit – v terminálu stačí:
#
#   python -m pytest
#
# Pytest projde složky, najde všechny soubory test_*.py a v nich
# všechny funkce test_*.


# ----- Panel Testing -----
#
# Ve VS Code nemusíš psát do terminálu vůbec. Vlevo je ikona baňky,
# panel Testing. Ukáže strom: složky, soubory s testy a v nich
# jednotlivé testy.
#
#   - Dvojitá šipka nahoře spustí všechny testy.
#   - Šipka u složky nebo souboru spustí jen ty testy pod ní.
#   - Zelená fajfka prošel, červený křížek neprošel.
#   - Kliknutím na neprošlý test se otevře výpis, stejný jako
#     v terminálu.
#
# Když panel testy nevidí, zmáčkni nahoře v panelu tlačítko
# Refresh Tests (kolečková šipka).
#
# V repozitáři workshopu je VS Code nastavený tak, že panel testy
# najde, když otevřeš celou složku workshopu (File → Open Folder).
#
# Soubory v téhle lekci schválně nezačínají test_. Panel je proto
# nevidí a jejich červené testy se nepletou mezi testy projektů.


# ----- Jak se s testy pracuje -----
#
# V projektu se střídá pořád to samé:
#
#   1. V zadání kroku je popsaná funkce a testy k ní.
#   2. Testy zkopíruješ do test_….py. Jsou červené, funkce ještě
#      neexistuje.
#   3. Píšeš funkci, dokud testy nezezelenají.
#   4. Spustíš všechny testy, ne jen ty nové. Když zčervená starý
#      test, nová změna rozbila něco, co už fungovalo.
#
# V pozdějších krocích hotové testy nedostaneš. V zadání bude jen,
# co má funkce umět, a testy napíšeš sama – podle tří otázek
# z minulého souboru.
