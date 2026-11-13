def test_obarvi_obali_text_kody():
    assert finance.obarvi("ahoj", "zelena") == "\033[32mahoj\033[0m"


def test_obarvi_zachova_puvodni_text():
    assert "ahoj" in finance.obarvi("ahoj", "cervena")


def test_obarveny_text_je_delsi_o_kody():
    # Kód barvy má pět znaků, kód pro konec čtyři.
    assert len(finance.obarvi("ahoj", "zelena")) == len("ahoj") + 9
