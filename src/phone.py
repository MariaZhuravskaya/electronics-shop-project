from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :number_of_sim: Количество поддерживаемых сим-карт
        """

        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim):
        """
        Проверяет, что количество физических SIM-карт должно быть целым числом больше нуля
        """
        if sim <= 0:
            print(ValueError('Количество физических SIM-карт должно быть целым числом больше нуля'))
        else:
            self.__number_of_sim = sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


class Pass:
    def __init__(self, name, price, quantity):
        """
        Создание класса Pass.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
