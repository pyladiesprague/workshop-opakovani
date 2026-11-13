# ---------------------------------------------
#  Co testovat
# ---------------------------------------------
# Všechny vstupy vyzkoušet nejde. Stačí vybrat pár chytrých.
# Pomůžou tři otázky. Ukážeme si je na funkci, která z bodů
# udělá známku.
#
# Spusť testy v terminálu ve složce 02_pytest:
#
#   python -m pytest 03_co_testovat.py -v

def znamka(body):
    if body < 0 or body > 100:
        return None
    if body >= 90:
        return 1
    elif body >= 75:
        return 2
    elif body >= 60:
        return 3
    elif body >= 45:
        return 4
    else:
        return 5


# ----- 1. Obyčejný případ -----
#
# Vstup, u kterého víš z hlavy, co má vyjít. Tím začni vždycky.

def test_95_bodu_je_jednicka():
    assert znamka(95) == 1


def test_50_bodu_je_ctyrka():
    assert znamka(50) == 4


# ----- 2. Okraje -----
#
# Hranice mezi známkami, nula, maximum. Tady se chyby schovávají
# nejčastěji – stačí > místo >=. Na hranici testuj přesně tu
# hodnotu, kde se výsledek mění.

def test_90_bodu_je_jeste_jednicka():
    assert znamka(90) == 1


def test_89_bodu_je_uz_dvojka():
    assert znamka(89) == 2


def test_0_bodu_je_petka():
    assert znamka(0) == 5


def test_100_bodu_je_jednicka():
    assert znamka(100) == 1


# U seznamů a textů je okrajem prázdný seznam, prázdný text nebo
# jediná položka.


# ----- 3. Špatný vstup -----
#
# Co když přijde něco, co tam nepatří? Funkce se tu dohodla, že
# vrátí None. Test hlídá, že to opravdu dělá.

def test_zaporne_body_nejsou_znamka():
    assert znamka(-5) is None


def test_vic_nez_100_bodu_neni_znamka():
    assert znamka(101) is None


# Na None se ptá is None, ne == None. Funguje obojí, ale is None je
# zvyk, který uvidíš v cizím kódu i v projektech.


# ----- Jeden test, jedna věc -----
#
# Všechny asserty by se daly nacpat do jednoho testu. Když by ale
# neprošel, nevíš hned, co se rozbilo, a asserty pod tím chybným se
# vůbec neprovedou.
#
# Malé testy s popisným jménem řeknou víc: výpis s -v je pak seznam
# toho, co funkce umí, a červený řádek ukáže přesně na to, co
# nefunguje.


# ----- Kdy testů stačí -----
#
# Žádné pravidlo neexistuje. Dobré znamení je, když si zkusíš
# ve funkci udělat chybu – třeba >= 90 přepsat na > 90 – a aspoň
# jeden test zčervená. Zkus to.
