class SingletonMeta(type):
    """ Мета класс для Singleton """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # позволяет в любой части программы получать один и тот же экземпляр класса
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
