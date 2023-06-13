"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src import item


def test_calculate_total_price():
    assert item.calculate_total_price() == 2


