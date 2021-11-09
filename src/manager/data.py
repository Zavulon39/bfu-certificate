from typing import Optional
from src.types import Certificate


class SingletonMeta(type):
    """ Мета класс для Singleton """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # позволяет в любой части программы получать один и тот же экземпляр класса
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataManager(metaclass=SingletonMeta):
    """ Менеджер глобальных данных """

    def __init__(self):
        self.authentication_list = list[tuple[str, str]]
        self.certificate_list: list[Certificate] = []
        self.certificate_detail: Optional[Certificate] = None
