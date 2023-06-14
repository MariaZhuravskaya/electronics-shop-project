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

