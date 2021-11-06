_ui = None


class ScreenManager:
    """ Менеджер для навигации по экранам (основан на ООП паттерне dispatcher-emitter) """

    @staticmethod
    def connect(ui):
        global _ui
        _ui = ui  # присваиваем ссылку на главное окно

    @staticmethod
    def get_ui():
        return _ui

    @staticmethod
    def set_screen(new_screen, prev_screen) -> object:
        global _ui
        _ui._screen = new_screen  # присваиваем новый экран
        _ui._screen.show()  # показываем новый
        prev_screen.close()  # закрываем старый
