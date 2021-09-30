from dataclasses import dataclass


@dataclass
class Auth:
    valid_logins_and_passwords: list[tuple[str, str]]


@dataclass
class Certificate:
    name: str
    is_checked: str


class IEmitter:
    """ Интерфейс IEmitter """

    def emit(self): ...
