import csv

import pathlib
from pathlib import Path


class InstantiateCSVError(Exception):

    def __init__(self, *args):
        self.messege = args[0] if args else 'Файл items.csv поврежден'

    def __str__(self):
        return self.messege


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_len):
        """
        Проверяет, что длина наименования товара не больше 10 симвовов. В противном случае, обрезать строку (оставить первые 10 символов)
        """
        if len(name_len) < 10:
            self.__name = name_len
        else:
            self.__name = name_len[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализируюет экземпляры класса `Item` данными из файла _src/items.csv
        """
        # Получаем строку, содержащую путь к рабочей директории:
        # dir_path = pathlib.Path.home()

        # Объединяем полученную строку с недостающими частями пути
        # path = Path(dir_path, 'Documents', 'skypro_projects', 'electronics-shop-project', 'src', 'items.csv')
        file = '../src/items.csv'
        cls.all.clear()
        # with open(path, newline='') as csvfile:
        try:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'quantity' not in reader.fieldnames and 'name' not in reader.fieldnames and 'price' not in reader.fieldnames:
                        raise InstantiateCSVError
                    item = cls(row['name'], row['price'], row['quantity'])
                return item
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(string))

    def __add__(self, other):
        if not isinstance(self, Item) or not isinstance(other, Item):
            raise Exception
        else:
            return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'
