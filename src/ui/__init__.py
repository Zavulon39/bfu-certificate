from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow
from .certificate_list import CertificateListScreen
from ..manager.bootsrap import BootstrapManager


class MainWindow(QMainWindow):
    """ Главный экран, на котором будут рисоваться остальные скрины """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Печать справок для БФУ имени Канта')
        self.resize(972, 531)
        self.setFixedSize(self.size())
        self.setFont(QFont('Montserrat'))
        self.setWindowIcon(QIcon('assets/img/favicon.ico'))

        BootstrapManager.bootstrap()

        self._screen = CertificateListScreen(self)
        self._screen.show()
