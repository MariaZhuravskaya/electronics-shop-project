from src.item import Item


class Language:

    def __init__(self, language='EN'):
        self.__language = language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self

    @property
    def language(self):
        return self.__language

    def __setattr__(self, key, value):
        if key == 'language':
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        else:
            object.__setattr__(self, key, value)


class Keyboard(Item, Language):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)




