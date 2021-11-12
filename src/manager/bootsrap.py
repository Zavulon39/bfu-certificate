from datetime import date
from .data import DataManager
from .http import HttpManager
from .db import DBManager
from ..types import Certificate


db = [()]


def map_data(el: dict[str, str]):

    birthday = date(*reversed(list(map(int, el['ДатаРождения'].split(' ')[0].split('.')))))

    try:
        sql = list(filter(lambda sql: el['ФизическоеЛицо'] == ' '.join(sql[2: 5]) and birthday == sql[5], db))[0]
    except IndexError:
        return Certificate(
            name=f'Ошибка, запись в БД для {el["ФизическоеЛицо"]} не найдена',
            birthday=date.today(),
            course='None',
            base='None',
            direction='None',
            enrolment_order='None',
            from_date=date.today(),
            to_date=date.today(),
            is_checked=False,
            spr_id=-1,
            copies_count=0
        )

    return Certificate(
        name=el['ФизическоеЛицо'],
        birthday=birthday,
        course=(el['Курс'] + ' курс ' + el['ФормаОбучения']).lower(),
        base=el['Основа'].lower(),
        direction=el['Направление'],
        enrolment_order=el['ПриказОЗачислении'],
        from_date=date(*reversed(list(map(int, el['ДатаНачалаОбучения'].split('.'))))),
        to_date=date(*reversed(list(map(int, el['ДатаОкончанияОбучения'].split('.'))))),
        is_checked=True if sql[7] == 'Отпечатана' else False,
        spr_id=sql[0],
        copies_count=sql[6]
    )


class BootstrapManager:
    """ Менеджер для подготовления приложения к работе """

    @staticmethod
    def bootstrap():
        # заполнение менеджера глобальных данных
        global db

        data = DataManager()
        db = DBManager.dev_get_request_spr()
        data.authentication_list = [
            ('admin', 'admin')
        ]
        data.certificate_list = list(map(map_data, HttpManager.dev_get()))
