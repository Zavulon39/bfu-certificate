from typing import Optional
from src.utils.singletone import SingletonMeta
from src.types import Certificate


class DataManager(metaclass=SingletonMeta):
    """ Менеджер глобальных данных """

    def __init__(self):
        self.authentication_list = list[tuple[str, str]]
        self.certificate_list: list[Certificate] = []
        self.certificate_detail: Optional[Certificate] = None
