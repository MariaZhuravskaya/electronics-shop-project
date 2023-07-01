from src.keyboard import Keyboard


def test_init():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb1 = Keyboard('Toshiba T122', 22000, 1)

    assert str(kb) == "Dark Project KD87A"
    assert str(kb1) == "Toshiba T122"

    assert str(kb.language) == "EN"
    assert str(kb1.language) == "EN"

    assert kb.price == 9600
    assert kb.quantity == 5


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb1 = Keyboard('Toshiba T122', 22000, 1)
    kb.change_lang()
    assert str(kb.language) == "RU"
    assert str(kb1.language) == "EN"

    #Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    #kb.language = 'CH'

