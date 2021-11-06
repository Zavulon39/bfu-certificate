from dataclasses import dataclass
from datetime import date


@dataclass
class Certificate:
    """ Заявка на сертификат """

    id: int
    name: str
    is_checked: bool
    from_date: date
    to_date: date
    birthday: date
    course: str
    base: str
    direction: str
    enrolment_order: str
