from dataclasses import dataclass
from datetime import date
from ..manager.db import DBManager


@dataclass
class Certificate:
    """ Заявка на сертификат """

    name: str
    is_checked: bool
    from_date: date
    to_date: date
    birthday: date
    course: str
    base: str
    direction: str
    enrolment_order: str
    spr_id: int
    copies_count: int

    def update_db(self):
        """ Обновляет запись в БД """
        DBManager.update_request_spr(self.spr_id, 3)  # отпечатана
