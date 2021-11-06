from datetime import date
import requests
from ..types import Certificate

_id = 0


def map_json(el: dict[str, str]):
    global _id
    _id += 1

    return Certificate(
        id=_id,
        name=el['ФизическоеЛицо'],
        birthday=date(*reversed(list(map(int, el['ДатаРождения'].split(' ')[0].split('.'))))),
        course=(el['Курс'] + ' ' + el['ФормаОбучения']).lower(),
        base=el['Основа'].lower(),
        direction=el['Направление'],
        enrolment_order=el['ПриказОЗачислении'],
        from_date=date(*reversed(list(map(int, el['ДатаНачалаОбучения'].split('.'))))),
        to_date=date(*reversed(list(map(int, el['ДатаОкончанияОбучения'].split('.'))))),
        is_checked=False
    )


class HttpManager:
    """ Менеджер для получения данных с сервера """

    @staticmethod
    def get(url: str) -> list[Certificate]:
        res = requests.get(url)

        if res.status_code == 200:
            return list(map(map_json, res.json()))

        return []

    @staticmethod
    def dev_get():
        data = [{"GUID": "c94ab382-ef88-11eb-a694-005056970631",
                 "ПриказОЗачислении": "Приказ о зачислении №3019 ст от 01.09.2019", "ЭлектроннаяПочта": "",
                 "Телефон": "", "АдресПроживания": "", "АдресРегистрации": "",
                 "ФизическоеЛицо": "Костылева Екатерина Михайловна", "Пол": "Женский", "Фамилия": "Костылева",
                 "Имя": "Екатерина", "Отчество": "Михайловна", "ДатаРождения": "17.04.1997 0:00:00", "Серия": None,
                 "Номер": None, "ДатаВыдачи": None, "ОВД": None, "КодПодразделения": None, "МестоРождения": "",
                 "Курс": "Третий", "Направление": "44.03.01 Педагогическое образование", "Специализация": "",
                 "Группа": "03_пед_19_З_д", "Подгруппа": "", "Институт": "Институт образования",
                 "ФормаОбучения": "Заочная", "УровеньПодготовки": "Бакалавриат", "Основа": "Бюджетная основа",
                 "КанцелярскаяДата": "01.09.2019 0:00:00", "КанцелярскийНомер": "3019", "Комната": None,
                 "Общежитие": None, "Гражданство": "РОССИЯ", "Статус": "Является студентом",
                 "ДатаНачалаОбучения": "01.09.2019", "СрокОбучения": 5, "ДатаОкончанияОбучения": "31.08.2024"},
                {"GUID": "bf3c67e6-c08f-11eb-8294-005056970631",
                 "ПриказОЗачислении": "Приказ о зачислении №3018 ст от 01.09.2019", "ЭлектроннаяПочта": "",
                 "Телефон": "79527158275 ;",
                 "АдресПроживания": ", Ханты-Мансийский , Нижневартовский, Излучинск, , Набережная, 20, , 47",
                 "АдресРегистрации": ", Ханты-Мансийский , Нижневартовский, Излучинск, , Набережная, 20, , 47",
                 "ФизическоеЛицо": "Костылева Елизавета Максимовна", "Пол": "Женский", "Фамилия": "Костылева",
                 "Имя": "Елизавета", "Отчество": "Максимовна", "ДатаРождения": "05.03.2001 0:00:00", "Серия": "6714",
                 "Номер": "431831", "ДатаВыдачи": "30.03.2015 0:00:00",
                 "ОВД": "ТП в п.г.т. Излучинск ОУФМС России по ХМАО-Югре в Нижневартовском районе",
                 "КодПодразделения": "860-038", "МестоРождения": "Тюменская обл, Тюмень г", "Курс": "Третий",
                 "Направление": "45.03.02 Лингвистика", "Специализация": "", "Группа": "03_линг_19_О_па",
                 "Подгруппа": "", "Институт": "Институт гуманитарных наук", "ФормаОбучения": "Очная",
                 "УровеньПодготовки": "Бакалавриат", "Основа": "Бюджетная основа",
                 "КанцелярскаяДата": "01.09.2019 0:00:00", "КанцелярскийНомер": "3018", "Комната": "Общ6_102",
                 "Общежитие": "Общежитие № 6, ул.Чайковского, д.56, корпус 26", "Гражданство": "РОССИЯ",
                 "Статус": "Является студентом", "ДатаНачалаОбучения": "01.09.2019", "СрокОбучения": 4,
                 "ДатаОкончанияОбучения": "31.08.2023"}]

        return list(map(map_json, data))
