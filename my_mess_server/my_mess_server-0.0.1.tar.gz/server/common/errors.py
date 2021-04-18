"""Ошибки"""


class IncorrectDataRecivedError(Exception):
    """
    Исключение  - некорректные данные получены от сокета.
    """
    def __str__(self):
        return 'Принято некорректное сообщение от удалённого компьютера.'


class NonDictInputError(Exception):
    """
    Исключение - аргумент функции не словарь.
    """
    def __str__(self):
        return 'Аргумент функции должен быть словарём.'


class ReqFieldMissingError(Exception):
    """
    Ошибка - отсутствует обязательное поле в принятом словаре.
    """
    def __init__(self, missing_field):
        self.missing_field = missing_field

    def __str__(self):
        return f'В принятом словаре почему-то отсутствует обязательное поле {self.missing_field}.'


class JIMError(Exception):
    """
    Исключение - ошибка протокола JIM.
    """
    def __init__(self, text=''):
        self.text = text

    def __str__(self):
        if len(self.text) > 0:
            return f'Ошибка протокола JIM: {self.text}'
        else:
            return f'Ошибка протокола JIM'


class ServerError(Exception):
    """
    Исключение - ошибка сервера.
    """
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text
