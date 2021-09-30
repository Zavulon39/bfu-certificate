import sys
import os
from PyQt5.QtWidgets import QApplication

from src.hooks.use_screen import UseScreen
from src.ui import MainWindow

if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    UseScreen.connect(ui)
    sys.exit(app.exec())
