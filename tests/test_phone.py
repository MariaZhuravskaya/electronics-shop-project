from src.item import Item
from src.phone import Phone


def test_init():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2



def test_calculate_total_price():
    assert Phone.calculate_total_price(Phone("iPhone 14", 120000, 5, 2)) == 600000
    assert Phone.calculate_total_price(Phone("Ноутбук", 20000, 5, 1)) == 100000


def test_apply_discount():
    phone1 = Phone("Смартфон", 10000, 20, 1)
    phone2 = Phone("Ноутбук", 20000, 5, 2)
    phone3 = Phone("Планшет", 50000, 15, 2)
    Phone.pay_rate = 0.5
    phone1.apply_discount()
    phone2.apply_discount()
    phone3.apply_discount()
    assert phone1.price == 5000
    assert phone2.price == 10000
    assert phone3.price == 25000

def test_name():
    phone1 = Phone("СуперСмартфон", 10000, 20, 1)
    phone2 = Phone("Ноутбук", 20000, 5, 2)
    phone3 = Phone("Планшет", 50000, 15, 2)
    phone1.name = 'СуперСмартфон'
    phone2.name = 'Ноутбук'
    assert phone1.name == 'СуперСмарт'
    assert phone2.name == 'Ноутбук'
    assert phone3.name == 'Планшет'


def test_string_to_number():
    assert Phone.string_to_number('5') == 5
    assert Phone.string_to_number('5.0') == 5
    assert Phone.string_to_number('5.5') == 5


def test_repr():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    phone2 = Phone("Ноутбук", 20000, 5, 3)
    assert repr(phone1) == "Phone('Смартфон', 10000, 20, 2)"
    assert repr(phone2) == "Phone('Ноутбук', 20000, 5, 3)"

def test_str():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    phone2 = Phone("Ноутбук", 20000, 5, 1)
    assert str(phone1) == 'Смартфон'
    assert str(phone2) == 'Ноутбук'
    assert phone1.number_of_sim == 2
    assert phone2.number_of_sim == 1


def test_add():
    item1 = Item("Смартфон", 10000, 10)
    phone1 = Phone("Смартфон", 10000, 20, 2)
    assert item1 + phone1 == 30
    assert phone1 + phone1 == 40
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == 2