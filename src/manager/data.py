from src.utils.singletone import SingletonMeta
from src.types import Certificate


class DataManager(metaclass=SingletonMeta):
    """ Менеджер глобальных данных """

    def __init__(self):
        self.authentication_list = list[tuple[str, str]]
        self.certificates: list[Certificate] = []


