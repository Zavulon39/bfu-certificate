from src.manager.data import DataManager
from src.manager.http import HttpManager


class BootstrapManager:
    """ Менеджер для подготовления приложения к работе """

    @staticmethod
    def bootstrap():
        # заполнение менеджера глобальных данных
        data = DataManager()
        data.authentication_list = [
            ('admin', 'admin')
        ]
        data.certificate_list = HttpManager.dev_get()
