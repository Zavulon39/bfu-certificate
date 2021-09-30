from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow
from .auth import AuthScreen
from src.manager.data import DataManager
from ..types import Auth, IEmitter


class MainWindow(QMainWindow, IEmitter):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Печать справок для БФУ имени Канта')
        self.resize(972, 531)
        self.setFont(QFont('Montserrat'))
        self.setWindowIcon(QIcon('assets/img/favicon.png'))

        data = DataManager()
        data.auth = Auth([
            ('admin', 'admin')
        ])

        self._screen = AuthScreen(self)
        self._screen.show()

    def emit(self):
        self._screen.show()
