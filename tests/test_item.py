"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_calculate_total_price():
    assert Item.calculate_total_price(Item("Смартфон", 10000, 20)) == 200000
    assert Item.calculate_total_price(Item("Ноутбук", 20000, 5)) == 100000



def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item3 = Item("Планшет", 50000, 15)
    Item.pay_rate = 0.7
    item1.apply_discount()
    item2.apply_discount()
    item3.apply_discount()
    assert item1.price == 7000
    assert item2.price == 14000
    assert item3.price == 35000

def test_name():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item3 = Item("Супер", 50000, 15)
    item3.name = 'СуперСмартфон'
    item2.name = 'Ноутбук'
    assert item1.name == 'Смартфон'
    assert item2.name == 'Ноутбук'
    assert item3.name == 'СуперСмарт'



def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    item2 = Item.all[1]
    item3 = Item.all[2]
    assert item1.name == 'Смартфон'
    assert item2.name == 'Ноутбук'
    assert item3.name == 'Кабель'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5