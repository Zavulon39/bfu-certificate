_ui = None


class ScreenManager:
    """ Менеджер для навигации по экранам (основан на ООП паттерне dispatcher-emitter) """

    @staticmethod
    def connect(ui):
        global _ui
        _ui = ui

    @staticmethod
    def get_ui():
        return _ui

    @staticmethod
    def set_screen(new_screen, prev_screen):
        global _ui
        _ui._screen = new_screen
        _ui._screen.show()
        prev_screen.close()
