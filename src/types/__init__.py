from dataclasses import dataclass


@dataclass
class Certificate:
    name: str
    is_checked: str


class IEmitter:
    """ Интерфейс IEmitter """

    def emit(self): ...
