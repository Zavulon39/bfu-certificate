import sys
import os
from PyQt5.QtWidgets import QApplication
from src.manager.screen import ScreenManager
from src.ui import MainWindow

# TODO: при использовании в production, убрать префикс dev_ в .\src\manager\bootstrap.py
if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    ScreenManager.connect(ui)
    sys.exit(app.exec())
