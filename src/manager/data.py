from src.utils.singletone import SingletonMeta
from src.types import Auth, Certificate


class DataManager(metaclass=SingletonMeta):
    """ Менеджер глобальных данных """

    def __init__(self):
        self.auth: Auth = Auth([])
        self.certificates: list[Certificate] = []


